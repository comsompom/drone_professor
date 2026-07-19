-- Emergency Test Script for Servo 1
-- Use this to verify the Lua-to-Servo link
local STICK_CH = 3
local SERVO_IDX = 0 -- MAIN OUT 1
local current_val = 1100

function update()
    local stick = rc:get_pwm(STICK_CH)

    -- Very fast relative movement for testing
    if stick > 1550 then
        current_val = current_val + 5
    elseif stick < 1450 then
        current_val = current_val - 5
    end

    -- Limits
    if current_val > 1900 then current_val = 1900 end
    if current_val < 1100 then current_val = 1100 end

    -- This sends the command to the output
    SRV_Channels:set_output_pwm_chan_timeout(SERVO_IDX, math.floor(current_val), 100)

    return update, 20
end

gcs:send_text(6, "TEST SCRIPT ACTIVE")
return update()