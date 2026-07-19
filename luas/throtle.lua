-- SIYI MK32 centered-stick relative throttle for MAIN OUT 1.
--
-- Important setup:
--   1. Keep ArduPilot throttle on RC channel 3.
--   2. Mirror the centered left-stick throttle control to another channel,
--      for example RC7, and set RC7_OPTION=300 (Scripting1).
--
-- The script reads that scripting channel as a spring-centered up/down
-- command, holds the real throttle internally, drives MAIN OUT 1, and
-- overrides RC throttle channel 3 so telemetry reports the held throttle
-- value instead of the centered stick position.

local STICK_OPTION = 300     -- RCx_OPTION value for the centered stick input
local FALLBACK_STICK_CH = 0  -- set to 7 only if RCx_OPTION=300 cannot be used
local THROTTLE_CH = 3        -- ArduPilot throttle channel shown in telemetry
local SERVO_IDX = 0          -- MAIN OUT 1, zero indexed

local MIN_PWM = 1100         -- real idle throttle output
local MAX_PWM = 1600         -- real full throttle output
local REPORT_MIN_PWM = 1000  -- value reported as 0% throttle
local REPORT_MAX_PWM = 2000  -- value reported as 100% throttle

local CENTER = 1500
local DEADZONE = 50
local STICK_DEADZONE = 0.10
local STEP_PWM = 5
local LOOP_MS = 20
local OUTPUT_TIMEOUT_MS = 100
local STATUS_LOOPS = 100

local current_val = MIN_PWM
local throttle_channel = rc:get_channel(THROTTLE_CH)
local stick_channel = rc:find_channel_for_option(STICK_OPTION)
local stick_source = "none"
local stick_neutral_seen = false
local status_count = 0
local warned_same_channel = false

local function clamp(value, min_value, max_value)
    if value < min_value then return min_value end
    if value > max_value then return max_value end
    return value
end

local function throttle_to_report_pwm(throttle_pwm)
    local throttle_range = MAX_PWM - MIN_PWM
    local report_range = REPORT_MAX_PWM - REPORT_MIN_PWM
    local normalized = (throttle_pwm - MIN_PWM) / throttle_range

    return REPORT_MIN_PWM + (normalized * report_range)
end

local function get_stick_direction()
    stick_channel = stick_channel or rc:find_channel_for_option(STICK_OPTION)

    if stick_channel then
        stick_source = "option"
        local input = stick_channel:norm_input_dz()
        if input > STICK_DEADZONE then
            if stick_neutral_seen then
                return 1
            end
            return 0
        elseif input < -STICK_DEADZONE then
            if stick_neutral_seen then
                return -1
            end
            return 0
        end

        stick_neutral_seen = true
        return 0
    end

    if FALLBACK_STICK_CH <= 0 then
        stick_source = "none"
        return 0
    end

    local stick = rc:get_pwm(FALLBACK_STICK_CH)
    if not stick then
        stick_source = "none"
        return 0
    end
    stick_source = "fallback"

    if FALLBACK_STICK_CH == THROTTLE_CH and not warned_same_channel then
        gcs:send_text(4, "REL THR: use separate RCx_OPTION=300 input")
        warned_same_channel = true
    end

    if stick > (CENTER + DEADZONE) then
        if stick_neutral_seen then
            return 1
        end
        return 0
    elseif stick < (CENTER - DEADZONE) then
        if stick_neutral_seen then
            return -1
        end
        return 0
    end

    stick_neutral_seen = true
    return 0
end

local function set_throttle_report()
    if not throttle_channel then
        return
    end

    local report_pwm = throttle_to_report_pwm(current_val)
    throttle_channel:set_override(math.floor(clamp(report_pwm, REPORT_MIN_PWM, REPORT_MAX_PWM)))
end

local function send_status()
    status_count = status_count + 1
    if status_count < STATUS_LOOPS then
        return
    end

    status_count = 0

    if stick_source == "option" then
        gcs:send_text(6, "REL THR: input RCx_OPTION=300")
    elseif stick_source == "fallback" then
        gcs:send_text(6, "REL THR: input RC" .. tostring(FALLBACK_STICK_CH))
    else
        gcs:send_text(4, "REL THR: mirror stick to RC7 and set RC7_OPTION=300")
    end
end

function update()
    local armed = arming:is_armed()
    local stick_dir = get_stick_direction()

    if armed then
        if stick_dir > 0 then
            current_val = current_val + STEP_PWM
        elseif stick_dir < 0 then
            current_val = current_val - STEP_PWM
        end
    else
        current_val = MIN_PWM
    end

    current_val = clamp(current_val, MIN_PWM, MAX_PWM)

    SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, math.floor(current_val), OUTPUT_TIMEOUT_MS)
    set_throttle_report()
    send_status()

    return update, LOOP_MS
end

gcs:send_text(6, "SIYI RELATIVE THROTTLE ACTIVE")
return update()
