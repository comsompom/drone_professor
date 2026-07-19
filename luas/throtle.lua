-- SIYI MK32 centered-stick relative throttle for MAIN OUT 1.
--
-- Important setup:
--   1. Keep ArduPilot throttle on RC channel 3.
--   2. The centered left stick remains on RC3.
--
-- The script briefly clears the RC3 override, reads the physical centered
-- stick, holds the
-- real throttle internally, drives MAIN OUT 1, and
-- overrides RC throttle channel 3 so telemetry reports the held throttle
-- value instead of the centered stick position.

local STICK_CH = 3           -- physical centered-stick input
local THROTTLE_CH = 3        -- ArduPilot throttle channel shown in telemetry
local SERVO_IDX = 0          -- MAIN OUT 1, zero indexed

local MIN_PWM = 1100         -- real idle throttle output
local MAX_PWM = 1480         -- real full throttle output for gasoline servo
local REPORT_MIN_PWM = 900   -- value reported as 0% throttle on MK32
local REPORT_MAX_PWM = 2000  -- value reported as 100% throttle

local CENTER = 1500
local DEADZONE = 50
local STEP_PERCENT = 1
local LOOP_MS = 20
local OUTPUT_TIMEOUT_MS = 100
local STATUS_LOOPS = 100

local current_percent = 0
local throttle_channel = rc:get_channel(THROTTLE_CH)
local stick_source = "none"
local stick_neutral_seen = false
local status_count = 0

local function clamp(value, min_value, max_value)
    if value < min_value then return min_value end
    if value > max_value then return max_value end
    return value
end

local function percent_to_pwm(percent, min_pwm, max_pwm)
    return min_pwm + ((max_pwm - min_pwm) * percent / 100)
end

local function get_stick_direction()
    local stick = rc:get_pwm(STICK_CH)
    if not stick then
        stick_source = "none"
        return 0
    end
    stick_source = "rc"

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

    local report_pwm = percent_to_pwm(current_percent, REPORT_MIN_PWM, REPORT_MAX_PWM)
    throttle_channel:set_override(math.floor(clamp(report_pwm, REPORT_MIN_PWM, REPORT_MAX_PWM)))
end

local function send_status()
    status_count = status_count + 1
    if status_count < STATUS_LOOPS then
        return
    end

    status_count = 0

    if stick_source == "rc" then
        gcs:send_text(6, "REL THR: input RC" .. tostring(STICK_CH))
    else
        gcs:send_text(4, "REL THR: mirror stick to RC" .. tostring(STICK_CH))
    end
end

function update()
    local armed = arming:is_armed()

    if throttle_channel then
        throttle_channel:set_override(0)
    end

    local stick_dir = get_stick_direction()

    if armed then
        if stick_dir > 0 then
            current_percent = current_percent + STEP_PERCENT
        elseif stick_dir < 0 then
            current_percent = current_percent - STEP_PERCENT
        end
    else
        current_percent = 0
    end

    current_percent = clamp(current_percent, 0, 100)

    local servo_pwm = percent_to_pwm(current_percent, MIN_PWM, MAX_PWM)
    SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, math.floor(servo_pwm), OUTPUT_TIMEOUT_MS)
    set_throttle_report()
    send_status()

    return update, LOOP_MS
end

gcs:send_text(6, "SIYI RELATIVE THROTTLE ACTIVE")
return update()
