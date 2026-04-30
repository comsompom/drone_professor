-- SIYI MK32 Relative Throttle Script
-- Designed for Cube Orange Plus: Throttle on MAIN OUT 1
-- SERVO1_FUNCTION must be set to 94 (Script1)

local STICK_CH = 3       -- RC Input Channel (Left Stick Vertical)
local SERVO_IDX = 0      -- Physical MAIN OUT 1 (Lua index: 1-1 = 0)
local MIN_PWM = 1100     -- Your requested Idle
local MAX_PWM = 1900     -- Your requested Full Throttle
local CENTER = 1500      -- Stick Center
local DZ = 40            -- Deadzone (1460 to 1540 does nothing)
local SPEED = 0.12       -- Increase this to make throttle move faster

local current_thr = MIN_PWM

function update()
    local mode = FWVersion:get_mode()
    local stick = rc:get_pwm(STICK_CH)

    -- 1. MANUAL MODE LOGIC (Incremental/Relative)
    if mode == 0 then -- Mode 0 is MANUAL in ArduPlane
        if stick > (CENTER + DZ) then
            local delta = (stick - CENTER) * SPEED * 0.1
            current_thr = current_thr + delta
        elseif stick < (CENTER - DZ) then
            local delta = (CENTER - stick) * SPEED * 0.1
            current_thr = current_thr - delta
        end

        -- Keep within limits (1100 to 1900)
        if current_thr > MAX_PWM then current_thr = MAX_PWM end
        if current_thr < MIN_PWM then current_thr = MIN_PWM end

        -- Output to MAIN OUT 1
        SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, math.floor(current_thr), 100)

    -- 2. AUTOPILOT MODES (FBWA, RTL, AUTO)
    else
        -- Fetch ArduPilot's calculated throttle for function 70
        -- This automatically obeys your THR_RTL = 75 setting
        local ap_throttle_pwm = SRV_Channels:get_output_pwm(70)

        -- Let Autopilot drive MAIN OUT 1
        SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, ap_throttle_pwm, 100)

        -- Sync our manual variable so it doesn't "jump" when switching back to Manual
        current_thr = ap_throttle_pwm
    end

    return update, 20 -- Run at 50Hz for smooth servo movement
end

gcs:send_text(6, "GAS RELATIVE THR: LOADED ON SERVO 1")
return update()