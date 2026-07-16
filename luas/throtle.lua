-- SIYI MK32 centered-stick relative throttle for MAIN OUT 1.
-- The physical stick is centered at rest, but the engine throttle is held
-- internally and reported back as a normal low-to-high throttle channel.

local STICK_CH = 3          -- physical throttle stick input
local REPORT_CH = 3         -- throttle channel shown in transmitter telemetry
local SERVO_IDX = 0         -- MAIN OUT 1, zero indexed

local MIN_PWM = 1100        -- real idle throttle output
local MAX_PWM = 1600        -- real full throttle output
local REPORT_MIN_PWM = 1000 -- value shown as 0% throttle
local REPORT_MAX_PWM = 2000 -- value shown as 100% throttle

local CENTER = 1500
local DEADZONE = 50
local STEP_PWM = 5
local LOOP_MS = 20
local OUTPUT_TIMEOUT_MS = 100

local current_val = MIN_PWM
local report_channel = rc:get_channel(REPORT_CH)

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

function update()
    local armed = arming:is_armed()

    if report_channel then
        report_channel:set_override(0)
    end

    local stick = rc:get_pwm(STICK_CH)

    if armed then
        if stick and stick > (CENTER + DEADZONE) then
            current_val = current_val + STEP_PWM
        elseif stick and stick < (CENTER - DEADZONE) then
            current_val = current_val - STEP_PWM
        end
    else
        current_val = MIN_PWM
    end

    current_val = clamp(current_val, MIN_PWM, MAX_PWM)

    SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, math.floor(current_val), OUTPUT_TIMEOUT_MS)

    -- This affects ArduPilot telemetry/RC-channel display, not the local
    -- physical stick position inside the SIYI transmitter.
    if report_channel and armed then
        local report_pwm = throttle_to_report_pwm(current_val)
        report_channel:set_override(math.floor(clamp(report_pwm, REPORT_MIN_PWM, REPORT_MAX_PWM)))
    end

    return update, LOOP_MS
end

gcs:send_text(6, "SIYI RELATIVE THROTTLE ACTIVE")
return update()
