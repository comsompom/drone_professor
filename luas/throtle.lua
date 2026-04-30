-- SIYI MK32 Relative Throttle Script for ArduPlane (Gasoline Engine)
-- SERVO3_FUNCTION must be set to 94 (Script1)

local STICK_CH = 3       -- RC Input Channel (Left Stick)
local SERVO_IDX = 2      -- Physical Servo 3 (0-indexed, so 3-1=2)
local MIN_PWM = 1100     -- Idle
local MAX_PWM = 1900     -- Full Throttle
local CENTER = 1500      -- Stick Center
local DZ = 40            -- Deadzone to prevent drifting
local SPEED = 0.1        -- Adjust this to change how fast throttle climbs (0.05 to 0.3)

local current_thr = MIN_PWM
local last_mode = -1

function update()
    local mode = FWVersion:get_mode()
    local stick = rc:get_pwm(STICK_CH)

    -- 1. IF IN MANUAL MODE (Mode 0 in ArduPlane)
    if mode == 0 then
        -- Logic: Incremental Throttle
        if stick > (CENTER + DZ) then
            local delta = (stick - CENTER) * SPEED * 0.1
            current_thr = current_thr + delta
        elseif stick < (CENTER - DZ) then
            local delta = (CENTER - stick) * SPEED * 0.1
            current_thr = current_thr - delta
        end

        -- Keep within user limits
        if current_thr > MAX_PWM then current_thr = MAX_PWM end
        if current_thr < MIN_PWM then current_thr = MIN_PWM end

        -- Output to Servo 3
        SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, math.floor(current_thr), 100)

    -- 2. IF IN ANY OTHER MODE (FBWA, RTL, AUTO, etc.)
    else
        -- Fetch what ArduPilot wants the throttle to be (Function 70)
        local ap_throttle_pwm = SRV_Channels:get_output_pwm(70)

        -- Override the script and let Autopilot drive the servo
        SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, ap_throttle_pwm, 100)

        -- Synchronize our manual variable so it doesn't "jump" when switching back to Manual
        current_thr = ap_throttle_pwm
    end

    return update, 20 -- Run at 50Hz
end

gcs:send_text(6, "Relative Throttle Loaded on Servo 3")
return update()