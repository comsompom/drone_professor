-- SIYI MK32 centered-stick relative throttle for MAIN OUT 1.
-- This keeps the same control path as throtle_old.lua:
-- read RC3 stick, hold an internal throttle value, and drive only MAIN OUT 1.

local STICK_CH = 3
local SERVO_IDX = 0 -- MAIN OUT 1, zero indexed

local MIN_PWM = 1000
local MAX_PWM = 1480
local STEP_PWM = (MAX_PWM - MIN_PWM) / 100 -- 1% throttle step

local CENTER = 1500
local DEADZONE = 50
local LOOP_MS = 20
local OUTPUT_TIMEOUT_MS = 100

local current_val = MIN_PWM

local function clamp(value, min_value, max_value)
    if value < min_value then return min_value end
    if value > max_value then return max_value end
    return value
end

function update()
    local stick = rc:get_pwm(STICK_CH)
    local armed = arming:is_armed()

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

    return update, LOOP_MS
end

gcs:send_text(6, "RELATIVE THROTTLE ACTIVE")
return update()
