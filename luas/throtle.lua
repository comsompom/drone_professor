-- SIYI MK32 centered-stick relative throttle for MAIN OUT 1.
--
-- Required transmitter setup:
--   RC3: throttle value shown on MK32 / ArduPilot throttle channel
--   RC7: copy of the physical centered left throttle stick
--
-- The script reads RC7, holds a real throttle value, drives MAIN OUT 1,
-- and overrides RC3 so MK32 shows the held throttle instead of stick center.

local STICK_CH = 7
local FALLBACK_STICK_CH = 3
local DISPLAY_CH = 3
local SERVO_IDX = 0 -- MAIN OUT 1, zero indexed

local MIN_PWM = 1000
local MAX_PWM = 1480
local STEP_PWM = (MAX_PWM - MIN_PWM) / 100 -- 1% throttle step

local DISPLAY_MIN_PWM = 900
local DISPLAY_MAX_PWM = 1900

local CENTER = 1500
local DEADZONE = 50
local LOOP_MS = 20
local OUTPUT_TIMEOUT_MS = 100
local STATUS_LOOPS = 100

local current_val = MIN_PWM
local display_channel = rc:get_channel(DISPLAY_CH)
local status_count = 0
local using_fallback_stick = false
local separate_stick_ready = false
local separate_stick_neutral_seen = false

local function clamp(value, min_value, max_value)
    if value < min_value then return min_value end
    if value > max_value then return max_value end
    return value
end

local function throttle_percent()
    return (current_val - MIN_PWM) / (MAX_PWM - MIN_PWM) * 100
end

local function percent_to_display_pwm(percent)
    return DISPLAY_MIN_PWM + ((DISPLAY_MAX_PWM - DISPLAY_MIN_PWM) * percent / 100)
end

local function get_stick()
    local stick = rc:get_pwm(STICK_CH)

    if separate_stick_ready then
        using_fallback_stick = false
        return stick
    end

    if stick and stick > (CENTER - DEADZONE) and stick < (CENTER + DEADZONE) then
        separate_stick_neutral_seen = true
    elseif stick and separate_stick_neutral_seen then
        separate_stick_ready = true
        using_fallback_stick = false
        return stick
    end

    using_fallback_stick = true
    return rc:get_pwm(FALLBACK_STICK_CH)
end

local function set_display_value()
    if using_fallback_stick or not display_channel then
        return
    end

    local display_pwm = percent_to_display_pwm(throttle_percent())
    display_channel:set_override(math.floor(clamp(display_pwm, DISPLAY_MIN_PWM, DISPLAY_MAX_PWM)))
end

local function send_status(stick)
    status_count = status_count + 1
    if status_count < STATUS_LOOPS then
        return
    end

    status_count = 0

    if using_fallback_stick then
        gcs:send_text(4, "REL THR: move/copy stick on RC7 for MK32 display")
    elseif stick then
        gcs:send_text(6, "REL THR: stick RC" .. tostring(STICK_CH) .. " display RC" .. tostring(DISPLAY_CH))
    else
        gcs:send_text(4, "REL THR: no RC" .. tostring(STICK_CH) .. " stick input")
    end
end

function update()
    local stick = get_stick()
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
    set_display_value()
    send_status(stick)

    return update, LOOP_MS
end

gcs:send_text(6, "RELATIVE THROTTLE ACTIVE")
return update()
