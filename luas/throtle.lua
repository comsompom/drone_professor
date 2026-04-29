-- SIYI MK32 Relative Throttle Script for Gasoline Engine
-- Stick Up > 1520: Increase Throttle
-- Stick Center 1480-1520: Hold Throttle
-- Stick Down < 1480: Decrease Throttle

local STICK_CHANNEL = 3      -- Typically Channel 3 for Throttle
local SERVO_CHANNEL = 3      -- The output port on the Cube (Main Out 3)
local MIN_PWM = 1100         -- Your requested Minimum
local MAX_PWM = 1900         -- Your requested Maximum
local CENTER_PWM = 1500      -- Stick center
local DEADZONE = 30          -- Ignore small stick movements
local SENSITIVITY = 0.15     -- Adjust this to make throttle change faster or slower

local current_throttle = MIN_PWM

function update()
    -- Get current stick position
    local stick_pwm = rc:get_pwm(STICK_CHANNEL)

    -- Only run in MANUAL mode to avoid interfering with Autopilot
    local mode = FWVersion:get_mode()
    if mode ~= 0 then -- mode 0 is usually Manual in Plane. Adjust if using Copter/Rover
        return update, 20
    end

    -- Logic: Increase/Decrease based on stick distance from center
    if stick_pwm > (CENTER_PWM + DEADZONE) then
        local delta = (stick_pwm - CENTER_PWM) * SENSITIVITY
        current_throttle = current_throttle + delta
    elseif stick_pwm < (CENTER_PWM - DEADZONE) then
        local delta = (CENTER_PWM - stick_pwm) * SENSITIVITY
        current_throttle = current_throttle - delta
    end

    -- Constrain values to your limits
    if current_throttle > MAX_PWM then current_throttle = MAX_PWM end
    if current_throttle < MIN_PWM then current_throttle = MIN_PWM end

    -- Apply the output to the engine servo
    SRV_Channels:set_output_pwm_chan_timeout(SERVO_CHANNEL - 1, math.floor(current_throttle), 100)

    return update, 20 -- Run at 50Hz
end

return update()