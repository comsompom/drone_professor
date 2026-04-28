# ArduPilot Hardware & Flight Controller Knowledge Base

## Firmware Limitations
**Source URL:** https://ardupilot.org/plane/docs/common-limited-firmware.html

### Description
The ArduPilot firmware in some configurations exceeds 1 MB in size. Some autopilots may not have enough flash memory to store the full firmware.
For the affected autopilots, a reduced firmware is generated. This firmware omits less-commonly used features in order to reduce the firmware size to less than 1 MB.
The missing features are listed on this pagefor each board type for the current âlatestâ firmware. If you require any of these features, you can try to create a build with them in it (at the expense of other non-needed features) using theCustom Firmware Build Server. The missing features list for a board are listed in the same groups and labels as those shown on the Custom Firmware Build Server.
Using the server does require you to know which features you DO want to have and check them, as well as the ones desired that are currently missing.
A table of all current build options that can be selected are shownhere.


---

## AcctonGodwit GA1
**Source URL:** https://ardupilot.org/plane/docs/common-acctongodwit-ga1.html

### Description
The G-A1 is a state-of-the-art autopilot (flight controller) developed based on thePixhawk Autopilot v6X Standard. It adopts an STM32H753 double-precision floating-point FMU processor and an STM32F103 IO coprocessor. There are also independent buses and power supplies. Multiple IMUs with its 6-axis inertial sensors, two pressure/temperature sensors, and a geomagnetic sensor are designed for safety and rich expansion capabilities. With an integrated 10/100M Ethernet Physical Layer (PHY), the G-A1 can also communicate with the mission computer (airborne computer), high-end surveying and mapping cameras, and other UxV-mounted equipment for high-speed communications, meeting the needs of advanced UxV systems.
VisitAccton-IoT Godwitfor more information.

### Ports, UARTs & Pin Mapping
**External portsÂ**
- 2 CAN Buses (CAN1 and CAN2)
- 3 TELEM Ports (TELEM1, TELEM2 and TELEM3)
- 2 GPS Ports (GPS1 with safety switch, LED, buzzer, and GPS2)
- 1 PPM IN
- 1 SBUS OUT
- 2 USB Ports (1 TYPE-C and 1 JST GH1.25)
- 1 10/100Base-T Ethernet Port
- 1 DSM/SBUS RC
- 1 UART 4
- 1 AD&IO Port
- 2 Debug Ports (1 IO Debug and 1 FMU Debug)
- 1 SPI6 Bus
- 4 Power Inputs (Power 1, Power 2, Power C1 and Power C2)
- 16 PWM Servo Outputs (A1-A8 from FMU and M1-M8 from IO)
- Micro SD Socket (supports SD 4.1 & SDIO 4.0 in two databus modes: 1 bit (default) and 4 bits)

**UART MappingÂ**
Serial# | Protocol | Port | Notes
SERIAL1 | Telem1 | UART7 | CTS/RTS, DMA
SERIAL2 | Telem2 | UART5 | CTS/RTS, DMA
SERIAL3 | GPS1 | USART1 | DMA
SERIAL4 | GPS2 | UART8 | DMA
SERIAL5 | Telem3 | USART2 | CTS/RTS, DMA
SERIAL6 | UART4 | UART4 | No DMA
SERIAL7 | FMU Debug | USART3 | No DMA
SERIAL8 | OTG2 | USB | DMA

**More Information and SupportÂ**
- Accton-IoT Godwit
- sales@accton-iot.com
- support@accton-iot.com



---

## ARKV6X DS-10 Pixhawk6
**Source URL:** https://ardupilot.org/plane/docs/common-ark-v6x-overview.html

### Description
The USA-built ARKV6X flight controller is based on theFMUV6X and Pixhawk Autopilot Bus open source standards.
With triple synced IMUs, data averaging, voting, and filtering is possible. The Pixhawk Autopilot Bus (PAB) form factor enables the ARKV6X to be used on any PAB-compatible carrier board, such as theARK Pixhawk Autopilot Bus Carrier.

### Specifications
**SpecificationsÂ**
- SensorsDual Invensense ICM-42688-P IMUsInvensense IIM-42652 Industrial IMUBosch BMP390 BarometerBosch BMM150 Magnetometer
- Dual Invensense ICM-42688-P IMUs
- Invensense IIM-42652 Industrial IMU
- Bosch BMP390 Barometer
- Bosch BMM150 Magnetometer
- MicroprocessorSTM32H743IIK6 MCU480Mhz / 1MB RAM / 2MB Flash
- STM32H743IIK6 MCU
- 480Mhz / 1MB RAM / 2MB Flash
- Power Requirements5V500mA300ma for main system200ma for heater
- 5V
- 500mA
- 300ma for main system
- 200ma for heater
- OtherFRAMPixhawk Autopilot Bus (PAB) Form FactorLED IndicatorsMicroSD SlotUSA BuiltDesigned with a 1W heater. Keeps sensors warm in extreme conditions
- FRAM
- Pixhawk Autopilot Bus (PAB) Form Factor
- LED Indicators
- MicroSD Slot
- USA Built
- Designed with a 1W heater. Keeps sensors warm in extreme conditions
- Additional InformationWeight: 5.0 gDimensions: 3.6 x 2.9 x 0.5 cm
- Weight: 5.0 g
- Dimensions: 3.6 x 2.9 x 0.5 cm
- PinoutFor pinout of the ARKV6X see theDS-10 Pixhawk Autopilot Bus Standard
- For pinout of the ARKV6X see theDS-10 Pixhawk Autopilot Bus Standard


### Ports, UARTs & Pin Mapping
**Serial Port MappingÂ**
UART | Serial Number | Port
UART7 | SERIAL1 | TELEM1
UART5 | SERIAL2 | TELEM2
USART1 | SERIAL3 | GPS
UART8 | SERIAL4 | GPS2
USART2 | SERIAL5 | TELEM3
UART4 | SERIAL6 | UART4 & I2C
USART3 | SERIAL7 | Debug Console
USART6 | SERIAL8 | PX4IO/RC



---

## CUAV V5 Plus
**Source URL:** https://ardupilot.org/plane/docs/common-cuav-v5plus-overview.html

### Description
The CUAV v5 Plus is an advanced STM32F765 autopilot designed and made by CUAV.
It is a variant of the CUAV V5, updated to use Pixhawk standard pinouts.
The modular design allows the users to customize their own carrier board.
The Carrier Board design reference ishere

### Specifications
**SpecificationsÂ**
- Processor32-bit ARM Cortex M7 core with DPFPU216 Mhz/512 KB RAM/2 MB Flash32 bit IOMCU co-processor
- 32-bit ARM Cortex M7 core with DPFPU
- 216 Mhz/512 KB RAM/2 MB Flash
- 32 bit IOMCU co-processor
- SensorsInvenSense ICM20689 accelerometer / gyroscopeInvenSense ICM20602 : accelerometer / gyroscopeBosch BMI055 accelerometer / gyroscopeMS5611 barometerIST8310 magnetometer
- InvenSense ICM20689 accelerometer / gyroscope
- InvenSense ICM20602 : accelerometer / gyroscope
- Bosch BMI055 accelerometer / gyroscope
- MS5611 barometer
- IST8310 magnetometer
- PowerOperating power: 4.3~5.4VUSB Input: 4.75~5.25VHigh-power servo rail, up to 36V
(servo rail does not power the autopilot)Dual voltage and current monitor inputsCUAV v5 Plus can be triple redundant if power is provided
to both battery monitor inputs and the USB port
- Operating power: 4.3~5.4V
- USB Input: 4.75~5.25V
- High-power servo rail, up to 36V
(servo rail does not power the autopilot)
- Dual voltage and current monitor inputs
- CUAV v5 Plus can be triple redundant if power is provided
to both battery monitor inputs and the USB port
- Interfaces8 - 14 PWM servo outputs (6 IOMCU, 8 FMU)3 dedicated PWM/Capture inputs on FMUS.Bus servo outputPPM connector supports only PPMSBUS/DSM/RSSI connector supports all RC protocols (including SBUS, DSM, ST24, SRXL and PPM)Analog / PWM RSSI input5x general purpose serial ports4x I2C ports4x SPI bus2x CAN Bus ports2x analog battery monitor ports
- 8 - 14 PWM servo outputs (6 IOMCU, 8 FMU)
- 3 dedicated PWM/Capture inputs on FMU
- S.Bus servo output
- PPM connector supports only PPM
- SBUS/DSM/RSSI connector supports all RC protocols (including SBUS, DSM, ST24, SRXL and PPM)
- Analog / PWM RSSI input
- 5x general purpose serial ports
- 4x I2C ports
- 4x SPI bus
- 2x CAN Bus ports
- 2x analog battery monitor ports
- Other



---

## CUAV V5 Nano
**Source URL:** https://ardupilot.org/plane/docs/common-cuav-v5nano-overview.html

### Description
The CUAV v5 Nano is an advanced STM32F765 autopilot designed and made by CUAV.
CUAV v5 Nano is intended for engineers and hobbyists who are looking for the power of CUAV V5+ but are working with smaller drones.

### Specifications
**SpecificationsÂ**
- Processor32-bit ARM Cortex M7 core with DPFPU216 Mhz/512 KB RAM/2 MB Flash
- 32-bit ARM Cortex M7 core with DPFPU
- 216 Mhz/512 KB RAM/2 MB Flash
- SensorsInvenSense ICM20689 accelerometer / gyroscopeInvenSense ICM20602 : accelerometer / gyroscopeBosch BMI055 accelerometer / gyroscopeMS5611 barometerIST8310 magnetometer
- InvenSense ICM20689 accelerometer / gyroscope
- InvenSense ICM20602 : accelerometer / gyroscope
- Bosch BMI055 accelerometer / gyroscope
- MS5611 barometer
- IST8310 magnetometer
- PowerOperating power: 4.3~5.4VUSB Input: 4.75~5.25VHigh-power servo rail, up to 36V
(servo rail does not power the autopilot)Dual voltage and current monitor inputsCUAV v5 nano can be dual redundant if power is provided
to Power 1 and USB inputs
- Operating power: 4.3~5.4V
- USB Input: 4.75~5.25V
- High-power servo rail, up to 36V
(servo rail does not power the autopilot)
- Dual voltage and current monitor inputs
- CUAV v5 nano can be dual redundant if power is provided
to Power 1 and USB inputs
- Interfaces8 - 11 PWM servo outputs3 dedicated PWM/Capture inputs on FMUS.Bus servo outputPPM connector supports all RC protocols (including SBUS, DSM, ST24, SRXL and PPM)SBUS/DSM/RSSI connector supports all RC protocols (including SBUS, DSM, ST24, SRXL and PPM)
and analog / PWM RSSI input5x general purpose serial ports3x I2C ports4x SPI bus2x CAN Bus ports2x analog battery monitor ports
- 8 - 11 PWM servo outputs
- 3 dedicated PWM/Capture inputs on FMU
- S.Bus servo output
- PPM connector supports all RC protocols (including SBUS, DSM, ST24, SRXL and PPM)
- SBUS/DSM/RSSI connector supports all RC protocols (including SBUS, DSM, ST24, SRXL and PPM)
and analog / PWM RSSI input
- 5x general purpose serial ports
- 3x I2C ports
- 4x SPI bus
- 2x CAN Bus ports
- 2x analog battery monitor ports
- Other


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The SERIAL1/2 port have RTS/CTS pins.



---

## CUAV Nora
**Source URL:** https://ardupilot.org/plane/docs/common-cuav-nora-overview.html

### Description
NoraÂ®is an advanced autopilot independently designed by CUAVÂ®. It uses a higher-performance STM32H7 processor and integrates industrial-grade sensors and ultra-low temperature drift sensors. Compared with previous autopilots, it has better performance and more reliability. Nora is ideal for academic research and commercial systems integration.

### Specifications
**SpecificationsÂ**
- Processor32-bit STM32H743 main processor480Mhz / 1MB RAM / 2MB Flash
- 32-bit STM32H743 main processor
- 480Mhz / 1MB RAM / 2MB Flash
- SensorsInvenSense ICM20689 accelerometer / gyroscopeInvenSense ICM20649 accelerometer / gyroscopeBosch BMI088 accelerometer / gyroscope2 MS5611 barometerRM3100 Industrial grade magnetometer
- InvenSense ICM20689 accelerometer / gyroscope
- InvenSense ICM20649 accelerometer / gyroscope
- Bosch BMI088 accelerometer / gyroscope
- 2 MS5611 barometer
- RM3100 Industrial grade magnetometer
- PowerOperating voltage: 4.3~5.4VUSB Input: 4.75~5.25VHigh-voltage capable servo rail, up to 36V
(servo rail does not power the autopilot)Dual voltage and current monitor inputsNora can have triple redundant power (If 3 power sources are provided)
to both battery monitor inputs and the USB port
- Operating voltage: 4.3~5.4V
- USB Input: 4.75~5.25V
- High-voltage capable servo rail, up to 36V
(servo rail does not power the autopilot)
- Dual voltage and current monitor inputs
- Nora can have triple redundant power (If 3 power sources are provided)
to both battery monitor inputs and the USB port
- Interfaces14 PWM servo outputs (12 support DShot)Analog/ PWM RSSI input2 GPS ports (GPS and UART4 ports)4 I2C buses (Two I2C dedicated ports)2 CAN bus ports2 Power ports (Power A is an ADC interface, Power C is a DroneCAN battery interface)2 ADC input ports2 USB ports (Type C and JST-GH1.25)
- 14 PWM servo outputs (12 support DShot)
- Analog/ PWM RSSI input
- 2 GPS ports (GPS and UART4 ports)
- 4 I2C buses (Two I2C dedicated ports)
- 2 CAN bus ports
- 2 Power ports (Power A is an ADC interface, Power C is a DroneCAN battery interface)
- 2 ADC input ports
- 2 USB ports (Type C and JST-GH1.25)
- OtherWeight: 75gSize: 46mm x 64mm x 22mmOperating temperature: -20 ~ 80Â°C (Measured value)
- Weight: 75g
- Size: 46mm x 64mm x 22mm
- Operating temperature: -20 ~ 80Â°C (Measured value)


### Ports, UARTs & Pin Mapping
**Default UART OrderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART2 (TELEM1)
- SERIAL2 = Telemetry2 = USART6 (TELEM2)
- SERIAL3 = GPS1 = USART1 (GPS)
- SERIAL4 = GPS2 = UART4 (UART4)
- SERIAL5 = USER = UART8
- SERIAL6 = USER = UART7 (DEBUG TX/RX)
- SERIAL7 = USER = UART3
Serial protocols can be adjusted to personal preferences.



---

## CUAV Pixhawk v6X
**Source URL:** https://ardupilot.org/plane/docs/common-cuav-pixhawkv6X.html

### Description
Featuring STM32H7 cpu, vibration isolation of IMUs, redundant IMUs, double redundant barometers, IMU heating, and integrated Ethernet for high speed connections to companion computers.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H753IIK6STM32F103
- STM32H753IIK6
- STM32F103
- SensorsBosh BMI088 IMU (accel, gyro)InvenSense ICM-20649 IMU (accel, gyro)InvenSense ICM-42688-P IMU (accel, gyro)RM3100 magnetometerDual ICP-20100 barometers
- Bosh BMI088 IMU (accel, gyro)
- InvenSense ICM-20649 IMU (accel, gyro)
- InvenSense ICM-42688-P IMU (accel, gyro)
- RM3100 magnetometer
- Dual ICP-20100 barometers
- PowerDual SMBUS/I2C Power Module InputsCAN Power Module included with autopilot
- Dual SMBUS/I2C Power Module Inputs
- CAN Power Module included with autopilot
- Interfaces8x UARTS, 6 Available for customer use16x PWM outputsPPM/SBUS input, DSM/SBUS inputSPI6 port2x I2C ports for external compass, airspeed sensor, etc. on GPS connectorUSB port (with remote cabling), USB connector on module2 x CAN portBuzzer and Safety SwitchmicroSD cardEthernet
- 8x UARTS, 6 Available for customer use
- 16x PWM outputs
- PPM/SBUS input, DSM/SBUS input
- SPI6 port
- 2x I2C ports for external compass, airspeed sensor, etc. on GPS connector
- USB port (with remote cabling), USB connector on module
- 2 x CAN port
- Buzzer and Safety Switch
- microSD card
- Ethernet
- Size and DimensionsHeat disipating aluminum case
- Heat disipating aluminum case



---

## CUAV X7/X7Pro/X7+/X7+ Pro
**Source URL:** https://ardupilot.org/plane/docs/common-cuav-x7-family-overview.html

### Description
X7/X7 Pro/X7+/X7+ ProÂ®is an advanced autopilot family designed in-house by CUAVÂ®. It uses a higher-performance STM32H7 processor and integrates industrial-grade sensors. Compared with previous autopilots, it has better performance and higher reliability.
The first generation autopilots (X7/X7 Pro) have been updated with new sensors, providing the same high performance, but with more reliable source of supply, and some improvements to allow Bi-dir DShot and servo rail voltage monitoring.
The modular design allows users to customize the baseboard and is fully compatible with the CUAV V5+ carrier board. The X7+/X7+ Pro are ideal for academic research and commercial systems integration.

### Specifications
**Features of CUAV X7 SeriesÂ**
 | CUAV X7 | CUAV X7 Plus | CUAV X7 Pro | CUAV X7 Plus Pro
Processor | STM32H743
Sensors | BMI088 | ICM42688-P | ADIS16470 | ADIS16470
ICM20689 | ICM20689 | BMI088 | ICM42688-P
ICM20649 | ICM20689 | ICM20649 | ICM20689
MS5611*2 BAROs
RM3100  Compass
PWM  outputs | 14 | 14 | 14 | 14
Bidi DShot outputs | 6(M9~M14) | 12(M1~M12 ) | 6(M9~M14) | 12(M1~M12 )
Servo voltage monitor | NO | YES(9.9V max) | NO | YES(9.9V max)
Operating Voltage | 4.3~5.4V ï¼USB:4.75~5.25V)
Power monitor | 2(1 analog power monitor, 1 DroneCan power monitor)


### Ports, UARTs & Pin Mapping
**Default UART OrderÂ**
- SERIAL0 = console = USB (MAVLink2)
- SERIAL1 = Telemetry1 (MAVlink2 default)= USART2 DMA-enabled
- SERIAL2 = Telemetry2 (MAVlink2 default)= USART6 DMA-enabled
- SERIAL3 = GPS1 = USART1
- SERIAL4 = GPS2 = UART4
- SERIAL5 = USER = UART8 (not available except on custom carrier boards) DMA-enabled
- SERIAL6 = USER = UART7
- SERIAL7 = USB2 (Default protocol is MAVLink2)
Serial protocols can be adjusted to personal preferences.



---

## CUAV-7-Nano
**Source URL:** https://ardupilot.org/plane/docs/common-CUAV-7-Nano.html

### Description
The CUAV-7-Nano flight controller produced byCUAV.
It has an ultra-small size and a 100M Ethernet interface. Supports 3.3V/5V PWM output.

### Specifications
**FeaturesÂ**
- STM32H753 microcontroller
- 2 IMUs: IIM42652 and BMI088
- builtin IST8310 magnetometer
- 2 barometers: BMP581 and ICP20100
- microSD card slot
- USB-TypeC port
- 1 ETH network interface
- 5 UARTs plus USB
- 14 PWM outputs
- 3 I2C ports
- 3 CAN ports (two of which share a CAN bus and one is an independent CAN bus)
- Analog RSSI input
- 3.3V/5V configurable PWM output voltage


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART7 (TELEM1)
- SERIAL2 -> UART5 (TELEM2)
- SERIAL3 -> USART1 (GPS&SAFETY)
- SERIAL4 -> UART8 (GPS2)
- SERIAL5 -> USART3 (FMU DEBUG)
The TELEM1 and TELEM2 ports have RTS/CTS pins, the other UARTs do not have RTS/CTS. All have full DMA capability.



---

## F4BY
**Source URL:** https://ardupilot.org/plane/docs/common-f4by.html

### Description
above image and some content courtesy ofSwift-FlyerandMicroHobby.ru

### Specifications
**SpecificationsÂ**
- Processorsingle 32-bit ARM Cortex M4 core with FPU STM32 F407
- single 32-bit ARM Cortex M4 core with FPU STM32 F407
- SensorsInvenSense MPU6000 IMU (accel, gyro)MS5611 barometersHMC5983 compass
- InvenSense MPU6000 IMU (accel, gyro)
- MS5611 barometers
- HMC5983 compass
- Power3x separate 3,3v LDO for CPU, Sensors, CANServo rail backup power diodereverse voltage and overvoltage power protectionboard voltage and servo rail voltage sensors
- 3x separate 3,3v LDO for CPU, Sensors, CAN
- Servo rail backup power diode
- reverse voltage and overvoltage power protection
- board voltage and servo rail voltage sensors
- Interfaces5x UART serial ports, 1 with inverter for frsky telemetryUp to 12x PWM outputsSpektrum DSM/DSM2/DSM-X Satellite inputFutaba S.BUS input support (with external inverter)PPM sum signalRSSI (PWM or voltage) inputI2C, SPI,  CAN, USB3.3V and 6.6V ADC inputs
- 5x UART serial ports, 1 with inverter for frsky telemetry
- Up to 12x PWM outputs
- Spektrum DSM/DSM2/DSM-X Satellite input
- Futaba S.BUS input support (with external inverter)
- PPM sum signal
- RSSI (PWM or voltage) input
- I2C, SPI,  CAN, USB
- 3.3V and 6.6V ADC inputs
- Dimensions50mm x 50mm
- 50mm x 50mm
- Othermicro SD card (for logs)Fram memory for parameters
- micro SD card (for logs)
- Fram memory for parameters
Schematics



---

## CubePilot Cube Black
**Source URL:** https://ardupilot.org/plane/docs/common-thecube-overview.html

### Description


### Specifications
**System FeaturesÂ**
The Cube Black autopilot is a further evolution of the Pixhawk autopilot. It is designed for commercial systems and manufacturers who wish to fully integrate an autopilot into their system. On top of the existing features of Pixhawk, it has the following enhancements:
- 3 sets of IMU sensors for extra redundancy
- 2 sets of IMU are vibration-isolated mechanically, reducing the effect of frame vibration to state estimation
- IMUs are temperature-controlled by onboard heating resistors, allowing optimum working temperature of IMUs
- The entire flight management unit(FMU) and inertial management unit(IMU) are housed in a relatively small form factor (a cube). All inputs and outputs go through a 80-pin DF17 connector, allowing a plug-in solution for manufacturers of commercial systems. Manufacturers can design their own carrier boards to suite their specific needs.

**SpecificationsÂ**
- Processor32-bit ARM Cortex M4 core with FPU168 Mhz/256 KB RAM/2 MB Flash32-bit failsafe co-processor
- 32-bit ARM Cortex M4 core with FPU
- 168 Mhz/256 KB RAM/2 MB Flash
- 32-bit failsafe co-processor
- SensorsThree redundant IMUs (accels, gyros and compass)InvenSense MPU9250, ICM20948 and/or ICM20648 as first and third IMU (accel and gyro)ST Micro L3GD20+LSM303D or InvenSense ICM2076xx as backup IMU (accel and gyro)Two redundant MS5611 barometers
- Three redundant IMUs (accels, gyros and compass)
- InvenSense MPU9250, ICM20948 and/or ICM20648 as first and third IMU (accel and gyro)
- ST Micro L3GD20+LSM303D or InvenSense ICM2076xx as backup IMU (accel and gyro)
- Two redundant MS5611 barometers
- PowerRedundant power supply with automatic failoverServo rail high-power (7 V) and high-current readyAll peripheral outputs over-current protected, all inputs ESD
protected
- Redundant power supply with automatic failover
- Servo rail high-power (7 V) and high-current ready
- All peripheral outputs over-current protected, all inputs ESD
protected
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for CPPM, Spektrum / DSM and S.BusAnalogue / PWM RSSI input5x general purpose serial ports, 2 with full flow control2x I2C portsSPI port (un-buffered, for short cables only not recommended for use)2x CAN Bus interface3x Analogue inputs (3.3V and 6.6V)High-powered piezo buzzer driver (on expansion board)High-power RGB LED (I2C driver compatible connected externally only)Safety switch / LEDOptional carrier board for Intel Edison
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for CPPM, Spektrum / DSM and S.Bus
- Analogue / PWM RSSI input
- 5x general purpose serial ports, 2 with full flow control
- 2x I2C ports
- SPI port (un-buffered, for short cables only not recommended for use)
- 2x CAN Bus interface
- 3x Analogue inputs (3.3V and 6.6V)
- High-powered piezo buzzer driver (on expansion board)
- High-power RGB LED (I2C driver compatible connected externally only)
- Safety switch / LED
- Optional carrier board for Intel Edison


### Ports, UARTs & Pin Mapping
**The Cube connector pin assignmentsÂ**
This section details the pin assignments of the standard carrier board of The Cube. There are other types of carrier boards available, please refer to the manufacturer pages for pinouts of specific carrier board.
TELEM1, TELEM2 ports
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | CTS | +3.3V
5 (blk) | RTS | +3.3V
6 (blk) | GND | GND
GPS1 port
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | SCL I2C1 | +3.3V
5 (blk) | SDA I2C1 | +3.3V
6 (blk) | Button | GND
7 (blk) | button LED | GND
8 (blk) | GND | GND
GPS2 port
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | SCL I2C2 | +3.3V
5 (blk) | SDA I2C2 | +3.3V
6 (blk) | GND | GND
ADC
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | ADC IN | 
3 (blk) | GND | GND
I2C2
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | SCL | +3.3 (pullups)
3 (blk) | SDA | +3.3 (pullups)
4 (blk) | GND | GND
CAN1&2
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | CAN_H | +12V
3 (blk) | CAN_L | +12V
4 (blk) | GND | GND
POWER1
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (red) | VCC | +5V
3 (blk) | CURRENT | up to +3.3V,pin 3
4 (blk) | VOLTAGE | up to +3.3V,pin 2
POWER2
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (red) | VCC | +5V
3 (blk) | CURRENT | up to +3.3V,pin 14
4 (blk) | VOLTAGE | up to +3.3V,pin 13
USB
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | D_plus | +3.3V
3 (blk) | D_minus | +3.3V
4 (blk) | GND | GND
5 (blk) | BUZZER | battery voltage
6 (blk) | Boot/Error LED | 
RSSI Input
Analog/PWM RSSI Input is pin 103



---

## CubePilot Cube Orange/+
**Source URL:** https://ardupilot.org/plane/docs/common-thecubeorange-overview.html

### Description


### Specifications
**System FeaturesÂ**
The Cube Orange autopilot is the latest and most powerful model in the CubePilot ecosystem. Designed for hobby users, commercial system integrators and UAS manufacturers the Cube Orange autopilot is part of a wide ecosystem of autopilot modules and carrier boards. All Cube models are compatible with all carriers which allows users to choose an off the shelf carrier board that best suits their needs. System designers are able to integrate the Cube directly into their designs via published carrier board specifications.
The Cube Orange is available as a standalone module or as a package with a new updated version of the original carrier board that now includes an integrated ADS-B In module from uAvionics.

**Cube Orange/+ FeaturesÂ**
- Faster H7 SOC with 1MB ram
- Upgraded triple redundant IMU sensors for extra redundancy
- 2 sets of IMU are vibration-isolated mechanically, reducing the effect of frame vibration to state estimation
- IMUs are temperature-controlled by onboard heating resistors, allowing optimum working temperature of IMUs
- The entire flight management unit(FMU) and inertial management unit(IMU) are housed in a reatively small form factor (a cube).
- Fully CubePilot carrierboard compatible, all inputs and outputs go through a 80-pin DF17 connector, allowing a plug-in solution for manufacturers of commercial systems. Manufacturers can design their own carrier boards to suit their specific needs now and in the future.

**SpecificationsÂ**
- Processor32bit ARMÂ® STM32H753 CortexÂ®-M7ï¼with DP-FPU; Cube Orange+ uses ARMÂ® STM32H757400 Mhz/1 MB RAM/2 MB Flash32 bit STM32F103 failsafe co-processor
- 32bit ARMÂ® STM32H753 CortexÂ®-M7ï¼with DP-FPU; Cube Orange+ uses ARMÂ® STM32H757
- 400 Mhz/1 MB RAM/2 MB Flash
- 32 bit STM32F103 failsafe co-processor
- SensorsThree redundant IMUs (Accelerometers/Gyroscopes), Two Barometers, One MagnetometerAll sensors connected via SPI.ICM 20649 integrated accelerometer / gyro, MS5611 barometer on base boardCubeOrange:
-  InvenSense ICM20602 IMU,ICM20948 IMU/MAG, MS5611 barometer on temperature controlled, vibration isolated boardCubeOrange+:
-  Invensense ICM42688 IMU, ICM20948 IMU/MAG, MS5611 barometer on temperature controlled, vibration isolated boardAK099916 MAG
- Three redundant IMUs (Accelerometers/Gyroscopes), Two Barometers, One Magnetometer
- All sensors connected via SPI.
- ICM 20649 integrated accelerometer / gyro, MS5611 barometer on base board
- AK099916 MAG
- PowerRedundant power supply with automatic failoverServo rail high-power (7 V) and high-current readyAll peripheral outputs over-current protected, all inputs ESD
protected
- Redundant power supply with automatic failover
- Servo rail high-power (7 V) and high-current ready
- All peripheral outputs over-current protected, all inputs ESD
protected
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for CPPM, Spektrum / DSM and S.BusAnalogue / PWM RSSI input5x general purpose serial ports, 2 with full flow control2x I2C portsSPI port (un-buffered, for short cables only not recommended for use)2x CAN Bus interface3x Analogue inputs (3.3V and 6.6V)High-powered piezo buzzer driver (on expansion board)High-power RGB LED (I2C driver compatible connected externally only)Safety switch / LEDOptional carrier board for Intel Edison (now obsolete)
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for CPPM, Spektrum / DSM and S.Bus
- Analogue / PWM RSSI input
- 5x general purpose serial ports, 2 with full flow control
- 2x I2C ports
- SPI port (un-buffered, for short cables only not recommended for use)
- 2x CAN Bus interface
- 3x Analogue inputs (3.3V and 6.6V)
- High-powered piezo buzzer driver (on expansion board)
- High-power RGB LED (I2C driver compatible connected externally only)
- Safety switch / LED
- Optional carrier board for Intel Edison (now obsolete)


### Ports, UARTs & Pin Mapping
**The Cube connector pin assignmentsÂ**
TELEM1, TELEM2 ports
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | CTS | +3.3V
5 (blk) | RTS | +3.3V
6 (blk) | GND | GND
GPS1 port
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | SCL I2C2 | +3.3V
5 (blk) | SDA I2C2 | +3.3V
6 (blk) | Button | GND
7 (blk) | button LED | GND
8 (blk) | GND | GND
GPS2 port
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | SCL I2C1 | +3.3V
5 (blk) | SDA I2C1 | +3.3V
6 (blk) | GND | GND
ADC
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | ADC IN | 6.6Vmax,pin 8
3 (blk) | GND | GND
I2C2
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | SCL | +3.3 (pullups)
3 (blk) | SDA | +3.3 (pullups)
4 (blk) | GND | GND
CAN1&2
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | CAN_H | +12V
3 (blk) | CAN_L | +12V
4 (blk) | GND | GND
POWER1
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (red) | VCC | +5V
3 (blk) | CURRENT | up to +3.3V,pin 15
4 (blk) | VOLTAGE | up to +3.3V,pin 14
POWER2
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (red) | VCC | +5V
3 (blk) | CURRENT | up to +3.3V,pin 4
4 (blk) | VOLTAGE | up to +3.3V,pin 13
USB
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | D_plus | +3.3V
3 (blk) | D_minus | +3.3V
4 (blk) | GND | GND
5 (blk) | BUZZER | battery voltage
6 (blk) | Boot/Error LED | 
RSSI Input
Analog/PWM RSSI Input is pin 103



---

## CubePilot Cube Purple
**Source URL:** https://ardupilot.org/plane/docs/common-thecubepurple-overview.html

### Description


### Specifications
**System FeaturesÂ**
The Cube Purple autopilot is designed for ground based applications such as boat, car or rover. Based on the Cube Black main module the purple is a much smaller platform for applications where sensor redundancy is not required.
- Single IMU sensor
- Single Baro Sensor
- The entire flight management unit(FMU) and inertial management unit(IMU) are housed in a reatively small form factor (a cube). All inputs and outputs go through a 80-pin DF17 connector, allowing a plug-in solution for manufacturers of commercial systems. Manufacturers can design their own carrier boards to suit their specific needs.

**SpecificationsÂ**
- Processor32-bit ARM Cortex M4 core with FPU168 Mhz/256 KB RAM/2 MB Flash32-bit failsafe co-processor
- 32-bit ARM Cortex M4 core with FPU
- 168 Mhz/256 KB RAM/2 MB Flash
- 32-bit failsafe co-processor
- Sensors1 x IMU (accels, gyros and compass)1 x InvenSense MPU9250 (accel and gyro)1 x MS5611 barometers
- 1 x IMU (accels, gyros and compass)
- 1 x InvenSense MPU9250 (accel and gyro)
- 1 x MS5611 barometers


### Ports, UARTs & Pin Mapping
**The Cube connector pin assignmentsÂ**
All other specification and external connections remain identical to the original board as listed on the Cube Black page.



---

## CubePilot Cube Yellow
**Source URL:** https://ardupilot.org/plane/docs/common-thecubeyellow-overview.html

### Description


### Specifications
**System FeaturesÂ**
The Cube Yellow autopilot is a new model in the CubePilot ecosystem, designed for hobby users, commercial system integrators and UAS manufacturers the Cube Yellow is based on the Arm STM32F7 series SOC. Sitting directly between the Cube Black and Orange this model offers better performance and newer sensors over the Cube Black while retaining F series SOC compatibility.
Just like the other models the Yellow is part of a wide ecosystem of autopilot modules and carrier boards. All the Cube models are compatible with all of the carriers which allows users to choose an off the shelf carrier board design that best suits their needs. System designers are able to integrate the Cube directly into their designs via published carrier board specifications.

**Cube Yellow FeaturesÂ**
- Faster F7 SOC with 512KB ram
- Upgraded triple redundant IMU sensors for extra redundancy
- 2 sets of IMU are vibration-isolated mechanically, reducing the effect of frame vibration to state estimation
- IMUs are temperature-controlled by onboard heating resistors, allowing optimum working temperature of IMUs
- The entire flight management unit(FMU) and inertial management unit(IMU) are housed in a reatively small form factor (a cube).
- Fully CubePilot carrierboard compatible, all inputs and outputs go through a 80-pin DF17 connector, allowing a plug-in solution for manufacturers of commercial systems. Manufacturers can design their own carrier boards to suit their specific needs now and in the future.

**SpecificationsÂ**
- ProcessorSTM32F777VIT6 CortexÂ®-M7 Core (with DPFPU)216 Mhz/512KB RAM/2 MB Flash32 bit STM32F103 failsafe co-processor
- STM32F777VIT6 CortexÂ®-M7 Core (with DPFPU)
- 216 Mhz/512KB RAM/2 MB Flash
- 32 bit STM32F103 failsafe co-processor
- SensorsThree redundant IMUs (accels, gyros and compass)ICM 20649 integrated accelerometer / gyro, MS5611 barometer on base boardInvenSense ICM20602 IMU,ICM20948 IMU/MAG, MS5611 barometer on temperature controlled, vibration isolated boardAll sensors connected via SPI.
- Three redundant IMUs (accels, gyros and compass)
- ICM 20649 integrated accelerometer / gyro, MS5611 barometer on base board
- InvenSense ICM20602 IMU,ICM20948 IMU/MAG, MS5611 barometer on temperature controlled, vibration isolated board
- All sensors connected via SPI.
- PowerRedundant power supply with automatic failoverServo rail high-power (7 V) and high-current readyAll peripheral outputs over-current protected, all inputs ESD
protected
- Redundant power supply with automatic failover
- Servo rail high-power (7 V) and high-current ready
- All peripheral outputs over-current protected, all inputs ESD
protected
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for CPPM, Spektrum / DSM and S.BusAnalogue / PWM RSSI input5x general purpose serial ports, 2 with full flow control2x I2C portsSPI port (un-buffered, for short cables only not recommended for use)2x CAN Bus interface3x Analogue inputs (3.3V and 6.6V)High-powered piezo buzzer driver (on expansion board)High-power RGB LED (I2C driver compatible connected externally only)Safety switch / LEDOptional carrier board for Intel Edison (now obsolete)
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for CPPM, Spektrum / DSM and S.Bus
- Analogue / PWM RSSI input
- 5x general purpose serial ports, 2 with full flow control
- 2x I2C ports
- SPI port (un-buffered, for short cables only not recommended for use)
- 2x CAN Bus interface
- 3x Analogue inputs (3.3V and 6.6V)
- High-powered piezo buzzer driver (on expansion board)
- High-power RGB LED (I2C driver compatible connected externally only)
- Safety switch / LED
- Optional carrier board for Intel Edison (now obsolete)


### Ports, UARTs & Pin Mapping
**The Cube connector pin assignmentsÂ**
All other specification and external connections remain identical to the original board listed on the Cube Black page.



---

## Holybro Durandal H7
**Source URL:** https://ardupilot.org/plane/docs/common-durandal-overview.html

### Description
Durandal is the latest update to the successful family of Holybro autopilots.
It was designed and developed by Holybro, optimized to run the latest ArduPilot firmware.
It features the STM32H743 microprocessor, the latest advanced processor technology from STMicroelectronicsÂ®,
plus sensor technology from BoschÂ® and InvenSenseÂ®, and a ChibiOS real-time operating system, delivering incredible
performance, flexibility, and reliability for controlling any autonomous vehicle.
Durandalâs microcontroller now has 2 MB of Flash memory and 1 MB of RAM.

### Specifications
**SpecificationsÂ**
- Processor32-bit STM32H743 main processor400Mhz / 1MB RAM / 2MB Flash32-bit co-processor
- 32-bit STM32H743 main processor
- 400Mhz / 1MB RAM / 2MB Flash
- 32-bit co-processor
- SensorsInvenSense ICM20689 accelerometer / gyroscopeBosch BMI088 accelerometer / gyroscopeMS5611 barometerIST8310 magnetometer
- InvenSense ICM20689 accelerometer / gyroscope
- Bosch BMI088 accelerometer / gyroscope
- MS5611 barometer
- IST8310 magnetometer
- PowerOperating power: 4.9~5.5V (6v max input)USB Input: 4.75~5.25VHigh-power servo rail, up to 36V
(servo rail does not power the autopilot)Dual voltage and current monitor inputs
- Operating power: 4.9~5.5V (6v max input)
- USB Input: 4.75~5.25V
- High-power servo rail, up to 36V
(servo rail does not power the autopilot)
- Dual voltage and current monitor inputs
- InterfacesUSB-C and JST_GH USB ports16 PWM outputs, 8 of which can be used as GPIO pinsDual power module inputsS.Bus servo outputR/C inputs for CPPM and S.BusDSM input portAnalogue / PWM RSSI input5x general purpose serial ports plus debug port3x I2C ports4x SPI buses enabled2x CAN Bus ports2x additional analog inputsSafety Switch/LED
- USB-C and JST_GH USB ports
- 16 PWM outputs, 8 of which can be used as GPIO pins
- Dual power module inputs
- S.Bus servo output
- R/C inputs for CPPM and S.Bus
- DSM input port
- Analogue / PWM RSSI input
- 5x general purpose serial ports plus debug port
- 3x I2C ports
- 4x SPI buses enabled
- 2x CAN Bus ports
- 2x additional analog inputs
- Safety Switch/LED
- Other


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The Telem1, Telem2 and Telem3 ports have RTS/CTS pins, the other UARTs do not
have RTS/CTS.

**TELEM1, TELEM2, TELEM3 portsÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | CTS | +3.3V
5 (blk) | RTS | +3.3V
6 (blk) | GND | GND

**GPS1 portÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | SCL I2C1 | +3.3V
5 (blk) | SDA I2C1 | +3.3V
6 (blk) | Button | GND
7 (blk) | button LED | GND
8 (blk) | 3.3V | 3.3
9 (blk) | buzzer | GND
(blk) | GND | GND

**GPS2, Telem4/I2C portÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | SCL I2C2 | +3.3V
5 (blk) | SDA I2C2 | +3.3V
6 (blk) | GND | GND

**SBUS Out portÂ**
The SBUS out port is a port attached to the IO processor which can be
used to output all servo channels via SBUS. It is enabled by setting
theBRD_SBUS_OUTparameter.
When SBUS output is disabled (by settingBRD_SBUS_OUTto 0, you can
use the pin for analog RSSI input from receivers. To enable for RSSI
input you need to set:
You cannot have both SBUS output and analog RSSI input at the same time.
Pin | Signal | Volt
1 | GND | GND
2 | 5v(Vservo) | +5.0V
3 | TX (OUT) | +3.3V

**DSM/SPKT portÂ**
The SPKT port provides a connector for Spektrum satellite
receivers. It is needed to allow for software controlled binding of
satellite receivers.
Pin | Signal | Volt
1 | RX (IN) | +3.3V
2 | GND | GND
3 | 3.3v | +3.3V



---

## Holybro Pix32 v5
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-pix32v5.html

### Description


### Specifications
**System FeaturesÂ**
HolyBro Pix32 v5 is a new autopilot developed on the base of FMUv5
scheme, which can be regarded as a variant version of âPixhawk4â.
The Pix32 v5 is comprised of a separate autopilot and carrier board which are
connected by a 100pin connector. It is designed for those pilots who need a high power,
flexible and customizable flight control system.
Holybro offers two variations of the carrier board, including an ultra compact âMiniâ version.
Manufacturers can design  carrier boards to suit their specific needs.

**SpecificationsÂ**
- Processors32 Bit Arm Cortex-M7®, 216MHz, 2MB memory, 512KB RAM32 Bit Arm Cortex-M3®IO co-processor, 24MHz, 8KB SRAM
- 32 Bit Arm Cortex-M7®, 216MHz, 2MB memory, 512KB RAM
- 32 Bit Arm Cortex-M3®IO co-processor, 24MHz, 8KB SRAM
- SensorsAccel/Gyro: ICM-20689Accel/Gyro: BMI055Mag: IST8310Barometer: MS5611
- Accel/Gyro: ICM-20689
- Accel/Gyro: BMI055
- Mag: IST8310
- Barometer: MS5611
- Interfaces8-16 PWM servo outputs (8 from IO co-processor, 8 from main cpu)3 dedicated PWM/Capture inputsDedicated R/C input for CPPMDedicated R/C input for Spektrum/DSM and S.BusAnalog/PWM RSSI inputDedicated S.Bus servo output5 general purpose serial portsTwo USARTs with full flow controlUART1 port on carrier board 5V supply capable of 1.5A current limit3 I2C ports4 SPI buses1 internal high speed SPI sensor bus with 4 chip selects and 6 DRDYs1 internal low noise SPI bus dedicated for Barometer with 2 chip selects, no DRDYs1 internal SPI bus dedicated for FRAMSupports dedicated SPI calibration EEPROM located on sensor module1 external busUp to 2 CANBuses for dual CAN with serial EEPROMEach CANBus has individual silent controls for ESC RX-MUX controlAnalog inputs for voltage/current from two battery monitors with two additional analog inputs
- 8-16 PWM servo outputs (8 from IO co-processor, 8 from main cpu)
- 3 dedicated PWM/Capture inputs
- Dedicated R/C input for CPPM
- Dedicated R/C input for Spektrum/DSM and S.Bus
- Analog/PWM RSSI input
- Dedicated S.Bus servo output
- 5 general purpose serial portsTwo USARTs with full flow controlUART1 port on carrier board 5V supply capable of 1.5A current limit
- Two USARTs with full flow control
- UART1 port on carrier board 5V supply capable of 1.5A current limit
- 3 I2C ports
- 4 SPI buses1 internal high speed SPI sensor bus with 4 chip selects and 6 DRDYs1 internal low noise SPI bus dedicated for Barometer with 2 chip selects, no DRDYs1 internal SPI bus dedicated for FRAMSupports dedicated SPI calibration EEPROM located on sensor module1 external bus
- 1 internal high speed SPI sensor bus with 4 chip selects and 6 DRDYs
- 1 internal low noise SPI bus dedicated for Barometer with 2 chip selects, no DRDYs
- 1 internal SPI bus dedicated for FRAM
- Supports dedicated SPI calibration EEPROM located on sensor module
- 1 external bus
- Up to 2 CANBuses for dual CAN with serial EEPROM
- Each CANBus has individual silent controls for ESC RX-MUX control
- Analog inputs for voltage/current from two battery monitors with two additional analog inputs
- Voltage RatingsPower module input to autopilot: 4.9~5.5VMaximum input voltage: 6VUSB Voltage Input: 4.75~5.25V (supplies voltage to all carrier board 5V outputs, limited to USB current sourceâs capability)Servo Rail Input: 0~36V; servo rail isolated from other internal components and requires its own supply)
- Power module input to autopilot: 4.9~5.5V
- Maximum input voltage: 6V
- USB Voltage Input: 4.75~5.25V (supplies voltage to all carrier board 5V outputs, limited to USB current sourceâs capability)
- Servo Rail Input: 0~36V; servo rail isolated from other internal components and requires its own supply)
- Mechanical DataDimensions: 45mm x 45mm x 13.5mmWeight: 33.0g
- Dimensions: 45mm x 45mm x 13.5mm
- Weight: 33.0g


### Ports, UARTs & Pin Mapping
**Carrier board pin assignmentsÂ**
This section details the pin assignments of the standard and mini carrier board. OEMs can design their own carrier board, as needed for specific requirements. Design schematics, module connector and pinout, 3D printer files, etc. are locatedhere.



---

## Holybro Pixhawk6X/6X Pro
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-pixhawk6X.html

### Description
Pixhawk6XÂ®  is the latest update to the successful family of PixhawkÂ® autopilots made by Holybro, featuring STM32H7 cpus, vibration isolation of IMUs, redundant IMUs, double redundant barometers on separate buses, IMU heating, and integrated Ethernet for high speed connections to companion computers.
Pixhawk6X:

### Specifications
**Features of Pixhawk6 SeriesÂ**
(click table below to expand)


### Ports, UARTs & Pin Mapping
**Baseboard PinoutsÂ**
Baseboard options and pinouts



---

## Holybro Pixhawk6C/ 6C Mini
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-pixhawk6C.html

### Description
Pixhawk6C is the latest update to the successful family of PixhawkÂ® autopilots made by Holybro, featuring STM32H7 cpus, vibration isolation of IMUs, redundant IMUs, and IMU heating. It comes in two form factors. The 6C Mini reduces the size and has a built-in PWM motor/servo header, at the expense of a bit fewer ports.

### Specifications
**Features of Pixhawk6 SeriesÂ**
(click table below to expand)



---

## Holybro Pix32v6(Pixhawk6C variant)
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-pix32v6.html

### Description
Pix32v6 is a variant of the Holybro Pixhawk 6C. It is comprised of a separate flight controller and carrier board which are connected by a 100 pin connector. It is designed for those pilots who need a high power, flexible and customizable flight control system.

### Specifications
**Features of Pixhawk6 SeriesÂ**
(click table below to expand)


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
All UARTs except UART4 have full DMA capability.



---

## mRo Pixhawk
**Source URL:** https://ardupilot.org/plane/docs/common-pixhawk-overview.html

### Description


### Specifications
**SpecificationsÂ**
- Processor32-bit ARM Cortex M4 core with FPU168 Mhz/256 KB RAM/2 MB Flash32-bit failsafe co-processor
- 32-bit ARM Cortex M4 core with FPU
- 168 Mhz/256 KB RAM/2 MB Flash
- 32-bit failsafe co-processor
- SensorsMPU6000 as main accel and gyroST Micro 16-bit gyroscopeST Micro 14-bit accelerometer/compass (magnetometer)MEAS barometer
- MPU6000 as main accel and gyro
- ST Micro 16-bit gyroscope
- ST Micro 14-bit accelerometer/compass (magnetometer)
- MEAS barometer
- PowerIdeal diode controller with automatic failoverServo rail high-power (7 V) and high-current readyAll peripheral outputs over-current protected, all inputs ESD
protected
- Ideal diode controller with automatic failover
- Servo rail high-power (7 V) and high-current ready
- All peripheral outputs over-current protected, all inputs ESD
protected
- Interfaces5x UART serial ports, 1 high-power capable, 2 with HW flow
controlSpektrum DSM/DSM2/DSM-X Satellite inputFutaba S.BUS input (output not yet implemented)PPM sum signalRSSI (PWM or voltage) inputI2C, SPI, 2x CAN, USB3.3V and 6.6V ADC inputs
- 5x UART serial ports, 1 high-power capable, 2 with HW flow
control
- Spektrum DSM/DSM2/DSM-X Satellite input
- Futaba S.BUS input (output not yet implemented)
- PPM sum signal
- RSSI (PWM or voltage) input
- I2C, SPI, 2x CAN, USB
- 3.3V and 6.6V ADC inputs
- DimensionsWeight 38 g (1.3 oz)Width 50 mm (2.0â)Height 15.5 mm (.6â)Length 81.5 mm (3.2â)
- Weight 38 g (1.3 oz)
- Width 50 mm (2.0â)
- Height 15.5 mm (.6â)
- Length 81.5 mm (3.2â)


### Ports, UARTs & Pin Mapping
**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | CTS | +3.3V
5 (blk) | RTS | +3.3V
6 (blk) | GND | GND

**GPS portÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | CAN2 TX | +3.3V
5 (blk) | CAN2 RX | +3.3V
6 (blk) | GND | GND

**SERIAL 4/5 port - due to space constraints two ports are on one connector.Â**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (#4) | +3.3V
3 (blk) | RX (#4) | +3.3V
4 (blk) | TX (#5) | +3.3V
5 (blk) | RX (#5) | +3.3V
6 (blk) | GND | GND

**Console PortÂ**
The systemâs serial console runs on the port labeled SERIAL4/5. The
pinout is standard serial pinout, to connect to a standard FTDI cable
(3.3V, but itâs 5V tolerant).
Pixhawk |  | FTDI | 
1 | +5V (red) |  | N/C
2 | Tx |  | N/C
3 | Rx |  | N/C
4 | Tx | 5 | Rx (yellow)
5 | Rx | 4 | Tx (orange)
6 | GND | 1 | GND (black)

**Spektrum/DSM PortÂ**
The Spektrum/DSM port is for connecting Spektrum DSM-2/DSMX receiver
modules.
Pin | Signal | Volt
1 (white) | Signal | +3.3V
2 (black) | GND | GND
3 (red) | VCC | +3.3V

**Pixhawk analog input pinsÂ**
This section lists the analog pins available on the Pixhawk. These are
virtual pins, defined in the firmware.
Virtual Pin 2 and Power connector Pin 4: power
management connector voltage pin, accepts up to 3.3V, usually attached
to a power module with 10.1:1 scaling
Virtual Pin 3 and Power connector Pin 3: power management connector
current pin, accepts up to 3.3V, usually attached to a power module
with 17:1 scaling
Virtual Pin 4 and (No connector Pin): VCC 5V rail sensing. This
virtual pin reads the voltage on the 5V supply rail. It is used to
provide the HWSTATUS.Vcc reading that ground stations use to display 5V
status
Virtual Pin 13 and ADC 3.3V connector Pin 4: This takes a max of
3.3V. May be used for sonar or other analog sensors.
Virtual Pin 14 and ADC 3.3V connector Pin 2: This takes a max of
3.3V. May be used for second sonar or other analog sensor.
Virtual Pin 15 and ADC 6.6V connector Pin 2: analog airspeed sensor
port. This has 2:1 scaling builtin, so can take up to 6.6v analog
inputs. Usually used for analog airspeed, but may be used for analog
sonar or other analog sensors.
Virtual Pin 102: Servo power rail voltage. This is an internal
measurement of the servo rail voltage made by the IO board within the
Pixhawk. It has 3:1 scaling, allowing it to measure up to 9.9V.
Virtual Pin 103: RSSI (Received Signal Strength Input) input pin
voltage (SBus connector output pin). This is the voltage measured by the
RSSI input pin on the SBUS-out connector (the bottom pin of the 2nd last
servo connector on the 14 connector servo rail).
This can alternatively serve as SBus out by setting theBRD_SBUS_OUTparameter (Copter,Plane,Rover).

**Pixhawk digital outputs and inputs (Virtual Pins 50-55)Â**
The Pixhawk has no dedicated digital output or input pins on its DF13
connectors, but you can assign up to 6 of the âAUX SERVOâ connectors to
be digital GPIO outputs/inputs. These are the first 6 of the 14 three-pin
servo connectors on the end of the board. They are marked as AUX servo
pins 1 - 6 on the silkscreen as seen above.
To set the number of these pins that are available as digital
inputs/outputs, set theBRD_PWM_COUNTparameter. On Pixhawk this
defaults to 4, which means the first 4 AUX connectors are for servos
(PWM) and the last 2 are for digital inputs/outputs. If you setBRD_PWM_COUNTto 0 then you would have 6 virtual digital pins and
still have 8 PWM outputs on the rest of the connector.
The 6 possible pins are available for PIN variables as pin numbers 50 to
55 inclusive.
In summary:
IfBRD_PWM_CNT= 2 then
50 = RC9
51 = RC10
52 = Aux 3
53 = Aux 4
54 = Aux 5
55 = Aux 6
IfBRD_PWM_CNT= 4 then
50 = RC9
51 = RC10
52 = RC11
53 = RC12
54 = Aux 5
55 = Aux 6
IfBRD_PWM_CNT= 6 then
50 = RC9
51 = RC10
52 = RC11
53 = RC12
54 = RC13
55 = RC14
By default, the pins are digital outputs as outlined above. A digital
pin will instead be a digital input if it is assigned to a parameter
that represents a digital input. For example, settingCAM1_FEEDBAK_PINto 50 will make pin 50 the digital input that receives a signal from the
camera when a picture has been taken.



---

## mRo Pixracer
**Source URL:** https://ardupilot.org/plane/docs/common-pixracer-overview.html

### Description
ThePixraceris the first
autopilot of the FMUv4 Pixhawk generation. It comes with a small Wifi extension board.

### Specifications
**SpecificationsÂ**
- Processor:MCU - STM32F427VIT6 rev.3Ultra low noise LDOs for sensors and FMUFRAM - FM25V02-G
- MCU - STM32F427VIT6 rev.3
- Ultra low noise LDOs for sensors and FMU
- FRAM - FM25V02-G
- SensorsGyro/Accelerometer: Invensense MPU9250 Accel / Gyro / Mag (4 KHz)Gyro/Accelerometer: Invensense ICM-20608 Accel / Gyro (4 KHz)Barometer: MS5611Compass: Honeywell HMC5983 magnetometer with temperature
compensation
- Gyro/Accelerometer: Invensense MPU9250 Accel / Gyro / Mag (4 KHz)
- Gyro/Accelerometer: Invensense ICM-20608 Accel / Gyro (4 KHz)
- Barometer: MS5611
- Compass: Honeywell HMC5983 magnetometer with temperature
compensation
- Power5-5.5VDC from USB or PowerBrick connector. Optional/recommendedACSP4 +5V/+12V Power Supply.
- 5-5.5VDC from USB or PowerBrick connector. Optional/recommendedACSP4 +5V/+12V Power Supply.
- Interfaces/ConnectivityWifi: ESP-01 802.11bgn Flashed with MavESP8266MicroSD card readerMicro USBRGB LEDGPS (serial + I2C)TELEM1/TELEM2Wifi serialFrSky Telemetry serial(see note)Debug connector (serial + SWD)Connectors: GPS+I2C, RC-IN, PPM-IN, RSSI, SBus-IN, Spektrum-IN,
USART3 (TxD, RxD, CTS, RTS), USART2 (TxD, RxD, CTS, RTS),
FRSky-IN, FRSky-OUT, CAN, USART8 (TxD, RxD), ESP8266 (full set),
SERVO1-SERVO6, USART7 (TxD, RxD), JTAG (SWDIO, SWCLK), POWER-BRICK
(VDD, Voltage, Current, GND), BUZZER-LED_BUTTON.
- Wifi: ESP-01 802.11bgn Flashed with MavESP8266
- MicroSD card reader
- Micro USB
- RGB LED
- GPS (serial + I2C)
- TELEM1/TELEM2
- Wifi serial
- FrSky Telemetry serial(see note)
- Debug connector (serial + SWD)
- Connectors: GPS+I2C, RC-IN, PPM-IN, RSSI, SBus-IN, Spektrum-IN,
USART3 (TxD, RxD, CTS, RTS), USART2 (TxD, RxD, CTS, RTS),
FRSky-IN, FRSky-OUT, CAN, USART8 (TxD, RxD), ESP8266 (full set),
SERVO1-SERVO6, USART7 (TxD, RxD), JTAG (SWDIO, SWCLK), POWER-BRICK
(VDD, Voltage, Current, GND), BUZZER-LED_BUTTON.
- DimensionsWeight ?36 x 36mm with 30.5 x 30.5mm hole grid with 3.2mm holes
- Weight ?
- 36 x 36mm with 30.5 x 30.5mm hole grid with 3.2mm holes


### Ports, UARTs & Pin Mapping
**Connector pin assignmentsÂ**
Unless noted otherwise all connectors are JST GH

**TELEM1, TELEM2+OSD portsÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | CTS (IN) | +3.3V
5 (blk) | RTS (OUT) | +3.3V
6 (blk) | GND | GND

**GPS portÂ**
PIN | SIGNAL | VOLT
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | I2C1 SCL | +3.3V
5 (blk) | I2C1 SDA | +3.3V
6 (blk) | GND | GND

**FrSky Telemetry / SERIAL4Â**
PIN | SIGNAL | VOLT
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | GND | GND
This port has built in inverters on the TX and RX lines and shunt resistors which allow them to be tied together and connected to an FrSky receiverâs SPort input for telemetry. It is on by default, and onlySERIAL4_PROTOCOLneeds to be set to â10â for FrSky passthrough telemetry to be sent to the receiver. SeeFrSky Telemetryfor more information.
The operation of the TX/RX path inverter can be disabled by setting theSERIAL4_OPTIONSparameter to â2â to âinvertâ the TX , which will turn off the inversion for both the TX and RX pins. This will allow normal UART operation, if desired.

**Debug port (JST SM06B connector)Â**
PIN | SIGNAL | VOLT
1 (red) | VCC TARGET SHIFT | +3.3V
2 (blk) | CONSOLE TX (OUT) | +3.3V
3 (blk) | CONSOLE RX (IN) | +3.3V
4 (blk) | SWDIO | +3.3V
5 (blk) | SWCLK | +3.3V
6 (blk) | GND | GND



---

## OpenPilot Revolution
**Source URL:** https://ardupilot.org/plane/docs/common-openpilot-revo-mini.html

### Description
Images and some content courtesy of theLibrePilot wiki

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM Cortex-M4 microcontroller168 Mhz/1 MB Flash
- STM32F405RGT6 ARM Cortex-M4 microcontroller
- 168 Mhz/1 MB Flash
- SensorsInvenSense MPU6000 IMU (accel, gyro)Honeywell HMC5883L compassMS5611 barometer
- InvenSense MPU6000 IMU (accel, gyro)
- Honeywell HMC5883L compass
- MS5611 barometer
- Power4.8V ~ 10V input power provided through ESC connection for fullsize Revolution5V max on RevoMini
- 4.8V ~ 10V input power provided through ESC connection for fullsize Revolution
- 5V max on RevoMini
- Default Interfaces8 PWM outputs (1 - 6 on PWM output pins, 7 & 8 on Flex-IO / RCInput port)RC input (requires PPM/sBus) on Flex-IO / RCInput portâs CH3 pin (yellow wire on fullsize revolution)analog to digital inputs for battery voltage and current monitoring ( set pins 12,11 in params ), more adcs possible on arbitrary pinsGPS (SERIAL3) on Flexi PortTelemetry (SERIAL1) on MainportUSB (SERIAL0) portSWD Port for flashing and debugging, including 3.3V output for optional peripheralsMMCX antenna connector for integrated HopeRF RFM22B 100mW 433MHz (fullsize Revolution only)OPLink port on RevoMini. OPLink hardware is not supported by ArduPilot, but this port exposes external SPI pins (SCK, CS, MOSI, MISO) that can be used for supported SPI peripherals like SD card adapters or SPI OSD breakout boards (requires additions to hardware definition file and compiling a custom firmware).
- 8 PWM outputs (1 - 6 on PWM output pins, 7 & 8 on Flex-IO / RCInput port)
- RC input (requires PPM/sBus) on Flex-IO / RCInput portâs CH3 pin (yellow wire on fullsize revolution)
- analog to digital inputs for battery voltage and current monitoring ( set pins 12,11 in params ), more adcs possible on arbitrary pins
- GPS (SERIAL3) on Flexi Port
- Telemetry (SERIAL1) on Mainport
- USB (SERIAL0) port
- SWD Port for flashing and debugging, including 3.3V output for optional peripherals
- MMCX antenna connector for integrated HopeRF RFM22B 100mW 433MHz (fullsize Revolution only)
- OPLink port on RevoMini. OPLink hardware is not supported by ArduPilot, but this port exposes external SPI pins (SCK, CS, MOSI, MISO) that can be used for supported SPI peripherals like SD card adapters or SPI OSD breakout boards (requires additions to hardware definition file and compiling a custom firmware).


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = Mainport
- SERIAL2 = NN in default config
- SERIAL3 = GPS1 = FlexiPort



---

## SULIGH7
**Source URL:** https://ardupilot.org/plane/docs/common-suligh7.html

### Description
Design information for these open-source autopilots is available fromhttps://oshwhub.com/shuyedeye/p1-flight-control.

### Specifications
**FeaturesÂ**
- MCUSTM32H743IIK6 32-bit processor running at 480MHz2MB Flash1MB RAM
- STM32H743IIK6 32-bit processor running at 480MHz
- 2MB Flash
- 1MB RAM
- IO MCUSTM32F103
- STM32F103
- IMU:P2:Internal Vibration Isolation for IMUsP2:IMU constant temperature heating(1 W heating power).IMU1-BMI088(With vibration isolation)IMU2-ICM42688-P(With vibration isolation)IMU3-ICM20689(No vibration isolation)
- P2:Internal Vibration Isolation for IMUs
- P2:IMU constant temperature heating(1 W heating power).
- IMU1-BMI088(With vibration isolation)
- IMU2-ICM42688-P(With vibration isolation)
- IMU3-ICM20689(No vibration isolation)
- Baro:Two barometers:Baro1-BMP581 , Baro2-ICP20100Magnetometer: IST8310
- Two barometers:Baro1-BMP581 , Baro2-ICP20100
- Magnetometer: IST8310


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.



---

## TauLabs Sparky2
**Source URL:** https://ardupilot.org/plane/docs/common-taulabs-sparky2.html

### Description
above image and some content courtesy of theTauLabs wiki

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 ARM Cortex-M4 microcontroller168 Mhz/1 MB Flash32-bit failsafe co-processor
- STM32F405 ARM Cortex-M4 microcontroller
- 168 Mhz/1 MB Flash
- 32-bit failsafe co-processor
- SensorsInvenSense MPU9250 IMU (accel, gyro, compass)MS5611 barometersDataflash for logging
- InvenSense MPU9250 IMU (accel, gyro, compass)
- MS5611 barometers
- Dataflash for logging
- Power4.8V ~ 10V input power provided through ESC connection
- 4.8V ~ 10V input power provided through ESC connection
- Interfaces6x PWM outputs (+4 more on LED port)1x RC input PWM/PPM2x analog to digital inputs for battery voltage and current monitoring1x serial input for GPS1x I2C port for external compass1x CAN busMMCX antenna connector for integrated radioUSB portSWD Port for flashing and debugging
- 6x PWM outputs (+4 more on LED port)
- 1x RC input PWM/PPM
- 2x analog to digital inputs for battery voltage and current monitoring
- 1x serial input for GPS
- 1x I2C port for external compass
- 1x CAN bus
- MMCX antenna connector for integrated radio
- USB port
- SWD Port for flashing and debugging



---

## ZeroOneX6/X6 Pro
**Source URL:** https://ardupilot.org/plane/docs/common-zeroonex6.html

### Description
The ZeroOne X6/X6 Pro are flight controllers manufactured by ZeroOne, which is based on the open-source FMU v6X architecture and Pixhawk Autopilot Bus open source specifications.

### Specifications
**Features:Â**
- MCUSTM32H753IIK6 32-bit processor running at 480MHzSTM32F103 IOMCU2MB Flash1MB RAM
- STM32H753IIK6 32-bit processor running at 480MHz
- STM32F103 IOMCU
- 2MB Flash
- 1MB RAM
- SensorsIMUs:Internal Vibration Isolation for IMUsIMU constant temperature heating(1 W heating power).Triple Synced IMUs, BalancedGyro technology, low noise and more shock-resistant:X6:IMU1-ICM45686(With vibration isolation)IMU2-BMI088(With vibration isolation)IMU3-ICM45686(No vibration isolation)X6 Proï¼IMU1-IIM42653(With vibration isolation)IMU2-BMI088(With vibration isolation)IMU3-IIM42653(No vibration isolation)Baros:Two barometers:2 x ICP20100Magnetometer: Built-in RM3100 magnetometer
- IMUs:Internal Vibration Isolation for IMUsIMU constant temperature heating(1 W heating power).Triple Synced IMUs, BalancedGyro technology, low noise and more shock-resistant:X6:IMU1-ICM45686(With vibration isolation)IMU2-BMI088(With vibration isolation)IMU3-ICM45686(No vibration isolation)X6 Proï¼IMU1-IIM42653(With vibration isolation)IMU2-BMI088(With vibration isolation)IMU3-IIM42653(No vibration isolation)
- Internal Vibration Isolation for IMUs
- IMU constant temperature heating(1 W heating power).
- Triple Synced IMUs, BalancedGyro technology, low noise and more shock-resistant:
- X6:IMU1-ICM45686(With vibration isolation)IMU2-BMI088(With vibration isolation)IMU3-ICM45686(No vibration isolation)
- IMU1-ICM45686(With vibration isolation)
- IMU2-BMI088(With vibration isolation)
- IMU3-ICM45686(No vibration isolation)
- X6 Proï¼IMU1-IIM42653(With vibration isolation)IMU2-BMI088(With vibration isolation)IMU3-IIM42653(No vibration isolation)
- IMU1-IIM42653(With vibration isolation)
- IMU2-BMI088(With vibration isolation)
- IMU3-IIM42653(No vibration isolation)
- Baros:Two barometers:2 x ICP20100Magnetometer: Built-in RM3100 magnetometer
- Two barometers:2 x ICP20100
- Magnetometer: Built-in RM3100 magnetometer
- InterfacesEthernetMicro-C USB7 UARTs, 3 with hardware flow controlSafety Switch2 CAN Power Monitor inputs2 CAN portsSPI and I2C ports16 motor/servo outputs, 8 supporting BiDirDShot, 14 supporting DShot
- Ethernet
- Micro-C USB
- 7 UARTs, 3 with hardware flow control
- Safety Switch
- 2 CAN Power Monitor inputs
- 2 CAN ports
- SPI and I2C ports
- 16 motor/servo outputs, 8 supporting BiDirDShot, 14 supporting DShot


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.  All are DMA enabled.
- SERIAL0 :USB     OTG1
- SERIAL1 :UART7   Telem1
- SERIAL2 :UART5   Telem2
- SERIAL3 :USART1  GPS1
- SERIAL4 :UART8   GPS2
- SERIAL5 :USART2  Telem3
- SERIAL6 :UART4   USER
- SERIAL7 :USART3  FMU DEBUG
- SERIAL8 :USB     OTG-SLCAN      |



---

## ZeroOneX6-Air/Air+
**Source URL:** https://ardupilot.org/plane/docs/common-zeroonex6-air.html

### Description
The ZeroOneX6_Air/Air+ is a series of flight controllers manufactured byZeroOne, which is based on the open-source FMU v6C architecture and Pixhawk Autopilot Bus open source specifications.

### Specifications
**Features:Â**
- MCUSTM32H743IIK6 32-bit processor running at 400MHz2MB Flash1MB RAMmicroSD card interfaceSafety Switch /LED2x CAN6x UART, one with RTS/CTS2x I2C2x ADC inputs
- STM32H743IIK6 32-bit processor running at 400MHz
- 2MB Flash
- 1MB RAM
- microSD card interface
- Safety Switch /LED
- 2x CAN
- 6x UART, one with RTS/CTS
- 2x I2C
- 2x ADC inputs
- IO MCUSTM32F103
- Airâs Sensors* IMU: ICM45686
* Baro: ICP20100
* Magnetometer: IST8310
- Air+ Sensors* IMU1: ICM45686 (With vibration isolation)
* IMU2- ICM45686 (No vibration isolation)
* IMU constant temperature heating (1W heating power)
* Baros: 2 x ICP20100
* Magnetometer: IST8310 magnetometer



---

## 3DR Control Zero H7 OEM
**Source URL:** https://ardupilot.org/plane/docs/common-3DR_Control_Zero_OEM_G.html

### Description
The Control Zero H7 OEM revision G is a flight controller produced by3DR (mRo)]

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743IIK6 32-bit processor256KB FRAM
- STM32H743IIK6 32-bit processor
- 256KB FRAM
- SensorsBMI088, ICM20602 Acc/GyroICM20948 Acc/Gyro/MagDPS368 Barometer
- BMI088, ICM20602 Acc/Gyro
- ICM20948 Acc/Gyro/Mag
- DPS368 Barometer
- PowerExternal 5V , 1A supply is requiredInternal 3.3V BEC for sensors is provided on-board
- External 5V , 1A supply is required
- Internal 3.3V BEC for sensors is provided on-board
- InterfacesOne 36pin and one 40pin Samtec Connector for signals on bottom8x PWM outputs BiDirDShot capable1x RC input5x UARTs (2 with flow control)3x I2C ports for external compass, airspeed, etc.2x CAN1x SPISWD via TC2030 headerMicroSD card socketExternal battery monitor inputs for current and voltage
- One 36pin and one 40pin Samtec Connector for signals on bottom
- 8x PWM outputs BiDirDShot capable
- 1x RC input
- 5x UARTs (2 with flow control)
- 3x I2C ports for external compass, airspeed, etc.
- 2x CAN
- 1x SPI
- SWD via TC2030 header
- MicroSD card socket
- External battery monitor inputs for current and voltage
- Size and Dimensions34mm x 20mm3.66g
- 34mm x 20mm
- 3.66g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Serial protocols shown are defaults, but can be adjusted to personal preferences.



---

## ACNS-CM4Pilot
**Source URL:** https://ardupilot.org/plane/docs/common-acns-cm4pilot.html

### Description
The ACNS-CM4Pilot is a low-cost and compact flight controller which integrates a Raspberry Pi CM4 onboard as itsCompanion computer.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 ARM (168MHz)Broadcom BCM2711, quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz (Raspberry Pi CM4)
- STM32F405 ARM (168MHz)
- Broadcom BCM2711, quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5GHz (Raspberry Pi CM4)
- SensorsBMI088 IMU (accel, gyro)BMP280 barometerLIS3MDLTR magnetometer
- BMI088 IMU (accel, gyro)
- BMP280 barometer
- LIS3MDLTR magnetometer
- Interfaces (Autopilot)8x PWM outputs DShot capable1 CAN1x RC input5x UARTs/serial for GPS and other peripherals, one normally used for RC input, one for CM4 connectionI2C port for external compass, airspeed, etc.Power module inputmicroSDCard for logging, etc.USB-C portAnalog RSSI/Airspeed inputDFU boot button
- 8x PWM outputs DShot capable
- 1 CAN
- 1x RC input
- 5x UARTs/serial for GPS and other peripherals, one normally used for RC input, one for CM4 connection
- I2C port for external compass, airspeed, etc.
- Power module input
- microSDCard for logging, etc.
- USB-C port
- Analog RSSI/Airspeed input
- DFU boot button
- Interfaces (CM4)4 USB, 1 OTG USB-C portsmicroSDCard2x GPIOUART2x Camera Interfaces
- 4 USB, 1 OTG USB-C ports
- microSDCard
- 2x GPIO
- UART
- 2x Camera Interfaces
- Size and Dimensions


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the
receive pin for UARTn. The TXn pin is the transmit pin for UARTn.
Serial protocols shown are defaults, but can be adjusted to personal preferences.



---

## AEDROX H7
**Source URL:** https://ardupilot.org/plane/docs/common-aedroxh7.html

### Description


### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- ICM42688-P IMU with external clock
- DPS368 barometer
- 10V 2.3A BEC, GPIO controlled; 5V 2.3A BEC
- Flash Memory
- 6x UART
- 9x PWM
- 1x I2C
- 1x CAN
- 2x GPIOs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink2, DMA-enabled)
- SERIAL2 -> UART2 (GPS, DMA-enabled)
- SERIAL3 -> UART3 (RCIN, DMA-enabled)
- SERIAL4 -> UART4 (MAVLink2, DMA-enabled)
- SERIAL7 -> UART7 (ESC Telemetry, DMA-enabled)
- SERIAL8 -> UART8 (DisplayPort, DMA-enabled)

**OSD SupportÂ**
DisplayPort OSD is available by default on the HD VTX connector.

**VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 10v so be careful not to connect this to a peripheral requiring 5v. DisplayPort OSD is enabled by default on SERIAL8.



---

## AeroFox H7
**Source URL:** https://ardupilot.org/plane/docs/common-aerofox-h7.html

### Description
The AEROFOX-H7 is a flight controller produced byAEROFOX

### Ports, UARTs & Pin Mapping
**UART MappingÂ**
All UARTs, except UART1, are DMA enabled. UART corresponding to each SERIAL port, and its default protocol, are shown below:
- SERIAL0 -> USB (MAVLink2)
- SERIAL1 -> UART7 (ESC Telemetry)
- SERIAL2 -> UART4 (User configured)
- SERIAL3 -> UART5 (User configured)
- SERIAL4 -> USART2 (User configured)
- SERIAL5 -> USART1 (GPS)
- SERIAL6 -> UART8 (RCIN)
- SERIAL7 -> USART3 (MAVLink2)
Any UART may be re-tasked by changing its protocol parameter.



---

## Airvolute DroneCore
**Source URL:** https://ardupilot.org/plane/docs/common-airvolute-DroneCore-Suite.html

### Description
DroneCore.Suiteis a one stop autopilot and flight computer solution for developers of advanced drone systems demanding high computing power and high level of modularity.
It is the âcoreâ of the drone containing most of its electronics in a compact form and it provides wide options for software development of the the most challenging AI and vision based applications.
It consists of a control part calledDroneCore.Pilotand power part calledDroneCore.Power.
DroneCore.Pilot- top board for control of the aircraft containing
DroneCore.Power- bottom board with power electronics containing:

### Specifications
**SpecificationsÂ**
Mechanical parameters
- Weight 247g - including Cube orange, Xavier NX, Xavier heatsink with
fan
- Dimensions 115 x 80 x 45mm
- Mount with 4 screws/spacers M3 109 x 74mm
- WiFi module
- WiFi antennas 2pcs
Electrical parameters
- Power supply range: 12V â 35V (6S LiHV)
- Integrated DC/DC converter for control circuits
- Redundant power supply with power good monitoring for control unit
- Current protected peripheral connectors
- 4 x FOC DroneCAN ESC 40A, featuring motor identification and motor
diagnostics
- Power sensor, SMBUS
ArduPilot (Cube) Connections
- RC input
- PWM output (7 + 7 lines)
- 2x CAN
- 4x UART
- 2x I2C
- Buzzer
- Power sensor input
- ADC input
- Buzzer
Jetson connections
- PCI Express (M2, Key E connector)
- 4 USB 3.0 (ZIF connectors, reductions available)
- Gigabit Ethernet (ZIF connector, reductions available)
- 6 CSI (22 pin)
- 4 GPIO
- DroneCAN, UART, I2C, SPI
- IMU BMI088 and barometer BMP388 on board
- USB 2.0 for debugging
- Micro SD card
- Video output connector (micro HDMI)
- Fan
DroneCore.Power(bottom power board)
- 4 x FOC DroneCAN ESCs â 40A peak / 20A continuous
- power sensor, SMBUS,
- LED Driver for 4x WS2812B strips



---

## AET-H743-Basic
**Source URL:** https://ardupilot.org/plane/docs/common-AET-H743-Basic.html

### Description
The AET-H743-Basic is a flight controller designed and produced byAeroEggTech

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- Dual ICM42688P IMUs
- 13s PWM / Dshot outputs (13th is setup for serial LED)
- 8s UARTs, one with CTS/RTS flow control pins
- 1s CAN
- Dedicated USB board
- DPS310 or SPL06 barometer
- 5V/6V/7V 10A Servo rail BEC
- 9V 2A BEC for VTX, GPIO controlled
- 5V 4A BEC
- MicroSD Card Slot
- Selectable dual camera input
- AT7456E OSD
- 2x I2Cs
- Integrated power monitor


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
All UARTs are DMA capable. The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink2)
- SERIAL2 -> UART2 (GPS)
- SERIAL3 -> UART3 (MAVLink2)
- SERIAL4 -> UART4 (GPS2, RX4 is also available as ESC telem if protocol is changed for this UART)
- SERIAL5 -> USB (SLCAN)
- SERIAL6 -> UART6 (RCIN)
- SERIAL7 -> UART7 (MAVLink2, Integrated Bluetooth module)
- SERIAL8 -> UART8 (User)
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The AET-H743-Basic supports onboard analog SD OSD using a AT7456 chip. The analog VTX should connect to the VTX pin.



---

## AnyleafH7
**Source URL:** https://ardupilot.org/plane/docs/common-anyleafh7.html

### Description
above image and some content courtesy ofAnyleaf

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processor8 MByte flash for loggingIntegrated ELRS receiver
- STM32H743 32-bit processor
- 8 MByte flash for logging
- Integrated ELRS receiver
- SensorsICM42688 IMU (accel and gyro only, no compass)DPS310 barometer
- ICM42688 IMU (accel and gyro only, no compass)
- DPS310 barometer
- Power2S  - 6S Lipo input voltage with voltage monitoring9V, 3A BEC for powering Video Transmitter5V, 2A BEC for peripherals
- 2S  - 6S Lipo input voltage with voltage monitoring
- 9V, 3A BEC for powering Video Transmitter
- 5V, 2A BEC for peripherals
- Interfaces8x PWM/BDShot outputs, 4 on ESC connector1x CAN_FD portDJI VTX Connector4x UARTs/serial for GPS and other peripherals1x I2C port for external compassUSB-C portSwitchable VTX powerAll UARTS support hardware inversion.External current monitor input
- 8x PWM/BDShot outputs, 4 on ESC connector
- 1x CAN_FD port
- DJI VTX Connector
- 4x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- USB-C port
- Switchable VTX power
- All UARTS support hardware inversion.
- External current monitor input
- DimensionsSize: 37.5mm x 37.5mmWeight: 8g
- Size: 37.5mm x 37.5mm
- Weight: 8g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn. All UARTS are DMA capable
Any UART may be re-tasked by changing its protocol parameter.

**Can FD portÂ**
This flight controller includes a 4-pin DroneCAN standard CAN port. Itâs capable of 64-byte frames,
and up to 5Mbps data rates. Itâs useful for connecting GPS devices, compasses, power monitoring, sensors, motors, servos, and other CAN peripherals.



---

## AocodaRC H743Dual
**Source URL:** https://ardupilot.org/plane/docs/common-aocoda-h743dual.html

### Description
the above image and some content courtesy ofaocoda-rc.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743VIH6 (480MHz)128MByte Flash for datalogging
- STM32H743VIH6 (480MHz)
- 128MByte Flash for datalogging
- SensorsInvenSense MPU6000 or 2x BOSCH BMI270 IMU (accel, gyro)DPS310 barometerVoltage & 130A current sensor
- InvenSense MPU6000 or 2x BOSCH BMI270 IMU (accel, gyro)
- DPS310 barometer
- Voltage & 130A current sensor
- Power3-6S Lipo input power5V 2.5A BEC for peripherals9V 3A BEC for video
- 3-6S Lipo input power
- 5V 2.5A BEC for peripherals
- 9V 3A BEC for video
- InterfacesUSB port (type-C)7x UARTS12x PWM outputs via two 8 pin ESC connectors and/or solder pads1x RC input PWM/SBUSI2C port for external compass, airspeed sensor, etc.DJI Goggles2x Power MonitorBuzzer and LED stripeBuilt-in OSD
- USB port (type-C)
- 7x UARTS
- 12x PWM outputs via two 8 pin ESC connectors and/or solder pads
- 1x RC input PWM/SBUS
- I2C port for external compass, airspeed sensor, etc.
- DJI Goggles
- 2x Power Monitor
- Buzzer and LED stripe
- Built-in OSD
- Size and Dimensions37 mm x 37 mm8.8 g
- 37 mm x 37 mm
- 8.8 g
- Mounting Hole30.5 mm x 30.5 mm
- 30.5 mm x 30.5 mm


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = USB (MAVLink2)
- SERIAL1 = UART1 (RCinput)
- SERIAL2 = UART2 (GPS)
- SERIAL3 = UART3 (VTX or DJI HD Air Unit)
- SERIAL4 = UART4 (USER)
- SERIAL5 = not available
- SERIAL6 = UART6 (ESC Telemetry)
- SERIAL7 = UART7 (USER)
- SERIAL8 = UART8 (USER)

**OSD SupportÂ**
The Aocoda-RC H743Dual has an on-board OSD usingOSD_TYPE=  1 (MAX7456 driver). The CAM and VTX pins provide connections for using the internal OSD.



---

## ARK FPV
**Source URL:** https://ardupilot.org/plane/docs/common-ark-fpv.html

### Description


### Specifications
**FeaturesÂ**
- STM32H743 32-bit processor
- 480MHz
- 2MB Flash
- 1MB RAM
- Invensense IIM-42653 Industrial IMU with heater resistor
- Bosch BMP390 Barometer
- ST IIS2MDC Magnetometer
- 9x PWM  Bidirectional-DSHOT capable
- 5x UARTS, one with hardware flow control
- 1x CAN
- 1x SPI, 1x I2C
- 5.5V - 54V (2S - 12S) input
- 12V, 2A output for video systems
- 5V, 2A output. 300ma for main system, 200ma for heater, 1.5A peripherals
- Micro SD
- USB-C


### Ports, UARTs & Pin Mapping
**PWM UART4 - 8 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | VBAT IN | 5.5V-54V
2 | CURR_IN | 3.3V
3 | UART4_RX | 3.3V
4 | FMU_CH1 | 3.3V
5 | FMU_CH2 | 3.3V
6 | FMU_CH3 | 3.3V
7 | FMU_CH4 | 3.3V
8 | GND | GND

**RC - 4 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | USART6_RX_IN | 3.3V
3 | USART6_TX_OUTPUT | 3.3V
4 | GND | GND

**PWM AUX - 6 Pin JST-SHÂ**
Pin | Signal Name | Voltage
1 | FMU_CH5 | 3.3V
2 | FMU_CH6 | 3.3V
3 | FMU_CH7 | 3.3V
4 | FMU_CH8 | 3.3V
5 | FMU_CH9 | 3.3V
6 | GND | GND

**POWER AUX - 3 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 12.0V | 12.0V
2 | GND | GND
3 | VBAT IN/OUT | 5.5V-54V

**CAN - 4 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | CAN1_P | 5.0V
3 | CAN1_N | 5.0V
4 | GND | GND

**GPS - 6 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | USART1_TX_GPS1 | 3.3V
3 | USART1_RX_GPS1 | 3.3V
4 | I2C1_SCL_GPS1 | 3.3V
5 | I2C1_SDA_GPS1 | 3.3V
6 | GND | GND

**TELEM - 6 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | UART7_TX_TELEM1 | 3.3V
3 | UART7_RX_TELEM1 | 3.3V
4 | UART7_CTS_TELEM1 | 3.3V
5 | UART7_RTS_TELEM1 | 3.3V
6 | GND | GND

**SPI (OSD or IMU) - 8 Pin JST-SHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | SPI6_SCK | 3.3V
3 | SPI6_MISO | 3.3V
4 | SPI6_MOSI | 3.3V
5 | SPI6_nCS1 | 3.3V
6 | SPI6_DRDY1 | 3.3V
7 | SPI6_nRESET | 3.3V
8 | GND | GND

**Flight Controller Debug - 6 Pin JST-SHÂ**
Pin | Signal Name | Voltage
1 | 3V3_FMU | 3.3V
2 | USART3_TX_DEBUG | 3.3V
3 | USART3_RX_DEBUG | 3.3V
4 | FMU_SWDIO | 3.3V
5 | FMU_SWCLK | 3.3V
6 | GND | GND

**UART MappingÂ**
Name | Function
SERIAL0 | USB
SERIAL1 | UART7 (Telem)
SERIAL2 | UART5 (DisplayPort HD VTX)
SERIAL3 | USART1 (GPS1)
SERIAL4 | USART2 (User, SBUS pin on HD VTX, RX only)
SERIAL5 | UART4 (ESC Telem, RX only)
SERIAL6 | USART6 (RC Input)
SERIAL7 | OTG2 (SLCAN)
All UARTS support DMA. Any UART may be re-tasked by changing its protocol parameter.

**OSD SupportÂ**
This flight controller has an MSP-DisplayPort output on a 6-pin DJI-compatible JST SH.

**Using the Debug Port as a Serial PortÂ**
The debug connector includes USART3, which is configured as a debug console by default. To use it as a regular serial port (SERIAL8), modifyhwdef.datto add USART3 to the end of the SERIAL_ORDER list:
SERIAL_ORDER OTG1 UART7 UART5 USART1 USART2 UART4 USART6 OTG2 USART3
And remove the debug console lines:
- STDOUT_SERIAL SD3
- STDOUT_BAUDRATE 57600
This requires building the firmware locally. See theBuilding the codeWiki section for build instructions.



---

## AtomRC F405-NAVI
**Source URL:** https://ardupilot.org/plane/docs/common-atomrcf405-navi.html

### Description
the above image and some content courtesy ofATOMRC

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)AT7456E OSD
- STM32F405RGT6 ARM (168MHz)
- AT7456E OSD
- SensorsBMI270 IMU (accel, gyro)SPL-06 barometerVoltage & 120A current sensor
- BMI270 IMU (accel, gyro)
- SPL-06 barometer
- Voltage & 120A current sensor
- Power6V ~ 30V DC input power5V, 5A BEC for servos5V or 9V, 2A BEC for video
- 6V ~ 30V DC input power
- 5V, 5A BEC for servos
- 5V or 9V, 2A BEC for video
- Interfaces6x UARTS8x PWM outputs1x RC input with inverter for SBUS/PPMI2C port for external compass and airspeed sensorType-C USB portSD Card Slot6 pin JST-GH for GPS/Compass6 pin JST-GH for DJI air units6 pin JST-GH for remote USB/Buzzer included with autopilot
- 6x UARTS
- 8x PWM outputs
- 1x RC input with inverter for SBUS/PPM
- I2C port for external compass and airspeed sensor
- Type-C USB port
- SD Card Slot
- 6 pin JST-GH for GPS/Compass
- 6 pin JST-GH for DJI air units
- 6 pin JST-GH for remote USB/Buzzer included with autopilot
- Size and Dimensions50mm x 30mm x 12mm21g
- 50mm x 30mm x 12mm
- 21g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (DMA capable)
- SERIAL2 = RCinput = USART2 (RX2 connected to SBUS via inverter, to use as UART input useBRD_ALT_CONFIG= 1 and do not attach anything to SBUS pin)
- SERIAL3 = GPS1 = USART3
- SERIAL4 = GPS2 = UART4
- SERIAL5 = USER = UART5 (typically used for DJI Goggles (seeMSP OSD) or Tramp VTX control (seeVideo Transmitter Support))
- SERIAL6 = USER = USART6 (solder pads)
Serial protocols shown are defaults, but can be adjusted to personal preferences.



---

## AtomRC F405-NAVI-Deluxe
**Source URL:** https://ardupilot.org/plane/docs/common-atomrcf405-navi-deluxe.html

### Description
the above image and some content courtesy ofATOMRC

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)AT7456E OSDESP32 Bluetooth RF module
- STM32F405RGT6 ARM (168MHz)
- AT7456E OSD
- ESP32 Bluetooth RF module
- SensorsICM-42688 IMU (accel, gyro)SPL-06 barometerVoltage & 120A current sensor
- ICM-42688 IMU (accel, gyro)
- SPL-06 barometer
- Voltage & 120A current sensor
- Power6V ~ 30V DC input power5V, 5A BEC for servos5V or 9V, 2A BEC for video
- 6V ~ 30V DC input power
- 5V, 5A BEC for servos
- 5V or 9V, 2A BEC for video
- Interfaces6x UARTS12x PWM outputs (PWM12 defaults to serial LED)SBUS input; compatible with all ArduPilot supported RC systems except PPMI2C port for external compass and airspeed sensorType-C USB portSD Card Slot6 pin JST-GH for GPS/Compass6 pin JST-GH for HD Video air units6 pin JST-GH for remote USB/Buzzer included with autopilot
- 6x UARTS
- 12x PWM outputs (PWM12 defaults to serial LED)
- SBUS input; compatible with all ArduPilot supported RC systems except PPM
- I2C port for external compass and airspeed sensor
- Type-C USB port
- SD Card Slot
- 6 pin JST-GH for GPS/Compass
- 6 pin JST-GH for HD Video air units
- 6 pin JST-GH for remote USB/Buzzer included with autopilot
- Size and Dimensions50mm x 30mm x 12mm21g
- 50mm x 30mm x 12mm
- 21g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
Name | UART | Default Protocol
SERIAL0 | USB | MAVLink2
SERIAL1 | USART1 | MAVLink2 (internal BLE RF Module currently not supported by ArduPilot GCS)
SERIAL2 | SART2 | RCinput, DMA capable (RX2 connected to SBUS pins via inverter)
SERIAL3 | USART3 | USER
SERIAL4 | UART4 | GPS1
SERIAL5 | UART5 | DisplayPort
SERIAL6 | USART6 | USER, DMA capable
Serial protocols shown are defaults, but can be adjusted to personal preferences.



---

## BetaFPV F405 family
**Source URL:** https://ardupilot.org/plane/docs/common-betafpvf405.html

### Description
The BETAFPV F405 family are autopilots intended for smaller size (âWhoopâ) multicopters. ArduPilot supports the following units:

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)16MByte flash for logging
- STM32F405RGT6 ARM (168MHz)
- 16MByte flash for logging
- SensorsICM-42688P IMU (accel, gyro)Voltage & 234A current sensor
- ICM-42688P IMU (accel, gyro)
- Voltage & 234A current sensor
- PowerWhoop: 1S - 2S Lipo input voltage with voltage monitoringAIO:   2S - 3S Lipo input voltage with voltage monitoringTotthpick: 2s -4s Lipo input voltage with voltage monitoring5V, 2A BEC for internal and peripherals including air unit power
- Whoop: 1S - 2S Lipo input voltage with voltage monitoring
- AIO:   2S - 3S Lipo input voltage with voltage monitoring
- Totthpick: 2s -4s Lipo input voltage with voltage monitoring
- 5V, 2A BEC for internal and peripherals including air unit power
- InterfacesIntegrated 4 in 1 ESC with current monitoring and telemetryWhoop: 12AAIO: 20AToothpick: 20ASBUS input with inversion for optional use instead of internal ELRS RXUARTs/serial for GPS and other peripheralsWhoop: 3AIO: 4Toothpick: 4USB-C port on remote dongle
- Integrated 4 in 1 ESC with current monitoring and telemetryWhoop: 12AAIO: 20AToothpick: 20A
- Whoop: 12A
- AIO: 20A
- Toothpick: 20A
- SBUS input with inversion for optional use instead of internal ELRS RX
- UARTs/serial for GPS and other peripheralsWhoop: 3AIO: 4Toothpick: 4
- Whoop: 3
- AIO: 4
- Toothpick: 4
- USB-C port on remote dongle


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.

**OSD SupportÂ**
The units supports HD air units with telemetry using UART4 RX/TX. SeeMSP OSDfor more info.



---

## BrahmaF4
**Source URL:** https://ardupilot.org/plane/docs/common-brahmaf4.html

### Description
The BrahmaF4 is an autopilot manufactured byDarkmatterÂ®

### Specifications
**FeaturesÂ**
- MCU: STM32F405RGT6, 168MHz
- Gyro: BMI270
- 32MB Onboard Flash (32 Megabyte)
- BEC output: 5V,2A@4V
- Barometer: BMP280
- OSD: AT7456E
- 4 UARTS: (UART1, UART3, UART4, UART6)
- 9 PWM Outputs (includes 1 neopixel out that can be used for PWM)
- 5V Power Out: 2.0A max
- 9V Power Out: 2.0A max


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rx and Tx in the above pinouts.
Name | Pad | Port | Default Protocol
SERIAL 0 | DM/DP | USB | Mavlink2
SERIAL 1 | RX1/TX1 | USART 1 | RCin (DMA capable)
SERIAL 2 | RX3/TX3 | USART 3 | ESC (T3 pin also on ESC connector)
SERIAL 3 | RX6/TX6 | USART 6 | GPS1 (DMAcapable)
SERIAL 4 | RX4/TX4 | USART 4 | MSP DisplayPort
- ESC Telemetry needs to be manually configured based upon esc used.



---

## BOTWINGF405
**Source URL:** https://ardupilot.org/plane/docs/common-botwingf405.html

### Description
The BOTWINGF405 is a compact, high-performance flight controller developed for fixed-wing and FPV applications. Designed for reliability and flexibility, it integrates essential sensors and features for smooth flight and rich telemetry, produced byBOTLAB DYNAMICS.

### Specifications
**FeaturesÂ**
- ProcessorSTM32F405RGT6, 168 MHz, 1MB flash24MHz external crystal
- STM32F405RGT6, 168 MHz, 1MB flash
- 24MHz external crystal
- SensorsICM42688P Accelerometer/GyroscopeDPS310 BarometerOptional External Compass (AK8963 supported)
- ICM42688P Accelerometer/Gyroscope
- DPS310 Barometer
- Optional External Compass (AK8963 supported)
- Power2Sâ6S LiPo input with onboard voltage and current monitoringBEC Outputs:5V @ 2.0A9V @ 2.0A, GPIO controlled
- 2Sâ6S LiPo input with onboard voltage and current monitoring
- BEC Outputs:5V @ 2.0A9V @ 2.0A, GPIO controlled
- 5V @ 2.0A
- 9V @ 2.0A, GPIO controlled
- Storage32MB onboard dataflash for loggingJEDEC-compatible SPI Flash (W25Q256)
- 32MB onboard dataflash for logging
- JEDEC-compatible SPI Flash (W25Q256)
- Interfaces6x UARTs (for GPS, telemetry, RC, camera, etc.)I2C port for barometer and external compassUSB OTG port (USB connector)5 configured PWM outputs (4 for motors, 1 for RGB LED)1x RC input (SBUS, PPM or CRSF/ELRS selectable)
- 6x UARTs (for GPS, telemetry, RC, camera, etc.)
- I2C port for barometer and external compass
- USB OTG port (USB connector)
- 5 configured PWM outputs (4 for motors, 1 for RGB LED)
- 1x RC input (SBUS, PPM or CRSF/ELRS selectable)
- External Connections6-pin JST-GH for GPS/Compass6-pin JST-GH for HD VTXX or other peripherals8-pin JST-GH for ESC4-pin JST-GH for Receiver input5-pin JST-GH for User5-pin JST-GH for Camera Input4 x 4-pin JST-GH for LED Strip-NEOPIXEL
- 6-pin JST-GH for GPS/Compass
- 6-pin JST-GH for HD VTXX or other peripherals
- 8-pin JST-GH for ESC
- 4-pin JST-GH for Receiver input
- 5-pin JST-GH for User
- 5-pin JST-GH for Camera Input
- 4 x 4-pin JST-GH for LED Strip-NEOPIXEL


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs default protocol and serial port assignments are:
- SERIAL0 -> USB
- SERIAL1 -> USART1 (DMA capable,RX tied to SBUS RC input and pin used as an interrupt input, but can be used as normal UART ifBRD_ALT_CONFIG=1 )
- SERIAL2 -> USART2 (ESC Telemetry)
- SERIAL3 -> USART3 (DisplayPort, TX DMA Capable)
- SERIAL4 -> UART4  (USER, TX DMA Capable)
- SERIAL5 -> UART5  (USER, TX DMA Capable)
- SERIAL6 -> USART6 (GPS)

**OSD SupportÂ**
The BOTWINGF405 includes an internal AT7456E OSD enabled for analog video. Simultaneous DisplayPort operation is enabled by default on UART3



---

## brainFPV RADIX2 HD
**Source URL:** https://ardupilot.org/plane/docs/common-radix2hd.html

### Description
The BrainFPV RADIX 2 HD is a flight controller primarily intended for
First Person View (FPV) applications that use a HD (digital) FPV system.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H750 ARM (480MHz)16MB external program flash loaded from SD card on boot
- STM32H750 ARM (480MHz)
- 16MB external program flash loaded from SD card on boot
- SensorsBMI270 IMU (accel, gyro)DPS310 barometerVoltage sensor (up to 12S)
- BMI270 IMU (accel, gyro)
- DPS310 barometer
- Voltage sensor (up to 12S)
- Power2S - 8S Lipo input voltage9V, 2A BEC for powering Video Transmitter5V, 1.5A BEC for internal and peripherals
- 2S - 8S Lipo input voltage
- 9V, 2A BEC for powering Video Transmitter
- 5V, 1.5A BEC for internal and peripherals
- Interfaces8x PWM outputs Bir-Directional DShot capable1x RC inputCAN Bus port7x UARTs/serial for GPS and other peripherals. UART6 RX and TX can be re-tasked as the 9th and 10th PWM outputsI2C port for external compass, airspeed, etc.microSDCard for program firmward, logging, etc.USB-C portAnalog Current sense inputBuzzer outputAnalog RSSI Input
- 8x PWM outputs Bir-Directional DShot capable
- 1x RC input
- CAN Bus port
- 7x UARTs/serial for GPS and other peripherals. UART6 RX and TX can be re-tasked as the 9th and 10th PWM outputs
- I2C port for external compass, airspeed, etc.
- microSDCard for program firmward, logging, etc.
- USB-C port
- Analog Current sense input
- Buzzer output
- Analog RSSI Input
- Size and Dimensions37mm x 37mm (30.5mm hole spacing)7g
- 37mm x 37mm (30.5mm hole spacing)
- 7g


### Ports, UARTs & Pin Mapping
**PinoutÂ**
Refer to the User Manual link above for how to use the âPWR:VBATâ jumper.

**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DMA-enabled, MSP DisplayPort OSD on DJI Connector)
- SERIAL2 -> UART2 (DMA-enabled, GPS)
- SERIAL3 -> UART3 (DMA-enabled, RCin)
- SERIAL4 -> UART4 (RX on ESC connector for ESC Telemetry)
- SERIAL5 -> UART5 (spare)
- SERIAL6 -> UART6 (spare, PWM 9 and 10 by default, useBRD_ALT_CONFIG= 1 for UART)
- SERIAL7 -> UART7 (RX pin only on DJI Connector)



---

## Brother Hobby F405v3
**Source URL:** https://ardupilot.org/plane/docs/common-brotherhobbyf405v3.html

### Description
The BROTHERHOBBYF405v3 is a flight controller produced byBROTHERHOBBY.

### Specifications
**FeaturesÂ**
- STM32F405 microcontroller
- ICM42688P IMU
- SPL06 barometer
- AT7456E OSD
- 10V 2A BEC; 5V 2A BEC
- 16Mb Onboard Flash
- 6 UARTs
- 8 PWM outputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
Default protocols and serial port mapping
- SERIAL0 -> USB (MAVLink2)
- SERIAL1 -> UART1 (RX1 only and is inverted from SBUS pin in HD VTX connector)
- SERIAL2 -> UART2 (RX, DMA-enabled)
- SERIAL3 -> UART3 (DJI)
- SERIAL4 -> UART4 (USER)
- SERIAL5 -> UART5 (ESC Telemetry)
- SERIAL6 -> UART6 (GPS)

**OSD SupportÂ**
The BROTHERHOBBYF405v3 supports OSD using OSD_TYPE 1 (MAX7456 driver). Simultaneously, DisplayPort HD VTX connections can be made to UART3 (included on the HD VTX connector).

**VTX SupportÂ**
The SH1.0-6P connector supports a standard DJI HD VTX connection. Pin 1 of the connector is 10v so be careful not to connect
anything that could be damaged by this voltage.



---

## Brother Hobby H743
**Source URL:** https://ardupilot.org/plane/docs/common-brotherhobbyh743.html

### Description
The BROTHERHOBBYH743 is a flight controller produced byBROTHERHOBBY.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- ICM42688P IMU
- SPL06 barometer
- AT7456E OSD
- 12V 3A BEC; 5V 3A BEC
- SDCard
- 7 UARTs
- 13 PWM outputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (ESC Telemetry)
- SERIAL2 -> UART2 (RX/SBUS, DMA-enabled)
- SERIAL3 -> UART3 (Spare, DMA-enabled)
- SERIAL4 -> UART4 (Spare)
- SERIAL6 -> UART6 (DJI, DMA-enabled)
- SERIAL7 -> UART7 (GPS, DMA-enabled)
- SERIAL8 -> UART8 (Spare)

**OSD SupportÂ**
The BROTHERHOBBYH743 supports using its internal OSD (MAX7456 driver). Simultaneous DisplayPort OSD operation  is also pre-configured on SERIAL 6. SeeMSP OSDfor more info.

**VTX SupportÂ**
The SH1.0-6P connector supports a standard DJI HD VTX connection. Pin 1 of the connector is 12v so be careful not to connect to devices that cannot accept that voltage.



---

## CORVON743V1
**Source URL:** https://ardupilot.org/plane/docs/common-corvon743v1.html

### Description
The CORVON743V1 is a flight controller designed and produced by CORVON.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- BMI088/BMI270 dual IMUs
- DPS310 barometer
- IST8310 magnetometer
- AT7456E OSD
- 9V 3A BEC; 5V 3A BEC
- MicroSD Card Slot
- 7 UARTs
- 10 PWM outputs
- 1 CAN
- 1 I2C
- 1 SWD


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink2, DMA-enabled)
- SERIAL2 -> UART2 (DisplayPort, DMA-enabled)
- SERIAL3 -> UART3 (GPS, DMA-enabled)
- SERIAL4 -> UART4 (MAVLink2, DMA-enabled)
- SERIAL5 -> UART6 (RCIN, DMA-enabled)
- SERIAL6 -> UART7 (RX only, ESC Telemetry, DMA-enabled)
- SERIAL7 -> UART8 (User, DMA-enabled)

**OSD SupportÂ**
The CORVON743V1 supports onboard OSD using OSD_TYPE 1 (MAX7456 driver). Simultaneously, DisplayPort OSD is available on the HD VTX connector, See below.

**HD VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 9v so be careful not to connect this to a peripheral that can not tolerate this voltage.



---

## CBUnmanned H743 Stamp
**Source URL:** https://ardupilot.org/plane/docs/common-StampH743.html

### Description
TheCBUnmanned H743 Stampis a flight controller loosely based on the FMUv6 standards & is designed for low volume OEMs as a drop in way to add ArduPilot to their custom hardware builds. It is a part of CBUnmannedâs widerâStampâ Eco-System, which brings together all the typical avionics hardware into a neat custom carrier PCB. Mounting footprints and symbols are available along with examples of basic usage on theWiki.

### Specifications
**FeaturesÂ**
- Class leading H7 SOC.
- Triple IMU sensors for extra redundancy.
- Based on the FMU-V6 standards.
- Micro SD Card for Logging/LUA Scripting.
- Direct solder mounting or optional 1.27mm header.
- x1 Ethernet and x2 CAN for easy integration with the next generation of UAV accessories.
- All complicated/supporting circuitry is on-board, just power with 5v.
- Just 22mm x 24.25mm & 1.9g.

**SpecificationsÂ**
- Processor
- Sensors
- Power
- Interfaces


### Ports, UARTs & Pin Mapping
**UART Mapping (Yellow Fade)Â**
- SERIAL0 -> USB
- SERIAL1 -> USART1
- SERIAL2 -> USART2    (With RTS/CTS, DMA-enabled)
- SERIAL3 -> USART3    (GPS1, DMA-enabled)
- SERIAL4 -> UART4     (GPS2, DMA-enabled)
- SERIAL5 -> UART5     (With RTS/CTS, DMA-enabled)
- SERIAL6 -> USART6    (RCIN / IO coprocessor if fitted, DMA-enabled)
- SERIAL7 -> UART7     (With RTS/CTS, DMA-enabled)
- SERIAL8 -> UART8

**CAN Ports (Light Green Fade)Â**
2 CAN buses are available, each with a built in 120 ohm termination resistors.



---

## CORVONF405V2.1
**Source URL:** https://ardupilot.org/plane/docs/common-corvonf405v2_1.html

### Description
The CORVON405V2.1 is a flight controller produced by CORVON.

### Specifications
**FeaturesÂ**
- STM32F405 microcontroller
- BMI088 IMU
- SPL06 barometer
- AT7456E OSD
- 9V 3A BEC; 5V 3A BEC
- SDCard
- 6 UARTs
- 10 PWM outputs
- 1 SWD


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink 2,DMA-enabled)
- SERIAL2 -> UART2 (DJI - VTX, TX only is DMA Enabled)
- SERIAL3 -> UART3 (GPS)
- SERIAL4 -> UART4 (MAVLink2,TX only is DMA Enabled)
- SERIAL5 -> UART5 (ESC Telemetry,RX 5 only pinned out)
- SERIAL6 -> UART6 (RCin, RX6 is inverted from SBUS pin, RX only is DMA Enabled)

**OSD SupportÂ**
The CORVON405V2.1 supports analog OSD via its internal MAX7456. Simultaneous external HD OSD support is preconfigured on SERIAL6. SeeMSP OSDfor more info.

**VTX SupportÂ**
Both Analog and HD VTX connectors are provided. Pin 1 of the connector is 9v so be careful not to connect this to a peripheral unable to support that voltage.



---

## CrazyF405
**Source URL:** https://ardupilot.org/plane/docs/common-crazyf405.html

### Description
The CrazyF405HD ELRS 1-2S AIO is an autopilot produced byHappymodel

### Specifications
**FeaturesÂ**
- MCU: STM32F405RGT6, 168MHz
- Gyro: BMI270 (SPI)
- 1Mb Onboard Flash
- BEC output: 5V, 2A
- Barometer: BMP280
- 3 UARTS: (UART1, UART2 ,UART6)
- 5 PWM outputs (4 motor outputs used internally for integrated 4-in-1 ESC and 1 integrated LED)
- Integrated 4-in-1 BlueJay ESC


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DisplayPort, DMA-enabled)
- SERIAL2 -> UART2 (RCin, connected to internal ELRS,DMA-enabled)
- SERIAL5 -> UART6 (USER, DMA-enabled)

**OSD SupportÂ**
The CrazyF405 is configured for Digital HD FPV using the HD VTX connector.



---

## CSKY405
**Source URL:** https://ardupilot.org/plane/docs/common-CSKYF405.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)AT7456E OSD
- STM32F405RGT6 ARM (168MHz)
- AT7456E OSD
- SensorsBMI088 IMU (accel, gyro)BMP390 barometerVoltage & 90A(215A PEak) current sensor
- BMI088 IMU (accel, gyro)
- BMP390 barometer
- Voltage & 90A(215A PEak) current sensor
- Power2S-6S DC input power5V, 2.5A BEC for servos12V, 2A BEC for video
- 2S-6S DC input power
- 5V, 2.5A BEC for servos
- 12V, 2A BEC for video
- Interfaces6x UARTS10x PWM outputs1x RC input with inverter for SBUS/PPMI2C port for external compass and airspeed sensorType-C USB portSD Card Slot
- 6x UARTS
- 10x PWM outputs
- 1x RC input with inverter for SBUS/PPM
- I2C port for external compass and airspeed sensor
- Type-C USB port
- SD Card Slot


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = UART4 (MAVLink2)
- SERIAL2 = USART1 (MAVLink2, DMA capable)
- SERIAL3 = UART5 (GPS)
- SERIAL4 = USART3 (GPS, TX3 DMA capable)
- SERIAL5 = USART6 ((User, TX3 DMA capable)
- SERIAL6 = USART2 (RCinput on RX2, to use as normal UART input useBRD_ALT_CONFIG= 1)
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The CSKY405 supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort can be supported using USART6 or any other free UART. SeeMSP OSDfor more info.



---

## DAKEFPVH743Pro
**Source URL:** https://ardupilot.org/plane/docs/common-dakefpvh743pro.html

### Description
The DAKEFPV H743/H743 Pro are flight controllers produced byDAKEFPV.

### Specifications
**FeaturesÂ**
- MCU - STM32H743 32-bit processor running at 480 MHz
- IMU - Dual ICM42688
- Barometer - SPL06
- OSD - AT7456E
- Onboard Flash: 16MByte
- 8x UARTs
- 1x CAN port
- 13x PWM Outputs (12 Motor Output, 1 LED)
- Battery input voltage: 4S-12S
- BEC 3.3V 0.5A
- BEC 5V 3A
- BEC 12V 3A for video, gpio controlled
- Dual switchable camera inputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (GPS) DMA capable
- SERIAL2 -> UART2 (MAVLink2)
- SERIAL3 -> UART3 (ESC Telemetry)
- SERIAL4 -> UART4 (DisplayPort) DMA capable
- SERIAL5 -> UART5 (RCin) RX DMA capable
- SERIAL6 -> UART6 (User) DMA capable
- SERIAL7 -> UART7 (User) DMA Capable
- SERIAL8 -> UART8 (User)

**OSD SupportÂ**
The DAKEFPVH743/Pro has an onboard OSD using a MAX7456 chip and is enabled by default. The CAM1/2 and VTX pins provide connections for using the internal OSD. Simultaneous DisplayPort OSD is also possible and is configured by default.
The HD VTX connector can have RX4 replaced by the analog VTX signal if that connector is used for analog VTX connection by using the DJI/VTX jumper pads.



---

## DAKEFPVF405
**Source URL:** https://ardupilot.org/plane/docs/common-dakefpvf405.html

### Description
The DAKEFPV F405 is a flight controller produced byDAKEFPV.

### Specifications
**FeaturesÂ**
- MCU - STM32F405 32-bit processor. 1024Kbytes Flash
- IMU - Dual ICM42688
- Barometer - SPL06
- OSD - AT7456E
- Onboard Flash: 16MByte
- 8x UARTs
- 13x PWM Outputs (12 Motor Output, 1 LED)
- Battery input voltage: 4S-12S
- BEC 3.3V 0.5A
- BEC 5V 3A
- BEC 12V 3A for video, gpio controlled
- Dual switchable camera inputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (GPS) DMA capable
- SERIAL2 -> UART2 (RCin) RX DMA capable
- SERIAL3 -> UART3 (ESC Telemetry) DMA capable
- SERIAL4 -> UART4 (DisplayPort) TX DMA capable
- SERIAL5 -> UART5 (User)
- SERIAL6 -> UART6 (User)

**OSD SupportÂ**
The autopilot has an onboard OSD using a MAX7456 chip and is enabled by default. The CAM1/2 and VTX pins provide connections for using the internal OSD. Simultaneous DisplayPort OSD is also possible and is configured by default.



---

## DroneerF405
**Source URL:** https://ardupilot.org/plane/docs/common-DroneerF405.html

### Description
The Droneer F405 is a flight controller produced byDroneer.

### Specifications
**FeaturesÂ**
- STM32F405 microcontroller
- ICM42688-P IMU
- max7456 OSD
- 5 UARTs
- 9 PWM outputs
- Dual Camera inputs
- 3S to 8S LIPO operation
- 5V,3A BEC, 10V,2A VTX BEC
- Physical: 37x37mm, 7g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn or RXn and Tn or TXn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (Tramp)
- SERIAL2 -> UART2 (RCIN, DMA-enabled)
- SERIAL3 -> UART3 (User)
- SERIAL4 -> UART4 (GPS)
- SERIAL5 -> UART5 (ESC Telem, RX5(only)on ESC connector)
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The Droneer F405 supports analog OSD using its integrated MAX7456. Simultaneous HD TVX OSD operation can also be obtained using an available UART whose protocol is set to âDisplayPort (42)â andOSD_TYPE2set to â5â.
The JST-GH-4P connector supports a standard âTrampâ VTX connection. Pin 1 of the connector is 10v so be careful not to connect this to a peripheral requiring 5v.



---

## Emlid NAVIO2 (Linux)
**Source URL:** https://ardupilot.org/plane/docs/common-navio2-overview.html

### Description
This page presentsNavio2- Raspberry Pi autopilot, which runs well proven ArduPilot flight stack and supports all its features.

### Specifications
**SpecificationsÂ**
- Processor(Raspberry PI 3)1.2GHz 64-bit quad-core ARMv8 CPU1GB RAM
- 1.2GHz 64-bit quad-core ARMv8 CPU
- 1GB RAM
- SensorsMPU9250 9DOF IMULSM9DS1 9DOF IMUMS5611 BarometerU-blox M8N Glonass/GPS/BeidouRC I/O co-processor
- MPU9250 9DOF IMU
- LSM9DS1 9DOF IMU
- MS5611 Barometer
- U-blox M8N Glonass/GPS/Beidou
- RC I/O co-processor
- PowerTriple redundant power supply
- Triple redundant power supply
- InterfacesUART, I2C, ADC for extensionsPPM/S.Bus input14 PWM servo outputs
- UART, I2C, ADC for extensions
- PPM/S.Bus input
- 14 PWM servo outputs
- DimensionsWeight 23g (shield) + 54g (RPi2)Size: 55x65mm (shield only)
- Weight 23g (shield) + 54g (RPi2)
- Size: 55x65mm (shield only)



---

## Flywoo F405 Pro
**Source URL:** https://ardupilot.org/plane/docs/common-flywoof405pro.html

### Description


### Specifications
**SpecificationsÂ**
- Processor and SensorsSTM32F405 ARM microcontrollerICM42688 IMU (Gyro and Accelerometers)BMP280 BarometerAT7456E OSD16Mbytes logging flash
- STM32F405 ARM microcontroller
- ICM42688 IMU (Gyro and Accelerometers)
- BMP280 Barometer
- AT7456E OSD
- 16Mbytes logging flash
- Interfaces9x PWM outputs (PWM9 for Neopixel LED)1x RC input (PWM/PPM, SBUS)6x serial port inputs (including RC input listed above)1x I2C for external compass or airspeed sensor4 in 1 ESC connectorDJI Air Unit connectorUSB-C connector
- 9x PWM outputs (PWM9 for Neopixel LED)
- 1x RC input (PWM/PPM, SBUS)
- 6x serial port inputs (including RC input listed above)
- 1x I2C for external compass or airspeed sensor
- 4 in 1 ESC connector
- DJI Air Unit connector
- USB-C connector
- Power9V ~ 25V DC input power (3S-6S)5V 2A BEC for peripheral10V 2A for Video
- 9V ~ 25V DC input power (3S-6S)
- 5V 2A BEC for peripheral
- 10V 2A for Video
- Size and Dimensions20mm x 20mm or 30.5mm x 30.5mm mount pattern5.5g
- 20mm x 20mm or 30.5mm x 30.5mm mount pattern
- 5.5g


### Ports, UARTs & Pin Mapping
**UART DefaultsÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (GPS)
- SERIAL2 -> USART2 (RX only,ESC Telemetry)
- SERIAL3 -> USART3 (DJI, DMA Enabled)
- SERIAL4 -> UART4 (SBUS pin is inverted and connects to RX pin)(TX DMA Enabled) For normal UART use,BRD_ALT_CONFIG= 1.
- SERIAL5 -> UART5 (RX5 is fed from an inverter connected to DJI connectorâs SBUS pin, no TX pin)
- SERIAL6 -> UART6 (RC serial input, DMA-enabled)

**OSD SupportÂ**
The FlywooF405 Pro has an on-board OSD usingOSD_TYPE=  1 (MAX7456 driver). The CAM and VTX pins provide connections for using the internal OSD.



---

## Flywoo F405HD 1-2S
**Source URL:** https://ardupilot.org/plane/docs/common-flywoof405hd.html

### Description
The Flywoo Goku F405HD is a small autopilot for 1-2S tiny whoop quadcopter applications with integrated 12A(25A peak) ESC and ELRS receiver.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 ARM (168MHz)8MByte flash for logging
- STM32F405 ARM (168MHz)
- 8MByte flash for logging
- SensorsICM-42688P IMU or MPU6000(accel, gyro)DPS-310 or SPL06 barometerVoltage & 180A current sensor
- ICM-42688P IMU or MPU6000(accel, gyro)
- DPS-310 or SPL06 barometer
- Voltage & 180A current sensor
- Power1S - 2S Lipo input voltage with voltage monitoring5V, 2A BEC for internal and peripherals including air unit power9V, 2A on/off controlled BEC for video
- 1S - 2S Lipo input voltage with voltage monitoring
- 5V, 2A BEC for internal and peripherals including air unit power
- 9V, 2A on/off controlled BEC for video
- Interfaces4 Motor outputsSBUS input with inversion for optional use instead of internal ELRS RX6x UARTs/serial for GPS and other peripherals, 1st UART internally tied to ELRS boardUSB-C port on remote dongle
- 4 Motor outputs
- SBUS input with inversion for optional use instead of internal ELRS RX
- 6x UARTs/serial for GPS and other peripherals, 1st UART internally tied to ELRS board
- USB-C port on remote dongle
- Size and Dimensions20.5 x 20.5 mounting holes, 30 x 30mm overall4.9g
- 20.5 x 20.5 mounting holes, 30 x 30mm overall
- 4.9g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the
receive pin for UARTn. The TXn pin is the transmit pin for UARTn.
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The autopilot supports HD air units with telemetry using UART4 RX/TX on the DJI connector. SeeMSP OSDfor more info.



---

## Flywoo F745 AIO BL_32/ Nano
**Source URL:** https://ardupilot.org/plane/docs/common-flywoo-f745.html

### Description
The Flywoo GOKU GN 745 AIO is an autopilot produced by [Flywoo](https://flywoo.net/).
The Flywoo GOKU GN 745 45A AIO V3 is an updated version of the above, with 45A ESC.
The Nano version is a smaller reduced feature set version

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F745VG  ARM (216MHz), 1MB FlashIntegrated 4 output, BLHeli-32 40A ESC (AIO V1.2) or BLHeli-32 45A ESC (AIO V3)Onbord 8 Mbytes (versions 1.0 and 1.2) or 16 MBytes (version 3) for Blackbox logging
- STM32F745VG  ARM (216MHz), 1MB Flash
- Integrated 4 output, BLHeli-32 40A ESC (AIO V1.2) or BLHeli-32 45A ESC (AIO V3)
- Onbord 8 Mbytes (versions 1.0 and 1.2) or 16 MBytes (version 3) for Blackbox logging
- SensorsInvenSense MPU6000 IMU or ICM42668P (accel, gyro)BMP280 barometerVoltage & 100A Current sensor (AIO version only)
- InvenSense MPU6000 IMU or ICM42668P (accel, gyro)
- BMP280 barometer
- Voltage & 100A Current sensor (AIO version only)
- Power7.4V ~ 25V DC input power (4S MAX for Nano version)5V 2A BEC for peripherals9V 1.5A BEC for video (no 9V rail on V3 AIO)
- 7.4V ~ 25V DC input power (4S MAX for Nano version)
- 5V 2A BEC for peripherals
- 9V 1.5A BEC for video (no 9V rail on V3 AIO)
- Interfaces7x UARTS10x PWM outputs, first 4 are internally connected to 4in1 BLHeli32 ESC (AM32 in V3).I2C port for external compass, airspeed sensor, etc.USB portCamera input/ VTX outputBuilt-in OSDSize and Dimensions AIO33.5mm x 33.5mm (25.6 x 25.6mm mount pattern)8.5g for V1.2, 9.4g for V3Size and Dimensions Nano22mm x 23.5mm (16mm x16mm mount pattern)2.3g
- 7x UARTS
- 10x PWM outputs, first 4 are internally connected to 4in1 BLHeli32 ESC (AM32 in V3).
- I2C port for external compass, airspeed sensor, etc.
- USB port
- Camera input/ VTX output
- Built-in OSD
- 33.5mm x 33.5mm (25.6 x 25.6mm mount pattern)
- 8.5g for V1.2, 9.4g for V3
- 22mm x 23.5mm (16mm x16mm mount pattern)
- 2.3g


### Ports, UARTs & Pin Mapping
**PinoutsÂ**
AIO V1.2
AIO V3
Nano

**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (RX pin only in AIO V3)
- SERIAL2 = Telemetry2 = USART2
- SERIAL3 = RC Input = USART3
- SERIAL4 = USER = USART4
- SERIAL5 = USER = UART5
- SERIAL6 = GPS = USART6
- SERIAL7 = ESC Telem = UART7 (RX tied to ESC telemetry) Seeblheli32-esc-telemetry
UART3 supports RX and TX DMA. UART1, UART2, UART4, and UART6 supports TX DMA. UART5 and UART7 do not support DMA. Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences.



---

## Flywoo H743
**Source URL:** https://ardupilot.org/plane/docs/common-flywoo-h743.html

### Description
The Flywoo H743 Pro is a flight controller produced byFlywoo.

### Specifications
**FeaturesÂ**
- MCU - STM32H743 32-bit processor running at 480 MHz
- IMU - Dual ICM42688
- Barometer - SPL06
- OSD - AT7456E
- Onboard Flash: 500MByte which appears as a non-removeable SD card
- 7x UARTs
- 13x PWM Outputs (12 Motor Output, 1 LED)
- Battery input voltage: 2S-6S
- BEC 3.3V 0.5A
- BEC 5V 3A
- BEC 10V 3A for video, gpio controlled
- Dual switchable camera inputs


### Ports, UARTs & Pin Mapping
**PinoutÂ**
TOP
BOTTOM

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (User, DMA-enabled)
- SERIAL2 -> UART2 (RX, DMA-enabled)
- SERIAL3 -> UART3 (User)
- SERIAL4 -> UART4 (GPS, DMA-enabled)
- SERIAL6 -> UART6 (ESC Telemetry)
- SERIAL7 -> UART7 (User)
- SERIAL8 -> UART8 (DisplayPort, DMA-enabled)

**OSD SupportÂ**
The Flywoo H743 Pro supports OSD using OSD_TYPE 1 (MAX7456 driver) and simultaneously DisplayPort using TX8/RX8 on the HD VTX connector.



---

## Foxeer F405v2
**Source URL:** https://ardupilot.org/plane/docs/common-foxeerf405v2.html

### Description
above image and some content courtesy ofFoxeer

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 32-bit processorAT7456E OSD128 MBit flash for logging
- STM32F405 32-bit processor
- AT7456E OSD
- 128 MBit flash for logging
- SensorsICM42688 IMU (accel and gyro only, no compass)DPS310 barometer
- ICM42688 IMU (accel and gyro only, no compass)
- DPS310 barometer
- Power2S  - 8S Lipo input voltage with voltage monitoring5V, 2A BEC for perpherals10V, 2A BEC for powering Video Transmitter
- 2S  - 8S Lipo input voltage with voltage monitoring
- 5V, 2A BEC for perpherals
- 10V, 2A BEC for powering Video Transmitter
- Interfaces10x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad, 10th is labeled SER)1x RC input6x UARTs/serial for GPS and other peripherals1x I2C port for external compassUSB-C portSwitchable Camera InputCamera control GPIOExternal current monitor input
- 10x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad, 10th is labeled SER)
- 1x RC input
- 6x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- USB-C port
- Switchable Camera Input
- Camera control GPIO
- External current monitor input


### Ports, UARTs & Pin Mapping
**VTX PortÂ**
Pin | Function
10V | 10V for VTX
G | Ground
T3 | UART3 TX, VTX Control(Tramp default)
G | Ground
VTX | Video output to video transmitter

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn. Default protocols are shown below but may be changed by the user.
Any UART may be re-tasked by changing its protocol parameter.

**OSD SupportÂ**
The FoxeerF405v2  supports OSD usingOSD_TYPE1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART4. Both the internal analog OSD and the DisplayPort OSD can be used simultaneously by settingOSD_TYPE2= 5



---

## Foxeer H743 MPU600
**Source URL:** https://ardupilot.org/plane/docs/common-foxeerh743v1.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 ARM (480MHz)AT7456E OSD16MB data logging flash
- STM32H743 ARM (480MHz)
- AT7456E OSD
- 16MB data logging flash
- SensorsMPU-6000 IMU (accel, gyro)DPS310 barometer
- MPU-6000 IMU (accel, gyro)
- DPS310 barometer
- Power4S - 8S Lipo input voltage with voltage monitoring10V, 2A BEC for powering Video Transmitter5V, 2A BEC for internal and peripherals
- 4S - 8S Lipo input voltage with voltage monitoring
- 10V, 2A BEC for powering Video Transmitter
- 5V, 2A BEC for internal and peripherals
- Interfaces9x PWM outputs Bi-Directional DShot capable (Serial LED output is PWM9)1x RC input7x UARTsI2C port for external compass, airspeed, etc.USB-C port
- 9x PWM outputs Bi-Directional DShot capable (Serial LED output is PWM9)
- 1x RC input
- 7x UARTs
- I2C port for external compass, airspeed, etc.
- USB-C port
- Size and Dimensions37mm x 372mm x 19mm7.8g
- 37mm x 372mm x 19mm
- 7.8g


### Ports, UARTs & Pin Mapping
**Default UART OrderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The FoxeerH7 MPU6000 supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort is supported using UART7 or any other free UART. SeeMSP OSDfor more info.



---

## Foxeer Reaper F745-AIO V2/V3/V4
**Source URL:** https://ardupilot.org/plane/docs/common-foxeerf745aio.html

### Description
The Foxeer Reaper F745 AIO V2/V3/V4 features an F7 autopilot and an integrated 45A 2-6S BLHeli_S 4-in-1 Bluejay ESC.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F745VG  ARM (216MHz), 1MB FlashAT7456E OSD16Mbit Flash for datalogging
- STM32F745VG  ARM (216MHz), 1MB Flash
- AT7456E OSD
- 16Mbit Flash for datalogging
- Sensors(Accelerometer/Gyro) BMI-270 IMU on V2, ICM-42688 on V3, MPU6000 on V4Voltage & 130A Current sensor
- (Accelerometer/Gyro) BMI-270 IMU on V2, ICM-42688 on V3, MPU6000 on V4
- Voltage & 130A Current sensor
- Power7.4V ~ 25V DC input power (2-6S)5V 2.5A BEC for peripheral
- 7.4V ~ 25V DC input power (2-6S)
- 5V 2.5A BEC for peripheral
- Interfaces5x UARTS5x PWM outputs, first 4 are internally connected to 4in1 40A BLHeli32 ESC. 5th used for LED PWM outputI2C port for external compass, airspeed sensor, etc.Micro USB portCamera input/ VTX outputDJI Goggle connector
- 5x UARTS
- 5x PWM outputs, first 4 are internally connected to 4in1 40A BLHeli32 ESC. 5th used for LED PWM output
- I2C port for external compass, airspeed sensor, etc.
- Micro USB port
- Camera input/ VTX output
- DJI Goggle connector
- Integrated ESCs4 integrated BLHeli_S ESCsFirmware - BlueJay2S-6S input voltage, 45A burst currentDShot 300/600 capable
- 4 integrated BLHeli_S ESCs
- Firmware - BlueJay
- 2S-6S input voltage, 45A burst current
- DShot 300/600 capable
- Size and Dimensions32.5mm x 32.5mm (25.5 x 25.5mm mount pattern)8.6g
- 32.5mm x 32.5mm (25.5 x 25.5mm mount pattern)
- 8.6g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
default protocols shown
- SERIAL0 = console = USB
- SERIAL1 = Telemetry 1 = USART1 (RX1 used to for SBUS in DJI connector, protocol parameter must be changed)
- SERIAL2 = RC Input = USART2 (Defaults to RC input protocol) DMA-eanbled
- SERIAL3 = Telemetry 1/USER = UART3
- SERIAL4 = Telemetry 2/USER = UART4
- SERIAL5 and SERIAL 6 are not available
- SERIAL7 = GPS = USART7 (DMA-enabled)



---

## Furious FPV F-35 Lightning and Wing FC-10
**Source URL:** https://ardupilot.org/plane/docs/common-furiousfpv-f35.html

### Description
above image and some content courtesy of theFurious FPV websiteandbanggood.com

### Specifications
**SpecificationsÂ**
- Processor and SensorsSTM32F4 ARM microcontrollerInvenSense IMU (accel, gyro, compass)
- STM32F4 ARM microcontroller
- InvenSense IMU (accel, gyro, compass)
- Interfaces6x PWM outputs1x RC input (PWM/PPM, SBUS)6x serial port inputsbattery voltage and current monitorOnboard OSDUSB port2S to 6S input power
- 6x PWM outputs
- 1x RC input (PWM/PPM, SBUS)
- 6x serial port inputs
- battery voltage and current monitor
- Onboard OSD
- USB port
- 2S to 6S input power


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (= BLE port on orig. F-35)
- SERIAL2 = Telemetry2 = UART5 (= M-RX port on orig. F-35)
- SERIAL3 = GPS1 = USART2 (= GPS port)
- SERIAL4 = not used
- SERIAL5 = USER = UART4 (only TX4 pinned out, TX-pin on orig. F-35âs VTx port)
- SERIAL6 = USER = USART6 (only TX6 pinned out as âSPOâ with hardware inverter, TX-pin on orig. F-35âs F-RX port)
USART3 RX used as RC input (F-RX portâs Rx pin on orig. F-35)
Serial protocols can be adjusted to personal preferences.



---

## GEPRC Taker F745
**Source URL:** https://ardupilot.org/plane/docs/common-geprc-takerf745.html

### Description
The TAKER F745 is a flight controller produced byGEPRC.

### Specifications
**FeaturesÂ**
- STM32F745 microcontroller
- MPU6000+ICM42688 dual IMU
- BMP280 barometer
- microSD based 512MB flash logging
- AT7456E OSD
- 7 UARTs
- 8 PWM outputs


### Ports, UARTs & Pin Mapping
**PinoutÂ**
TOP
BOTTOM

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DisplayPort, DMA-enabled)
- SERIAL2 -> UART2 (RCIN, DMA-enabled)
- SERIAL3 -> UART3 (connected to internal BT module, not currently usable by ArduPilot)
- SERIAL4 -> UART4 (GPS)
- SERIAL6 -> UART6 (User)
- SERIAL7 -> UART7 (User)
- SERIAL8 -> UART8 (ESC Telemetry)

**OSD SupportÂ**
The TAKER F745 BT supports analog OSD using its internal OSD chip and simultaneously HD goggle DisplayPort OSDs via the HD VTX connector.

**VTX SupportÂ**
The SH1.0-6P connector supports a standard DJI HD VTX connection. Pin 1 of the connector is 12v (or VBAT by solder pad selection) so be careful not to connect to devices expecting 5v.



---

## GEPRC Taker H743 BT
**Source URL:** https://ardupilot.org/plane/docs/common-geprc-taker-h743-bt.html

### Description
The TAKER H743 BT is a flight controller produced byGEPRC.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- MPU6000+ICM42688 dual IMU
- SPL06-001 barometer
- microSD based 512MB flash logging
- AT7456E OSD
- 7 UARTs
- 8 PWM outputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the receive pin for UARTn. The Txn pin is the transmit pin for UARTn.
Default protocols are given below:
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DisplayPort, DMA-enabled)
- SERIAL2 -> UART2 (RCIN, DMA-enabled)
- SERIAL3 -> UART3 (connected to internal BT module, not currently usable by ArduPilot)
- SERIAL4 -> UART4 (GPS)
- SERIAL6 -> UART6 (User)
- SERIAL7 -> UART7 (User)
- SERIAL8 -> UART8 (ESC Telemetry)
Any UART may be re-tasked by changing its protocol parameter.

**OSD SupportÂ**
The TAKER H743 BT supports analog OSD using its internal OSD chip and simultaneously HD goggle DisplayPort OSDs via the HD VTX connector.

**VTX SupportÂ**
The SH1.0-6P connector supports a standard DJI HD VTX connection. Pin 1 of the connector is 12v (or VBAT selected by solder pad selection) so be careful not to connect to devices expecting 5v.



---

## GreenSightUltraBlue
**Source URL:** https://ardupilot.org/plane/docs/common-greensightultrablue.html

### Description
The UltraBlue flight controller is sold byGreenSight.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- Incorporates an NVIDIA Jetson SOM
- Three IMUs: two BMI088 units and one ICM20649
- Internal heater for IMU temperature control
- DPS310 SPI barometer
- microSD card slot
- DF9-41S-1V(32) Hirose Mezzanine Connector


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB (console)
- SERIAL1 -> USART2 (Jetson telem, no DMA)
- SERIAL2 -> USART6 (telem2)
- SERIAL3 -> USART1 (primary GPS)
- SERIAL4 -> UART4 (GPS2, no DMA)
- SERIAL5 -> UART8 (USER/[RCin: DSM/PPM/SBus])
- SERIAL6 -> USART3 (ESC telemetry)
- SERIAL7 -> UART7 (USER/[debug tx/rx], no DMA)
- SERIAL8 -> USB2

**JP14 - AP Debug (Autopilot debug UART)Â**
Pin | Signal | Volt
1 | VCC | +5V
2 | Autopilot Debug UART Transmit | +3.3V
3 | Autopilot Debug UART Receive | +3.3V
4 | GND | GND

**JP13 - Jetson Debug (Companion Computer UART)Â**
Pin | Signal | Volt
1 | Jetson UART Debug Transmit | +3.3V
2 | Jetson UART Debug Receive | +3.3V
3 | GND | GND

**JP2 - AP Telem 2 (Autopilot UART)Â**
Pin | Signal | Volt
1 | VCC | +5V
2 | Autopilot Telem 2 UART Transmit | +3.3V
3 | Autopilot Telem 2 UART Receive | +3.3V
4 | Autopilot Telem 2 UART Clear to Send | +3.3V
5 | Autopilot Telem 2 UART Request to Send | +3.3V
6 | GND | GND

**JP19 - JET_SER_1 (Companion Computer UART)Â**
Pin | Signal | Volt
1 | VCC | +5V
2 | Jetson UART 1 Transmit | +3.3V
3 | Jetson UART 1 Receive | +3.3V
4 | Jetson UART 1 Clear to Send | +3.3V
5 | Jetson UART 1 Request to Send | +3.3V
6 | GND | GND

**JP7 - GPS 2 (Autopilot UART/I2C)Â**
Pin | Signal | Volt
1 | VCC | +5V
2 | Autopilot GPS2 UART Transmit | +3.3V
3 | Autopilot GPS2 UART Receive | +3.3V
4 | Autopilot I2C Bus 2 Clock (GPS2 SCL) | +3.3V
5 | Autopilot I2C Bus 2 Data (GPS2 SDA) | +3.3V
6 | GND | GND

**JP6 - GPS 1 (Autopilot UART/I2C)Â**
Pin | Signal | Volt
1 | VCC | +5V
2 | Autopilot GPS1 UART Transmit | +3.3V
3 | Autopilot GPS1 UART Receive | +3.3V
4 | Autopilot I2C Bus 1 Clock (GPS1 SCL) | +3.3V
5 | Autopilot I2C Bus 1 Data (GPS1 SDA) | +3.3V
6 | GND | GND



---

## HeeWing F405/F405V2
**Source URL:** https://ardupilot.org/plane/docs/common-heewingf405.html

### Description
The HEEWING F405 is a flight controller produced by HEEWING that is incorporated into their Ranger-T1 VTOL RTF airframe.
the above image and some content courtesy ofHEEWING

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)AT7456E OSD
- STM32F405RGT6 ARM (168MHz)
- AT7456E OSD
- SensorsICM-42688P IMU (accel, gyro)SPL-06 barometerVoltage & current sensor input
- ICM-42688P IMU (accel, gyro)
- SPL-06 barometer
- Voltage & current sensor input
- Power2S - 6S Lipo PMU unit providing:88A Current monitor9V/3A BEC for powering Video Transmitter5V, 5A BEC for internal,servos, and peripherals
- 2S - 6S Lipo PMU unit providing:
- 88A Current monitor
- 9V/3A BEC for powering Video Transmitter
- 5V, 5A BEC for internal,servos, and peripherals
- Interfaces9x PWM outputs DShot capable1x RC input/ can be used as full UART withBRD_ALT_CONFIG= 14x UARTs/serial for GPS and other peripheralsI2C port for external compass, airspeed, etc.USB-C port on remote dongle
- 9x PWM outputs DShot capable
- 1x RC input/ can be used as full UART withBRD_ALT_CONFIG= 1
- 4x UARTs/serial for GPS and other peripherals
- I2C port for external compass, airspeed, etc.
- USB-C port on remote dongle
- Size and Dimensions44.3mm x 34.3mm x 13.7mm??g
- 44.3mm x 34.3mm x 13.7mm
- ??g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART3 (marked UART1 on casing, DMA-enabled)
- SERIAL2 -> UART1 (marked UART2 on casing, DMA-enabled)
- SERIAL3 -> UART5 (GPS)
- SERIAL4 -> UART4 (not pinned out)
- SERIAL5 -> UART6 (TX only on VTX connector)
- SERIAL6 -> UART2 (RCIN RX-only or RX/TX withBRD_ALT_CONFIG= 1, DMA-enabled)
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The HEEWINGF405 supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort is supported using any free UART. SeeMSP OSDfor more info.



---

## Holybro Kakute F4
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-kakutef4.html

### Description
above image and some content courtesy ofHolybro

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 32-bit processor
- STM32F405RGT6 32-bit processor
- SensorsInvenSense ICM20689 IMU (accel, gyro) on vibration isolating foamBMP280 barometers
- InvenSense ICM20689 IMU (accel, gyro) on vibration isolating foam
- BMP280 barometers
- Power7V ~ 42V input power directly from battery
- 7V ~ 42V input power directly from battery
- Interfaces4x PWM outputs1x RC input PWM/PPM5x UARTs/serial for GPS and other peripherals1x I2C port for external compassmicro USB port
- 4x PWM outputs
- 1x RC input PWM/PPM
- 5x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- micro USB port


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
The pin labeled Rx on each corner of the board is a common pin for
ESC telemetry input.

**OSD SupportÂ**
The KakuteF4 supports OSD usingOSD_TYPE1 (MAX7456 driver).



---

## Holybro Kakute F4 Mini
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-kakutef4-mini.html

### Description
above image and some content courtesy ofHolybro

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 32-bit processorMAX7456 OSD chip
- STM32F405RGT6 32-bit processor
- MAX7456 OSD chip
- SensorsMPU6000 IMU (accel, gyro)SPL06 barometer
- MPU6000 IMU (accel, gyro)
- SPL06 barometer
- Power7V ~ 42V input power directly from battery
- 7V ~ 42V input power directly from battery
- Interfaces5x PWM outputs1x RC input PWM/PPM5x UARTs/serial for GPS and other peripherals1x I2C port for external compassmicro USB portCamera and Video TX
- 5x PWM outputs
- 1x RC input PWM/PPM
- 5x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- micro USB port
- Camera and Video TX
- Logging128Mb flash for logging
- 128Mb flash for logging


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
The pin labeled Rx on each corner of the board is a common pin for
ESC telemetry input.

**OSD SupportÂ**
The KakuteF4 supports OSD usingOSD_TYPE1 (MAX7456 driver).



---

## Holybro Kakute F7 AIO
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-kakutef7aio.html

### Description
above image and some content courtesy ofHolybro

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F745 32-bit processor
- STM32F745 32-bit processor
- SensorsInvenSense ICM20689 IMU (accel and gyro only, no compass) on vibration isolating foamBMP280 barometers
- InvenSense ICM20689 IMU (accel and gyro only, no compass) on vibration isolating foam
- BMP280 barometers
- Power7V ~ 42V input power directly from batteryCurrent Sensor up to 120A maximum continuous current on the All-in-One version
- 7V ~ 42V input power directly from battery
- Current Sensor up to 120A maximum continuous current on the All-in-One version
- Interfaces6x PWM outputs1x RC input SBUS/PPM5x UARTs/serial for GPS and other peripherals1x I2C port for external compassmicro USB portAll UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâmicroSD Card Slot for loggingAT7456E OSD2A 5v regulator
- 6x PWM outputs
- 1x RC input SBUS/PPM
- 5x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- micro USB port
- All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- microSD Card Slot for logging
- AT7456E OSD
- 2A 5v regulator


### Ports, UARTs & Pin Mapping
**PinoutÂ**
The KakuteF7 comes in two variants with the primary difference being the AIO (All-In-One) board employs current sensor and provides power distribution in each of the four corners.
Both variants include a 5-volt regulator rated for 2 amps, OSD, vibration-isolated IMU, etc.
Kakute F7 AIO
Kakute F7

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
The SERIAL5 port (UART7) is normally for ESC telemetry, and has an R7 pad on
each of the four corners of the KakuteF7 AIO board.

**Servo Output MappingÂ**
The PWM outputs are marked M1-M6 in the above pinouts. The corresponding servo outputs are:

**OSD SupportÂ**
The KakuteF7 AIO supports OSD usingOSD_TYPE1 (MAX7456 driver).



---

## Holybro Kakute F4 Wing
**Source URL:** https://ardupilot.org/plane/docs/common-KakuteF4-Wing.html

### Description
The KakuteF4-Wing is a flight controller produced byHolybro.

### Specifications
**FeaturesÂ**
- ProcessorSTM32F405 32-bit processorAT7456E OSD16MB dataflash for logging
- STM32F405 32-bit processor
- AT7456E OSD
- 16MB dataflash for logging
- SensorsICM42688 Acc/GyroSLP06 barometer
- ICM42688 Acc/Gyro
- SLP06 barometer
- Power2S - 8S Lipo input voltage with voltage monitoring9V/12V, 1.5A BEC for powering Video Transmitter6V/7.2V, ?A BEC for servos3.3V, 1A BEC
- 2S - 8S Lipo input voltage with voltage monitoring
- 9V/12V, 1.5A BEC for powering Video Transmitter
- 6V/7.2V, ?A BEC for servos
- 3.3V, 1A BEC
- Interfaces7x PWM outputs DShot capable, 4 outputs BiDirDShot capable1x RC input5x UARTs/serial for GPS and other peripherals1x I2C ports for external compass, airspeed, etc.USB-C port
- 7x PWM outputs DShot capable, 4 outputs BiDirDShot capable
- 1x RC input
- 5x UARTs/serial for GPS and other peripherals
- 1x I2C ports for external compass, airspeed, etc.
- USB-C port


### Ports, UARTs & Pin Mapping
**PinoutÂ**
Top
Top-underside
Bottom

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (GPS) DMA-Enabled
- SERIAL2 -> UART2 (Telem1) DMA Enabled
- SERIAL3 -> UART3 (RX) DMA Enabled
- SERIAL5 -> UART5 (User)
- SERIAL6 -> USART6 (User)

**OSD SupportÂ**
The KakuteF4-Wing supports OSD using OSD_TYPE 1 (MAX7456 driver).



---

## Holybro Kakute F7 Mini (only V1 and V2 are compatible)
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-kakutef7mini.html

### Description
above image and some content courtesy ofHolybro

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F745VGH6 32-bit processor
- STM32F745VGH6 32-bit processor
- SensorsInvenSense ICM20689 IMU (accel, gyro, compass) on vibration isolating foamBMP280 barometers
- InvenSense ICM20689 IMU (accel, gyro, compass) on vibration isolating foam
- BMP280 barometers
- Power7V ~ 42V input power directly from battery
- 7V ~ 42V input power directly from battery
- Interfaces6x PWM outputs1x RC input7x UARTs/serial for GPS and other peripherals1x I2C port for external compassmicro USB port
- 6x PWM outputs
- 1x RC input
- 7x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- micro USB port


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (Telem1)
- SERIAL2 -> UART2 (Telem2)
- SERIAL3 -> UART3 (GPS)
- SERIAL4 -> UART4
- SERIAL6 -> UART6 (RC input)
- SERIAL7 -> UART7 (Receive only, ESC Telemetry)

**OSD SupportÂ**
The KakuteF7 Mini supports OSD usingOSD_TYPE1 (MAX7456 driver).



---

## Holybro Kakute H7 V1
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-kakuteh7.html

### Description
above image and some content courtesy ofHolybro

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processor
- STM32H743 32-bit processor
- SensorsInvenSense MPU6000 IMU (accel and gyro only, no compass)BMP280 barometer
- InvenSense MPU6000 IMU (accel and gyro only, no compass)
- BMP280 barometer
- Power2S  - 6S Lipo input voltage with voltage monitoring9V, 1.5A BEC for powering Video Transmitter
- 2S  - 6S Lipo input voltage with voltage monitoring
- 9V, 1.5A BEC for powering Video Transmitter
- Interfaces9x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad)1x RC input6x UARTs/serial for GPS and other peripherals1x I2C port for external compassmicro USB portAll UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâmicroSD Card Slot for loggingAT7456E OSDExternal current monitor input
- 9x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad)
- 1x RC input
- 6x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- micro USB port
- All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- microSD Card Slot for logging
- AT7456E OSD
- External current monitor input


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
The SERIAL7 port (UART7) is normally for ESC telemetry, and has an R7 pin on
both of the ESC connectors.

**OSD SupportÂ**
The KakuteH7  supports OSD usingOSD_TYPE1 (MAX7456 driver).



---

## Holybro Kakute H7 V2
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-kakuteh7-v2.html

### Description
above image and some content courtesy ofHolybro

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processorAT7456E OSD128 MByte flash for logging
- STM32H743 32-bit processor
- AT7456E OSD
- 128 MByte flash for logging
- SensorsBMI270 IMU (accel and gyro only, no compass)BMP280 barometer
- BMI270 IMU (accel and gyro only, no compass)
- BMP280 barometer
- Power2S  - 8S Lipo input voltage with voltage monitoring9V, 1.5A BEC for powering Video Transmitter
- 2S  - 8S Lipo input voltage with voltage monitoring
- 9V, 1.5A BEC for powering Video Transmitter
- Interfaces9x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad)1x RC input6x UARTs/serial for GPS and other peripherals1x I2C port for external compassUSB-C portSwitchable VTX powerAll UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâExternal current monitor input
- 9x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad)
- 1x RC input
- 6x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- USB-C port
- Switchable VTX power
- All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- External current monitor input


### Ports, UARTs & Pin Mapping
**PinoutÂ**
Pin | Function
VTX+ | 9V for HD System or other VTX, by default ON/OFF is
controlled by RELAY2. SeeRelay SwitchCan be controlled by RELAY2
SDA, SCL | I2C connection (for peripherals)
5v | 5v output (1.5A max)
3v3 | 3.3v output (0.25A max)
Vi | Video input from FPV camera
Vo | Video output to video transmitter
CAM | To camera OSD control
G or GND | Ground
RSI | Analog RSSI (0-3.3v) input from receiver
R3, T3 | UART3 RX and TX
R4, T4 | UART4 RX and TX
R6, T6 | UART6 RX and TX (UART6 RX is also located in the
GH plug)
LED | WS2182 addressable LED signal wire
Z- | Piezo buzzer negative leg

**ESC Port 1Â**
Pin | Function
B+ | Battery positive voltage (2S-8S)
R7 | UART7 RX
GND | Ground
CURRENT | CURRENT
M1 | Motor signal output 1
M2 | Motor signal output 2
M3 | Motor signal output 3
M4 | Motor signal output 4

**ESC Port 2Â**
Pin | Function
B+ | Battery positive voltage (2S-8S)
R7 | UART7 RX
GND | Ground
CURRENT | CURRENT
M5 | Motor signal output 5
M6 | Motor signal output 6
M7 | Motor signal output 7
M8 | Motor signal output 8

**VTX PortÂ**
Pin | Function
Vtx+ | 9V for HD System or other VTX, by default ON/OFF is
controlled by RELAY2. SeeRelay Switch
G | Ground
T1 | UART1 TX
R1 | UART1 RX
G | Ground
R6 | UART6 RX

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
The SERIAL7 port (UART7) is normally for ESC telemetry, and has an R7 pin on
both of the ESC connectors.
Any UART may be re-tasked by changing its protocol parameter.

**OSD SupportÂ**
The KakuteH7  supports OSD usingOSD_TYPE1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART1.



---

## Holybro Kakute H7 Wing
**Source URL:** https://ardupilot.org/plane/docs/common-kakuteh7wing.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processorAT7456E OSD
- STM32H743 32-bit processor
- AT7456E OSD
- SensorsICM42688 Acc/GyroBMP280 barometer
- ICM42688 Acc/Gyro
- BMP280 barometer
- PowerSeparate stacked power supply and power monitor board for isolation2S - 8S Lipo input voltage with voltage monitoring5V, 2A (3A Peak) BEC for Receiver, OSD, Camera, 2812 LED Strip, Buzzer, GPS, Air Speed Sensor, etc.9V/12V, 2A (3A peak) BEC for powering Video Transmitter6V/7.2V, 6A (8A Peak) BEC for servos3.3V, 1A BEC
- Separate stacked power supply and power monitor board for isolation
- 2S - 8S Lipo input voltage with voltage monitoring
- 5V, 2A (3A Peak) BEC for Receiver, OSD, Camera, 2812 LED Strip, Buzzer, GPS, Air Speed Sensor, etc.
- 9V/12V, 2A (3A peak) BEC for powering Video Transmitter
- 6V/7.2V, 6A (8A Peak) BEC for servos
- 3.3V, 1A BEC
- Interfaces14x PWM outputs DShot capable, 4 outputs BiDirDShot capable1x RC input6x UARTs/serial for GPS and other peripherals2x I2C ports for external compass, airspeed, etc.USB-C port and boot button on separate dongle for ease of accessSwitchable 9V/12V VTX power2 Switchable Camera inputsAll UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâIntegrated 6S, 120A battery monitorInput for second battery monitor
- 14x PWM outputs DShot capable, 4 outputs BiDirDShot capable
- 1x RC input
- 6x UARTs/serial for GPS and other peripherals
- 2x I2C ports for external compass, airspeed, etc.
- USB-C port and boot button on separate dongle for ease of access
- Switchable 9V/12V VTX power
- 2 Switchable Camera inputs
- All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- Integrated 6S, 120A battery monitor
- Input for second battery monitor
- Size and Dimensions45mm x 30mm x 13.5mm28g (with USB Extender Board)
- 45mm x 30mm x 13.5mm
- 28g (with USB Extender Board)


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The KakuteH7-Wing supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort is supported using UART5 or any other free UART. SeeMSP OSDfor more info.



---

## Holybro Pixhawk 4 Mini
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-ph4mini.html

### Description
The Pixhawk4-Mini autopilot is sold byHolybro

### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The SERIAL1 port has RTS/CTS pins, the other UARTs do not have RTS/CTS.
The RCIN port can be used as RX or TX as a general UART using the
SERIAL4_OPTIONS bits to swap pins. It is not used for RC input (the
PPM pin is used for RC input)
The UART7 connector is inside the case and labelled as debug, but is
available as a general purpose UART with ArduPilot.

**TELEM portÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | CTS | +3.3V
5 (blk) | RTS | +3.3V
6 (blk) | GND | GND

**GPS portÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | SERIAL3 TX (OUT) | +3.3V
3 (blk) | SERIAL3 RX (IN) | +3.3V
4 (blk) | SCL | +3.3 (pullups)
5 (blk) | SDA | +3.3 (pullups)
6 (blk) | SafetyButton | +3.3V
7 (blk) | SafetyLED | +3.3V
8 (blk) | VDD 3.3 (OUT) | +3.3V
9 (blk) | Buzzer | +3.3V
10 (blk) | GND | GND

**TELEM2 & I2CB portÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | TX (OUT) | +3.3V
3 (blk) | RX (IN) | +3.3V
4 (blk) | SCL I2C2 | +3.3V
5 (blk) | SDA I2C2 | +3.3V
6 (blk) | GND | GND

**RCIN portÂ**
Pin | Signal | Volt
1 (red) | VCC | +5V
2 (blk) | RCIN (IN) | +3.3V
3 (blk) | RSSI (IN) | +3.3V
4 (blk) | VDD3.3 | +3.3V
5 (blk) | GND | GND



---

## Holybro Pixhawk5X
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-ph5x.html

### Description
Pixhawk 5XÂ® is the latest update to the successful family of PixhawkÂ® autopilots made by Holybro, featuring vibration isolation of IMUs, triple redundant IMUs, double redundant barometers on separate buses, and IMU heating.

### Specifications
**FeaturesÂ**
- ProcessorsSTM32F765: 32 Bit ArmÂ® CortexÂ®-M7, 216MHz, 2MB memory, 512KB RAMIO Processor: STM32F100: 32 Bit ArmÂ® CortexÂ®-M3, 24MHz, 8KB SRAM
- STM32F765: 32 Bit ArmÂ® CortexÂ®-M7, 216MHz, 2MB memory, 512KB RAM
- IO Processor: STM32F100: 32 Bit ArmÂ® CortexÂ®-M3, 24MHz, 8KB SRAM
- On-board SensorsAccel/Gyro: ICM-20649Accel/Gyro: ICM-42688PAccel/Gyro: ICM-20602Magnetometer: BMM150Barometer: 2x BMP388
- Accel/Gyro: ICM-20649
- Accel/Gyro: ICM-42688P
- Accel/Gyro: ICM-20602
- Magnetometer: BMM150
- Barometer: 2x BMP388
- Interfaces16- PWM servo outputsR/C input for Spektrum / DSMDedicated R/C input for PPM and S.Bus inputDedicated analog / PWM RSSI input and S.Bus output4 general purpose serial ports3 with full flow control1 with separate 1.5A current limit1 with I2C and additional GPIO line for external NFC reader2 GPS ports1 full GPS & Safety Switch Port1 basic GPS port1 I2C port1 Ethernet port,100Mbps1 SPI bus2 chip select lines2 data-ready lines1 SPI SYNC line1 SPI reset line2 CAN Buses for CAN peripheralCAN Bus has individual silent controls or ESC RX-MUX control2 Power input ports with SMBus1 AD & IO port2 additional analog input, one 3.3V and one 6.6V max input1 PWM/Capture input2 Dedicated debug and GPIO lines
- 16- PWM servo outputs
- R/C input for Spektrum / DSM
- Dedicated R/C input for PPM and S.Bus input
- Dedicated analog / PWM RSSI input and S.Bus output
- 4 general purpose serial ports3 with full flow control1 with separate 1.5A current limit1 with I2C and additional GPIO line for external NFC reader
- 3 with full flow control
- 1 with separate 1.5A current limit
- 1 with I2C and additional GPIO line for external NFC reader
- 2 GPS ports1 full GPS & Safety Switch Port1 basic GPS port
- 1 full GPS & Safety Switch Port
- 1 basic GPS port
- 1 I2C port
- 1 Ethernet port,100Mbps
- 1 SPI bus2 chip select lines2 data-ready lines1 SPI SYNC line1 SPI reset line
- 2 chip select lines
- 2 data-ready lines
- 1 SPI SYNC line
- 1 SPI reset line
- 2 CAN Buses for CAN peripheralCAN Bus has individual silent controls or ESC RX-MUX control
- CAN Bus has individual silent controls or ESC RX-MUX control
- 2 Power input ports with SMBus
- 1 AD & IO port2 additional analog input, one 3.3V and one 6.6V max input1 PWM/Capture input2 Dedicated debug and GPIO lines
- 2 additional analog input, one 3.3V and one 6.6V max input
- 1 PWM/Capture input
- 2 Dedicated debug and GPIO lines
- Voltage RatingsMax input voltage: 6VUSB Power Input: 4.75~5.25VServo Rail Input: 0~36V
- Max input voltage: 6V
- USB Power Input: 4.75~5.25V
- Servo Rail Input: 0~36V
- DimensionsFlight Controller Module: 38.8 x 31.8 x 14.6mmStandard Baseboard: 52.4 x 103.4 x 16.7mm
- Flight Controller Module: 38.8 x 31.8 x 14.6mm
- Standard Baseboard: 52.4 x 103.4 x 16.7mm
- WeightFlight Controller Module: 23gStandard Baseboard: 51g
- Flight Controller Module: 23g
- Standard Baseboard: 51g
- Other CharacteristicsOperating & storage temperature: -40 ~ 85Â°c



---

## Horizon31 PixC4-Jetson
**Source URL:** https://ardupilot.org/plane/docs/common-horizon31-pixc4-jetson.html

### Description
The PixC4-Jetson is a professional-quality and NDAA Compliant Flight Management Unit (FMU), powerful single board computer and peripheral support system (USB, MIPI, Ethernet, M.2 slot, etc.) in a small form factor, designed to be integrated into end-user platforms. The term âPixC4â is derived from the Pixhawk, on which the FMU design is based (FMUv5) and C4, representing Command, Control, Compute and Communication.
Available as a turnkey solution including software pre-flashed on the Nvidia Jetson companion computer to enable the following features:

### Specifications
**SpecificationsÂ**
- STM32H743 Processor with STM32F103 IO Processor (FMUv5 design)
- Integrated Nvidia Jetson companion computer, compatible with Nvidia Jetson Nano, Xavier NX or TX2 NX
- Ethernet switch (3 port)
- USB 2.0 Hub (7 port)
- Cellular/LTE Modem support (M.2. Key B slot)
- Support for RockBlock 9603 Iridium Modem
- F-RAM Cypress MF25V02A-DG 256-Kbit nonvolatile memory (Flash memory that performs as fast as RAM)
- Invensense ICM-20602 (x2) 3-axis accelerometer/gyroscope
- Invensense ICM-42688 3-axis accelerometer/gyroscope/magnetometer
- MS5611 barometer
- RM3100 Compass
- Micro SD Card for FMU
- Nano SIM card slot for M.2 cellular Modem
Board to board connector with the following IO:
- Spektrum DSM / DSM2 / DSM-XÂ® Satellite compatible input and binding (FMU)
- Futaba S.BUSÂ® & S.BUS2Â® compatible input (FMU)
- 1x Telemetry port output (FMU)
- PPM sum input signal (FMU)
- 14x PWM outputs (6 DShot capable) (FMU)
- 1x RSSI (PWM or voltage) input (FMU)
- 2x I2C (FMU)
- 1x UART (FMU)
- 1x SPI (FMU)
- 2x CAN (FMU)
- Voltage/Current Sense (FMU)
- Safety Switch (FMU)
- Buzzer Out (FMU)
- Jetson UART/Console (Jetson)
- MIPI/CSI (Jetson)
- UART (Jetson)
- I2S (Jetson)
- I2C x2 (Jetson)
- GPIO x5 (Jetson)
- Ethernet (x2) 100 Mbps (Jetson)
- USB 2.0 (x4) (Jetson)
- Power Input (5V, ~2-5A depending on compute module used). Accepts redundant/separate supplies for FMU and Jetson.
Other IO:
- JTAG for FMU and IO
- USB 3.0 SS Type C (Jetson)
- USB 2.0 Type C (FMU)
- Jetson Fan Control
- M.2 Key B Connector
- FMU and IO RGB LED, Ethernet status LEDs, Power LEDs



---

## iFlight Beast F7 45A AIO
**Source URL:** https://ardupilot.org/plane/docs/common-iflight-beastf7AIO.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32F745 BGA ARM (216MHz), 1MB FlashIntegrated 4 output, BLHeli-S 45A ESC
- STM32F745 BGA ARM (216MHz), 1MB Flash
- Integrated 4 output, BLHeli-S 45A ESC
- SensorsInvenSense MPU6000 IMU (accel, gyro)BMP280 barometer (not in V2 version)Voltage & 300A Current sensor
- InvenSense MPU6000 IMU (accel, gyro)
- BMP280 barometer (not in V2 version)
- Voltage & 300A Current sensor
- Power7.4V ~ 25V DC input power5V 2.5A BEC for peripherals
- 7.4V ~ 25V DC input power
- 5V 2.5A BEC for peripherals
- Interfaces5x UARTS5x PWM outputs, first 4 are internally connected to 4in1 45A BLHeli-S ESC, the fifth for LEDI2C port for external compass, airspeed sensor, etc.USB port8MB on board Flash for logging (setLOG_BACKEND_TYPE= 4)Camera input/ VTX output300A current sensorBuilt-in OSD
- 5x UARTS
- 5x PWM outputs, first 4 are internally connected to 4in1 45A BLHeli-S ESC, the fifth for LED
- I2C port for external compass, airspeed sensor, etc.
- USB port
- 8MB on board Flash for logging (setLOG_BACKEND_TYPE= 4)
- Camera input/ VTX output
- 300A current sensor
- Built-in OSD
- Size and Dimensions32.5mm x 32.5mm (25.5 x 25.5mm mount pattern)8.5g
- 32.5mm x 32.5mm (25.5 x 25.5mm mount pattern)
- 8.5g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
he UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (Alternate RC input/output)
- SERIAL2 = Telemetry2 = USART2 (DJI)
- SERIAL3 = RC Input = USART3
- SERIAL4 = GPS = USART4
- SERIAL7 = USER = UART7
UART1 supports RX and TX DMA. UART2, UART3 and UART4 support RX DMA. UART7 supports TX DMA



---

## iFlight BeastH7 AIO
**Source URL:** https://ardupilot.org/plane/docs/common-iflight-beasth7AIO.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 BGA ARM (489MHz), 1MB FlashIntegrated 4 output, BLHeli-S 55A ESC
- STM32H743 BGA ARM (489MHz), 1MB Flash
- Integrated 4 output, BLHeli-S 55A ESC
- SensorsInvenSense MPU6000 IMU (accel, gyro)DSP310 barometer (not in V2 version)Voltage & 300A Current sensor
- InvenSense MPU6000 IMU (accel, gyro)
- DSP310 barometer (not in V2 version)
- Voltage & 300A Current sensor
- Power7.4V ~ 25V DC input power5V 2.5A BEC for peripherals
- 7.4V ~ 25V DC input power
- 5V 2.5A BEC for peripherals
- Interfaces5x UARTS5x PWM outputs, first 4 are internally connected to 4in1 45A BLHeli-S ESC, the fifth for LEDI2C port for external compass, airspeed sensor, etc.USB port16MB on board Flash for logging (setLOG_BACKEND_TYPE=4)Camera input/ VTX output300A current sensorBuilt-in OSD
- 5x UARTS
- 5x PWM outputs, first 4 are internally connected to 4in1 45A BLHeli-S ESC, the fifth for LED
- I2C port for external compass, airspeed sensor, etc.
- USB port
- 16MB on board Flash for logging (setLOG_BACKEND_TYPE=4)
- Camera input/ VTX output
- 300A current sensor
- Built-in OSD
- Size and Dimensions32.5mm x 32.5mm (25.5 x 25.5mm mount pattern)8.5g
- 32.5mm x 32.5mm (25.5 x 25.5mm mount pattern)
- 8.5g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
he UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (Alternate RC input/output)
- SERIAL2 = Telemetry2 = USART2 (DJI)
- SERIAL3 = RC Input = USART3
- SERIAL4 = GPS = USART4
- SERIAL7 = USER = UART7
UART1 supports RX and TX DMA. UART2, UART3 and UART4 support RX DMA. UART7 supports TX DMA



---

## iFlight Blitz F745/F745 Mini
**Source URL:** https://ardupilot.org/plane/docs/common-blitz-f745.html

### Description
BLITZ F745
BLITZ MINI
BLITZ MINI STACK
above image and some content courtesy ofiFlight

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F745 32-bit processor, 216 MHzAT7456E OSD32 MB (16MB on Mini) flash for logging
- STM32F745 32-bit processor, 216 MHz
- AT7456E OSD
- 32 MB (16MB on Mini) flash for logging
- SensorsICM42688 IMU (accel and gyro only, no compass)DPS310 or SPL06 barometer
- ICM42688 IMU (accel and gyro only, no compass)
- DPS310 or SPL06 barometer
- Power2S  - 6S Lipo input voltage with voltage monitoring5V, 2.5A BEC for perpherals19V, 2A BEC for powering Video Transmitter
- 2S  - 6S Lipo input voltage with voltage monitoring
- 5V, 2.5A BEC for perpherals
- 19V, 2A BEC for powering Video Transmitter
- Interfaces9x PWM outputs (8 motor outputs[4 on Mini], and 1 LED output)1x RC input pre-configured on a UART6x total UARTs/serial for GPS and other peripherals1x I2C port for external compassUSB-C portExternal current monitor input
- 9x PWM outputs (8 motor outputs[4 on Mini], and 1 LED output)
- 1x RC input pre-configured on a UART
- 6x total UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- USB-C port
- External current monitor input


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn. Default protocols are shown below but may be changed by the user.
Any UART may be re-tasked by changing its protocol parameter.

**OSD SupportÂ**
The autopilot  supports OSD usingOSD_TYPE1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART4. Both the internal analog OSD and the DisplayPort OSD can be used simultaneously by settingOSD_TYPE2= 5 (setup by default)



---

## iFlight Blitz Whoop F7 AIO
**Source URL:** https://ardupilot.org/plane/docs/common-iflight-blitzf7AIO.html

### Description
the above image and some content courtesy ofIFlight

### Specifications
**SpecificationsÂ**
- ProcessorBGA-STM32F745, 216MHzAT7456E OSD16MB flash for dataloggingIntegrated 55A 4in1 BLHeli_S / BlueJay ESC
- BGA-STM32F745, 216MHz
- AT7456E OSD
- 16MB flash for datalogging
- Integrated 55A 4in1 BLHeli_S / BlueJay ESC
- SensorsBMI270 IMU (accel, gyro)DPS310 or SPL06 barometerVoltage & 165A current sensor
- BMI270 IMU (accel, gyro)
- DPS310 or SPL06 barometer
- Voltage & 165A current sensor
- Power2S - 6S LiHV input voltage with voltage monitoring55A Cont., 165A peak current monitor5V, 2A BEC for internal and peripherals
- 2S - 6S LiHV input voltage with voltage monitoring
- 55A Cont., 165A peak current monitor
- 5V, 2A BEC for internal and peripherals
- Interfaces5x PWM outputs, 4 Bi-Directionla DShot capable connected in onboard ESC + integrated NeoPixel LED on board(4x UARTs/serial for GPS and other peripheralsI2C port for external compass, airspeed, etc.USB-C port
- 5x PWM outputs, 4 Bi-Directionla DShot capable connected in onboard ESC + integrated NeoPixel LED on board(
- 4x UARTs/serial for GPS and other peripherals
- I2C port for external compass, airspeed, etc.
- USB-C port
- Size and Dimensions35mm x 35mm  (25.5mm mounting pattern)10.5g
- 35mm x 35mm  (25.5mm mounting pattern)
- 10.5g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The Blitz Whoop F7 AIO supports analog video transmission using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort is supported by default on USART1 RX/TX or any other free UART. SeeMSP OSDfor more info.



---

## iFlight Blitz H743 Pro
**Source URL:** https://ardupilot.org/plane/docs/common-blitzh743pro.html

### Description
The BLITZ H743 Pro is a flight controller produced byiFlight.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processor, 480 MHzAT7456E OSD
- STM32H743 32-bit processor, 480 MHz
- AT7456E OSD
- SensorsICM42688 IMU (accel and gyro only, no compass)DPS310 barometer (v1), SPA06 (v2)
- ICM42688 IMU (accel and gyro only, no compass)
- DPS310 barometer (v1), SPA06 (v2)
- Power2S  - 8S Lipo input voltage with voltage and current monitoring5V, 2.5A BEC for perpherals12V, 2A Switched BEC for powering Video Transmitter
- 2S  - 8S Lipo input voltage with voltage and current monitoring
- 5V, 2.5A BEC for perpherals
- 12V, 2A Switched BEC for powering Video Transmitter
- Interfaces13x PWM outputs (12 motor outputs and 1 LED output)1x RC input pre-configured on a UART7x total UARTs/serial for GPS and other peripheralsintegrated microSD chip for logging2x I2C port for external compass,airspeed,etc.1x CAN portUSB-C portExternal current monitor input
- 13x PWM outputs (12 motor outputs and 1 LED output)
- 1x RC input pre-configured on a UART
- 7x total UARTs/serial for GPS and other peripherals
- integrated microSD chip for logging
- 2x I2C port for external compass,airspeed,etc.
- 1x CAN port
- USB-C port
- External current monitor input
- PhysicalMount pattern: 30.5*30.5mm/?4Dimensions: 36.9*52mmWeight: 35g
- Mount pattern: 30.5*30.5mm/?4
- Dimensions: 36.9*52mm
- Weight: 35g


### Ports, UARTs & Pin Mapping
**PinoutÂ**
TOP
BOTTOM
EXPANSION BOARD

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn. Default protocols are shown below but may be changed by the user.

**OSD SupportÂ**
The autopilot  supports OSD usingOSD_TYPE1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART4. Both the internal analog OSD and the DisplayPort OSD can be used simultaneously by settingOSD_TYPE2= 5



---

## iFlight Blitz Wing H743
**Source URL:** https://ardupilot.org/plane/docs/common-blitzh743wing.html

### Description
The BLITZ Wing H743 is a flight controller produced byiFlight.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processor, 480 MHzAT7456E OSD
- STM32H743 32-bit processor, 480 MHz
- AT7456E OSD
- SensorsICM42688 IMU (accel and gyro only, no compass)DPS310 barometer
- ICM42688 IMU (accel and gyro only, no compass)
- DPS310 barometer
- Power2S  - 8S Lipo input voltage with voltage and current monitoring5V, 3A BEC for perpherals9V, 3A BEC for powering Video Transmitter5/7.4/8.4V 6A BEC for Servo
- 2S  - 8S Lipo input voltage with voltage and current monitoring
- 5V, 3A BEC for perpherals
- 9V, 3A BEC for powering Video Transmitter
- 5/7.4/8.4V 6A BEC for Servo
- Interfaces13x PWM outputs (12 motor outputs and 1 LED output)1x RC input pre-configured on a UART7x total UARTs/serial for GPS and other peripheralsmicroSD Card2x I2C port for external compass,airspeed,etc.1x CAN portUSB-C portExternal current monitor input
- 13x PWM outputs (12 motor outputs and 1 LED output)
- 1x RC input pre-configured on a UART
- 7x total UARTs/serial for GPS and other peripherals
- microSD Card
- 2x I2C port for external compass,airspeed,etc.
- 1x CAN port
- USB-C port
- External current monitor input
- PhysicalDimensions: 36.9*52mmWeight: 35g
- Dimensions: 36.9*52mm
- Weight: 35g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn. Default protocols are shown below but may be changed by the user.

**OSD SupportÂ**
The autopilot  supports OSD usingOSD_TYPE1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART4. Both the internal analog OSD and the DisplayPort OSD can be used simultaneously by settingOSD_TYPE2= 5



---

## iFlight Thunder H7
**Source URL:** https://ardupilot.org/plane/docs/common-iflight-thunder-H7.html

### Description
The iFlight Thunder H7 is a flight controller produced byiFlight.

### Specifications
**SpecificationsÂ**
- ProcessorMCU - STM32H743 32-bit processor running at 480 MHzOnboard Flash: 1GBit (appears a non-removeable SD card for logging)
- MCU - STM32H743 32-bit processor running at 480 MHz
- Onboard Flash: 1GBit (appears a non-removeable SD card for logging)
- SensorsIMU - ICM42688PBarometer - SPL06-001
- IMU - ICM42688P
- Barometer - SPL06-001
- PowerBattery input voltage: 2S-6SBEC 5V 1.5ASwitchable TX power BEC 10V 1.5A
- Battery input voltage: 2S-6S
- BEC 5V 1.5A
- Switchable TX power BEC 10V 1.5A
- Interfaces9x PWM Outputs (8 Motor Output, 1 LED)6x UARTs/serial for GPS and other peripherals. All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ2x I2C ports for external compass, airspeed, etc.USB-C port and boot button on separate dongle for ease of access
- 9x PWM Outputs (8 Motor Output, 1 LED)
- 6x UARTs/serial for GPS and other peripherals. All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- 2x I2C ports for external compass, airspeed, etc.
- USB-C port and boot button on separate dongle for ease of access
- Size and Dimensions42mm x 42mm30.5*30.5mm mount holes 4mm dia14g
- 42mm x 42mm
- 30.5*30.5mm mount holes 4mm dia
- 14g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DisplayPort, DMA-enabled)
- SERIAL2 -> UART2 (RC, DMA-enabled)
- SERIAL3 -> UART3 (GPS, DMA-enabled)
- SERIAL4 -> UART4 (GPS, DMA-enabled)
- SERIAL6 -> UART6 (ESC Telemetry)

**OSD SupportÂ**
The iFlight Thunder H7 supports MSP DisplayPort OSDs using OSD_TYPE 5 and SERIAL1 by default (on HD VTX connector)



---

## JAE JFB-110
**Source URL:** https://ardupilot.org/plane/docs/common-jae-jfb110.html

### Description
The JAE (Japan Aviation Electronics Industry) JFB-110 autopilot is made in Japan with a focus on robustness and reliability.  Instead of the more common JST connectors, this autopilot uses automotive grade water proof connectors for most peripherals.  It also includes an automotive grade IMU and high speed TypeC USB.

### Specifications
**FeaturesÂ**
- High speed STM32H755 microcontroller
- 1x SCHA63T and 2x TDK InvenSense IIM-42652 IMUs
- 2x MS5611 barometers
- Built-in iSentek IST8310 magnetometer
- MicroSD card slot
- 5 UARTs plus USB, RCIN, SBUS_OUT
- 16 PWM outputs
- Four I2C and two CAN ports
- External buzzer (Open/Drain and 33V Out)
- External safety switch
- Voltage monitoring for servo rail and Vcc
- 2x power input ports for external power bricks

**SpecificationsÂ**
- Size: 67mm x 88mm x 17mm
- Weight: 60g
- Power consumption: under 3W
- Input voltage: 4.9V ~ 5.5V
- Temp Min/Max: -40C ~ +85C


### Ports, UARTs & Pin Mapping
**PWR1, PWR2 port pin assignmentsÂ**
Pin No | Name | Details
1 | Current | 0V~3.3V input
2 | Voltage | 0V~3.3V input
3 ~ 5 | VCC | 4.9V ~ 5.5V input
6 ~ 8 | GND | 

**101 port pin assignmentsÂ**
Pin No | Name | Details
1 | Serial1 TX | Telem1
2 | Serial1 RX | Telem1
3 | VCC Periph 5V | 5V
4 | VCC Periph 5V | 5V
5 | CAN H1 | CAN1 port
6 | VCC Periph 5V | 5V
7 | Serial3 TX | GPS
8 | I2C1 SCL | I2C1 port
9 | Safety Switch | 
10 | VCC 5V High Power | 5V 1.5A max
11 | VCC 3.3V High Power | 3.3V 1A max
12 | SPI5 SCK | SPI5 port
13 | SPI5 MISO | SPI5 port
14 | SPI5 MOSI | SPI5 port
15 | VCC Periph 5V | 5V
16 | VCC Periph 5V | 5V
17 | Serial4 TX | GPS2
18 | I2C2 SCL | I2C2 port
19 | Serial1 CTS | 
20 | Serial1 RTS | 
21 | GND | 
22 | GND | 
23 | CANL1 | CAN1 port
24 | GND | 
25 | Serial3 RX | GPS
26 | I2C1 SDA | I2C1 port
27 | Safety Switch LED | Open 3.3V / Drain
28 | Buzzer | Open/Drain
29 | VCC 3.3V High Power | 3.3V 1A max
30 | Serial5 RX | RC input2
31 | RSSI | Pin 10
32 | GND | 
33 | Serial6 | SBUS Out
34 | RC In | 
35 | Buzzer | Open , 5KOhm pull down
36 | SPI5 CS1 | SPI5 port
37 | GND | 
38 | GND | 
39 | Serial4 RX | GPS2
40 | I2C2 SDA | I2C2 port

**102 port pin assignmentsÂ**
Pin No | Name | Details
1 | VCC Periph 5V | 5V
2 | Serial2 TX | Telem2
3 | Serial2 RX | Telem2
4 | VCC Periph 5V | 5V
5 | CAN H2 | CAN2 port
6 | Chassis GND | 
7 | FMU CAP1 | GPIO 66
8 | VCC Periph 5V | 5V
9 | I2C4 SCL | I2C4 port
10 | PWM OUT 1 | GPIO 50
11 | PWM OUT 2 | GPIO 51
12 | PWM OUT 3 | GPIO 52
13 | PWM OUT 4 | GPIO 53
14 | VCC Servo | 5V 1.5A max
15 | GND | 
16 | Serial2 CTS | 
17 | Serial2 RTS | 
18 | GND | 
19 | CAN L2 | CAN2 port
20 | GND | 
21 | FMU CAP2 | GPIO 67
22 | WDT FAIL | TTL
23 | External Reset | TTL
24 | ADC 3.3V | Pin 13
25 | ADC 3.3V | Pin 12
26 | GND | 
27 | I2C4 SDA | I2C4 port
28 | PWM OUT 5 | GPIO 54
29 | PWM OUT 6 | GPIO 55
30 | PWM OUT 7 | GPIO 56
31 | PWM OUT 8 | GPIO 57
32 | GND | for PWM OUT

**103 port pin assignmentsÂ**
Pin No | Name | Details
1 | GND | For PWM OUT
2 | GND | For USB
3 | USB OTG FS DM | USB port
4 | USB OTG FS DP | USB port
5 | PWM OUT 9 | GPIO 58
6 | PWM OUT 10 | GPIO 59
7 | PWM OUT 11 | GPIO 60
8 | PWM OUT 12 | GPIO 61
9 | PWM OUT 13 | GPIO 62
10 | PWM OUT 14 | GPIO 63
11 | PWM OUT 15 | GPIO 64
12 | PWM OUT 16 | GPIO 64

**UART / SerialÂ**
Port | Default Use | CTS/RTS | DMA
Serial0 | USB | N/A | No
Serial1 | Telem1 | Yes | Yes
Serial2 | Telem2 | Yes | No
Serial3 | GPS | No | No
Serial4 | GPS2 | No | Yes
Serial5 | RCin2 | No | Yes
Serial6 | SBUS Out | No | Yes
Serial7 | Unused | No | Yes
Serial8 | USB SLCAN | N/A | Yes



---

## JHEMCU F405Pro
**Source URL:** https://ardupilot.org/plane/docs/common-jhemcuf405pro.html

### Description
(aka GHF405AIO-HD) Flight Controller
The JHEMCUF405PRO is an AIO flight controller produced byJHEMCU.
,.. note: Thereâs another version of the board that doesnât have I2C pads exposed. This is not that one.

### Specifications
**FeaturesÂ**
- MCU - STM32F405 32-bit processor running at 168 MHz
- IMU - ICM42605
- Barometer - DPS310
- Voltage & current sensor
- OSD - AT7456E
- Onboard Flash: 8MB
- 5x UARTs (1,2,3,4,6)
- 5x PWM Outputs (4 Motor Output, 1 LED)
- Battery input voltage: 2S-6S
- BEC 5V/2.5A, 10V/2.0A
- I2C: exposed pins
- ESCs: BlheliS 40A (advertised)
- LED strip: Supported
- Buzzer: supported


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the
receive pin for UARTn. The TXn pin is the transmit pin for UARTn.
The board also has SH6P 1mm connector for digital FPV systems which has UART6.
Please note that the board will not enter DFU mode if the receiver is connected to either USART1/USART3/USART4). If you have it soldered there due to DMA requirements you will need to temporarily desolder the wire on the FCâs RX pad and solder it back after flashing.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (RCin,DMA-enabled)
- SERIAL2 -> USART2 (MAVLink2)
- SERIAL3 -> USART3 (GPS1, DMA-enabled)
- SERIAL4 -> UART4  (GPS2)
- SERIAL6 -> USART6 (MSP DisplayPort, DMA-enabled)

**OSD SupportÂ**
JHEMCUF405PRO supports OSD using its internal analog OSD (MAX7456). Simultaneous HD VTX OSD support is pre-configured on UART6 on the HD VTX connector.



---

## JHEMCU H743HD
**Source URL:** https://ardupilot.org/plane/docs/common-jhemcu-h743hd.html

### Description
The JHEMCU H743 HD is a flight controller produced byJHEMCU.

### Specifications
**FeaturesÂ**
- MCU - STM32H743 32-bit processor running at 480 MHz
- IMU - dual ICM42688P
- Barometer - DPS310
- Voltage & current sensor inputs
- OSD - AT7456E
- Onboard Datalogging Flash: 1 Gbits (W25N01G)
- 7x UARTs (1,2,3,4,5,6,7)
- 9x PWM Outputs (8 Motor Output, 1 LED)
- Battery input voltage: 3S-6S
- BEC 5V/2.5A, 10V/2.0A


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the
receive pin for UARTn. The TXn pin is the transmit pin for UARTn.
In addition to pads, the board also has SH6P 1mm connector for DJI FPV and SH8P 1mm connector for 4 in 1 ESC.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (MAVLink2,DMA-enabled)
- SERIAL2 -> USART2 (RCIN, DMA-enabled)
- SERIAL3 -> USART3 (User,DMA-enabled)
- SERIAL4 -> UART4 (GPS, DMA-enabled)
- SERIAL5 -> UART5 (Solder pads labeled R5 T5)
- SERIAL6 -> USART6 (DisplayPort, DMA-enabled)
- SERIAL7 -> UART7 (RX pin only, ESC Telemetry)
- SERIAL8 -> UART8 (Unused, not tested, no pinout, need to solder direct on processor pins to utilize if you need just one more UART)

**OSD SupportÂ**
JHEMCU H743 supports OSD using OSD_TYPE 1 (MAX7456 driver). HD goggle OSD is pre-configured on UART6 on the HD goggle connector. Change OSD_TYPE to â5â to use HD systems. This also enables the internal analog OSD system which can be used simultaneously.



---

## LongBowF405WING
**Source URL:** https://ardupilot.org/plane/docs/common-longbowf405wing.html

### Description
The LongBowF405WING is a flight controller produced bylefei rc.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)AT7456E OSDInternal Wireless Telemetry Module
- STM32F405RGT6 ARM (168MHz)
- AT7456E OSD
- Internal Wireless Telemetry Module
- SensorsICM-42688P IMU (accel, gyro)SPL-06 barometer
- ICM-42688P IMU (accel, gyro)
- SPL-06 barometer
- Power2S - 6S Lipo input voltage with voltage monitoring120A Cont., 215A peak current monitor9V/12/5V, 1.8A BEC for powering Video Transmitter controlled by GPIO4.9V/6V/7.2V, 6A BEC for servos5V, 2.4A BEC for internal and peripherals
- 2S - 6S Lipo input voltage with voltage monitoring
- 120A Cont., 215A peak current monitor
- 9V/12/5V, 1.8A BEC for powering Video Transmitter controlled by GPIO
- 4.9V/6V/7.2V, 6A BEC for servos
- 5V, 2.4A BEC for internal and peripherals
- Interfaces12x PWM outputs DShot capable (Serail LED output is PWM12)1x RC input5x UARTs/serial for GPS and other peripherals, 6th UART internally tied to Wireless board)I2C port for external compass, airspeed, etc.microSDCard for logging, etc.USB-C port
- 12x PWM outputs DShot capable (Serail LED output is PWM12)
- 1x RC input
- 5x UARTs/serial for GPS and other peripherals, 6th UART internally tied to Wireless board)
- I2C port for external compass, airspeed, etc.
- microSDCard for logging, etc.
- USB-C port


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (User) (DMA capable)
- SERIAL2 -> USART2 (RX tied to inverted SBUS RC input, but can be used as normal UART ifBRD_ALT_CONFIG= 1)
- SERIAL3 -> UART3 (GPS) (TX DMA capable)
- SERIAL4 -> UART4 (User) (TX DMA capable)
- SERIAL5 -> UART5 (DisplayPort, available on DJI air unit connector) (TX DMA capable)
- SERIAL6 -> UART6 (tied to internal wireless module, MAVLink2 telem)

**OSD SupportÂ**
The LongBowF405WING supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such DisplayPor is setup by default using UART5. Simultaneous use of the internal OSD and Displayport is allowed. SeeMSP OSDfor more info.



---

## Lumineer LUXF765-NDAA
**Source URL:** https://ardupilot.org/plane/docs/common-luxf765-ndaa.html

### Description
The Lumenier LUX F765 NDAA autopilot is sold byGetFPV.

### Specifications
**FeaturesÂ**
- Processor: MCU STM32F765, 216MHz, 512KB RAM, 2MB Flash
- ICM42688 IMU
- BMP280 Barometer
- microSD Card Slot
- 12 PWM Outputs
- I2C Ports for External Sensors
- CANbus Support
- 8 UART Ports
- Buzzer Control
- LED Strip Control
- Analog Current Sensor Input
- Analog Battery Sensor Input
- USB Type-C (2.0)
- Blackbox Storage - SD Card and Flash (128Mbit/16Mbyte)
- Camera Control Output
- AT7456E OSD
- 10V Regulator for VTX Power
- 5V Regulator for Accessories
- Supported Firmware - Betaflight, Ardupilot, and PX4
- NDAA compliant
- Power Supply: 3S to 6S Battery Voltage


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> USART1 (TElem1, DMA enabled)
- SERIAL2 -> UART5  (Telem2, DMA enabled)
- SERIAL3 -> USART3 (GPS1, TX DMA enabled)
- SERIAL4 -> UART8  (GPS2)
- SERIAL5 -> USART2 (ESC Telemetry)
- SERIAL6 -> UART4  (DisplayPort)
- SERIAL7 -> UART7  (RCinput,DMA enabled)
- SERIAL8 -> USART6 (Spare)

**ESC #1 PortÂ**
Pin | Signal | Volt
1 | VCC | VBAT
2 | GND | GND
3 | CURRENT | +3.3V
4 | TELEMETRY | +3.3V
5 | MOTOR 1 (TIM2_CH1) | +3.3V
6 | MOTOR 2 (TIM2_CH2) | +3.3V
7 | MOTOR 3 (TIM2_CH3) | +3.3V
8 | MOTOR 4 (TIM2_CH4) | +3.3V

**ESC #2 PortÂ**
Pin | Signal | Volt
1 | NOT CONNECTED | NOT CONNECTED
2 | GND | GND
3 | NOT CONNECTED | NOT CONNECTED
4 | TELEMETRY | +3.3V
5 | MOTOR 5 (TIM4_CH1) | +3.3V
6 | MOTOR 6 (TIM4_CH2) | +3.3V
7 | MOTOR 7 (TIM4_CH3) | +3.3V
8 | MOTOR 8 (TIM4_CH4) | +3.3V

**GPS portÂ**
Pin | Signal | Volt
1 | +5V | +5V
2 | TX3 | +3.3V
3 | RX3 | +3.3V
4 | I2C3 SCL | +3.3V
5 | I2C3 SDA | +3.3V
6 | GND | GND

**HD VTX portÂ**
Pin | Signal | Volt
1 | +10V | +10V
2 | GND | GND
3 | TX4 | +3.3V
4 | RX4 | +3.3V
5 | GND | GND
6 | RX7 | +3V3

**Receiver PortÂ**
Pin | Signal | Volt
1 | +5V | +5V
2 | GND | GND
3 | RX7 | +3.3
4 | TX7 | +3.3V

**CANbus PortÂ**
Pin | Signal | Volt
1 | +5V | +5V
2 | GND | GND
3 | CAN_H | +5V
4 | CAN_L | +5V

**OSD SupportÂ**
The LUX F765 - NDAA supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). Simultaneous DisplayPort OSD operation  is pre-configured on SERIAL 6. SeeMSP OSDfor more info.



---

## Mamba F405 MK2
**Source URL:** https://ardupilot.org/plane/docs/common-mamba405-mk2.html

### Description
The Mamba F405 MK2 is an autopilot produced byDiatone.

### Specifications
**FeaturesÂ**
- STM32F405RGT6 microcontroller
- MPU6000 IMU
- AT7456E OSD
- 3 UARTs
- 5 PWM outputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
Name | Pin labels | Function
SERIAL0 |  | USB
SERIAL1 | PPM / SBUS | RC Input (SBUS pin MUST be used for RC input unless alt config used)
SERIAL3 | TX3 / RX3 | UART3 (IRC Tramp)
SERIAL6 | TX6 / RX6 | UART6 (ESC Telemetry)
BRD_ALT_CONFIG | PPM pin function
ALT 0 (default) | tied internally to an inverter, cannot be driven from the outside
ALT 1 | RX1(PPM)/TX1

**OSD SupportÂ**
The Mamba F405 MK2 has an integrated OSD.



---

## Mamba MK4 F405Mini
**Source URL:** https://ardupilot.org/plane/docs/common-mambaf405-mini.html

### Description
The Mamba MK4 F405Mini is an autopilot produced byDiatone.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 32-bit processor running at 168 MHzOSD - AT7456E128Kb (16MB) Data Log Flash (LOG_BACKEND_TYPE= 2)
- STM32F405 32-bit processor running at 168 MHz
- OSD - AT7456E
- 128Kb (16MB) Data Log Flash (LOG_BACKEND_TYPE= 2)
- SensorsAccelerometer/Gryo: MPU6000 (Version A) or IMC42688 (Version B)SPL06 Barometer
- Accelerometer/Gryo: MPU6000 (Version A) or IMC42688 (Version B)
- SPL06 Barometer
- Power6.8V ~ 26V DC input power5V 2.5A BEC for peripherals9V 2A BEC for video
- 6.8V ~ 26V DC input power
- 5V 2.5A BEC for peripherals
- 9V 2A BEC for video
- Interfaces4 UARTS7x PWM outputs (one is used for serial LED)I2C port for external compass, airspeed sensor, etc.USB port
- 4 UARTS
- 7x PWM outputs (one is used for serial LED)
- I2C port for external compass, airspeed sensor, etc.
- USB port
- Size and Dimensions29mm x 29.5mm x 6.5mm, 20mm x 20mmx mounting6g
- 29mm x 29.5mm x 6.5mm, 20mm x 20mmx mounting
- 6g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the receive pin for UARTn. The TXn pin is the transmit pin for UARTn. Default protocols for each port are shown and may be changed by the user.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (RX/SBUS)
- SERIAL2 -> USART2 (GPS, DMA-enabled)
- SERIAL3 -> USART3 (User, TX has DMA capability, on DJI AIR connector)
- SERIAL4 -> UART4  (User, TX has DMA capability)
- SERIAL5 -> UART5  (Unavailable, not pinned out)
- SERIAL6 -> USART6 (RX only, ESC Telem, DMA capable)

**OSD SupportÂ**
The Mamba MK4 F405Mini supports internal OSD usingOSD_TYPE= 1 (MAX7456 driver).



---

## Mamba Basic F405 mk3
**Source URL:** https://ardupilot.org/plane/docs/common-mamba-basic-mk3.html

### Description
The Mamba Basic line of autopilots are produced by [Diatone](https://www.diatone.us).

### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Name | Pin | Function
SERIAL0 | COMPUTER | USB
SERIAL1 | PPM/RX1/SBUS/TX1 | UART1 (RC Input)
SERIAL2 | TX2/RX2 | UART2 (Empty)
SERIAL3 | TX3/RX3 | UART3 (Telem1)
SERIAL4 | TX4/RX4 | UART4 (Empty)
SERIAL6 | TX6/RX6 | UART6 (GPS)

**OSD SupportÂ**
The Mamba F405 MK2 has an integrated OSD enabled byOSD_TYPE=` 1 (MAX7456 driver).



---

## Mamba H743 v4
**Source URL:** https://ardupilot.org/plane/docs/common-mambaH743v4.html

### Description
The MambaH743v4 is an autopilot produced byDiatone.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processor running at 480 MHzOSD - AT7456E128MB Data Log Flash
- STM32H743 32-bit processor running at 480 MHz
- OSD - AT7456E
- 128MB Data Log Flash
- SensorsDual MPU6000 (Version A) or BMI270 (Version B)DPS280
- Dual MPU6000 (Version A) or BMI270 (Version B)
- DPS280
- Power6.8V ~ 26V DC input power5V 3A BEC for peripherals9V 3A BEC for video
- 6.8V ~ 26V DC input power
- 5V 3A BEC for peripherals
- 9V 3A BEC for video
- Interfaces8 UARTS9x PWM outputsI2C ports for external compass, airspeed sensor, etc.USB port
- 8 UARTS
- 9x PWM outputs
- I2C ports for external compass, airspeed sensor, etc.
- USB port
- Size and Dimensions38mm x 38mm x 7.5mm11g
- 38mm x 38mm x 7.5mm
- 11g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the receive pin for UARTn. The TXn pin is the transmit pin for UARTn. Default protocols for each port are shown and may be changed by the user.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (RX/SBUS, DMA-enabled)
- SERIAL2 -> USART2 (GPS)
- SERIAL3 -> USART3 (GPS)
- SERIAL4 -> UART4 (WIFI, DMA-enabled)
- SERIAL5 -> UART5
- SERIAL6 -> USART6 (ESC Telemetry)
- SERIAL7 -> UART7 (DMA-enabled)
- SEIRAL8 -> UART8

**OSD SupportÂ**
The MambaH743v4 supports OSD usingOSD_TYPE= 1 (MAX7456 driver).



---

## MakeFlyEasy PixSurveyA1
**Source URL:** https://ardupilot.org/plane/docs/common-makeflyeasy-PixSurveyA1.html

### Description


### Specifications
**SpecificationsÂ**
- Processor:32-bit STM32F427VIT6 ARM Cortex M4 core with FPU168 Mhz/256 KB RAM/2 MB Flash32-bit failsafe co-processor (STMF103)
- 32-bit STM32F427VIT6 ARM Cortex M4 core with FPU
- 168 Mhz/256 KB RAM/2 MB Flash
- 32-bit failsafe co-processor (STMF103)
- SensorsThree redundant IMUs (accels, gyros and compass)Gyro/Accelerometers: ICM20948 or MPU9250, ICM20602, MPU6000Barometers: Two redundant MS5611 barometersCompass: AK8960 or AK09916
- Three redundant IMUs (accels, gyros and compass)
- Gyro/Accelerometers: ICM20948 or MPU9250, ICM20602, MPU6000
- Barometers: Two redundant MS5611 barometers
- Compass: AK8960 or AK09916
- PowerRedundant power supply with automatic failoverPower supply 4.8V-5.8V
- Redundant power supply with automatic failover
- Power supply 4.8V-5.8V
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for CPPM, Spektrum / DSM and S.Bus5x general purpose serial ports2x I2C ports2x CAN Bus interfaceMicroSD card readerType-C USBHigh-powered piezo buzzer driver (on expansion board)Safety switch / LED
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for CPPM, Spektrum / DSM and S.Bus
- 5x general purpose serial ports
- 2x I2C ports
- 2x CAN Bus interface
- MicroSD card reader
- Type-C USB
- High-powered piezo buzzer driver (on expansion board)
- Safety switch / LED
- DimensionsWeight 117gSize 110mm x 100mm x 23mm
- Weight 117g
- Size 110mm x 100mm x 23mm


### Ports, UARTs & Pin Mapping
**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**I2C1, I2C2 portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL | +3.3V
3 | SDA | +3.3V
4 | GND | GND

**CAN1, CAN2 portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**Safety portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | LED | +3.3V
3 | SafKey | +3.3V

**GPS1/I2C1, GPS2/I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Power1, Power2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND



---

## MakeFlyEasy PixSurveyA1-IND
**Source URL:** https://ardupilot.org/plane/docs/common-makeflyeasy-PixSurveyA1-IND.html

### Description
The PixSurveyA1-IND flight controller is an upgrade to PixSurveyA1, with better sensors and a better power solution. It is sold by a range of resellers listed on the makeflyeasy(http://www.makeflyeasy.com)

### Specifications
**SpecificationsÂ**
- Processor:32-bit STM32F427VIT6 ARM Cortex M4 core with FPU168 Mhz/256 KB RAM/2 MB Flash32-bit failsafe co-processor (STMF103)
- 32-bit STM32F427VIT6 ARM Cortex M4 core with FPU
- 168 Mhz/256 KB RAM/2 MB Flash
- 32-bit failsafe co-processor (STMF103)
- SensorsThree redundant IMUs (accels, gyros and compass)Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)Barometers: Two redundant MS5611 barometersCompass: IST8310(internal I2C)
- Three redundant IMUs (accels, gyros and compass)
- Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)
- Barometers: Two redundant MS5611 barometers
- Compass: IST8310(internal I2C)
- PowerRedundant power supply with automatic failoverPower supply 4V-6V
- Redundant power supply with automatic failover
- Power supply 4V-6V
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus  outputR/C inputs for CPPM and S.Bus5x general purpose serial ports2x I2C ports2x CAN Bus interfaceMicroSD card readerType-C USBHigh-powered piezo buzzer driverSafety switch / LEDServo rail BEC independent power input for servos12V Power Output
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus  output
- R/C inputs for CPPM and S.Bus
- 5x general purpose serial ports
- 2x I2C ports
- 2x CAN Bus interface
- MicroSD card reader
- Type-C USB
- High-powered piezo buzzer driver
- Safety switch / LED
- Servo rail BEC independent power input for servos
- 12V Power Output
- DimensionsWeight 117gSize 110mm x 100mm x 23mm
- Weight 117g
- Size 110mm x 100mm x 23mm


### Ports, UARTs & Pin Mapping
**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**I2C1, I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL | +3.3V
3 | SDA | +3.3V
4 | GND | GND

**CAN1, CAN2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**Safety and LED portÂ**
PIN | SIGNAL | VOLT | 1 | VCC | +3.3V | 2 | LED | +3.3V | 3 | SAFKEY | +3.3V
1 | VCC | +3.3V
2 | LED | +3.3V
3 | SAFKEY | +3.3V

**GPS1/I2C1, GPS2/I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Serial5 portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**Power1, Power2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND

**12V Power Output portÂ**
Pin | Signal | Volt
1 | GND | GND
2 | VCC | +12V
3 | GND | GND

**S.BUS Output portÂ**
Pin | Signal | Volt
1 | SBUS.out | +3.3V
2 | NC | NC
3 | GND | GND



---

## MakeFlyEasy PixPilot-C3
**Source URL:** https://ardupilot.org/plane/docs/common-makeflyeasy-PixPilot-C3.html

### Description
The PixPilot-C3 is a low cost flight controller with fully redundant IMUs. In most cases, an onboard compass is more susceptible to interference, so we removed the onboard compass and used an external compass instead. Integrated high gain buzzer.
The PixPilot-C3 flight controller is sold by a range of resellers listed on the makeflyeasy(http://www.makeflyeasy.com)

### Specifications
**SpecificationsÂ**
- Processor:32-bit STM32F427VIT6 ARM Cortex M4 core with FPU168 Mhz/256 KB RAM/2 MB Flash32-bit failsafe co-processor (STMF103)
- 32-bit STM32F427VIT6 ARM Cortex M4 core with FPU
- 168 Mhz/256 KB RAM/2 MB Flash
- 32-bit failsafe co-processor (STMF103)
- SensorsTWO redundant IMUs (accels and gyrosï¼Gyro/Accelerometers: two ICM42688-P(SPI)Barometers: Two redundant BMP388 barometers
- TWO redundant IMUs (accels and gyrosï¼
- Gyro/Accelerometers: two ICM42688-P(SPI)
- Barometers: Two redundant BMP388 barometers
- PowerRedundant power supply with automatic failoverPower supply 4V-6V
- Redundant power supply with automatic failover
- Power supply 4V-6V
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for CPPM, Spektrum / DSM and S.Bus5x general-purpose serial ports2x I2C ports2x CAN Bus interfaceMicroSD card readerType-C USBHigh-powered piezo buzzer driverSafety switch / LEDServo rail BEC independent power input for servos
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for CPPM, Spektrum / DSM and S.Bus
- 5x general-purpose serial ports
- 2x I2C ports
- 2x CAN Bus interface
- MicroSD card reader
- Type-C USB
- High-powered piezo buzzer driver
- Safety switch / LED
- Servo rail BEC independent power input for servos
- DimensionsWeight 40gSize 74mm x 45mm x 16mm
- Weight 40g
- Size 74mm x 45mm x 16mm


### Ports, UARTs & Pin Mapping
**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**I2C1, I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL | +3.3V
3 | SDA | +3.3V
4 | GND | GND

**CAN1, CAN2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**Safety portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | LED | +5V
3 | SAFKEY | +5V

**GPS1/I2C1, GPS2/I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Serial5 portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**Power1, Power2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND

**DSM portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +3.3V
2 | RX | +3.3V
3 | GND | GND



---

## MakeFlyEasy PixPilot-V3
**Source URL:** https://ardupilot.org/plane/docs/common-makeflyeasy-PixPilot-V3.html

### Description
The PixPilot-V3 flight controller is sold by a range of resellers listed on the makeflyeasy(http://www.makeflyeasy.com)

### Specifications
**SpecificationsÂ**
- Processor:32-bit STM32F427VIT6 ARM Cortex M4 core with FPU168 Mhz/256 KB RAM/2 MB Flash32-bit failsafe co-processor (STMF103)
- 32-bit STM32F427VIT6 ARM Cortex M4 core with FPU
- 168 Mhz/256 KB RAM/2 MB Flash
- 32-bit failsafe co-processor (STMF103)
- SensorsThree redundant IMUs (accels, gyros and compass)Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)Barometers: Two redundant MS5611 barometersCompass: IST8310(internal I2C)
- Three redundant IMUs (accels, gyros and compass)
- Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)
- Barometers: Two redundant MS5611 barometers
- Compass: IST8310(internal I2C)
- PowerRedundant power supply with automatic failoverPower supply 4V-6V
- Redundant power supply with automatic failover
- Power supply 4V-6V
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for CPPM, Spektrum / DSM and S.Bus5x general purpose serial ports2x I2C ports2x CAN Bus interfaceMicroSD card readerType-C USBHigh-powered piezo buzzer driver (on expansion modules)Safety switch / LEDServo rail BEC independent power input for servos
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for CPPM, Spektrum / DSM and S.Bus
- 5x general purpose serial ports
- 2x I2C ports
- 2x CAN Bus interface
- MicroSD card reader
- Type-C USB
- High-powered piezo buzzer driver (on expansion modules)
- Safety switch / LED
- Servo rail BEC independent power input for servos
- DimensionsWeight 62gSize 76mm x 45mm x 19mm
- Weight 62g
- Size 76mm x 45mm x 19mm


### Ports, UARTs & Pin Mapping
**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**I2C1, I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL | +3.3V
3 | SDA | +3.3V
4 | GND | GND

**CAN1, CAN2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**Safety and buzzer portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | LED | +5V
3 | SAFKEY | +5V
4 | BUZZER | +5V
5 | 3V+ | +3.3V
6 | GND | GND

**GPS1/I2C1, GPS2/I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Serial5 portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**Power1, Power2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND



---

## MakeFlyEasy PixPilot-V6
**Source URL:** https://ardupilot.org/plane/docs/common-makeflyeasy-PixPilot-V6.html

### Description
The PixPilot-V6 autopilot is sold by a range of resellers listed on the makeflyeasy(http://www.makeflyeasy.com)

### Specifications
**SpecificationsÂ**
- Processor:32-bit STM32H743VIT6 ARM Cortex M7 core with FPU480 Mhz/1 MB RAM/2 MB Flash32-bit failsafe co-processor (STMF103)
- 32-bit STM32H743VIT6 ARM Cortex M7 core with FPU
- 480 Mhz/1 MB RAM/2 MB Flash
- 32-bit failsafe co-processor (STMF103)
- SensorsThree redundant IMUs (accels, gyros and compass)Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)Barometers: Two redundant MS5611 barometersCompass: IST8310(internal I2C)
- Three redundant IMUs (accels, gyros and compass)
- Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)
- Barometers: Two redundant MS5611 barometers
- Compass: IST8310(internal I2C)
- PowerRedundant power supply with automatic failoverPower supply 4V-6V
- Redundant power supply with automatic failover
- Power supply 4V-6V
- Interfaces14x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for CPPM, Spektrum / DSM and S.Bus5x general purpose serial ports2x I2C ports2x CAN Bus interfaceMicroSD card readerType-C USBHigh-powered piezo buzzer driver (on expansion board)Safety switch / LED
- 14x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for CPPM, Spektrum / DSM and S.Bus
- 5x general purpose serial ports
- 2x I2C ports
- 2x CAN Bus interface
- MicroSD card reader
- Type-C USB
- High-powered piezo buzzer driver (on expansion board)
- Safety switch / LED
- DimensionsWeight 62gSize 76mm x 45mm x 19mm
- Weight 62g
- Size 76mm x 45mm x 19mm


### Ports, UARTs & Pin Mapping
**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**I2C1, I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL | +3.3V
3 | SDA | +3.3V
4 | GND | GND

**CAN1, CAN2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**Safety and buzzer portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | LED | +5V
3 | SAFKEY | +5V
4 | BUZZER | +5V
5 | 3V+ | +3.3V
6 | GND | GND

**GPS1/I2C1, GPS2/I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Serial5 portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**Power1, Power2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND



---

## MakeFlyEasy PixPilot-V6PRO
**Source URL:** https://ardupilot.org/plane/docs/common-makeflyeasy-PixPilot-V6PRO.html

### Description
The PixPilot-V6PRO autopilot is sold by a range of resellers listed on themakeflyeasy

### Specifications
**SpecificationsÂ**
- Processor:32-bit STM32H743VIT6 ARM Cortex M7 core with FPU480 Mhz/1 MB RAM/2 MB Flash32-bit failsafe co-processor (STMF103)
- 32-bit STM32H743VIT6 ARM Cortex M7 core with FPU
- 480 Mhz/1 MB RAM/2 MB Flash
- 32-bit failsafe co-processor (STMF103)
- SensorsThree redundant IMUs (accels, gyros and compass)Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)Barometers: Two redundant BMP388 barometers
- Three redundant IMUs (accels, gyros and compass)
- Gyro/Accelerometers: two ICM42688-P(SPI), one ICM40605(SPI)
- Barometers: Two redundant BMP388 barometers
- PowerRedundant power supply with automatic failoverPower supply 4V-6V
- Redundant power supply with automatic failover
- Power supply 4V-6V
- Interfaces16x PWM servo outputs (8 from IO, 6 from FMU)S.Bus servo outputR/C inputs for PPM,DSM and S.Bus5x general purpose serial ports2x I2C ports4x CAN Bus interfaceMicroSD card readerType-C USBHigh-powered piezo buzzer driver (on expansion board)Safety switch
- 16x PWM servo outputs (8 from IO, 6 from FMU)
- S.Bus servo output
- R/C inputs for PPM,DSM and S.Bus
- 5x general purpose serial ports
- 2x I2C ports
- 4x CAN Bus interface
- MicroSD card reader
- Type-C USB
- High-powered piezo buzzer driver (on expansion board)
- Safety switch
- DimensionsWeight 62gSize 94mm x 49mm x 23mm
- Weight 62g
- Size 94mm x 49mm x 23mm


### Ports, UARTs & Pin Mapping
**POWER_CAN 1 port, POWER_CAN 2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CAN_H | +12V
4 | CAN_L | +12V
5 | GND | GND
6 | GND | GND

**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**I2C1, I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL | +3.3V
3 | SDA | +3.3V
4 | GND | GND

**CAN1, CAN2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**DSM portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | DSM_IN | +5V
3 | GND | GND

**Safety and buzzer portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | LED | +5V
3 | Safety Switch | +5V

**GPS1/I2C1, GPS2/I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Serial 5 portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**Power_ADC 1, Power_ADC 2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND



---

## Mateksys F405 TE Family
**Source URL:** https://ardupilot.org/plane/docs/common-matekf405-te.html

### Description
This family consists of:
the above images and some content courtesy ofmateksys.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6  ARMOSD: AT7456E16MB Flash for data logging, WTE has microSD card reader instead of flash chipESP8285 (WTE only) for ELRS or ESP WIFI Telemetry
- STM32F405RGT6  ARM
- OSD: AT7456E
- 16MB Flash for data logging, WTE has microSD card reader instead of flash chip
- ESP8285 (WTE only) for ELRS or ESP WIFI Telemetry
- SensorsICM42688-PSPL06-001 barometerVoltage sensor (30V max, 60V max for -HDTE)Current Sensor (220A -WTE, 132A -WMN, input pin -miniTE/HDTE)
- ICM42688-P
- SPL06-001 barometer
- Voltage sensor (30V max, 60V max for -HDTE)
- Current Sensor (220A -WTE, 132A -WMN, input pin -miniTE/HDTE)
- Power Input6V ~ 30V DC input power (9v - 60V for -HDTE)
- 6V ~ 30V DC input power (9v - 60V for -HDTE)
- BECs
Board | Typical Use | Voltage | Current(cont/peak)
WTE | Peripherals | 5V | 2A/3A
Servos | 5V,6V, or 7.2V | 8A/10A
VTX/CAM | 9V or 12V | 2A/3A
WMN | Peripherals | 5V | 1.5A/1.5A
Servos | 5V or 6V | 5A/5A
HDTE | Peripherals | 5V | 1.5A/1.5A
Servos/VTX | 9V, 12V, or 16V | 1-2A depending
on input
miniTE | Peripherals | 5V | 1.7A/1.7A
VTX | 10V | 1.4A/1.4A
- Interfaces
Board | UARTS | PWM | I2C | Buzzer | ADC | SD Card | USB
WTE | 6 | 12 | 1 | Yes | 4 | Yes | Remote
WMN | 5 | 12 | 1 | Yes | 3 | No | Remote
HDTE | 6 | 12 | 1 | Yes | 4 | Yes | Yes
miniTE | 6 | 12 | 1 | Yes | 3 | Yes | Yes


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (has DMA)
- SERIAL2 = Telemetry2 = USART3
- SERIAL3 = GPS1 = UART5
- SERIAL4 = GPS2 = UART4
- SERIAL5 = USER = USART6 (has DMA on TX only)(not available on WMN)
- SERIAL6 = USER = USART2 (TX only unlessBRD_ALT_CONFIG= 1, then RX available also) and has DMA
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences.



---

## Mateksys H743-Wing/MINI/SLIM/WLITE
**Source URL:** https://ardupilot.org/plane/docs/common-matekh743-wing.html

### Description
the above image and some content courtesy ofmateksys.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743VIT6  ARM (480MHz)
- STM32H743VIT6  ARM (480MHz)
- SensorsInvenSense MPU6000 IMU (accel, gyro) & ICM20602DPS310 barometerVoltage & 132A current sensor (integrated current sensor only on -WING V2/V3 and -WLITE)
- InvenSense MPU6000 IMU (accel, gyro) & ICM20602
- DPS310 barometer
- Voltage & 132A current sensor (integrated current sensor only on -WING V2/V3 and -WLITE)
- Power9V ~ 36V DC input power5V 2A BEC for peripherals9/12V 2A BEC for video5/6/7.2V 8A BEC for servos
- 9V ~ 36V DC input power
- 5V 2A BEC for peripherals
- 9/12V 2A BEC for video
- 5/6/7.2V 8A BEC for servos
- Interfaces7x UARTS13x PWM outputs1x RC input PWM/PPM, SBUS2x I2C ports for external compass, airspeed sensor, etc.SPI4 portUSB port (with remote cabling)CAN port6 ADCBuzzer and Safety SwitchDual Switchable Camera inputsBuilt-in OSDmicroSD cardSecond battery monitor input pins
- 7x UARTS
- 13x PWM outputs
- 1x RC input PWM/PPM, SBUS
- 2x I2C ports for external compass, airspeed sensor, etc.
- SPI4 port
- USB port (with remote cabling)
- CAN port
- 6 ADC
- Buzzer and Safety Switch
- Dual Switchable Camera inputs
- Built-in OSD
- microSD card
- Second battery monitor input pins
- Size and Dimensionstbd mm x tbd mm x tbd mmtbd g
- tbd mm x tbd mm x tbd mm
- tbd g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = UART7 (support CTS and RTS signaling)
- SERIAL2 = Telemetry2 = USART1
- SERIAL3 = GPS1 = USART2
- SERIAL4 = GPS2 = USART3
- SERIAL5 = USER = UART8
- SERIAL6 = USER = UART4
- SERIAL7 = USER = UART6 (TX only unlessBRD_ALT_CONFIG= 1, then RX available also)
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences.



---

## MFT-SEMA100
**Source URL:** https://ardupilot.org/plane/docs/common-mft-sema100.html

### Description
The MFT-SEMA100 is a flight controller designed and produced byMFT  Savunma ve HavacÄ±lÄ±k LTD. ÅTÄ°.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- BMI088 IMU
- BMP390 barometer
- LIB3MDL magnetometer
- MicroSD Card Slot
- 5 UARTs
- 12 PWM outputs
- 2 CANs
- 3 I2Cs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink2, DMA-enabled)
- SERIAL2 -> UART2 (MAVLink2, DMA-enabled)
- SERIAL3 -> UART3 (GPS, DMA-enabled)
- SERIAL4 -> UART5 (GPS2, DMA-enabled)
- SERIAL5 -> UART7 (DMA-enabled)
- SERIAL6 -> UART8 (RX only)



---

## MicoAir405v2/Mini
**Source URL:** https://ardupilot.org/plane/docs/common-MicoAir405v2.html

### Description
The MicoAir405v2 is a autopilot produced byMicoAir.
MINI

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 microcontrollerAT7456E OSD
- STM32F405 microcontroller
- AT7456E OSD
- SensorsBMI088 IMU (accel and gyro)/ Mini: BMI270 IMUSPL06 barometer / Mini: DPS310
- BMI088 IMU (accel and gyro)/ Mini: BMI270 IMU
- SPL06 barometer / Mini: DPS310
- Power2S  - 6S Lipo input voltage with voltage monitoring9V 3A (Mini: 2.5A) BEC for powering Video Transmitter5V 3A (Mini:2.5A) BEC for peripherals
- 2S  - 6S Lipo input voltage with voltage monitoring
- 9V 3A (Mini: 2.5A) BEC for powering Video Transmitter
- 5V 3A (Mini:2.5A) BEC for peripherals
- Interfaces10x PWM outputs/ Mini: 9 PWM outputs1x SBUS RC input6x UARTs/serial for GPS and other peripherals1x I2C port for external compassCamera/VTX/HD(DJI) VTX connectorsMicro-C USB portMicroSD Card Slot for loggingExternal current monitor input
- 10x PWM outputs/ Mini: 9 PWM outputs
- 1x SBUS RC input
- 6x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- Camera/VTX/HD(DJI) VTX connectors
- Micro-C USB port
- MicroSD Card Slot for logging
- External current monitor input


### Ports, UARTs & Pin Mapping
**PinoutÂ**
Mini

**UART MappingÂ**
The UARTs are marked Rxn and Tn in the above pinouts. The Rxn pin is the
receive pin for UARTn. The Txn pin is the transmit pin for UARTn.

**OSD SupportÂ**
The MicoAir405v2 supports analog OSD using OSD_TYPE 1 (MAX7456 driver) using the CAM and VTX connectors. DisplayPort HD OSD via the DJI connector is enabled simultaneously byOSD_TYPE2= 5.

**HD VTX SupportÂ**
The SH1.0-6P connector supports a standard DJI HD VTX connection. Pin 1 of the connector is 9v so be careful not to connect this to a peripheral requiring 5v.



---

## MicoAir743
**Source URL:** https://ardupilot.org/plane/docs/common-MicoAir743.html

### Description
The MicoAir743 is a flight controller designed and produced byMicoAir Tech..

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 microcontrollerAT7456E OSD
- STM32H743 microcontroller
- AT7456E OSD
- SensorsBMI088/BMI270 dual IMUsDPS310 barometerIST8310 magnetometer
- BMI088/BMI270 dual IMUs
- DPS310 barometer
- IST8310 magnetometer
- Power2S  - 6S Lipo input voltage with voltage monitoring9V 3A BEC; 5V 3A BEC
- 2S  - 6S Lipo input voltage with voltage monitoring
- 9V 3A BEC; 5V 3A BEC
- Interfaces10 PWM outputs7x UARTs/serial for GPS and other peripherals1x CAN portmicro USB portAll UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ1x I2C port for external compassmicroSD Card Slot for loggingExternal current monitor input1x SWD port
- 10 PWM outputs
- 7x UARTs/serial for GPS and other peripherals
- 1x CAN port
- micro USB port
- All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- 1x I2C port for external compass
- microSD Card Slot for logging
- External current monitor input
- 1x SWD port
- MechanicalMounting: 30.5 x 30.5mm, Î¦4mmDimensions: 36 x 36 x 8 mmWeight: 9g
- Mounting: 30.5 x 30.5mm, Î¦4mm
- Dimensions: 36 x 36 x 8 mm
- Weight: 9g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the
receive pin for UARTn. The TXn pin is the transmit pin for UARTn.

**OSD SupportÂ**
The MicoAir743 supports onboard OSD using OSD_TYPE 1 (MAX7456 driver). Simultaneously, DisplayPort HD OSD is enabled by default and available on the HD VTX connector, See below.

**VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 9v so be careful not to connect this to a peripheral requiring 5v.



---

## MicoAir743-AIO
**Source URL:** https://ardupilot.org/plane/docs/common-MicoAir743-AIO.html

### Description
The MicoAir743-AIO is a flight controller designed and produced byMicoAir Tech.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- BMI088/BMI270 dual IMUs
- DPS310 barometer
- 12V 2A BEC; 5V 2A BEC
- MicroSD Card Slot
- 7 UARTs
- Integrated 4-in-1 AM32 35A ESC, 5 additional PWM outputs, one defaulted as serial LED
- 1 I2C
- 1 SWD


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink2, DMA-enabled)
- SERIAL2 -> UART2 (DisplayPort, DMA-enabled)
- SERIAL3 -> UART3 (GPS, DMA-enabled)
- SERIAL4 -> UART4 (MAVLink2, DMA-enabled)
- SERIAL5 -> UART6 (RCIN, DMA-enabled)
- SERIAL6 -> UART7 (RX only, ESC Telemetry, DMA-enabled)
- SERIAL7 -> UART8 (User, DMA-enabled)
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 12v so be careful not to connect this to a peripheral requiring 5v.



---

## MicoAir743v2
**Source URL:** https://ardupilot.org/plane/docs/common-MicoAir743v2.html

### Description
The MicoAir743v2 is a flight controller designed and produced byMicoAir Tech.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- BMI088/BMI270 dual IMUs
- Integrated BlueTooth module for telemetry
- SPL06 barometer
- QMC5883L magnetometer
- AT7456E OSD
- 9V 3A BEC; 5V 3A BEC
- MicroSD Card Slot
- 8 UARTs
- 11 PWM outputs
- 1 I2C
- 1 SWD


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink2, DMA-enabled)
- SERIAL2 -> UART2 (DisplayPort, DMA-enabled)
- SERIAL3 -> UART3 (GPS, DMA-enabled)
- SERIAL4 -> UART4 (MAVLink2, DMA-enabled)
- SERIAL5 -> UART5 (User, DMA-enabled)
- SERIAL6 -> UART6 (RCIN, DMA-enabled)
- SERIAL7 -> UART7 (RX only, ESC Telemetry, DMA-enabled)
- SERIAL8 -> UART8 (MAVLink2, connected to on board BlueTooth module)

**OSD SupportÂ**
The MicoAir743v2 supports onboard OSD using OSD_TYPE 1 (MAX7456 driver). Simultaneously, DisplayPort OSD is available on the HD VTX connector, set OSD_TYPE2 = â5â.

**VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 9v so be careful not to connect this to a peripheral requiring 5v.



---

## Morakot
**Source URL:** https://ardupilot.org/plane/docs/common-morakot.html

### Description
The Morakot is a flight controller designed and produced byTaiphoon
Morakot Flight Controller âNDAA-Compliant. Made in Taiwan.Built for Performance.
Engineered, tested, and manufactured in Taiwan, the Morakot Flight Controller meets full NDAA compliance, ensuring trusted quality and security for professional applications. With an integrated Ethernet interface, it delivers high-speed, reliable connectivity for next-generation FPV and unmanned aerial systems.

### Ports, UARTs & Pin Mapping
**UART MappingÂ**
UART Mapping
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Port | UART | Protocol | TX DMA | RX DMA
0 | USB | MAVLink2 | â | â
1 | USART1 | MSP_DisplayPort | â | â
2 | USART2 | MAVLink2 | â | â
3 | USART3 | None | â | â
4 | UART5 | GPS | â | â
5 | USART6 | ESCTelemetry | â | â
6 | UART7 | MAVLink2 | â | â
7 | UART8 | RCIN | â | â
-RTS/CTS flow control is available on UART7.

**VTX SupportÂ**
The JST-GH 7p connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 12v so be careful not to connect this to a peripheral that can not tolerate this voltage.

**ESC1 - 8 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | VBAT IN | 12V-33.6V
2 | UART6_RX | 3.3V
3 | GND | 3.3V
4 | CURRENT | 3.3V
5 | MOTOR/SERVO 1 | 3.3V
6 | MOTOR/SERVO 2 | 3.3V
7 | MOTOR/SERVO 3 | 3.3V
8 | MOTOR/SERVO 4 | 3.3V

**ESC2 - 8 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | VBAT IN | 12V-33.6V
2 | MOTOR/SERVO 9 | 3.3V
3 | GND | 3.3V
4 | CURRENT | 3.3V
5 | MOTOR/SERVO 5 | 3.3V
6 | MOTOR/SERVO 6 | 3.3V
7 | MOTOR/SERVO 7 | 3.3V
8 | MOTOR/SERVO 8 | 3.3V

**CAN - 4 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | CAN1_H | 5.0V
3 | CAN1_L | 5.0V
4 | GND | GND

**GPS - 6 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | UART5_TX | 3.3V
3 | UART5_RX | 3.3V
4 | I2C1_SCL | 3.3V
5 | I2C1_SDA | 3.3V
6 | GND | GND

**UART(TELEM) - 6 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | UART7_TX | 3.3V
3 | UART7_RX | 3.3V
4 | UART7_CTS | 3.3V
5 | UART7_RTS | 3.3V
6 | GND | GND

**VTX - 7 Pin JST-GHÂ**
Note: connector pinout not in same order as standard HD VTX cabling
Pin | Signal Name | Voltage
1 | VIDEO | na
2 | 12.0V | 12.0V
3 | GND | GND
4 | USART1_RX | 3.3V
5 | USART1_TX | 3.3V
6 | GND | 3.3V
7 | USART3_RX | GND

**SPI (external OSD or IMU) - 6 Pin JST-SHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | SPI4_MOSI | 3.3V
3 | SPI4_MISO | 3.3V
4 | SPI4_SCK | 3.3V
5 | SPI4_CS | 3.3V
6 | GND | GND

**RC - 4 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | 5.0V | 5.0V
2 | UART8_RX | 3.3V
3 | UART8_TX | 3.3V
4 | GND | GND

**ETH - 4 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | RXN | 3.3V
2 | RXP | 3.3V
3 | TXN | 3.3V
4 | TXP | 3.3V



---

## mRo ControlZero F7
**Source URL:** https://ardupilot.org/plane/docs/common-mro-control-zero-F7.html

### Description


### Specifications
**SpecificationsÂ**
- 32-bit STM32F777 Cortex M4 core with FPU rev. 3 216 MHz/512 KB RAM/2 MB Flash
- F-RAM Cypress MF25V02-G 256-Kbit nonvolatile memory (Flash memory that performs as fast as RAM)
- Bosch BMI088 3-axis accelerometer/gyroscope (internally vibration dampened)
- Invensense ICM-20602 3-axis accelerometer/gyroscope
- Invensense ICM-20948 3-axis accelerometer/gyroscope/magnetometer
- Infineon DPS310 barometer (So smooth and NO more light sensitivity)
- Spektrum DSM / DSM2 / DSM-XÂ® Satellite compatible input and binding
- Futaba S.BUSÂ® & S.BUS2Â® compatible input
- FRSky Telemetry port output
- Graupner SUMD
- Yuneec ST24
- PPM sum input signal
- 8x PWM outputs (all DShot capable)
- 1x RSSI (PWM or voltage) input
- 6x UART (serial ports total), two with HW flow control
- USB console input with two endpoints, one defaults to MAVLink for GCS, one for SLCAN
- 1x I2C
- 1x SPI
- 1x CAN
- 1x JTAG (TC2030 Connector)
- 3x Ultra low noise LDO voltage regulators
- Tricolor LED


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB (normally for GCS connection)
- SERIAL1 = Telemetry1 = USART2
- SERIAL2 = Telemetry2 = USART3
- SERIAL3 = GPS1 = UART4
- SERIAL4 = GPS2 = UART8 (labelled as FrSky Telem, but can be used for any serial device, defaults to GPS protocol)
- SERIAL5 = User = UART7 (USER/DEBUG)
- SERIAL6 = OTG2 (virtual USB connection for SLCAN or passthru use)
Serial protocols can be adjusted to personal preferences.



---

## mRo Pixracer Pro (H7)
**Source URL:** https://ardupilot.org/plane/docs/common-pixracer-pro.html

### Description
ThePixracer Prois the next generation
autopilot of mRoâs Pixracer family.

### Specifications
**SpecificationsÂ**
- Processor:MCU - STM32H743IIK62MB flash allows full features of ArduPilot to be flashed256KB FRAM - FM25V02-G
- MCU - STM32H743IIK6
- 2MB flash allows full features of ArduPilot to be flashed
- 256KB FRAM - FM25V02-G
- SensorsGyro/Accelerometer: Invensense ICM-20948 / Gyro / Mag (? KHz)Gyro/Accelerometer: Invensense ICM-20602 Accel / Gyro (? KHz)Gyro/Accelerometer: Bosch BMI088 Accel / Gyro (? KHz)Barometer: DSP310
- Gyro/Accelerometer: Invensense ICM-20948 / Gyro / Mag (? KHz)
- Gyro/Accelerometer: Invensense ICM-20602 Accel / Gyro (? KHz)
- Gyro/Accelerometer: Bosch BMI088 Accel / Gyro (? KHz)
- Barometer: DSP310
- Power5-5.5VDC from USB or PowerBrick connector. Optional/recommendedACSP4 +5V/+12V Power Supply.Ultra low noise LDOs for sensors and FMU
- 5-5.5VDC from USB or PowerBrick connector. Optional/recommendedACSP4 +5V/+12V Power Supply.
- Ultra low noise LDOs for sensors and FMU
- Interfaces/ConnectivityMicroSD card readerMicro-C USBRGB LEDGPS (serial + I2C)TELEM1/TELEM2FrSky Telemetry serial portOn-Board Buzzer8 Servo/Motor Outputs, 3.3V (default) or 5V level selectable (GPIO 74)Connectors: GPS+I2C (USART4), RC-IN/PPM-IN/RSSI/SBus-IN/Spektrum-IN,
USART3 (TxD, RxD, CTS, RTS), USART2 (TxD, RxD, CTS, RTS),
USART8(FRSky-IN/FRSky-OUT), CAN1, CAN2,
SERVO1-SERVO8, USART1/USART7 (TxD, RxD), SPI6, POWER-BRICK
(VDD, Voltage, Current, GND).
- MicroSD card reader
- Micro-C USB
- RGB LED
- GPS (serial + I2C)
- TELEM1/TELEM2
- FrSky Telemetry serial port
- On-Board Buzzer
- 8 Servo/Motor Outputs, 3.3V (default) or 5V level selectable (GPIO 74)
- Connectors: GPS+I2C (USART4), RC-IN/PPM-IN/RSSI/SBus-IN/Spektrum-IN,
USART3 (TxD, RxD, CTS, RTS), USART2 (TxD, RxD, CTS, RTS),
USART8(FRSky-IN/FRSky-OUT), CAN1, CAN2,
SERVO1-SERVO8, USART1/USART7 (TxD, RxD), SPI6, POWER-BRICK
(VDD, Voltage, Current, GND).
- DimensionsWeight ?Size
- Weight ?
- Size


### Ports, UARTs & Pin Mapping
**Connector pin assignmentsÂ**
Unless noted otherwise all connectors are JST GH

**UART1/UART7 connectorÂ**
PIN | SIGNAL | VOLTAGE/TOLERANCE
1 | +5V | +5V
2 | TX1 | +3.3V/5V
3 | RX1 | +3.3V/5V
4 | GND | GND
5 | +5V | +5V
6 | TX7 | +3.3V/5V
7 | RX7 | +3.3V/5V
8 | GND | GND

**Default UART orderÂ**
Parameter | Default Protocol** | Connector
SERIAL0 | console | USB
SERIAL1 | Telemetry1 | USART2 (supports CTS and RTS signaling)
SERIAL2 | Telemetry2 | USART3 (supports CTS and RTS signaling)
SERIAL3 | GPS1 | UART4
SERIAL4 | GPS2 | UART8  (targeted for FrSky Telem, but must change SERIAL4_PROTOCOL)
SERIAL5 | USER | USART1
SERIAL6 | USER | UART7
SERIAL7 | SLCAN | USB (second composite USB interface)
** User may change SERIALx_PROTOCOL as required for application



---

## mRo Nexus
**Source URL:** https://ardupilot.org/plane/docs/common-mro-nexus.html

### Description
ThemRo Nexusis new member of mRoâs Pixracer autopilot family.

### Specifications
**SpecificationsÂ**
- Processor:MCU - STM32H743VIH62MB flash allows full features of ArduPilot to be flashed
- MCU - STM32H743VIH6
- 2MB flash allows full features of ArduPilot to be flashed
- SensorsGyro/Accelerometer: Invensense ICM-40609D / Gyro (? KHz)Barometer: DSP310RM3100 Precision Compass
- Gyro/Accelerometer: Invensense ICM-40609D / Gyro (? KHz)
- Barometer: DSP310
- RM3100 Precision Compass
- Power5-5.5VDC from USB or PowerBrick connector. Optional/recommendedACSP4 +5V/+12V Power Supply.Ultra low noise LDOs for sensors and FMU
- 5-5.5VDC from USB or PowerBrick connector. Optional/recommendedACSP4 +5V/+12V Power Supply.
- Ultra low noise LDOs for sensors and FMU
- Interfaces/ConnectivityDual CAN/DroneCAN portsMicroSD card readerMicro-C USBRGB LEDGPS (serial + I2C)UART for serial RC inputConnectors: GPS+I2C (USART4),CAN1, CAN2,
USART7 (TxD, RxD), POWER-BRICK(VDD, Voltage, Current, GND).
- Dual CAN/DroneCAN ports
- MicroSD card reader
- Micro-C USB
- RGB LED
- GPS (serial + I2C)
- UART for serial RC input
- Connectors: GPS+I2C (USART4),CAN1, CAN2,
USART7 (TxD, RxD), POWER-BRICK(VDD, Voltage, Current, GND).
- DimensionsWeight ?Size
- Weight ?
- Size


### Ports, UARTs & Pin Mapping
**Connector pin assignmentsÂ**
Unless noted otherwise all connectors are JST GH

**UART7 connectorÂ**
PIN | SIGNAL | VOLTAGE/TOLERANCE
1 | +5V | +5V
2 | TX1 | +3.3V/5V
3 | RX1 | +3.3V/5V
4 | GND | GND

**Default UART orderÂ**
Parameter | Default Protocol** | Connector/Suggested Use
SERIAL0 | console | USB
SERIAL1 | Telemetry1 | UART7/Serial RC input
SERIAL2 | Telemetry2 | USB (second composite USB interface)/SLCAN
SERIAL3 | GPS1 | UART4/GPS
** User may change SERIALx_PROTOCOL as required for application



---

## MUPilot
**Source URL:** https://ardupilot.org/plane/docs/common-MUPilot.html

### Description
The MUPilot flight controller is sold byMUGIN UAV

### Specifications
**FeaturesÂ**
- STM32F765 Microcontroller
- STM32F103 IOMCU
- Three IMUs: ICM20689, MPU6000 and BMI055
- Internal vibration isolation for IMUs
- Two MS5611 SPI barometers
- IST8310 magnetometer
- MicroSD card slot
- 6 UARTs plus USB
- 14 PWM outputs with selectable 5V or 3.3V output voltage
- Four I2C and two CAN ports
- External Buzzer
- builtin RGB LED
- external safety Switch
- voltage monitoring for servo rail and Vcc
- two dedicated power input ports for external power bricks


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART2 (Telem1)
- SERIAL2 -> UART3 (Telem2)
- SERIAL3 -> UART1 (GPS)
- SERIAL4 -> UART4 (GPS2)
- SERIAL5 -> UART6 (spare)
- SERIAL6 -> UART7 (spare, debug)
- SERIAL7 -> USB2  (SLCAN)
The Telem1 and Telem2 ports have RTS/CTS pins, the other UARTs do not
have RTS/CTS.
The UART7 connector is labeled debug, but is available as a general
purpose UART with ArduPilot.



---

## NarinFC-H7/H5
**Source URL:** https://ardupilot.org/plane/docs/common-NarinFC-H7.html

### Description
The NarinFC-H7/H5 is an advanced autopilot family designed in-house byVOLOLAND CO., LTD.
It uses a high performance STM32H7 processor and integrates industrial-grade sensors.

### Specifications
**Features/SpecificationsÂ**
- ProcessorSTM32H743
- STM32H743
- SensorsAccelerometer/Gyroscope: ADIS16470(H7) or ICM-45686(H5)Accelerometer/Gyroscope: ICM-20649(H7 or ICM-45686(H5)Accelerometer/Gyroscope: BMI088Magnetometer: RM3100Barometer: MS5611*2
- Accelerometer/Gyroscope: ADIS16470(H7) or ICM-45686(H5)
- Accelerometer/Gyroscope: ICM-20649(H7 or ICM-45686(H5)
- Accelerometer/Gyroscope: BMI088
- Magnetometer: RM3100
- Barometer: MS5611*2
- Interfaces14 PWM servo outputsSupport multiple RC inputs (SBus / CPPM / DSM)Analog/PWM RSSI input2 GPS ports (GPS and UART4 ports)4 â¹ I2C buses2 â¹ CAN bus ports2 â¹ Power ports2 â¹ ADC ports1 â¹ USB-C port
- 14 PWM servo outputs
- Support multiple RC inputs (SBus / CPPM / DSM)
- Analog/PWM RSSI input
- 2 GPS ports (GPS and UART4 ports)
- 4 â¹ I2C buses
- 2 â¹ CAN bus ports
- 2 â¹ Power ports
- 2 â¹ ADC ports
- 1 â¹ USB-C port
- PowerPower 4.3V ~ 5.4VUSB Input 4.75V ~ 5.25V
- Power 4.3V ~ 5.4V
- USB Input 4.75V ~ 5.25V
- Size and Dimensions93.4mm x 46.4mm x 34.1mm106g
- 93.4mm x 46.4mm x 34.1mm
- 106g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 = USB (MAVLink2 default)
- SERIAL1 = USART2,Telemetry1 (MAVlink2 default,DMA-enabled)
- SERIAL2 = USART6,Telemetry2 (MAVlink2 default,DMA-enabled)
- SERIAL3 = USART1,GPS1 (GPS default, DMA-enabled)
- SERIAL4 = UART4,GPS2 (GPS2 default)
- SERIAL5 = UART8 (not available except on custom carrier boards)(USER default,DMA-enabled)
- SERIAL6 = UART7,DEBUG (USER)
- SERIAL7 = USB2 (MAVLink2 default)
Serial protocols can be adjusted to personal preferences.

**Connectors and PinoutsÂ**
- 1. TELEM1, TELEM2 PortJST GH 6P connector
- JST GH 6P connector
- 2. CAN1, CAN2 PortJST GH 4P connector
- JST GH 4P connector
- 3. I2C, I2C2, I2C3, I2C4 PortJST GH 4P connector
- JST GH 4P connector
- 4. UART4 PortJST GH 6P connector
- JST GH 6P connector
- 5. RSSI PortRSSI input
- RSSI input
- 6. GPS & Safety PortJST GH 10P connector
- JST GH 10P connector
- 7. PWM & RC_INThe NarinFC-H7 supports up to 14 PWM outputs. Outputs are grouped and all outputs within their group must be the same protocol.2.54mm pitch DuPont connectorRC_IN : Remote control receiver input for unidirectional protocols, others need to use a full UART
- 2.54mm pitch DuPont connector
- RC_IN : Remote control receiver input for unidirectional protocols, others need to use a full UART
- 8. Power Input2mm pitch DuPont connector
- 2mm pitch DuPont connector
- 9. ADC PortSpare ADC inputs
- Spare ADC inputs
- 10. DEBUG & UART7 PortJST GH 6P connector
- JST GH 6P connector
- 11. USB PortUSB C Type
- USB C Type
- 12. SPI PortJST GH 7P connector
- JST GH 7P connector
- 13. SD CARDSD CARD
- SD CARD



---

## NarinFC-X3
**Source URL:** https://ardupilot.org/plane/docs/common-NarinFC-X3.html

### Description
The NarinFC-X3 is a flight controller produced by VOLOLAND Inc.
NarinFC-X3 is an advanced autopilot family designed in-house byVOLOLAND Inc.It uses a higher-performance STM32H7 processor and integrates industrial-grade sensors.
Compared with previous autopilots, it has better performance and higher reliability.

### Specifications
**Features/SpecificationsÂ**
- ProcessorSTM32H743
- STM32H743
- SensorsAccelerometer/Gyroscope: ICM-42688 * 2Barometer: DPS368XTSA1
- Accelerometer/Gyroscope: ICM-42688 * 2
- Barometer: DPS368XTSA1
- Interfaces12 * PWM servo outputs1 * I2C buses1 * CAN bus ports5 * UART1 * USB Type-C1 * MicroSD cardJST Connector (SH1.0)
- 12 * PWM servo outputs
- 1 * I2C buses
- 1 * CAN bus ports
- 5 * UART
- 1 * USB Type-C
- 1 * MicroSD card
- JST Connector (SH1.0)
- PowerInput Power 6VDC ~ 36VDC (2S ~ 8S)Output Power3.3V DC 0.5A5V DC 2.5A9V DC 2.5A
- Input Power 6VDC ~ 36VDC (2S ~ 8S)
- Output Power3.3V DC 0.5A5V DC 2.5A9V DC 2.5A
- 3.3V DC 0.5A
- 5V DC 2.5A
- 9V DC 2.5A
- Size and Dimensions38mm x 38mm ( mount hole 30.5mm * 30.5mm)8g
- 38mm x 38mm ( mount hole 30.5mm * 30.5mm)
- 8g


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB (MAVLink2)
- SERIAL1 -> UART1 (RX1 is SBUS in HD VTX connector)
- SERIAL2 -> UART2 (GPS, DMA-enabled)
- SERIAL3 -> UART3 (DisplayPort, DMA-enabled)
- SERIAL4 -> UART4 (MAVLink2, Telem1)
- SERIAL6 -> UART6 (RC Input, DMA-enabled)
- SERIAL7 -> UART7 (MAVLink2, Telem2, DMA and flow-control enabled)
- SERIAL8 -> UART8 (ESC Telemetry, RX8 on ESC connector for telem)
Serial protocols can be adjusted to personal preferences.

**Connectors and PinoutsÂ**
- 1. I2C, UART2 PortI2C1UART 2: Ardupilot port Serial2 GPS1
- I2C1
- UART 2: Ardupilot port Serial2 GPS1
- 2. UART 4, UART 7 PortUART 4: Ardupilot port Serial4 Telem_1UART 7: Ardupilot port Serial7 Telem_2
- UART 4: Ardupilot port Serial4 Telem_1
- UART 7: Ardupilot port Serial7 Telem_2
- 3. UART 6, RSSI PortUART 6: Ardupilot port Serial6 Receiver
- UART 6: Ardupilot port Serial6 Receiver
- 4. CAN PortJST GH 6P connector
- JST GH 6P connector
- 5. PWM Port-1PWM 1 ~ PWM 4UART8_RXADC 1BATT Input
- PWM 1 ~ PWM 4
- UART8_RX
- ADC 1
- BATT Input
- 6. PWM Port-2PWM 5 ~ PWM 8UART8_RXADC 2BATT Input
- PWM 5 ~ PWM 8
- UART8_RX
- ADC 2
- BATT Input
- 7. UART 3 PortUART 3: Ardupilot port Serial3 MSP Display Port2.54mm pitch DuPont connectorRC_IN : Remote control receiver
- 2.54mm pitch DuPont connector
- RC_IN : Remote control receiver
- 8. MicroSD Card Slot
- 9. PWM Port-3PWM 9 ~ PWM 12
- PWM 9 ~ PWM 12
- 10. DEBUG & UART7 PortJST GH 6P connectorDEBUG NODMA
- JST GH 6P connector
- DEBUG NODMA

**OSD SupportÂ**
The NarinFC-X3 supports analog OSD using its internal MAX7456 and simultaneously DisplayPort using TX3/RX3 on the HD VTX connector.



---

## NxtPX4v2
**Source URL:** https://ardupilot.org/plane/docs/common-NxtPX4v2.html

### Description
The NxtPX4v2 is an open-source hardware designed and maintained byHKUST UAV-Group. And it is produced byMicoAir Tech..

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 microcontroller
- STM32H743 microcontroller
- SensorsBMI088+BMI088(DUAL) IMU (accel and gyro)SPL06 barometer
- BMI088+BMI088(DUAL) IMU (accel and gyro)
- SPL06 barometer
- Power2S  - 6S Lipo input voltage with voltage monitoring12V 2.5A BEC for powering Video Transmitter5V 2.5A BEC for peripherals
- 2S  - 6S Lipo input voltage with voltage monitoring
- 12V 2.5A BEC for powering Video Transmitter
- 5V 2.5A BEC for peripherals
- Interfaces8x PWM outputs1x SBUS RC input7x UARTs/serial for GPS and other peripherals1x I2C port for external compass1x SPI1x SWD portCamera/VTX/HD(DJI) VTX connectorsMicro-C USB portMicroSD Card Slot for loggingExternal current monitor input
- 8x PWM outputs
- 1x SBUS RC input
- 7x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- 1x SPI
- 1x SWD port
- Camera/VTX/HD(DJI) VTX connectors
- Micro-C USB port
- MicroSD Card Slot for logging
- External current monitor input
- Physical


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rxn and Tn in the above pinouts. The Rxn pin is the
receive pin for UARTn. The Txn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART2 (MAVLink2, DMA-enabled)
- SERIAL2 -> UART4 (MAVLink2, DMA-enabled)
- SERIAL3 -> UART1 (GPS, DMA-enabled)
- SERIAL4 -> UART3 (DisplayPort, DMA-enabled)
- SERIAL5 -> UART7 (RX only, ESC Telemetry, DMA-enabled)
- SERIAL6 -> UART5 (RCIN, DMA-enabled)
- SERIAL7 -> UART8 (User, DMA-enabled)

**HD VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 12v so be careful not to connect this to a peripheral requiring 5v.



---

## Omnibus F4 AIO/Pro
**Source URL:** https://ardupilot.org/plane/docs/common-omnibusf4pro.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 ARM
- STM32F405 ARM
- SensorsInvenSense MPU6000 IMU (accel, gyro)BMP280 barometerVoltage and current (only Pro version) sensors
- InvenSense MPU6000 IMU (accel, gyro)
- BMP280 barometer
- Voltage and current (only Pro version) sensors
- InterfacesUARTS6 or 8 PWM (Pro only) outputsRC input PWM/PPM, SBUSI2C port for external compassUSB portBuilt-in OSD
- UARTS
- 6 or 8 PWM (Pro only) outputs
- RC input PWM/PPM, SBUS
- I2C port for external compass
- USB port
- Built-in OSD


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1
- SERIAL2 = not assigned (Telemetry2 = USART3 ifBRD_ALT_CONFIG=1)
- SERIAL3 = GPS1 = USART6
- SERIAL4 = GPS2 = UART4 (ifBRD_ALT_CONFIG= 2 or 3)
- SERIAL5 = not assigned
- SERIAL6 = not assigned
Serial protocols can be adjusted to personal preferences.

**How to trigger a camera with relay pinÂ**
Any PWM output can be used as a relay pin. SeeGPIOs
RELAY2_PIN= 54 for output PWM 5 to be assigned to RELAY2
Hardware definition is availablehere.



---

## OmnibusNanoV6
**Source URL:** https://ardupilot.org/plane/docs/common-omnibusnanov6.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 ARM
- STM32F405 ARM
- SensorsInvenSense MPU6000 IMU (accel, gyro)BMP280 barometerVoltage sensor
- InvenSense MPU6000 IMU (accel, gyro)
- BMP280 barometer
- Voltage sensor
- Interfaces2 full UARTS (RX and TX)1 RX only UART for ESC telemetry4 PWM outputsRC input PPM, SBUS, CRSF etc.I2C port for external compassUSB portBuilt-in OSDOnboard voltage sensoradditional ADC for current sensor on V6.x revision only. Current sensing on original V6 available using ESC telemetry.Onboard winbond 25Q128 for dataflash-type logging
- 2 full UARTS (RX and TX)
- 1 RX only UART for ESC telemetry
- 4 PWM outputs
- RC input PPM, SBUS, CRSF etc.
- I2C port for external compass
- USB port
- Built-in OSD
- Onboard voltage sensor
- additional ADC for current sensor on V6.x revision only. Current sensing on original V6 available using ESC telemetry.
- Onboard winbond 25Q128 for dataflash-type logging


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (only available on original V6 version)
- SERIAL2 = Telemetry2 = USART4 (RX only for ESC telemetry)
- SERIAL3 = GPS1 = USART6
- SERIAL4 = USART3 available inBRD_ALT_CONFIG= 1 (firmware 4.1 or later)
- SERIAL5 = not assigned
- SERIAL6 = not assigned
Serial protocols can be adjusted to personal preferences.



---

## Omnibus F7V2
**Source URL:** https://ardupilot.org/plane/docs/common-omnibusf7.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32F745VG ARM1MB of Flash memory
- STM32F745VG ARM
- 1MB of Flash memory
- SensorsInvenSense MPU6000 IMU (accel, gyro) with vibration isolationInvenSense ICM20608 IMU (accel, gyros, compass) with vibration isolationBMP280 barometer
- InvenSense MPU6000 IMU (accel, gyro) with vibration isolation
- InvenSense ICM20608 IMU (accel, gyros, compass) with vibration isolation
- BMP280 barometer
- InterfacesUARTSPWM outputsRC input PWM/PPM, SBUSI2C port for external compassUSB portBuilt-in OSDVoltage and Current sensing inputs (Needs external current sensor)
- UARTS
- PWM outputs
- RC input PWM/PPM, SBUS
- I2C port for external compass
- USB port
- Built-in OSD
- Voltage and Current sensing inputs (Needs external current sensor)
- Size and Dimensions36mm x 36mm
- 36mm x 36mm


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1
- SERIAL2 = Telemetry2 = USART3 ifBRD_ALT_CONFIG= 2, otherwise these pins are used for I2C pins (firmware 4.1 or later)
- SERIAL3 = GPS1 = USART6
- SERIAL4 = GPS2 = USART2 (RX only ifBRD_ALT_CONFIG= 1, otherwise this pin is used for RC input labeled SBUS on board)
- SERIAL5 = USER = UART7 (RX only, in V2 only)
- SERIAL6 = not assigned
Serial protocols can be adjusted to personal preferences.



---

## OrbitH743
**Source URL:** https://ardupilot.org/plane/docs/common-orbith743.html

### Description
The above image and some content courtesy ofOrbit Technology-.

### Specifications
**SpecificationsÂ**
Processor
- STM32H743VIH6 (480MHz)
- 256MB Flash for data logging
Sensors
- InvenSense 2x ICM42688 IMU (accel, gyro)
- DPS368 barometer
- Voltage & Current sensor
Power
- 2â6S LiPo input power
- 5V 3A BEC for peripherals
- 10V 3A BEC for video, GPIO controlled
Interfaces
- USB Type-C port
- 8x UARTs
- 13x PWM outputs(one for serial LED by default) via two 8-pin ESC connectors and/or solder pads
- 1x RC input (PWM/SBUS)
- I2C port for external compass, airspeed sensor, etc.
- HD VTX support
- Dual switchable analog Camera inputs
- 2x Power Monitor
- Buzzer and LED strip
- Built-in OSD
Size and Dimensions
- 38.3 mm x 39.8 mm
- 8.4 g
- 30.5 mm x 30.5 mm mounting holes


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0= USB (MAVLink2)
- SERIAL1= UART1 (ESC Telemetry)
- SERIAL2= UART2 (USER)
- SERIAL3= UART3 (DJI HD Air Unit)
- SERIAL4= UART4 (VTX)
- SERIAL5= UART5 (RC Input)
- SERIAL6= UART6 (GPS)
- SERIAL7= UART7 (USER)
- SERIAL8= UART8 (USER)
All UARTs have DMA capability except UART 1

**OSD SupportÂ**
The ORBITH743 has an onboard OSD using a MAX7456 chip and is enabled by default. The CAM1/2 and VTX pins provide connections for using the internal OSD. Simultaneous DisplayPort OSD is also possible and is configured by default.

**GPIO Pin MappingÂ**
- PWM1 â 50
- PWM2 â 51
- PWM3 â 52
- PWM4 â 53
- PWM5 â 54
- PWM6 â 55
- PWM7 â 56
- PWM8 â 57
- PWM9 â 58
- PWM10 â 59
- PWM11 â 60
- PWM12 â 61
- LED â 62
- BUZZER â 80
- VTX PWR â 81 (internal)
- CAM SWâ 82 (internal)



---

## OrqaF405
**Source URL:** https://ardupilot.org/plane/docs/common-OrqaF405.html

### Description
The Orqa FC 3030 F405 is an NDAA compliant flight controller produced byOrqa

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405 microcontrollerAT7456E OSD16Mbyte dataflash for logging
- STM32F405 microcontroller
- AT7456E OSD
- 16Mbyte dataflash for logging
- SensorsMPU6000 IMU (accel and gyro)DPS310 Barometer
- MPU6000 IMU (accel and gyro)
- DPS310 Barometer
- Power2S  - 6S Lipo input voltage with voltage monitoring10V 2A  BEC for powering Video Transmitter5V 2A (Mini:2.5A) BEC for peripherals
- 2S  - 6S Lipo input voltage with voltage monitoring
- 10V 2A  BEC for powering Video Transmitter
- 5V 2A (Mini:2.5A) BEC for peripherals
- Interfaces8x PWM outputs4x UARTs/serial for RCin, GPS, and other peripherals1x I2C port for external compassVTX connectorSwitchable dual camera inputsMicro-C USB portMicroSD Card Slot for loggingExternal current monitor input
- 8x PWM outputs
- 4x UARTs/serial for RCin, GPS, and other peripherals
- 1x I2C port for external compass
- VTX connector
- Switchable dual camera inputs
- Micro-C USB port
- MicroSD Card Slot for logging
- External current monitor input


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rxn and Tn in the above pinouts. The Rxn pin is the
receive pin for UARTn. The Txn pin is the transmit pin for UARTn.

**OSD SupportÂ**
The Orqa FC 3030 F405 supports analog OSD using OSD_TYPE 1 (MAX7456 driver) using the CAM and VTX connectors. DisplayPort HD OSD can be enabled simultaneously by settingOSD_TYPE= 5 and using USART6 for telemetry to the HD air unit by settingSERIAL6_PROTOCOL= 42.



---

## Parrot C.H.U.C.K
**Source URL:** https://ardupilot.org/plane/docs/common-CHUCK-overview.html

### Description
The heart of the Parrot Disco is the C.H.U.C.K autopilot, an orange
box which is a general purpose autopilot. It is perfectly possible to
use the C.H.U.C.K in a different airframe.
To use the C.H.U.C.K outside of a Disco the first thing you will
notice is it has 7 servo/motor outputs available. There are 6 PWM
3-pin servo connectors, and one connector from the I2C ESC that can be
used to drive a brushless motor (it drives the motor on the Disco).
The mapping between ArduPilot output channel numbers and the 7 outputs
was chosen with ease of integration with the Disco in mind, which
resulted in a fairly strange pin ordering.
Servo rail pin numbers in the list below are from left to right when
looking at the C.H.U.C.K from the back, so pin1 on the servo rail is
closest to the first âCâ in âC.H.U.C.Kâ on the case.
Note that this pin ordering means you will need some extra parameter
settings if you are not using the I2C ESC motor controller for
throttle output. To take the simple example of a 4 channel fixed wing
plane (aileron, elevator, throttle, rudder) you could configure and
wire it like this:
Apart from that pin mapping, setting up a C.H.U.C.K with another
airframe is the same as with any aircraft with ArduPilot. It could be
used with any vehicle type supported by ArduPilot, including gliders,
quadplanes, petrol planes, multicopters or rovers.
For R/C input there is a 3-pin servo lead connector on the left side
of the C.H.U.C.K which accepts the following widely used R/C
protocols:
The use of the airspeed sensor and sonar will be dependent on the
physical shape of the airframe and whether the positioning of these
sensors is suitable for the layout of the C.H.U.C.K.


---

## PixFlamingo- F767
**Source URL:** https://ardupilot.org/plane/docs/common-pixflamingo-f767.html

### Description
The PixFlamingo-F767 is a flight controller produced by Dheeran Labs.
Contactdheeranlabs@gmail.comfor sales

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F767 32-bit processor
- STM32F767 32-bit processor
- SensorsICM42670, MPU6500/ICM20602 Acc/GyroOne SPI barometer, either: MS5611/BMP280/DPS310
- ICM42670, MPU6500/ICM20602 Acc/Gyro
- One SPI barometer, either: MS5611/BMP280/DPS310
- Power5v input voltage with voltage monitoring3.3V, 1A BEC
- 5v input voltage with voltage monitoring
- 3.3V, 1A BEC
- Interfaces10x PWM outputs, 8DShot capable1x RC input5x UARTs/serial for GPS and other peripherals2x I2C ports for external compass, airspeed, etc.USB-C port and boot button on separate dongle for ease of accessmicroSD card slot portInternal RGB LEDSafety switch portBuzzer port
- 10x PWM outputs, 8DShot capable
- 1x RC input
- 5x UARTs/serial for GPS and other peripherals
- 2x I2C ports for external compass, airspeed, etc.
- USB-C port and boot button on separate dongle for ease of access
- microSD card slot port
- Internal RGB LED
- Safety switch port
- Buzzer port


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB (OTG1)
- SERIAL1 -> UART3 (TELEM1) with CTS/RTS DMA Enabled
- SERIAL2 -> UART6 (TELEM2) with DMA Enabled
- SERIAL3 -> UART1 (GPS1) Tx(NODMA), Rx(DMA Enabled)
- SERIAL4 -> EMPTY
- SERIAL5 -> UART7 (User) NODMA
- SERIAL6 -> USART2 (User) NODMA



---

## PixSurveyA2-IND
**Source URL:** https://ardupilot.org/plane/docs/common-pixsurveya2-ind.html

### Description
The PixSurveyA2-IND flight controller is sold by a range of resellers listed on the makeflyeasy(http://www.makeflyeasy.com)

### Specifications
**FeaturesÂ**
- STM32H743VIT6 microcontroller
- STM32F103C8T6 IOMCU microcontroller
- 3x IMUs, 2- ICM-42652(SPI), one ICM42688-P(SPI)internal heater for IMUs temperature controlinternal Soft Rubber Damping Ball isolation for All interna IMUs
- internal heater for IMUs temperature control
- internal Soft Rubber Damping Ball isolation for All interna IMUs
- 2x barometers, BMP388(SPI)
- Built-in RAMTRON(SPI)
- microSD card slot
- 5 UARTs
- USB(Type-C)
- PPM & S.Bus input
- 14 PWM outputs
- Two I2C ports and Two FDCAN ports, with multiple connectors
- S.Bus output
- internal Buzzer
- Two power module inputs, one analog and one CAN
- Independent power input for servo rail BEC
- External safety Switch


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> console MAVLink2, USB)
- SERIAL1 -> USART2 (Telem1, MAVLINK2) (DMA capable)
- SERIAL2 -> USART3 (Telem2, MAVLink2) (DMA capable)
- SERIAL3 -> UART4 (GPS1) (TX is DMA capable)
- SERIAL4 -> UART8 (GPS2) (RX is DMA capable)
- SERIAL5 -> UART7 (USER)

**POWER_CAN1 portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CAN_H | +12V
4 | CAN_L | +12V
5 | GND | GND
6 | GND | GND

**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**I2C1, I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL | +3.3V
3 | SDA | +3.3V
4 | GND | GND

**CAN1, CAN2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**Safety and buzzer port(labeled SWITCH)Â**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | LED | +5V
3 | Safety Switch | +5V

**GPS1/I2C1, GPS2/I2C2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Serial5 portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**Power2 ADC portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND



---

## RadioLink MiniPix
**Source URL:** https://ardupilot.org/plane/docs/common-radiolink-minipix.html

### Description
above image and some content courtesy of theRadioLink website

### Specifications
**SpecificationsÂ**
- Processor and SensorsSTM32F405VGT6 ARM microcontrollerInvenSense MPU6500Compass QMC5883LBarometer LPS22HB
- STM32F405VGT6 ARM microcontroller
- InvenSense MPU6500
- Compass QMC5883L
- Barometer LPS22HB
- Interfaces6x PWM outputs1x RC input (PWM/PPM, SBUS)3 UARTS (flow-control on Telem 1 & 2, no flow-control on GPS port)external I2C2 x ADC for voltage and current sensor1 x additional ADC for analog RSSI or analog airspeedSDIO microSD card slotmicro USB connectorincludes buzzer / safety-switch, power module, I2C expansion board and TS100 GPS / mag combo depending on kit featuressize 39 x 39 x 12 mmweight 12 g without wires
- 6x PWM outputs
- 1x RC input (PWM/PPM, SBUS)
- 3 UARTS (flow-control on Telem 1 & 2, no flow-control on GPS port)
- external I2C
- 2 x ADC for voltage and current sensor
- 1 x additional ADC for analog RSSI or analog airspeed
- SDIO microSD card slot
- micro USB connector
- includes buzzer / safety-switch, power module, I2C expansion board and TS100 GPS / mag combo depending on kit features
- size 39 x 39 x 12 mm
- weight 12 g without wires


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART3
- SERIAL2 = Telemetry2 = USART2 (see Notes for reversed plastic case labels!)
- SERIAL3 = GPS1 = UART4
Serial protocols can be adjusted to personal preferences.



---

## RadioLinkPIX6
**Source URL:** https://ardupilot.org/plane/docs/common-radiolinkpix6.html

### Description
Featuring STM32F7 cpu, vibration isolation of IMUs, redundant IMUs, integrated OSD chip, IMU heating, and DShot.

### Specifications
**SpecificationsÂ**
- Processor
- Sensors
- Power
- Interfaces
- Physical


### Ports, UARTs & Pin Mapping
**TELEM1, TELEM2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX(OUT) | +3.3V
3 | RX(IN) | +3.3V
4 | CTS | +3.3V
5 | RTS | +3.3V
6 | GND | GND

**I2C portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | SCL | +3.3V (pullups)
3 | SDA | +3.3V (pullups)
4 | GND | GND

**CAN1, CAN2 portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**GPS1 portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX(OUT) | +3.3V
3 | RX(IN) | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**GPS2 PortÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX(OUT) | +3.3V
3 | RX(IN) | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**USB remote portÂ**
Pin | Signal | Volt
1 | USB VDD | +5V
2 | DM | +3.3V
3 | DP | +3.3V
4 | GND | GND

**Buzzer portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | BUZZER- | +5V

**Spektrum/DSM PortÂ**
Pin | Signal | Volt
1 | VCC | +3.3V
2 | GND | GND
3 | Signal | +3.3V

**Debug portÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | FMU_SWCLK | +3.3V
3 | FMU_SWDIO | +3.3V
4 | TX(UART7) | +3.3V
5 | RX(UART7) | +3.3V
6 | IO_SWCLK | +3.3V
7 | IO_SWDIO | +3.3V
8 | GND | GND

**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> USART2 (Telem1) RTS/CTS pins, RX DMA capable
- SERIAL2 -> USART3 (Telem2) RTS/CTS pins, TX/RX DMA capable
- SERIAL3 -> USART1 (GPS1), TX/RX DMA capable
- SERIAL4 -> UART4 (GPS2), No DMA
- SERIAL5 -> UART7 (User), No DMA

**OSD SupportÂ**
The RadiolinkPIX6 support using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort is supported using UART3 or any other free UART. SeeMSP OSDfor more info.

**Power1 port(Analog)Â**
The parameters should be set:
- BATT_MONITOR= 4, then reboot.
- BATT_VOLT_PIN= 2
- BATT_CURR_PIN= 5
- BATT_VOLT_MULT= 18
- BATT_AMP_PERVLT= 24

**Power2 port(I2C)Â**
The parameters should be set.:
- BATT2_MONITOR= 21
- BATT2_I2C_BUS= 1
- BATT2_I2C_ADDR= 65



---

## ResoluteH7
**Source URL:** https://ardupilot.org/plane/docs/common-resoluteh7.html

### Description
The Resolute H7 is a flight controller produced byStandard Systems.

### Specifications
**FeaturesÂ**
- MCU - STM32H743 32-bit processor running at 480 MHz
- IMU - ICM42688
- Barometer - DPS368
- OSD - AT7456E
- 7x UARTs
- 1x CAN port
- 12x PWM Outputs (10 Motor Output, 1 LED, 1 Smart Audio)
- Battery input voltage: 4S-6S
- BEC 3.3V 0.5A
- BEC 5V 3A
- Controllable 12V VTX BEC, 3A
- Dual switchable camera inputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rxn and Txn in the above pinouts. The Rxn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (DisplayPort) DMA capable
- SERIAL2 -> USART2 (RCin) DMA capable
- SERIAL3 -> UART3 (USER) DMA capable
- SERIAL4 -> UART4 (USER) DMA capable
- SERIAL6 -> USART6 (GPS)
- SERIAL7 -> UART7 (SmartAudio)
- SERIAL8 -> UART8 (ESC Telemetry)

**OSD SupportÂ**
The Resolute H7 has an onboard OSD using a MAX7456 chip and is enabled by default. The CAM1/2 and VTX pins provide connections for using the internal OSD. Simultaneous DisplayPort OSD is also possible and is configured by default.



---

## QioTek Zealot F427
**Source URL:** https://ardupilot.org/plane/docs/common-qiotek-zealot.html

### Description
The QioTek Zealot F427 is an internally vibration dampened autopilot with a protective CNC metal case for ruggedness. It features fully redundant sensors, expanded number of outputs, temperature controlled IMUs, and is the first high performance autopilot with integrated OSD chip.

### Specifications
**SpecificationsÂ**
- Processor:MCU - STM32F427VIT616KB FRAM - FM25V01AT7456E OSD
- MCU - STM32F427VIT6
- 16KB FRAM - FM25V01
- AT7456E OSD
- SensorsGyro/Accelerometers: ICM20689, ICM20602, and BMI088Barometers: MS5611 and DPS3018Compass: IST8310 or QMC5883L
- Gyro/Accelerometers: ICM20689, ICM20602, and BMI088
- Barometers: MS5611 and DPS3018
- Compass: IST8310 or QMC5883L
- Power5-5.5VDC from USB (internal circuitry and RX only) or via 2 x PowerModule connectors, or via internal BEC off VBAT input pin. All 5V pins are powered when USB, or Power Module(s), or VBAT input is used.Internal 5V, 1.5A BEC directly can be used with up to 6S LIPO batteries to supply board and peripheral power up to 1.5A max with voltage only monitoring via BATT2 monitor (500ma max recommended).ADC monitoring of board voltage??ADC monitoring of Servo/Outputâs power rail
- 5-5.5VDC from USB (internal circuitry and RX only) or via 2 x PowerModule connectors, or via internal BEC off VBAT input pin. All 5V pins are powered when USB, or Power Module(s), or VBAT input is used.
- Internal 5V, 1.5A BEC directly can be used with up to 6S LIPO batteries to supply board and peripheral power up to 1.5A max with voltage only monitoring via BATT2 monitor (500ma max recommended).
- ADC monitoring of board voltage??
- ADC monitoring of Servo/Outputâs power rail
- Interfaces/Connectivity14 PWM Outputs with independent power rail for external power source4 Relay outputsMicroSD card readerMicro USB or remote USB via a JST_GH connectorBuiltin RGB LEDCamera Input and Video OutputExternal Buzzer interface2, 6.6V tolerant ADC inputs for RSSI, Analog Airspeed, etc.5 UARTsSafety Switch connector
- 14 PWM Outputs with independent power rail for external power source
- 4 Relay outputs
- MicroSD card reader
- Micro USB or remote USB via a JST_GH connector
- Builtin RGB LED
- Camera Input and Video Output
- External Buzzer interface
- 2, 6.6V tolerant ADC inputs for RSSI, Analog Airspeed, etc.
- 5 UARTs
- Safety Switch connector
- DimensionsWeight 65gSize 42mm x 65mm x 25mm
- Weight 65g
- Size 42mm x 65mm x 25mm


### Ports, UARTs & Pin Mapping
**Connector pin assignmentsÂ**
Unless noted otherwise all connectors are JST GH

**UART2(TELEM1), UART1(TELEM2) portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**USB remote portÂ**
PIN | SIGNAL | VOLT
1 | USB VDD | +5V
2 | DM | +3.3V
3 | DP | +3.3V
4 | GND | GND

**I2C1 portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL1 | +3.3V
3 | SDA1 | +3.3V
4 | GND | GND

**CAN portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**USART5/ADC1/SBus Out portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX5 | +3.3V
3 | RX5 | +3.3V
4 | SBUS Out | +3.3V
5 | ADC1 | +6V
6 | GND | GND

**Safety/Buzzer portÂ**
PIN | SIGNAL | VOLT
1 | VCC3.3 | +3.3V
2 | VCC5.5 | +5V
3 | SafKey | +3.3V
4 | SafLED | +3.3V
5 | BUZZER- | +5V
6 | GND | GND

**Relay/ADC2 portÂ**
PIN | SIGNAL | VOLT
1 | ADC2 | +6V
2 | Relay1 | +5V
3 | Relay2 | +5V
4 | Relay3 | +5V
5 | Relay4 | +5V
6 | GND | GND

**USART3(GPS1/I2C1), UART4(GPS2/I2C2) portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Power1, Power2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND

**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1
- SERIAL2 = Telemetry2 = USART2
- SERIAL3 = GPS1 = USART3
- SERIAL4 = GPS2 = UART4
- SERIAL5 = USER = UART5



---

## QioTek Zealot H743
**Source URL:** https://ardupilot.org/plane/docs/common-qiotek-zealoth7.html

### Description
The QioTek Zealot H743 is an internally vibration dampened autopilot with a protective CNC metal case for ruggedness. It features fully redundant sensors, expanded number of outputs, temperature controlled IMUs, and is the first high performance autopilot with integrated OSD chip.

### Specifications
**SpecificationsÂ**
- Processor:MCU - STM32H743VIT616KB FRAM - FM25V01AT7456E OSD
- MCU - STM32H743VIT6
- 16KB FRAM - FM25V01
- AT7456E OSD
- SensorsGyro/Accelerometers:
- Standard: ICM42688P, ICM20689, ICM40605
- Industrial: IIM42652, ICM42688P, ICM20689
- Insdustry Application Version: ADIS16170, IIM42652, ICM42688PBarometers: 2x DSP310Compass: QMC5883L
- Gyro/Accelerometers:
- Standard: ICM42688P, ICM20689, ICM40605
- Industrial: IIM42652, ICM42688P, ICM20689
- Insdustry Application Version: ADIS16170, IIM42652, ICM42688P
- Barometers: 2x DSP310
- Compass: QMC5883L
- Power4.1-6.0VDC from USB (internal circuitry and RX only) or via 2 x PowerModule connectors, or via internal BEC off VBAT input pin. All 5V pins are powered when USB, or Power Module(s), or VBAT input is used.Internal 5V, 1.5A BEC directly can be used with up to 6S LIPO batteries to supply board and peripheral power up to 1.5A max with voltage only monitoring via BATT2 monitor (500ma max recommended).ADC monitoring of board voltageADC monitoring of Servo/Outputâs power rail
- 4.1-6.0VDC from USB (internal circuitry and RX only) or via 2 x PowerModule connectors, or via internal BEC off VBAT input pin. All 5V pins are powered when USB, or Power Module(s), or VBAT input is used.
- Internal 5V, 1.5A BEC directly can be used with up to 6S LIPO batteries to supply board and peripheral power up to 1.5A max with voltage only monitoring via BATT2 monitor (500ma max recommended).
- ADC monitoring of board voltage
- ADC monitoring of Servo/Outputâs power rail
- Interfaces/Connectivity14 PWM Outputs with independent power rail for external power source4 Relay outputsMicroSD card readerMicro USB or remote USB via a JST_GH connectorBuiltin RGB LEDCamera Input and Video OutputExternal Buzzer interface2, 6.6V tolerant ADC inputs for RSSI, Analog Airspeed, etc.5 UARTs2, DroneCAN/CAN interfacesSafety Switch connector
- 14 PWM Outputs with independent power rail for external power source
- 4 Relay outputs
- MicroSD card reader
- Micro USB or remote USB via a JST_GH connector
- Builtin RGB LED
- Camera Input and Video Output
- External Buzzer interface
- 2, 6.6V tolerant ADC inputs for RSSI, Analog Airspeed, etc.
- 5 UARTs
- 2, DroneCAN/CAN interfaces
- Safety Switch connector
- DimensionsWeight 65gSize 42mm x 65mm x 25mm
- Weight 65g
- Size 42mm x 65mm x 25mm


### Ports, UARTs & Pin Mapping
**Connector pin assignmentsÂ**
Unless noted otherwise all connectors are JST GH

**UART1(TELEM1), UART2(TELEM2) portsÂ**
Pin | Signal | Volt
1 | VCC | +5V
2 | TX (OUT) | +3.3V
3 | RX (IN) | +3.3V
4 | GND | GND

**USB remote portÂ**
PIN | SIGNAL | VOLT
1 | USB VDD | +5V
2 | DM | +3.3V
3 | DP | +3.3V
4 | GND | GND

**I2C1 portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | SCL1 | +3.3V
3 | SDA1 | +3.3V
4 | GND | GND

**DroneCAN/CAN portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | CAN_H | +12V
3 | CAN_L | +12V
4 | GND | GND

**USART5/ADC1/SBus Out portÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX5 | +3.3V
3 | RX5 | +3.3V
4 | SBUS Out | +3.3V
5 | ADC1 | +6V
6 | GND | GND

**Safety/Buzzer portÂ**
PIN | SIGNAL | VOLT
1 | VCC3.3 | +3.3V
2 | VCC5.5 | +5V
3 | SafKey | +3.3V
4 | SafLED | +3.3V
5 | BUZZER- | +5V
6 | GND | GND

**Relay/ADC2 portÂ**
PIN | SIGNAL | VOLT
1 | ADC2 | +6V
2 | Relay1 | +5V
3 | Relay2 | +5V
4 | Relay3 | +5V
5 | Relay4 | +5V
6 | GND | GND

**USART3(GPS1/I2C1), UART4(GPS2/I2C2) portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | TX | +3.3V
3 | RX | +3.3V
4 | SCL | +3.3V
5 | SDA | +3.3V
6 | GND | GND

**Power1, Power2 portsÂ**
PIN | SIGNAL | VOLT
1 | VCC | +5V
2 | VCC | +5V
3 | CURRENT | +3.3V
4 | VOLTAGE | +3.3V
5 | GND | GND
6 | GND | GND

**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1
- SERIAL2 = Telemetry2 = USART2
- SERIAL3 = GPS1 = USART3
- SERIAL4 = GPS2 = UART4
- SERIAL5 = USER = UART5



---

## SDMODEL H7 V2
**Source URL:** https://ardupilot.org/plane/docs/common-SDMODELH7V2.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processorAT7456E OSD
- STM32H743 32-bit processor
- AT7456E OSD
- SensorsInvenSense MPU6000 IMU (accel and gyro only, no compass)IST8310 CompassBMP280 barometer
- InvenSense MPU6000 IMU (accel and gyro only, no compass)
- IST8310 Compass
- BMP280 barometer
- Power2S  - 6S Lipo input voltage with voltage monitoring9V, 1.5A BEC for powering Video Transmitter
- 2S  - 6S Lipo input voltage with voltage monitoring
- 9V, 1.5A BEC for powering Video Transmitter
- Interfaces9x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad)1x RC input6x UARTs/serial for GPS and other peripherals1x I2C port for external compassMicro-C USB portAll UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâMicroSD Card Slot for loggingExternal current monitor input
- 9x PWM outputs (9th pwm output is for NeoPixel LED string via the LED pad)
- 1x RC input
- 6x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- Micro-C USB port
- All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- MicroSD Card Slot for logging
- External current monitor input


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
The SERIAL7 port (UART7) is normally for ESC telemetry, and has an R7 pin on
both of the ESC connectors.

**OSD SupportÂ**
The SDMODELH7V2  supports OSD usingOSD_TYPE1 (MAX7456 driver). Simultaneous DisplayPort OSD option is also available and SERIAL1 defaults to DisplayPort protocol.

**Camera Control PinÂ**
The Cam pin is GPIO 84 and is set to be controlled by RELAY4 by default. Relay pins can be controlled either by an RC switch or GCS command. SeeRelay Switchfor more information.



---

## SequreH743
**Source URL:** https://ardupilot.org/plane/docs/common-sequreh743.html

### Description
The SequreH743 and SequreH743v2 are flight controllers designed and produced bySequre.

### Specifications
**FeaturesÂ**
- MCU - STM32H743xx 32-bit processor running at 480 MHz
- IMU - MPU6000, ICM42688 (V2 version)
- Barometer - BMP280 (DPS368 and DPS310 on V2)
- OSD - AT7456E
- 6x UARTs
- 9x PWM Outputs (8 Motor Output, 1 LED)


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB (MAVLink2)
- SERIAL1 -> USART1 (RCIN, DMA-enabled)
- SERIAL2 -> USART2 (SmartAudio)
- SERIAL4 -> UART4 (None)
- SERIAL6 -> USART6 (GPS, DMA-enabled)
- SERIAL7 -> UART7 (DisplayPort, DMA-enabled)
- SERIAL8 -> UART8 (ESCTelemetry)

**OSD SupportÂ**
The SequreH743 supports OSD using its MAX7456by default, and simultaneously DisplayPort using UART7 on the HD VTX connector ifOSD_TYPE2is set to â5â.

**VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 9v so be careful not to connect this to a peripheral that can not tolerate this voltage.



---

## Sky-Drones AIRLink
**Source URL:** https://ardupilot.org/plane/docs/common-skydrones-airlink.html

### Description
AIRLinkstands for Artificial Intelligence & Remote Link. The unit includes a cutting-edge drone autopilot, AI mission computer and LTE connectivity unit. AIRLink helps to reduce the time to market for new drone manufacturers from years and months down to weeks.

### Specifications
**System FeaturesÂ**
SmartAP AIRLink has two computers and integrated LTE Module:
Feature highlights

**SpecificationsÂ**
- Sensors3x Accelerometers, 3x Gyroscopes, 3x Magnetometers, 3x Pressure sensorssGNSS, Rangefinders, Lidars, Optical Flow, Cameras3x-redundant IMUVibration dampeningTemperature stabilization
- 3x Accelerometers, 3x Gyroscopes, 3x Magnetometers, 3x Pressure sensorss
- GNSS, Rangefinders, Lidars, Optical Flow, Cameras
- 3x-redundant IMU
- Vibration dampening
- Temperature stabilization
- Flight ControllerSTM32F7, ARM Cortex M7 with FPU, 216 MHz, 2MB Flash, 512 kB RAMSTM32F1, I/O co-processorEthernet, 10/100 MbpsLAN with AI Mission Computer8x UARTs: Telemetry 1, Telemetry 2 (AI Mission Computer), Telemetry 3, GPS 1, GPS 2, Extra UART, Serial Debug Console, IO2x CAN: CAN1, CAN2USB with MAVLinkSerial console for debuggingRC Input, SBUS input, RSSI input, PPM input16x PWM servo outputs (8 from IO, 8 from FMU)3x I2C portsHigh-powered piezo buzzer driverHigh-power RGB LEDSafety switch / LED option
- STM32F7, ARM Cortex M7 with FPU, 216 MHz, 2MB Flash, 512 kB RAM
- STM32F1, I/O co-processor
- Ethernet, 10/100 Mbps
- LAN with AI Mission Computer
- 8x UARTs: Telemetry 1, Telemetry 2 (AI Mission Computer), Telemetry 3, GPS 1, GPS 2, Extra UART, Serial Debug Console, IO
- 2x CAN: CAN1, CAN2
- USB with MAVLink
- Serial console for debugging
- RC Input, SBUS input, RSSI input, PPM input
- 16x PWM servo outputs (8 from IO, 8 from FMU)
- 3x I2C ports
- High-powered piezo buzzer driver
- High-power RGB LED
- Safety switch / LED option
- AI Mission Computer6-Core CPU: Dual-Core Cortex-A72 + Quad-Core Cortex-A53GPU Mali-T864, OpenGL ES1.1/2.0/3.0/3.1VPU with 4K VP8/9, 4K 10bits H265/H264 60fps DecodingRemote power control, software reset, power down, RTC Wake-Up, sleep modeRAM Dual-Channel 4GB LPDDR416GB eMMCMicroSD up to 256GBEthernet 10/100/1000 Native GigabitWiFi 802.11a/b/g/n/ac, BluetoothUSB 3.0 Type C2x Video: 4-Lane MIPI CSI (FPV Camera) and 4-Lane MIPI CSI with HDMI Input (Payload Camera)
- 6-Core CPU: Dual-Core Cortex-A72 + Quad-Core Cortex-A53
- GPU Mali-T864, OpenGL ES1.1/2.0/3.0/3.1
- VPU with 4K VP8/9, 4K 10bits H265/H264 60fps Decoding
- Remote power control, software reset, power down, RTC Wake-Up, sleep mode
- RAM Dual-Channel 4GB LPDDR4
- 16GB eMMC
- MicroSD up to 256GB
- Ethernet 10/100/1000 Native Gigabit
- WiFi 802.11a/b/g/n/ac, Bluetooth
- USB 3.0 Type C
- 2x Video: 4-Lane MIPI CSI (FPV Camera) and 4-Lane MIPI CSI with HDMI Input (Payload Camera)
- LTE Connectivity Module4G LTE UMTS/HSPA(+), GSM/GPRS/EDGE1x External slot, 1x Integrated eSIMLTE Antenna, 2x2 MIMOBands: Europe, North America, Australia, Japan, Other
- 4G LTE UMTS/HSPA(+), GSM/GPRS/EDGE
- 1x External slot, 1x Integrated eSIM
- LTE Antenna, 2x2 MIMO
- Bands: Europe, North America, Australia, Japan, Other

**FeaturesÂ**
- Easy to mount
- FPV camera comes as standard


### Ports, UARTs & Pin Mapping
**UART OrderÂ**
AIRLink has a large number of internal and external serial ports:
Serial | UART | Function
Serial 0 | USB | Console
Serial 1 | UART 7 | Telemetry 1
Serial 2 | UART 5 | Telemetry 2 (used internally with Mission Computer)
Serial 3 | USART 1 | GPS 1
Serial 4 | UART 8 | GPS 2
Serial 5 | USART 3 | Debug console (internal connector)
Serial 6 | USART 2 | Telemetry 3
Serial 7 | UART 4 | External UART



---

## SkySakuraH743
**Source URL:** https://ardupilot.org/plane/docs/common-SkySakuraH743.html

### Description
The SkySakura H743 is a flight controller produced by [SkySakuraRC]

### Specifications
**FeaturesÂ**
- MCU: STM32H743VIT6, 480MHz
- Gyro1: ICM42688
- Gyro2: IIM42652
- SD Card support
- BEC output: 5V 5A & 12V 5A (MAX 60W total) (switchable 12V)
- Barometer1: DPS310
- Barometer2: ICP20100
- Magnometer: IST8310
- CAN bus support
- 7 UARTS: (USART1, USART2, USART3, UART4, USART6, UART7 with flow control, UART8)
- 2 I2C, I2C1 is used internally.
- 13 PWM outputs (12 motor outputs, 1 led)
- 4-12s wide voltage support


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB (MAVLink2)
- SERIAL1 -> UART7 (MAVLink2, flow-control-capable)|
- SERIAL2 -> UART1 (MAVLink2, DMA-enabled)|
- SERIAL3 -> UART2 (USER)|
- SERIAL4 -> UART3 (GPS1, DMA-enabled)|
- SERIAL5 -> UART4 (RCIN, DMA-enabled)|
- SERIAL6 -> UART6 (DisplayPort, DMA-enabled)|
- SERIAL7 -> UART8 (ESC-Telemetry, RX8 on ESC connectors, TX8 can be used if protocol is change from ESC telem)|
- SERIAL8 -> USB (SLCAN)

**OSD SupportÂ**
SkySakura H743 supports HD VTX DisplayPort OSD through UART6 by default. SetOSD_TYPE= 5.



---

## SkystarsH7HD
**Source URL:** https://ardupilot.org/plane/docs/common-skystarsH7.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processorAT7456E OSD16 MByte flash for logging
- STM32H743 32-bit processor
- AT7456E OSD
- 16 MByte flash for logging
- SensorsBMI270 IMU (accel and gyro only, no compass)BMP280 barometer
- BMI270 IMU (accel and gyro only, no compass)
- BMP280 barometer
- Power3S  - 6S Lipo input voltage with voltage monitoring10V, 3A BEC for powering Video Transmitter with power switch
- 3S  - 6S Lipo input voltage with voltage monitoring
- 10V, 3A BEC for powering Video Transmitter with power switch
- Interfaces8x PWM outputs, BiDir DShot capable8x UARTs/serial for GPS and other peripherals1x I2C port for external compass or airspeedUSB-C portSwitchable VTX powerAll UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâExternal current monitor input
- 8x PWM outputs, BiDir DShot capable
- 8x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass or airspeed
- USB-C port
- Switchable VTX power
- All UARTS support hardware inversion. SBUS, SmartPort, and other inverted protocols work on any UART without âuninvert hackâ
- External current monitor input


### Ports, UARTs & Pin Mapping
**PinoutÂ**
Pin | Function
10V | Selectable 5V/10V for HD System or other VTX, by default ON/OFF is
controlled by RELAY2. SeeRelay SwitchCan be controlled by RELAY2
SDA, SCL | I2C connection (for peripherals)
5 | 5v output (1.5A max)
3v3 | 3.3v output (0.25A max)
C1 | Video input from FPV camera1
C2 | Video input from FPV camera2
VTX | Video output to video transmitter
CAM | To camera OSD control
OSD | GPIO output
G or GND | Ground
RSI | Analog RSSI (0-3.3v) input from receiver
R1, T1 | UART1 RX and TX, normally RC input
R2, T2 | UART2 RX and TX
R3, T3 | UART3 RX and TX, RX3 normally ESC telem input
R4, T4 | UART4 RX and TX, normally GPS
R5, T5 | UART5 RX and TX
R6, T6 | UART6 RX and TX (UART6 RX is also located in the
DJI GH plug)
R7, T7 | UART7 RX and TX
R8, T8 | UART8 RX and TX
L | WS2182 addressable LED signal wire
RSSI | Analog RSSI input (ArduPilot pin 13)
BB- | Piezo buzzer negative leg
BB+ | Piezo buzzer positive leg

**ESC Port 1Â**
Pin | Function
GND | Ground
BAT | Battery positive voltage (3S-6S)
M1 | Motor signal output 1
M2 | Motor signal output 2
M3 | Motor signal output 3
M4 | Motor signal output 4
R3 | UART3 RX
CURT | Current sesonr input

**DJI PortÂ**
Pin | Function
10V | Selectable 5V/10V for HD System or other VTX, by default ON/OFF is
controlled by RELAY2. SeeRelay SwitchCan be controlled by RELAY2
GND | Ground
TX6 | UART6 TX
RX6 | UART6 RX
GND | Ground
RX1 | UART1 RX (used for SBUS or other RC input)

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (default RC protocol, DMA-enabled)
- SERIAL2 -> UART2 (DMA-enabled)
- SERIAL3 -> UART3 (default ESC Telem protocol)
- SERIAL4 -> UART4 (default GPS protocol, DMA-enabled)
- SERIAL5 -> UART5 (User)
- SERIAL6 -> UART6 (default protocol DJI Goggles, DMA-enabled)
- SERIAL7 -> UART7 (DMA-enabled)
- SERIAL8 -> UART8
Any UART may be re-tasked by changing its protocol parameter.

**OSD SupportÂ**
The autopilot has an integrated OSD usingOSD_TYPE1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART6.



---

## SkystarsH7HDV2
**Source URL:** https://ardupilot.org/plane/docs/common-skystarsh7hdv2.html

### Description
The Skystars H7HDV2 is a flight controller produced bySkystars.

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- ICM42688 IMU x2
- BMP280 barometer
- AT7456E OSD
- 8 UARTs
- 9 PWM outputs
- Switchable Dual Camera inputs
- CAN port
- GPIO controlled video power switch


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (RCin, DMA-enabled)
- SERIAL2 -> UART2 (MAVLink2 DMA-enabled)
- SERIAL3 -> UART3 (ESC Telem)
- SERIAL4 -> UART4 (GPS, DMA-enabled)
- SERIAL5 -> UART5 (SmartAudio)
- SERIAL6 -> UART6 (DisplayPort, DMA-enabled)
- SERIAL7 -> UART7 (USER DMA-enabled)
- SERIAL8 -> UART8 (USER)

**OSD SupportÂ**
By default, Skystars H7HDV2 supports OSD using OSD_TYPE 1 (MAX7456 driver) and simultaneously DisplayPort using UART6 on the HD VTX connector.



---

## SPRacing H7 Extreme
**Source URL:** https://ardupilot.org/plane/docs/common-spracingh7-extreme.html

### Description
The SPRacingH7 Extreme is an autopilot produced bySeriously Pro Racing.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F750  ARM 32-bit processor running at 400 MHzOSD: AT7456E128MB Serial NOR flash via QuadSPI for program storage
- STM32F750  ARM 32-bit processor running at 400 MHz
- OSD: AT7456E
- 128MB Serial NOR flash via QuadSPI for program storage
- Sensors2x ICM20602BMP388 barometerVoltage sensor (2-6S)Current Sensor (110A Continuous/ 130A Maximum)
- 2x ICM20602
- BMP388 barometer
- Voltage sensor (2-6S)
- Current Sensor (110A Continuous/ 130A Maximum)
- Peripheral Connections7 UARTsMicro SD CardMicro USBI2CAnalog RSSI inputCamera and VTXActive Buzzer
- 7 UARTs
- Micro SD Card
- Micro USB
- I2C
- Analog RSSI input
- Camera and VTX
- Active Buzzer
- Power2-6S DC input power5V, 1A BEC for peripherals
- 2-6S DC input power
- 5V, 1A BEC for peripherals


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1 (has DMA) normally RC input
- SERIAL2 = Telemetry2 = USART2 (has DMA) (only TX pin available)
- SERIAL3 = GPS1 = USART3 (has DMA)
- SERIAL4 = GPS2 = UART4 (has DMA)
- SERIAL5 = USER = UART5 (has DMA)
- SERIAL6 = USER = USART6 (available instead of PWM outputs 7(TX6) and 8(RX6) ifBRD_ALT_CONFIG= 1)
- SERIAL8 = USER = UART8
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences.

**OSD SupportÂ**
The SPracing H7 Extreme onboard OSD is used by settingOSD_TYPE1 (MAX7456 driver).

**SmartPort TelemetryÂ**
SmartPort (Sport) telemetry setup by default to be connected directly to UART2 TX pin with no external inverters required.



---

## SPRacing H7 RF
**Source URL:** https://ardupilot.org/plane/docs/common-spracingh7-rf.html

### Description
The SPRacingH7 RF is an autopilot produced bySeriously Pro Racing.

### Specifications
**SpecificationsÂ**
- Processor
- Sensors
- Peripheral Connections
- Power2-8S DC input power5V, 1A BEC for peripherals
- 2-8S DC input power
- 5V, 1A BEC for peripherals


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
All UARTS are DMA capable
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences.

**OSD SupportÂ**
Ardupilot does not currently support the integrated OSD chip. UART3 is setup for use with DisplayPort goggles with OSD.



---

## Swan-K1
**Source URL:** https://ardupilot.org/plane/docs/common-Swan-K1.html

### Description
This autopilot is a part of aready-to-fly vehiclein  the form of a control-surfaceless, quad-copter Tailsitter QuadPlane. It comes with customized PX4 firmware installed and an GCS application that is downloadable for smart phones. This page describes the conversion to ArduPilot firmware and its setup.
It was initially offered with a 10 channel RC transmitter using an external smart phone for GCS and video display, and the Pro version comes with a 12 channel system with an integrated screen for the GCS/Video.

### Ports, UARTs & Pin Mapping
**Transmitter RC Channel MappingÂ**
Control | T10 | H12 | Default Setup
Sticks | 1-4 | 1-4 | Mode2 AETR
Button A | 7 | 7 | 
Button B | 8 | 8 | QRTL
Button/Knob C* | 9 | 9 | 
Button/Knob D* | 10 | 10 | 
Knob G |  | 11 | 
Knob H |  | 12 | 
Switch E | 5 | 5 | Flight Mode Switch
Switch F | 6 | 6 | 
- T10 this is a knob, H12 it is a locking button



---

## Spedix F405
**Source URL:** https://ardupilot.org/plane/docs/common-spedixf405.html

### Description
The SPEDIX F405 is a flight controller based on the STM32F405 MCU.

### Specifications
**FeaturesÂ**
- MCU - STM32F405 32-bit processor running at 168 MHz
- IMU - ICM42688
- Barometer - SPL06
- OSD - AT7456E
- Onboard Flash: 4MByte
- 6x UARTs
- 9x PWM Outputs (8 Motor Output, 1 LED)
- Battery input voltage: 2S-6S
- Dual Camera inputs
- BEC 3.3V 0.5A
- BEC 5V 3A
- BEC 9V 3A for video


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MSP DisplayPort, DMA-enabled)
- SERIAL2 -> UART2 (SBUS/Spare)
- SERIAL3 -> UART3 (RCin, DMA-enabled)
- SERIAL4 -> UART4 (GPS)
- SERIAL5 -> UART5 (ESC Telemetry)
- SERIAL6 -> UART6 (Spare)

**OSD SupportÂ**
Onboard OSD using OSD_TYPE 1 (MAX7456 driver) is supported by default. Simultaneously, DisplayPort OSD is available on the HD VTX connector by default.



---

## Spedix H743
**Source URL:** https://ardupilot.org/plane/docs/common-spedixh743.html

### Description
The SPEDIX H743 is a flight controller based on the STM32H743 MCU.

### Specifications
**FeaturesÂ**
- MCU - STM32H743 32-bit processor running at 480 MHz
- IMU - Dual ICM42688
- Barometer - SPL06
- OSD - MAX7456
- 8x UARTs
- CAN support
- 9x PWM Outputs (8 Motor Output, 1 LED)
- Battery input voltage: 2S-6S
- BEC 3.3V 0.5A
- BEC 5V 3A
- BEC 12V 3A for video, gpio controlled
- Dual camera inputs with switching support


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB
- SERIAL1 -> UART1 (Telem 1, DMA-enabled)
- SERIAL2 -> UART2 (RC Input, DMA-enabled)
- SERIAL3 -> UART3 (Telem 2, DMA-enabled)
- SERIAL4 -> UART4 (MSP DisplayPort, DMA-enabled)
- SERIAL5 -> UART5 (ESC Telemetry)
- SERIAL6 -> UART6 (GPS, DMA-enabled)
- SERIAL7 -> UART7 (Spare)
- SERIAL8 -> UART8 (OTG2)

**OSD SupportÂ**
Onboard OSD using OSD_TYPE 1 (MAX7456 driver) is supported by default. Simultaneously, DisplayPort OSD is available on the HD VTX connector.



---

## SpeedyBee F4 (this board currently is non-verified)
**Source URL:** https://ardupilot.org/plane/docs/common-speedybeef4.html

### Description
above image and some content courtesy of thespeedybee.com

### Specifications
**SpecificationsÂ**
- Processor and SensorsSTM32F405 ARM microcontrollerInvenSense MPU6000 IMU (accel, gyro, compass)
- STM32F405 ARM microcontroller
- InvenSense MPU6000 IMU (accel, gyro, compass)
- Interfaces4x PWM outputs1x RC input (PWM/PPM, SBUS)4x serial port inputs (including RC input listed above)1x I2C for external compassbattery voltage and current monitorOnboard BluetoothUSB port3S to 6S input power
- 4x PWM outputs
- 1x RC input (PWM/PPM, SBUS)
- 4x serial port inputs (including RC input listed above)
- 1x I2C for external compass
- battery voltage and current monitor
- Onboard Bluetooth
- USB port
- 3S to 6S input power



---

## SpeedyBee F405 AIO
**Source URL:** https://ardupilot.org/plane/docs/common-speedybeef405aio.html

### Description
The SpeedyBee F405 AIO is a flight controller produced bySpeedyBee.

### Specifications
**FeaturesÂ**
- MCU: STM32F405 32-bit processor. 1024Kbytes Flash
- IMU: ICM-42688P (SPI)
- Barometer: SPA06-003
- USB VCP Driver (all UARTs usable simultaneously; USB does not take up a UART)
- 6 UARTS (UART1 tied internally to BT module which is not currently supported by ArduPilot)
- 8MBytes for logging
- 5V Power Out: 2.0A max
- Dimensions: 33x33mm
- Mounting Holes: Standard 25.5/25.5mm square to center of holes
- Weight: 13.6g
- Built-in 40A BlueJay 4in1 ESC (Bluejay JH-40 48kHz)
- Input Voltage: 3S-6S Lipo
- Continuous Current: 40A


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Name | UART | Default Protocol
SERIAL0 | USB | MAVLink2
SERIAL1 | USART1 | (WiFi module, not usable by ArduPilot)
SERIAL2 | USART2 | (USER, RX pin only, tied to inverted SBUS pin
SERIAL3 | USART3 | (DisplayPort)
SERIAL4 | UART4 | (User)
SERIAL5 | UART5 | (GPS)
SERIAL6 | UART6 | (RCin, DMA-enabled)

**OSD SupportÂ**
The SpeedyBee F405 AIO supports OSD usingOSD_TYPE=  1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART3. Both the internal analog OSD and the DisplayPort OSD can be used simultaneously by settingOSD_TYPE2= 5



---

## SpeedyBee F4 V3/V4
**Source URL:** https://ardupilot.org/plane/docs/common-speedybeef4-v3.html

### Description
above image and some content courtesy of thespeedybee.com

### Specifications
**SpecificationsÂ**
- Processor and SensorsSTM32F405 ARM microcontrollerV3:BMI270 IMU, V4:ICM42688 (Gyro and Accelerometers)V3:SPL06, V4:DPS310 BarometerAT7456E OSD
- STM32F405 ARM microcontroller
- V3:BMI270 IMU, V4:ICM42688 (Gyro and Accelerometers)
- V3:SPL06, V4:DPS310 Barometer
- AT7456E OSD
- Interfaces9x PWM outputs (PWM9 for Neopixel LED)1x RC input (PWM/PPM, SBUS)6x serial port inputs (including RC input listed above)1x I2C for external compass or airspeed sensorMicro SD card slot4 in 1 ESC connectorDJI Air Unit connectorUSB-C connector
- 9x PWM outputs (PWM9 for Neopixel LED)
- 1x RC input (PWM/PPM, SBUS)
- 6x serial port inputs (including RC input listed above)
- 1x I2C for external compass or airspeed sensor
- Micro SD card slot
- 4 in 1 ESC connector
- DJI Air Unit connector
- USB-C connector
- Power9V ~ 25V DC input power (3S-6S)5V 2A BEC for peripheral9V 2A for Video
- 9V ~ 25V DC input power (3S-6S)
- 5V 2A BEC for peripheral
- 9V 2A for Video
- Size and Dimensions41.6mm x3 9.4mm x 7.8mm (30.5mm x 30.5mm mount pattern)9.6g
- 41.6mm x3 9.4mm x 7.8mm (30.5mm x 30.5mm mount pattern)
- 9.6g


### Ports, UARTs & Pin Mapping
**UART DefaultsÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn. N
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DJI-VTX, DMA-enabled)
- SERIAL2 -> UART2 (RCIN, DMA-enabled) Note that the SBUS input must be used for SBUS.
- SERIAL3 -> UART3 (User defined)
- SERIAL4 -> UART4 (connected to internal BT module, not currently usable by ArduPilot)
- SERIAL5 -> UART5 (ESC Telemetry)
- SERIAL6 -> UART6 (GPS, DMA-enabled)

**OSD SupportÂ**
The SpeedyBee F405 v3 has an on-board OSD usingOSD_TYPE=  1 (MAX7456 driver). The CAM and VTX pins provide connections for using the internal OSD.



---

## SpeedyBee F405 Mini
**Source URL:** https://ardupilot.org/plane/docs/common-speedybeef405-mini.html

### Description
the above image and some content courtesy ofSpeedyBeeand the autopilot is shown with a companion 4in1 ESC as a stack.

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)AT7456E OSD8MByte flash for logging
- STM32F405RGT6 ARM (168MHz)
- AT7456E OSD
- 8MByte flash for logging
- SensorsICM-42688P IMU (accel, gyro)DSP-310 barometerVoltage Sensor, Input for external current sensor
- ICM-42688P IMU (accel, gyro)
- DSP-310 barometer
- Voltage Sensor, Input for external current sensor
- Power4.75-5.25V input9V 3A BEC for powering Video Transmitter5V, 2A BEC for internal and peripherals
- 4.75-5.25V input
- 9V 3A BEC for powering Video Transmitter
- 5V, 2A BEC for internal and peripherals
- Interfaces4x PWM outputs DShot capable (Serial LED output is 5th output)1x RC input5x UARTs/serial for GPS and other peripherals, 6th UART internally tied to Wireless board)I2C port for external compass, airspeed, etc.USB-C port
- 4x PWM outputs DShot capable (Serial LED output is 5th output)
- 1x RC input
- 5x UARTs/serial for GPS and other peripherals, 6th UART internally tied to Wireless board)
- I2C port for external compass, airspeed, etc.
- USB-C port
- Size and Dimensions30mm x 32mm x 7.8mm9.6g
- 30mm x 32mm x 7.8mm
- 9.6g


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DJI-VTX, DMA-enabled)
- SERIAL2 -> UART2 (RX, DMA-enabled)
- SERIAL3 -> UART3
- SERIAL4 -> UART4 (connected to internal BT module, not currently usable by ArduPilot)
- SERIAL5 -> UART5 (ESC Telemetry, RX only on ESC connector)
- SERIAL6 -> UART6 (GPS, DMA-enabled)
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The SpeedyBeeF405-Mini supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort is supported using UART1 or any other free UART. SeeMSP OSDfor more info.



---

## SpeedyBeeF405WING/WING Mini
**Source URL:** https://ardupilot.org/plane/docs/common-speedybeef405wing.html

### Description
The SpeedyBeeF405wing/Wing Mini integrates all the highly desired features for a Plane autopilot:
Plus several unique features:
the above image and some content courtesy ofSpeedyBee

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)AT7456E OSD
- STM32F405RGT6 ARM (168MHz)
- AT7456E OSD
- SensorsICM-42688P IMU (accel, gyro)SPL-06 barometerVoltage & 120A current sensor
- ICM-42688P IMU (accel, gyro)
- SPL-06 barometer
- Voltage & 120A current sensor
- Power2S - 6S Lipo input voltage with voltage monitoring90A Cont., 215A peak current monitor9V/12/5V, 1.8A BEC for powering Video Transmitter controlled by GPIO(early bd revs do not have this feature)4.9V/6V/7.2V, 4.5A BEC for servos5V, 2.4A BEC for internal and peripherals
- 2S - 6S Lipo input voltage with voltage monitoring
- 90A Cont., 215A peak current monitor
- 9V/12/5V, 1.8A BEC for powering Video Transmitter controlled by GPIO(early bd revs do not have this feature)
- 4.9V/6V/7.2V, 4.5A BEC for servos
- 5V, 2.4A BEC for internal and peripherals
- Interfaces12x PWM outputs DShot capable (Serail LED output is PWM12)1x RC input5x UARTs/serial for GPS and other peripherals, 6th UART internally tied to Wireless board)I2C port for external compass, airspeed, etc.microSDCard for logging, etc.USB-C port
- 12x PWM outputs DShot capable (Serail LED output is PWM12)
- 1x RC input
- 5x UARTs/serial for GPS and other peripherals, 6th UART internally tied to Wireless board)
- I2C port for external compass, airspeed, etc.
- microSDCard for logging, etc.
- USB-C port
- Size and DimensionsWing: 52mm x 32mm x 19mm , Mini:37mm x 26mm x 14mmWing: 35g, Muini:19G
- Wing: 52mm x 32mm x 19mm , Mini:37mm x 26mm x 14mm
- Wing: 35g, Muini:19G


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
Serial protocols shown are defaults, but can be adjusted to personal preferences.

**OSD SupportÂ**
The SpeedyBeeF405Wing supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). External OSD support such as DJI or DisplayPort is supported using UART5 or any other free UART. SeeMSP OSDfor more info.



---

## StellarF4
**Source URL:** https://ardupilot.org/plane/docs/common-stellarf4.html

### Description
StellarF4 is an autopilot byStingbee.

### Specifications
**FeaturesÂ**
- ProcessorSTM32F405
- STM32F405
- SensorsICM-42688p/BMI270 Acc/GyroDPS310/BMP280 barometerAT7456E OSDW25Q128 dataflash
- ICM-42688p/BMI270 Acc/Gyro
- DPS310/BMP280 barometer
- AT7456E OSD
- W25Q128 dataflash
- Power2S-6S Lipo input voltage with voltage monitoring12V, 3A BEC for powering Video Transmitter5V, 2A BEC for internal and peripherals
- 2S-6S Lipo input voltage with voltage monitoring
- 12V, 3A BEC for powering Video Transmitter
- 5V, 2A BEC for internal and peripherals
- Interfaces10x PWM outputs DShot capable, PWM1-4 DShot capable6x UARTs1x I2C2x ADCSPI flash for loggingUSB-C port
- 10x PWM outputs DShot capable, PWM1-4 DShot capable
- 6x UARTs
- 1x I2C
- 2x ADC
- SPI flash for logging
- USB-C port
- LEDRed, 3.3V power indicatorGreen, FC status
- Red, 3.3V power indicator
- Green, FC status
- Size41 x 41mm PCB with 30.5mm M3 mounting
- 41 x 41mm PCB with 30.5mm M3 mounting


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the
receive pin for UARTn. The TXn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> USART1 (DJI / VTX, DMA capable)
- SERIAL2 -> USART2 (Serial RC input, DMA capable)
- SERIAL3 -> USART3 (User) (NO DMA)
- SERIAL4 -> UART4 (User) (NO DMA)
- SERIAL5 -> UART5 (ESC Telemetry) (NO DMA)
- SERIAL6 -> USART6 (GPS) (NO DMA)

**OSD SupportÂ**
StellarF4 supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver).
External OSD support such as DJI or DisplayPort can be used simultaneously and is preconfigured on SERIAL3 but can be supported on any spare UART. SeeMSP OSDfor more info.



---

## StellarF4V2
**Source URL:** https://ardupilot.org/plane/docs/common-stellarf4v2.html

### Description
Stellar F4V2 is an autopilot byStingbee.

### Specifications
**FeaturesÂ**
- ProcessorSTM32F405
- STM32F405
- SensorsICM-42688p Acc/Gyro with external clock featureDPS310/BMP280 barometerAT7456E OSDW25Q128 dataflash
- ICM-42688p Acc/Gyro with external clock feature
- DPS310/BMP280 barometer
- AT7456E OSD
- W25Q128 dataflash
- Power2S-8S Lipo input voltage with voltage monitoring12V, 3A BEC for powering Video Transmitter5V, 2A BEC for internal and peripherals
- 2S-8S Lipo input voltage with voltage monitoring
- 12V, 3A BEC for powering Video Transmitter
- 5V, 2A BEC for internal and peripherals
- Interfaces11x PWM outputs DShot capable, PWM1-4 DShot capable4x UARTs1x I2C2x ADCSPI flash for loggingUSB-C port
- 11x PWM outputs DShot capable, PWM1-4 DShot capable
- 4x UARTs
- 1x I2C
- 2x ADC
- SPI flash for logging
- USB-C port
- LEDRed, 3.3V power indicatorGreen, FC status
- Red, 3.3V power indicator
- Green, FC status
- Size41 x 41mm PCB with 30.5mm M3 mounting
- 41 x 41mm PCB with 30.5mm M3 mounting


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RXn and TXn in the above pinouts. The RXn pin is the
receive pin for UARTn. The TXn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART2 (Serial RC input, DMA capable)
- SERIAL2 -> UART3 (User)
- SERIAL3 -> UART4 (DisplayPort)
- SERIAL4 -> UART5 (ESC Telemetry)

**OSD SupportÂ**
StellarF4V2 supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver).
External OSD support such as DJI or DisplayPort can be used simultaneously and is preconfigured on SERIAL3 but can be supported on any spare UART. SeeMSP OSDfor more info.



---

## StellarH7V2
**Source URL:** https://ardupilot.org/plane/docs/common-stellarh7v2.html

### Description
An autopilot sold byStingBee

### Specifications
**FeaturesÂ**
- ProcessorSTM32H743VIH6 480 MHz, 2MB flash
- STM32H743VIH6 480 MHz, 2MB flash
- SensorsICM-42688p Acc/Gyro with external clock featureDPS310/BMP280 barometerAT7456E OSDSD Card
- ICM-42688p Acc/Gyro with external clock feature
- DPS310/BMP280 barometer
- AT7456E OSD
- SD Card
- Power2S-8S Lipo input voltage with voltage monitoring12V, 3A BEC for powering Video Transmitter5V, 2A BEC for internal and peripherals
- 2S-8S Lipo input voltage with voltage monitoring
- 12V, 3A BEC for powering Video Transmitter
- 5V, 2A BEC for internal and peripherals
- Interfaces10x PWM outputs DShot capable, 4 outputs BDShot capable7x UARTs1x CAN1x I2C3x ADCSD card for loggingUSB-C port
- 10x PWM outputs DShot capable, 4 outputs BDShot capable
- 7x UARTs
- 1x CAN
- 1x I2C
- 3x ADC
- SD card for logging
- USB-C port
- LEDRed, 3.3V power indicatorBlue and Green, FC status
- Red, 3.3V power indicator
- Blue and Green, FC status
- Size41 x 41mm PCB with 30.5mm M3 mounting holes
- 41 x 41mm PCB with 30.5mm M3 mounting holes


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked RX and TX in the above pinouts. The RX pin is the
receive pin for the UART. The TX pin is the transmit pin for UART. All UARTS except UART6 and UART8 are DMA capable. Default protocols are shown below and can be changed by the user.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (MAVLink2)
- SERIAL2 -> UART2 (MAVLink2)
- SERIAL3 -> UART3 (User)
- SERIAL4 -> UART4 (Serial RC input)
- SERIAL5 -> UART6 (GPS)
- SERIAL6 -> UART7 (DisplayPort)
- SERIAL7 -> UART8 (ESC Telemetry, RX8 pin only)

**OSD SupportÂ**
StellarH7V2 supports using its internal OSD using OSD_TYPE 1 (MAX7456 driver). Simultaneous DisplayPort OSD operation is preconfigured on SERIAL 6 but requires OSD_TYPE2 = 5. SeeMSP OSDfor more info.



---

## TBS Lucid H7
**Source URL:** https://ardupilot.org/plane/docs/common-tbs-lucidh7.html

### Description
The TBS LUCID H7 is a flight controller produced byTBS.

### Specifications
**FeaturesÂ**
- MCU - STM32H743 32-bit processor running at 480 MHz
- IMU - Dual ICM42688
- Barometer - DPS310
- OSD - AT7456E
- microSD card slot
- 7x UARTs
- CAN support
- 13x PWM Outputs (12 Motor Output, 1 LED)
- Battery input voltage: 2S-6S
- BEC 3.3V 0.5A
- BEC 5V 3A
- BEC 9V 3A for video, gpio controlled, pinned out on HD VTX connector
- Selectable 5V or VBAT pad, for analog VTX, gpio controlled on/off
- Dual switchable camera inputs


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB   (MAVLink2)
- SERIAL1 -> UART1 (USER, R1 is SBUS in HD VTX connector)
- SERIAL2 -> UART2 (GPS, DMA-enabled)
- SERIAL3 -> UART3 (DisplayPort, DMA-enabled)
- SERIAL4 -> UART4 (MAVLink2, Telem1)
- SERIAL6 -> UART6 (RC Input, DMA-enabled)
- SERIAL7 -> UART7 (MAVLink2, Telem2, DMA and flow-control enabled)
- SERIAL8 -> UART8 (ESC Telemetry, R8 on ESC connector for telem)

**OSD SupportÂ**
The TBS LUCID H7 supports OSD using OSD_TYPE 1 (MAX7456 driver) and simultaneously DisplayPort using TX3/RX3 on the HD VTX connector.



---

## TBS Lucid H7 Wing
**Source URL:** https://ardupilot.org/plane/docs/common-tbs-lucid-h7-wing.html

### Description
The TBS Lucid H7 Wing is a flight controller produced byTBS.

### Specifications
**FeaturesÂ**
- MCU: STM32H743VIH6, 480MHz, 2MB Flash
- Input voltage: 8V-50.4V (3-12S)
- Output power: 8A cont./10A peak BEC. 5V, 6V, 8.4V (selectable)
- Channels: 13x PWM (including LED)
- Gyro: ICM42688 x 2 (SPI1 & SPI4)
- Baro: DPS310 (I2C2)
- Peripherals: 7x UART, 2x I2C, 1x CAN
- Measurements: 6x ADC (Vbat, Current, CB2, CU2, RSSI, AirSpeed)
- High speed ports: MicroSD BlackBox, SPI3 on pin headers
- Analog FPV: Switchable dual camera inputs, AT7456E OSD, 5V/9V/12V support at 5A (selectable)
- Digital FPV: âDJIâ-connector with SBUS and OSD communication
- Current sensor: 165A cont. / 240A peak
- FC BEC: 5V 3A cont. (for FC & peripherals)
- FPV VTX BEC: 9V/12V 5A (selectable) and controlled by GPIO
- Dual  Camera inputs, GPIO selectable
- Camera supply selectable between 5V and VTX supply
- Dimensions:  54 x 36 x 13 mm


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB (MAVLink2)
- SERIAL1 -> UART1 (RX1 is SBUS in HD VTX connector)
- SERIAL2 -> UART2 (GPS, DMA-enabled)
- SERIAL3 -> UART3 (DisplayPort, DMA-enabled)
- SERIAL4 -> UART4 (MAVLink2, Telem1)
- SERIAL6 -> UART6 (RC Input, DMA-enabled)
- SERIAL7 -> UART7 (MAVLink2, Telem2, DMA and flow-control enabled)
- SERIAL8 -> UART8 (ESC Telemetry, RX8 on ESC connector for telem)

**OSD SupportÂ**
The TBS Lucid H7 Wing supports analog OSD using its onboard MAX7456 and simultaneously DisplayPort using TX3/RX3 on the HD VTX connector.



---

## ThePeach FCC-K1
**Source URL:** https://ardupilot.org/plane/docs/common-thepeach-k1.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32F427VIT6: 32bit ARM Cortex-M4, 168 MHz 256 KB RAM 2 MB Flash memoryIO Processor: STM32F100C8T6: ARM Cortex-M3, 32bit ARM Cortex-M3, 24 MHz, 8KB SRAM
- STM32F427VIT6: 32bit ARM Cortex-M4, 168 MHz 256 KB RAM 2 MB Flash memory
- IO Processor: STM32F100C8T6: ARM Cortex-M3, 32bit ARM Cortex-M3, 24 MHz, 8KB SRAM
- On-board SensorsAccel/Gyro: ICM-20602Accel/Gyro/Mag: MPU-9250Barometer: MS5611
- Accel/Gyro: ICM-20602
- Accel/Gyro/Mag: MPU-9250
- Barometer: MS5611
- Interfaces8+5 PWM output (8 from IO, 5 from FMU)Spektrum DSM / DSM2 / DSM-X Satellite compatible inputFutaba S.BUS compatible input and outputPPM sum signal inputAnalogue / PWM RSSI inputS.Bus servo outputSafety switch/LED4x UART Ports: TELEM1, TELEM2, GPS, SERIAL42x I2C Ports: I2C2, GPS1x CAN bus1x ADCAnalog inputs for voltage / Current of 1 battery
- 8+5 PWM output (8 from IO, 5 from FMU)
- Spektrum DSM / DSM2 / DSM-X Satellite compatible input
- Futaba S.BUS compatible input and output
- PPM sum signal input
- Analogue / PWM RSSI input
- S.Bus servo output
- Safety switch/LED
- 4x UART Ports: TELEM1, TELEM2, GPS, SERIAL4
- 2x I2C Ports: I2C2, GPS
- 1x CAN bus
- 1x ADC
- Analog inputs for voltage / Current of 1 battery
- MechanicalDimensions: 40.2 x 61.1 x 24.8mmWeight: 65g
- Dimensions: 40.2 x 61.1 x 24.8mm
- Weight: 65g
- Voltage RatingsPOWER input (5V to 5.5V)USB Input (4.75V to 5.25V)
- POWER input (5V to 5.5V)
- USB Input (4.75V to 5.25V)
note:
The output power railsFMU PWM OUTandI/O PWM OUTdo not power the autopilot board (and are not powered by it). You must supply power to one ofPOWERorUSBor the board will be unpowered.


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences using theSERIALx_PROTOCOLparameter.



---

## ThePeach FCC-R1
**Source URL:** https://ardupilot.org/plane/docs/common-thepeach-r1.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32F427VIT6: 32bit ARM Cortex-M4, 168 MHz 256 KB RAM 2 MB Flash memoryIO Processor: STM32F100C8T6: ARM Cortex-M3, 32bit ARM Cortex-M3, 24 MHz, 8KB SRAM
- STM32F427VIT6: 32bit ARM Cortex-M4, 168 MHz 256 KB RAM 2 MB Flash memory
- IO Processor: STM32F100C8T6: ARM Cortex-M3, 32bit ARM Cortex-M3, 24 MHz, 8KB SRAM
- On-board SensorsAccel/Gyro: ICM-20602Accel/Gyro/Mag: MPU-9250Barometer: MS5611
- Accel/Gyro: ICM-20602
- Accel/Gyro/Mag: MPU-9250
- Barometer: MS5611
- Interfaces8+5 PWM output (8 from IO, 6 from FMU)Spektrum DSM / DSM2 / DSM-X Satellite compatible inputFutaba S.BUS compatible input and outputPPM sum signal inputAnalogue / PWM RSSI inputS.Bus servo outputSafety switch/LED4x UART Ports: TELEM1, TELEM2(Raspberry Pi CM3+), GPS, SERIAL41x I2C Ports: GPS1x CAN busAnalog inputs for voltage / Current of 1 battery
- 8+5 PWM output (8 from IO, 6 from FMU)
- Spektrum DSM / DSM2 / DSM-X Satellite compatible input
- Futaba S.BUS compatible input and output
- PPM sum signal input
- Analogue / PWM RSSI input
- S.Bus servo output
- Safety switch/LED
- 4x UART Ports: TELEM1, TELEM2(Raspberry Pi CM3+), GPS, SERIAL4
- 1x I2C Ports: GPS
- 1x CAN bus
- Analog inputs for voltage / Current of 1 battery
- Interfaces For Raspberry Pi CM3+VBUSDDR2 Connector: Raspberry Pi CM3+1x UART2x USB1x Raspberry Pi Camera
- VBUS
- DDR2 Connector: Raspberry Pi CM3+
- 1x UART
- 2x USB
- 1x Raspberry Pi Camera
- MechanicalDimensions: 49.2 x 101 x 18.2mmWeight: 100g
- Dimensions: 49.2 x 101 x 18.2mm
- Weight: 100g
- Voltage RatingsPOWER input (5V to 5.5V)USB Input (4.75V to 5.25V)
- POWER input (5V to 5.5V)
- USB Input (4.75V to 5.25V)
note:


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences using theSERIALx_PROTOCOLparameter.



---

## TmotorH7Mini
**Source URL:** https://ardupilot.org/plane/docs/common-tmotor-h7-mini.html

### Description
The T-Motor H7 Mini is a flight controller produced byT-Motor.

### Specifications
**FeaturesÂ**
- MCU - STM32H743 32-bit processor running at 480 MHz
- IMU - ICM42688/BMI270
- Barometer - DPS310
- OSD - AT7456E
- Onboard Flash: 128Mbits
- 6x UARTs (1,5,6,7,9)
- 9x PWM Outputs (8 Motor Output, 1 LED)
- Battery input voltage: 2S-6S
- BEC 5V/2A, 10V/1.5A


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the
receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (ESC Telemetry)
- SERIAL3 -> UART3
- SERIAL5 -> UART5 (GPS, DMA-enabled)
- SERIAL6 -> UART6 (RX, DMA-enabled)
- SERIAL7 -> UART7 (DJI VTX, DMA-enabled)
- SERIAL8 -> UART8 (SBUS, DMA-enabled)

**OSD SupportÂ**
The T-Motor H7 Mini supports OSD using OSD_TYPE 1 (MAX7456 driver).



---

## UAV-DEV 743 UM082
**Source URL:** https://ardupilot.org/plane/docs/common-uav-dev-fc-um982.html

### Description
The UAV-DEV-FC-UM92 Flight Controller integrates an RTK GNSS module capable of producing compass-less heading when using a dual antenna configuration and is sold byUAV-DEV GmbH Webshop

### Specifications
**FeaturesÂ**
- ProcessorSTM32H743480MHz2MB Flash1MB RAM
- STM32H743
- 480MHz
- 2MB Flash
- 1MB RAM
- SensorsIMU TDK Invensense ICM-45686Barometer Infineon DPS310Magnetometer Bosch BMM150GNSS Unicore UM982 L1/L2/L5 RTK GNSS with GNSS Heading
- IMU TDK Invensense ICM-45686
- Barometer Infineon DPS310
- Magnetometer Bosch BMM150
- GNSS Unicore UM982 L1/L2/L5 RTK GNSS with GNSS Heading
- Power5.2V input via JST-GH
- 5.2V input via JST-GH
- InterfacesUSB-C100 MBits/s Ethernet6 x PWM / DShot, 2 x Bidirectional-DShot capableRC Input6 UARTs, 4 available externally2 x FD CAN ports with 120 Ohm termination resistormicroSDDEBUG
- USB-C
- 100 MBits/s Ethernet
- 6 x PWM / DShot, 2 x Bidirectional-DShot capable
- RC Input
- 6 UARTs, 4 available externally
- 2 x FD CAN ports with 120 Ohm termination resistor
- microSD
- DEBUG
- PhysicalSize: 50mm x 50mm (without SMA connector) x 15mmWeight: 22g with microSD card
- Size: 50mm x 50mm (without SMA connector) x 15mm
- Weight: 22g with microSD card


### Ports, UARTs & Pin Mapping
**S1 - SERIAL4 & SERIAL5 - 6 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | +5V | 5V
2 | USART6_TX | 3.3V
3 | USART6_RX | 3.3V
4 | UART7_TX | 3.3V
5 | UART7_RX | 3.3V
6 | GND | GND

**PWM - PWM / DShot / Telemetry - 8 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | PWM / DShot 1 BIDIR | 3.3V
2 | PWM / DShot 2 BIDIR | 3.3V
3 | PWM / DShot 3 BIDIR | 3.3V
4 | PWM / DShot 4 BIDIR | 3.3V
5 | PWM / DShot 5 | 3.3V
6 | PWM / DShot 6 | 3.3V
7 | USART3_RX / TELEM | 3.3V
8 | GND | GND

**C1 - CAN FD 1 - 4 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | +5V | 5V
2 | CAN_H | 
3 | CAN_L | 
4 | GND | GND

**C2 - CAN FD 2 - 4 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | +5V | 5V
2 | CAN_H | 
3 | CAN_L | 
4 | GND | GND

**Debug - 6 Pin Tag-ConnectÂ**
Pin | Signal Name | Voltage
1 | +3.3V | 3.3V
2 | SWDIO | 3.3V
3 | NRST | 3.3V
4 | SWCLK | 3.3V
5 | GND | GND
6 | not connected | 

**S2 - SERIAL1 & GNSS - 6 Pin JST-GHÂ**
Pin | Signal Name | Voltage
1 | +5V | 5V
2 | USART1_TX | 3.3V
3 | USART1_RX | 3.3V
4 | GNSS_PPS | 3.3V
5 | GNSS_EVENT | 3.3V
6 | GND | GND

**ETH - Ethernet - 4 Pin JST-GHÂ**
Pin | Signal Name
1 | RX-
2 | RX+
3 | TX-
4 | TX+

**UART MappingÂ**
Name | Function
SERIAL0 | USB
SERIAL1 | USART1 (MAVLink)
SERIAL2 | UART8 (GPS1) Internal: GNSS UM982 module
SERIAL3 | USART2 (Scripting) Internal: GNSS UM9892 module
SERIAL4 | USART6 (RCIN)
SERIAL5 | UART7 (MAVLink)
SERIAL6 | USART3 (ESC telemetry)
SERIAL7 | OTG2 (SLCAN)
All UARTs except USART3 TX have DMA capability. Any UART can be re-tasked by changing its protocol parameter.



---

## X-MAV-AP-H743v2
**Source URL:** https://ardupilot.org/plane/docs/common-X_MAV_H743v2.html

### Description
The AP-H743v2 is an autopilot designed and produced by X-MAV

### Specifications
**FeaturesÂ**
- STM32H743 microcontroller
- BMI088/ICM42688P dual IMUs
- DPS310 barometer
- QMC5883P magnetometer
- AT7456E OSD
- 9V 3A BEC; 5V 3A BEC
- MicroSD Card Slot
- 8 UARTs
- 8 PWM outputs
- 1 CAN
- 1 I2C
- 1 SWD


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn. Default protocols are shown below but may be changed by the user. All UARTs are DMA capable.
- SERIAL0 -> USB
- SERIAL1 -> UART2 (MAVLink2)
- SERIAL2 -> UART4 (User)
- SERIAL3 -> UART1 (GPS)
- SERIAL4 -> UART6 (User)
- SERIAL5 -> UART8 (User)
- SERIAL6 -> UART3 (DisplayPort)
- SERIAL7 -> UART5 (RCIN)
- SERIAL8 -> UART7 (RX only, ESC Telemetry)

**OSD SupportÂ**
The AP-H743v2 supports onboard analog SD OSD using a MAX7456 chip. Simultaneously, DisplayPort HD OSD is available on the DJI connector for HD VTX. Both on board OSD and DisplayPort OSD can be operated simultaneously and are enabled by default.

**VTX SupportÂ**
The SH1.0-6P connector supports a DJI Air Unit / HD VTX connection. Protocol defaults to DisplayPort. Pin 1 of the connector is 9v so be careful not to connect this to a peripheral requiring 5v.



---

## YJUAV A6SE
**Source URL:** https://ardupilot.org/plane/docs/common-yjuav-a6se.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32H750 32-bit processor480 Mhz/ 1 MB RAM16MB Onboard Flash32KB F-RAM nonvolatile memory
- STM32H750 32-bit processor
- 480 Mhz/ 1 MB RAM
- 16MB Onboard Flash
- 32KB F-RAM nonvolatile memory
- SensorsInvenSense ICM42688 accelerometer / gyroscopeInvenSense ICM42688 accelerometer / gyroscopeDPS310 barometerIST8310 magnetometer
- InvenSense ICM42688 accelerometer / gyroscope
- InvenSense ICM42688 accelerometer / gyroscope
- DPS310 barometer
- IST8310 magnetometer
- PowerPower supply: 4.5~5.5V
- Power supply: 4.5~5.5V
- Interfaces11x PWM servo outputs5x ADC pins5x Uart ports3x I2C ports2x CAN ports1x SPI port1x microSD port1x TypeC USB port1x JST_GH1.25 USB port1x Analog battery monitor port1x RC input (support SBUS, PPM and DSM)1x Safety switch and Buzzer port1x S.Bus servo output
- 11x PWM servo outputs
- 5x ADC pins
- 5x Uart ports
- 3x I2C ports
- 2x CAN ports
- 1x SPI port
- 1x microSD port
- 1x TypeC USB port
- 1x JST_GH1.25 USB port
- 1x Analog battery monitor port
- 1x RC input (support SBUS, PPM and DSM)
- 1x Safety switch and Buzzer port
- 1x S.Bus servo output
- OtherWeight 40gSize 58mm x 38mm x 16mmOperating temperature -20 ~ 85Â°c
- Weight 40g
- Size 58mm x 38mm x 16mm
- Operating temperature -20 ~ 85Â°c


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB (OTG1)
- SERIAL1 -> USART2 (Telem1)
- SERIAL2 -> USART6 (Telem2)
- SERIAL3 -> USART3 (GPS1), NODMA
- SERIAL4 -> USART1 (GPS2), NODMA
- SERIAL5 -> UART8 (USER) TX only, normally used for SBUS_OUT with protocol change
- SERIAL6 -> UART7 (USER/Debug), NODMA
- SERIAL7 -> USB2 (OTG2)



---

## YJUAV A6SE H743
**Source URL:** https://ardupilot.org/plane/docs/common-yjuav-a6se-h743.html

### Description


### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processor480 Mhz/ 1 MB RAM2MB Flash32KB F-RAM nonvolatile memory
- STM32H743 32-bit processor
- 480 Mhz/ 1 MB RAM
- 2MB Flash
- 32KB F-RAM nonvolatile memory
- SensorsInvenSense ICM42688 accelerometer / gyroscopeInvenSense ICM42688 accelerometer / gyroscopeDPS310 barometerIST8310 magnetometer
- InvenSense ICM42688 accelerometer / gyroscope
- InvenSense ICM42688 accelerometer / gyroscope
- DPS310 barometer
- IST8310 magnetometer
- PowerPower supply: 4.5~5.5V
- Power supply: 4.5~5.5V
- Interfaces11x PWM servo outputs5x ADC pins5x Uart ports3x I2C ports2x CAN ports1x SPI port1x microSD port1x TypeC USB port1x JST_GH1.25 USB port1x Analog battery monitor port1x RC input (supports SBUS, PPM and DSM)1x Safety switch and Buzzer port1x S.Bus servo output
- 11x PWM servo outputs
- 5x ADC pins
- 5x Uart ports
- 3x I2C ports
- 2x CAN ports
- 1x SPI port
- 1x microSD port
- 1x TypeC USB port
- 1x JST_GH1.25 USB port
- 1x Analog battery monitor port
- 1x RC input (supports SBUS, PPM and DSM)
- 1x Safety switch and Buzzer port
- 1x S.Bus servo output
- OtherWeight 40gSize 58mm x 38mm x 16mmOperating temperature -40 ~ 85Â°c
- Weight 40g
- Size 58mm x 38mm x 16mm
- Operating temperature -40 ~ 85Â°c


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB (OTG1)
- SERIAL1 -> USART2 (Telem1)
- SERIAL2 -> USART6 (Telem2)
- SERIAL3 -> USART3 (GPS1), NODMA
- SERIAL4 -> USART1 (GPS2), NODMA
- SERIAL5 -> UART8 (USER) TX only, normally used for SBUS_OUT with protocol change
- SERIAL6 -> UART7 (USER/Debug), NODMA
- SERIAL7 -> USB2 (OTG2)



---

## YJUAV-A6Ultra
**Source URL:** https://ardupilot.org/plane/docs/common-yjuav-a6ultra.html

### Description
The A6Ultra flight controller is manufactured and sold byYJUAV.

### Specifications
**Features:Â**
- MCUSTM32H743 32-bit processor running at 480MH2MB Flash1MB RAM
- STM32H743 32-bit processor running at 480MH
- 2MB Flash
- 1MB RAM
- SensorsIMUs:2x ICM42688, ICM42652Baros:Two barometers:2 x DPS310Magnetometer: Built-in ITS8310 magnetometer
- IMUs:2x ICM42688, ICM42652
- 2x ICM42688, ICM42652
- Baros:Two barometers:2 x DPS310Magnetometer: Built-in ITS8310 magnetometer
- Two barometers:2 x DPS310
- Magnetometer: Built-in ITS8310 magnetometer
- InterfacesEthernetMicro-C USBMicroSD card slot5 UARTs, 2 with hardware flow controlSafety Switch2 Analog Power Monitor inputs2 CAN ports2 I2C portsSPI portBuzzerRCin port13 motor/servo outputs, 8 supporting BiDirDShot, 11 supporting DShot
- Ethernet
- Micro-C USB
- MicroSD card slot
- 5 UARTs, 2 with hardware flow control
- Safety Switch
- 2 Analog Power Monitor inputs
- 2 CAN ports
- 2 I2C ports
- SPI port
- Buzzer
- RCin port
- 13 motor/servo outputs, 8 supporting BiDirDShot, 11 supporting DShot


### Ports, UARTs & Pin Mapping
**UART MappingÂ**
- SERIAL0 -> USB (OTG1)
- SERIAL1 -> USART2 (Telem1)
- SERIAL2 -> USART6 (Telem2)
- SERIAL3 -> USART3 (GPS1)
- SERIAL4 -> USART1 (GPS2)
- SERIAL5 -> UART8 (USER) TX only, normally used for SBUS_OUT with protocol change
- SERIAL6 -> UART7 (USER/Debug), NODMA
- SERIAL7 -> USB2 (OTG2)



---

## Companion Computers
**Source URL:** https://ardupilot.org/plane/docs/common-companion-computers.html#common-companion-computers

### Description



---

## Beagle Bone Blue (Linux)
**Source URL:** https://ardupilot.org/plane/docs/common-beagle-bone-blue.html

### Description
BeagleBone Blue(BBBlue) is a complete, Linux-enabled robotics computer.
Community-supported and fully open-source, the real-time performance, flexible networking and rich set of robotics-oriented peripherals make building mobile robots quick and affordable.
Confer theschematic(s)fromBBBlue repofor more details.

### Specifications
**SpecificationsÂ**
- Processor1GHz ARM Cortex-A82x32-bit 200-MHz programmable real-time units (PRUs)512MB DDR3 RAM integrated4GB 8-bit eMMC flash
- 1GHz ARM Cortex-A8
- 2x32-bit 200-MHz programmable real-time units (PRUs)
- 512MB DDR3 RAM integrated
- 4GB 8-bit eMMC flash
- SensorsMPU9250 for accelerometers, gyroscope and internal compass (I2C)BMP280 barometer
- MPU9250 for accelerometers, gyroscope and internal compass (I2C)
- BMP280 barometer
- InterfacesWifi (802.11bgn)Bluetooth 4.1 and BLE8x ESC/Servo out (6v), 4x DC motor outUSB 2.0 client and host11x programmable LEDs2x buttons1.8V analogSPI, I2C, UART2-cell LiPo support with balancing, 9-18V charger input
- Wifi (802.11bgn)
- Bluetooth 4.1 and BLE
- 8x ESC/Servo out (6v), 4x DC motor out
- USB 2.0 client and host
- 11x programmable LEDs
- 2x buttons
- 1.8V analog
- SPI, I2C, UART
- 2-cell LiPo support with balancing, 9-18V charger input
- OSLinux (Debian)
- Linux (Debian)



---

## Obal Board (Linux)
**Source URL:** https://ardupilot.org/plane/docs/common-obal-overview.html

### Description


### Specifications
**SpecificationsÂ**
- Processor(Raspberry PI Zero & 42)
- SensorsMPU9250 as main accel, gyro and compassBMP-180 barometer
- MPU9250 as main accel, gyro and compass
- BMP-180 barometer
- InterfacesUART, SPI, I2CPWM 8-Channels16 PWM servo outputs
- UART, SPI, I2C
- PWM 8-Channels
- 16 PWM servo outputs



---

## PocketBeagle 2 DIY Cape** (Linux)
**Source URL:** https://ardupilot.org/plane/docs/common-pocketbeagle-2.html

### Description
PocketBeagle 2(PB2) is an upgraded version of the popular PocketBeagle, designed as an ultra-compact, low-cost, and powerful single-board computer (SBC). Targeted at developers, students, and hobbyists, PocketBeagle 2 retains the simplicity and flexibility of its predecessor while delivering enhanced performance and expanded features to support modern development needs. PocketBeagle 2 is ideal for creating IoT devices, robotics projects, and educational applications. Its small form factor and low power consumption make it a versatile platform for embedded development, whether prototyping or deploying at scale.
PocketBeagle 2 is based on Texas Instruments AM6254 SoC. Its multiple A53 cores can provide higher performance than the classic PocketBeagle. The new design comes with pre-soldered headers, a 3-pin JST-SH 1.00mm UART debug port, a USB-C port, Texas Instruments MSPM0L1105 Cortex-M0+ MCU for ADC, 512MB RAM, and a LiPo Battery charger.

### Specifications
**SpecificationsÂ**
- ProcessorTexas Instruments AM6232 SoCMulticore 64-bit Arm Cortex-A53 microprocessor subsystem at up to 1.4 GHzEach A53 Core has 32KB L1 DCache with SECDED ECC and 32KB L1 ICache with Parity protectionSingle-core ArmÂ® CortexÂ®-M4F MCU at up to 400MHzDual-core Programmable Real-Time Unit Subsystem (PRUSS) running up to 333 MHz512MB LPDDR4 3200MHz
- Texas Instruments AM6232 SoC
- Multicore 64-bit Arm Cortex-A53 microprocessor subsystem at up to 1.4 GHz
- Each A53 Core has 32KB L1 DCache with SECDED ECC and 32KB L1 ICache with Parity protection
- Single-core ArmÂ® CortexÂ®-M4F MCU at up to 400MHz
- Dual-core Programmable Real-Time Unit Subsystem (PRUSS) running up to 333 MHz
- 512MB LPDDR4 3200MHz
- OSLinux (Debian)
- Linux (Debian)



---

## T3 Gemstone O1 (Linux)
**Source URL:** https://ardupilot.org/plane/docs/common-t3-gem-o1-overview.html

### Description
This page presentsT3 Gemstone O1- High-performance development board based
on Texas Instruments AM67A processor, which runs well proven ArduPilot flight stack on Linux.

### Specifications
**SpecificationsÂ**
- Processor(TI AM67A)Quad-core 64-bit ARM Cortex-A53 @1.4 GHz for running high-level operating systems such as LinuxDual single-core ARM Cortex-R5F @800 MHz for running real-time MCU applicationsDual 2 TOPS (4 TOPS total) deep learning accelerators for running vision applicationsAdvanced 50 GFLOPS GPU for high-performance graphics processing4GB LPDDR4 RAM
- Quad-core 64-bit ARM Cortex-A53 @1.4 GHz for running high-level operating systems such as Linux
- Dual single-core ARM Cortex-R5F @800 MHz for running real-time MCU applications
- Dual 2 TOPS (4 TOPS total) deep learning accelerators for running vision applications
- Advanced 50 GFLOPS GPU for high-performance graphics processing
- 4GB LPDDR4 RAM
- SensorsInvenSense ICM-20948 IMU (accel, gyro, compass)Bosch BMP390 barometerTI HDC2010 humidity and temperature
- InvenSense ICM-20948 IMU (accel, gyro, compass)
- Bosch BMP390 barometer
- TI HDC2010 humidity and temperature
- StorageOn-board32GB eMMC flash512Kbit EEPROMExpandablemicroSD card slotM.2 2280 SSD port
- On-board32GB eMMC flash512Kbit EEPROM
- 32GB eMMC flash
- 512Kbit EEPROM
- ExpandablemicroSD card slotM.2 2280 SSD port
- microSD card slot
- M.2 2280 SSD port
- Network Connections1x Gigabit ethernet1x CAN busWi-Fi 4 (802.11n)Bluetooth 5.1, Bluetooth Low Energy (BLE)
- 1x Gigabit ethernet
- 1x CAN bus
- Wi-Fi 4 (802.11n)
- Bluetooth 5.1, Bluetooth Low Energy (BLE)
- PowerUSB Type-C power (5-9V / 3A)DC power connector (5-12V / 3A)
- USB Type-C power (5-9V / 3A)
- DC power connector (5-12V / 3A)
- InterfacesUART, I2C and SPI for extensionsS.Bus input7x PWM servo outputsGreen-red status ledsReal-time clockFan with PWM speed control4x USB ports2x 4-lane MIPI CSI/DSI1x HDMI
- UART, I2C and SPI for extensions
- S.Bus input
- 7x PWM servo outputs
- Green-red status leds
- Real-time clock
- Fan with PWM speed control
- 4x USB ports
- 2x 4-lane MIPI CSI/DSI
- 1x HDMI



---

## CUAV V5
**Source URL:** https://ardupilot.org/plane/docs/common-pixhackV5-overview.html

### Description
The CUAV v5 is an advanced autopilot designed and made by CUAV.
The board is based on the FMUv5 open hardware design, with further attributionhere.
It is intended primarily for academic and commercial users.

### Specifications
**SpecificationsÂ**
- Processor32-bit ARM Cortex M7 core with DPFPU216 Mhz/512 KB RAM/2 MB Flash32-bit co-processor
- 32-bit ARM Cortex M7 core with DPFPU
- 216 Mhz/512 KB RAM/2 MB Flash
- 32-bit co-processor
- SensorsInvenSense ICM20689 accelerometer / gyroscopeBosch BMI055 accelerometer / gyroscopeMS5611 barometerIST8310 magnetometer
- InvenSense ICM20689 accelerometer / gyroscope
- Bosch BMI055 accelerometer / gyroscope
- MS5611 barometer
- IST8310 magnetometer
- PowerOperating power: 4.3~5.4VUSB Input: 4.75~5.25VHigh-power servo rail, up to 36V
(servo rail does not power the autopilot)Dual voltage and current monitor inputsCUAV v5 can be triple redundant if power is provided
to both battery monitor inputs and the USB port
- Operating power: 4.3~5.4V
- USB Input: 4.75~5.25V
- High-power servo rail, up to 36V
(servo rail does not power the autopilot)
- Dual voltage and current monitor inputs
- CUAV v5 can be triple redundant if power is provided
to both battery monitor inputs and the USB port
- Interfaces8 IOMCU PWM servo outputs6 FMU PWM outputs (D-Shot capable)3 dedicated PWM/Capture inputs on FMUS.Bus servo outputR/C inputs for CPPM and S.BusAnalogue / PWM RSSI input5x general purpose serial ports4x I2C ports4x SPI buses enabled2x CAN Bus ports
- 8 IOMCU PWM servo outputs
- 6 FMU PWM outputs (D-Shot capable)
- 3 dedicated PWM/Capture inputs on FMU
- S.Bus servo output
- R/C inputs for CPPM and S.Bus
- Analogue / PWM RSSI input
- 5x general purpose serial ports
- 4x I2C ports
- 4x SPI buses enabled
- 2x CAN Bus ports
- Other



---

## Emlid Edge
**Source URL:** https://ardupilot.org/plane/docs/common-emlid-edge.html

### Description
TheEmlid Edgeis an advanced autopilot with HDMI video input and 5.8 GHz data link which allows full HD video streaming and telemetry up to 2 km.  Dual temperature-controlled IMUs, external DroneCAN GNSS module and a wide range power module based on Hall sensor.

### Specifications
**SpecificationsÂ**
- ProcessorARM Cortex-A53 64-bit quad-core CPUARM Cortex-M3 co-processor1GB RAM
- ARM Cortex-A53 64-bit quad-core CPU
- ARM Cortex-M3 co-processor
- 1GB RAM
- Sensors2x InvenSense ICM20602 IMUs with temperature controlMS5611 Barometer2x IsenTek IST8310 compassesuBlox NEO-M8N
- 2x InvenSense ICM20602 IMUs with temperature control
- MS5611 Barometer
- 2x IsenTek IST8310 compasses
- uBlox NEO-M8N
- PowerTriple redundant power supply
- Triple redundant power supply
- InterfacesRC Inputs: 1x PPM, 1xSBUS inputRC Outputs: 12x PWM servo outputs2x CAN2x USB1x Serial+I2C1x Serial+ADC4.3 ~ 60V input5.180 ~ 5.825 Ghz datalink at up to 27 dBmPower monitor up to 12S, 200A
- RC Inputs: 1x PPM, 1xSBUS input
- RC Outputs: 12x PWM servo outputs
- 2x CAN
- 2x USB
- 1x Serial+I2C
- 1x Serial+ADC
- 4.3 ~ 60V input
- 5.180 ~ 5.825 Ghz datalink at up to 27 dBm
- Power monitor up to 12S, 200A
- DimensionsWeight 59gSize: 97mm x 46mm x 15mm
- Weight 59g
- Size: 97mm x 46mm x 15mm



---

## Erle PXFmini RPi Zero Shield
**Source URL:** https://ardupilot.org/plane/docs/common-pxfmini.html

### Description
ThePXFmini (Pixhawk Fire Cape Mini) Autopilot Shieldmade byErle Roboticsis a low cost
and open autopilot shield for the Raspberry Pi that allows you to create
a ready-to-fly autopilot with support for ArduPilot.
The shield has been designed specially for the Raspberry Pi Zero but it
is also pin to pin compatible with other models from the Raspberry Pi
family.
The PXFmini shield weighs only 15 grams and embeds all the power
electronics necessary to comply with most of the existing components for
drones through its I2C and UART ports. PXFmini includes 3 axes gravity
sensor, 3 axes gyroscope, 3 axes digital compass, pressure sensor,
temperature sensor and an ADC. It includes new JST GH connectors
provide an amazing new experience.
Whatâs best, the PXFmini schematics are open for you to hack around and
create your own robots based on the design. The board can be purchasedhere.


---

## Erle ErleBrain
**Source URL:** https://ardupilot.org/plane/docs/common-erle-brain-linux-autopilot.html

### Description
This page presents theErle-BrainLinux autopilot â an ArduPilot autopilot andcompanion computerin a single package.
Currently there are two versions of this Linux based Autopilot and a
shield:
Erle-Brain based drones can be assembled as discussed in theofficial documentation.
Erle-Brain based drones can also be purchased from the Erle Robotics
official store in bothready to useandDIY kitform.


---

## Holybro Kakute H7 Mini
**Source URL:** https://ardupilot.org/plane/docs/common-holybro-kakuteh7mini.html

### Description
above image and some content courtesy ofHolybro

### Specifications
**SpecificationsÂ**
- ProcessorSTM32H743 32-bit processorAT7456E Video processor for OSD16 MByte (v1.1) / 128 MByte (v1.3, v1.5) data flash for logging
- STM32H743 32-bit processor
- AT7456E Video processor for OSD
- 16 MByte (v1.1) / 128 MByte (v1.3, v1.5) data flash for logging
- SensorsV1.1: MPU6000, V1.3: BMI270, V1.5: ICM-42688-P (accel & gyro)BMP280 barometer
- V1.1: MPU6000, V1.3: BMI270, V1.5: ICM-42688-P (accel & gyro)
- BMP280 barometer
- Power7V ~ 26V input power directly from battery5V 2A supply for peripherals
- 7V ~ 26V input power directly from battery
- 5V 2A supply for peripherals
- Interfaces9x PWM outputs (8 servo/motor + WS2812 LED)6x UARTs/serial for GPS and other peripherals1x I2C port for external compassBattery Voltage and Current Sensor inputsUSB-C portSwitchable VTX powerAnalog RSSI input (pin 8)Buzzer output
- 9x PWM outputs (8 servo/motor + WS2812 LED)
- 6x UARTs/serial for GPS and other peripherals
- 1x I2C port for external compass
- Battery Voltage and Current Sensor inputs
- USB-C port
- Switchable VTX power
- Analog RSSI input (pin 8)
- Buzzer output


### Ports, UARTs & Pin Mapping
**PinoutÂ**
Pin | Function
VTX+ | 9V for HD System or other VTX, by default ON/OFF is
controlled by RELAY2. SeeRelay SwitchCan be controlled by RELAY2
SDA, SCL | I2C connection (for peripherals)
5v | 5v output (1.5A max)
3v3 | 3.3v output (0.25A max)
Vi | Video input from FPV camera
Vo | Video output to video transmitter
CAM | To camera OSD control
G or GND | Ground
RSI | Analog RSSI (0-3.3v) input from receiver
R2, T3 | UART2 RX and TX
R3, T3 | UART3 RX and TX
R4, T4 | UART4 RX and TX
R6, T6 | UART6 RX and TX (UART6 RX is also located in the
GH plug)
LED | WS2182 addressable LED signal wire
Z- | Piezo buzzer negative leg

**ESC PortÂ**
Pin | Function
B+ | Battery positive voltage (2S-6S)
R7 | UART7 RX
GND | Ground
CURRENT | CURRENT
M1 | Motor signal output 1
M2 | Motor signal output 2
M3 | Motor signal output 3
M4 | Motor signal output 4

**VTX PortÂ**
Pin | Function
Vtx+ | 9V for HD System or other VTX, by default ON/OFF is
controlled by RELAY2. SeeRelay Switch
G | Ground
T1 | UART1 TX
R1 | UART1 RX
G | Ground
R6 | UART6 RX

**UART MappingÂ**
The UARTs are marked Rn and Tn in the above pinouts. The Rn pin is the receive pin for UARTn. The Tn pin is the transmit pin for UARTn.
- SERIAL0 -> USB
- SERIAL1 -> UART1 (DJI Goggles OSD by default) DMA-Enabled
- SERIAL2 -> UART2 (Telem2) No DMA
- SERIAL3 -> UART3 (GPS) DMA-Enabled
- SERIAL4 -> UART4  DMA-Enabled
- SERIAL6 -> UART6 (used for RC input and RC telemetry, PPM is not supported) DMA-Enabled
- SERIAL7 -> UART7 (Receive only, ESC Telemetry by default) No DMA

**OSD SupportÂ**
The KakuteH7 Mini supports OSD usingOSD_TYPE1 (MAX7456 driver). The defaults are also setup to allow DJI Goggle OSD support on UART1.



---

## Intel Aero
**Source URL:** https://ardupilot.org/plane/docs/common-intel-aero-overview.html

### Description
TheIntel Aerocomputer board is a high performance linux board that can run ArduPilot natively while still having enough compute resources to do other CPU intensive tasks including vision processing.

### Specifications
**SpecificationsÂ**
- Processor-  IntelÂ® Atomâ¢ x7-Z8700 Processor
-  2.4 GHz burst, quad core, 2M cache, 64 bit
-  4GB RAM LPDDR3-1600
-  32GB eMMC
- SensorsBosch BMI160 6-Axis IMUBosch BMC150 6-axis compassMS5611 Barometer
- Bosch BMI160 6-Axis IMU
- Bosch BMC150 6-axis compass
- MS5611 Barometer
- OSLinux* 4.4.3-yocto-standard OS powered with Yocto Project* 2.1 (Krogoth)
- Linux* 4.4.3-yocto-standard OS powered with Yocto Project* 2.1 (Krogoth)
- InterfacesI2C x 2UARTSPICAN5 analog inputs25 programmable GPIO pinsWi-Fi (802.11ac)1 micro HDMI 1.4b1 USB 3.0 On-the-Go (OTG) connectorMIPI (CSI-2) 4-lanes + 1 lane connectormicroSD memory card slotM.2 connector 1 lane PCIe for SSD
- I2C x 2
- UART
- SPI
- CAN
- 5 analog inputs
- 25 programmable GPIO pins
- Wi-Fi (802.11ac)
- 1 micro HDMI 1.4b
- 1 USB 3.0 On-the-Go (OTG) connector
- MIPI (CSI-2) 4-lanes + 1 lane connector
- microSD memory card slot
- M.2 connector 1 lane PCIe for SSD
- DimensionsWeight: 30g (without heatsink, 60g (with heatsink)Size: 88mm x 63mm x 20mm (including heatsink)
- Weight: 30g (without heatsink, 60g (with heatsink)
- Size: 88mm x 63mm x 20mm (including heatsink)



---

## Intel Aero RTF vehicle
**Source URL:** https://ardupilot.org/plane/docs/common-intel-aero-rtf.html

### Description
TheIntel Aero RTF vehicleincludes theIntel Aero compute board,Vision Accessory Kitand aSpektrum DXe transmitter.
Within the vehicle is an STM32F427V autopilot board which can run ArduPilot (replacing the pre-loaded non-ArduPilot software).
In this way, the higher poweredIntel Aero compute boardis used as acompanion computer.


---

## Mateksys F405-SE
**Source URL:** https://ardupilot.org/plane/docs/common-matekf405-se.html

### Description
the above images and some content courtesy ofmateksys.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)
- STM32F405RGT6 ARM (168MHz)
- SensorsInvenSense MPU6000 IMU (accel, gyro)DPS310 BarometerVoltage & 184A current sensor
- InvenSense MPU6000 IMU (accel, gyro)
- DPS310 Barometer
- Voltage & 184A current sensor
- Power6V ~ 36V DC input power5V, 2A BEC for FC & Peripherals (GPS/Compass/etc.)BEC Vx 5A for servos, 5V/ 6V option (WSE 0nly)BEC 8V 1.5A for VTX and camera (WSE 0nly)
- 6V ~ 36V DC input power
- 5V, 2A BEC for FC & Peripherals (GPS/Compass/etc.)
- BEC Vx 5A for servos, 5V/ 6V option (WSE 0nly)
- BEC 8V 1.5A for VTX and camera (WSE 0nly)
- InterfacesVCP & 6x UARTS10x PWM outputs, (LED output used as PWM10)1x RC input PWM/PPM, SBUS2x I2C port for external compass and airspeed sensorUSB portBuilt-in OSD3x ADC (Vbat, Current, RSSI)Micro SD slot
- VCP & 6x UARTS
- 10x PWM outputs, (LED output used as PWM10)
- 1x RC input PWM/PPM, SBUS
- 2x I2C port for external compass and airspeed sensor
- USB port
- Built-in OSD
- 3x ADC (Vbat, Current, RSSI)
- Micro SD slot
- Size and DimensionsSE:46mm x 36mm (30.5mm spaced square mounting holes)10gWSE:44mm x 29mm x 10mm (25mm x25mm mounting, 2mm holes)20g with bottom plate and remoter USB/buzzer board
- SE:46mm x 36mm (30.5mm spaced square mounting holes)10g
- 46mm x 36mm (30.5mm spaced square mounting holes)
- 10g
- WSE:44mm x 29mm x 10mm (25mm x25mm mounting, 2mm holes)20g with bottom plate and remoter USB/buzzer board
- 44mm x 29mm x 10mm (25mm x25mm mounting, 2mm holes)
- 20g with bottom plate and remoter USB/buzzer board
These boards use the MatekF405-Wing firmwarehere.
See mateksys.com for SEdetailed specificationsandwiring diagramsand WSEdetailed specificationsandwiring diagrams


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1
- SERIAL2 = empty
- SERIAL3 = GPS1 = USART3
- SERIAL4 = GPS2 = UART4
- SERIAL5 = USER = UART5
- SERIAL6 = USER = USART6 (RX only; for ESC telemetry, use SERIAL6_PROTOCOL=16)
- SERIAL7 = USER = USART2 (only if BRD_ALT_CONFIG =1)
Serial protocols can be adjusted to personal preferences.



---

## Mateksys F405-STD and variants*
**Source URL:** https://ardupilot.org/plane/docs/common-matekf405.html

### Description
the above images and some content courtesy ofmateksys.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)
- STM32F405RGT6 ARM (168MHz)
- SensorsICM20602 IMU on STD version, MPU6000 on CTR versionBMP280 barometer (STD and CTR only)184A Voltage & current sensor on CTR version
- ICM20602 IMU on STD version, MPU6000 on CTR version
- BMP280 barometer (STD and CTR only)
- 184A Voltage & current sensor on CTR version
- Interfaces5x UARTS6x PWM outputs (7 on -STD)1x RC input PWM/PPM, SBUSI2C port for external compass and airspeed sensor (STD, CTR and AIO)USB portBuilt-in OSDMicroSD slot
- 5x UARTS
- 6x PWM outputs (7 on -STD)
- 1x RC input PWM/PPM, SBUS
- I2C port for external compass and airspeed sensor (STD, CTR and AIO)
- USB port
- Built-in OSD
- MicroSD slot
- Size and Dimensions36x36mm PCB with 30.5mm mounting holesSTD: 7gCTR: 10g
- 36x36mm PCB with 30.5mm mounting holes
- STD: 7g
- CTR: 10g
See mateksys.com for moredetailed specificationsandwiring diagrams.


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART3
- SERIAL2 = Telemetry2 = UART4
- SERIAL3 = GPS1 = USART1
- SERIAL4 = GPS2 = UART5
- SERIAL5 = User = USART2 (TX only unlessBRD_ALT_CONFIG= 1, then RX is available)
Serial protocols can be adjusted to personal preferences.



---

## Mateksys F405-Wing
**Source URL:** https://ardupilot.org/plane/docs/common-matekf405-wing.html

### Description
the above image and some content courtesy ofmateksys.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F405RGT6 ARM (168MHz)
- STM32F405RGT6 ARM (168MHz)
- SensorsInvenSense MPU6000 IMU (accel, gyro)BMP280 barometer (later models use DPS310)Voltage & current sensor
- InvenSense MPU6000 IMU (accel, gyro)
- BMP280 barometer (later models use DPS310)
- Voltage & current sensor
- Power9V ~ 30V DC input power
- 9V ~ 30V DC input power
- Interfaces6x UARTS10x PWM outputs1x RC input PWM/PPM, SBUSI2C port for external compass and airspeed sensorUSB portBuilt-in OSD
- 6x UARTS
- 10x PWM outputs
- 1x RC input PWM/PPM, SBUS
- I2C port for external compass and airspeed sensor
- USB port
- Built-in OSD
- Size and Dimensions56mm x 36mm x 15mm25g
- 56mm x 36mm x 15mm
- 25g
See mateksys.com for moredetailed specificationsandwiring diagrams.


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = USART1
- SERIAL2 = empty
- SERIAL3 = GPS1 = USART3
- SERIAL4 = GPS2 = UART4
- SERIAL5 = USER = UART5
- SERIAL6 = USER = USART6
- SERIAL7 = USER = USART2 (only if BRD_ALT_CONFIG =1)
Serial protocols can be adjusted to personal preferences.



---

## Mateksys F765-Wing
**Source URL:** https://ardupilot.org/plane/docs/common-matekf765-wing.html

### Description
the above image and some content courtesy ofmateksys.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F765VIT6  ARM (216MHz)
- STM32F765VIT6  ARM (216MHz)
- SensorsInvenSense MPU6000 IMU (accel, gyro) & ICM20602BMP280 barometer (later models use DPS310)Voltage & 132A current sensor
- InvenSense MPU6000 IMU (accel, gyro) & ICM20602
- BMP280 barometer (later models use DPS310)
- Voltage & 132A current sensor
- Power9V ~ 36V DC input power5V 2A BEC for peripherals9/12V 2A BEC for video5/6/7.2V 8A BEC for servos
- 9V ~ 36V DC input power
- 5V 2A BEC for peripherals
- 9/12V 2A BEC for video
- 5/6/7.2V 8A BEC for servos
- Interfaces7x UARTS12x PWM outputs1x RC input PWM/PPM, SBUS2x I2C ports for external compass, airspeed sensor, etc.SPI4 portUSB port6 ADCDual Switchable Camera inputsBuilt-in OSD
- 7x UARTS
- 12x PWM outputs
- 1x RC input PWM/PPM, SBUS
- 2x I2C ports for external compass, airspeed sensor, etc.
- SPI4 port
- USB port
- 6 ADC
- Dual Switchable Camera inputs
- Built-in OSD
- Size and Dimensions54mm x 36mm x 13mm26g
- 54mm x 36mm x 13mm
- 26g
See mateksys.com for moredetailed specificationsandwiring diagrams(ArduPilot connections may vary slightly due to different UART usage).


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = UART7 (support CTS and RTS signaling)
- SERIAL2 = Telemetry2 = USART1
- SERIAL3 = GPS1 = USART2
- SERIAL4 = GPS2 = USART3
- SERIAL5 = USER = UART8
- SERIAL6 = USER = UART4
- SERIAL7 = USER = UART6 (TX only unlessBRD_ALT_CONFIG= 1, then RX available also)
- SERIAL8 = USER = UART5 (RX only, for ESC telemetry)
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences.



---

## Mateksys F765-WSE
**Source URL:** https://ardupilot.org/plane/docs/common-matekf765-wse.html

### Description
the above image and some content courtesy ofmateksys.com

### Specifications
**SpecificationsÂ**
- ProcessorSTM32F765VIH6  ARM (216MHz)
- STM32F765VIH6  ARM (216MHz)
- SensorsICM-42688-PDPS310Voltage & 90A continuous, 220A peak current sensor
- ICM-42688-P
- DPS310
- Voltage & 90A continuous, 220A peak current sensor
- Power6.8V ~ 30V DC input power5V 2A BEC for peripherals9/12V 2A BEC for video5/6/7.2V 8A BEC for servos
- 6.8V ~ 30V DC input power
- 5V 2A BEC for peripherals
- 9/12V 2A BEC for video
- 5/6/7.2V 8A BEC for servos
- Interfaces6.5x UARTS12x PWM outputs1x RC input PWM/PPM, SBUS2x I2C ports for external compass, airspeed sensor, etc.CAN portUSB port6 ADCDual Switchable Camera inputsBuilt-in OSD (AT7456E)
- 6.5x UARTS
- 12x PWM outputs
- 1x RC input PWM/PPM, SBUS
- 2x I2C ports for external compass, airspeed sensor, etc.
- CAN port
- USB port
- 6 ADC
- Dual Switchable Camera inputs
- Built-in OSD (AT7456E)
- Size and Dimensions44mm x 29mm x 14.5mm22g
- 44mm x 29mm x 14.5mm
- 22g
See mateksys.com for moredetailed specificationsandwiring diagrams(ArduPilot connections may vary slightly due to different UART usage).
ArduPilot Firmware: MatekF7656-SE


### Ports, UARTs & Pin Mapping
**Default UART orderÂ**
- SERIAL0 = console = USB
- SERIAL1 = Telemetry1 = UART7 (support CTS and RTS signaling)
- SERIAL2 = Telemetry2 = USART1
- SERIAL3 = GPS1 = USART2
- SERIAL4 = GPS2 = USART3
- SERIAL5 = USER = UART8
- SERIAL7 = USER = UART6 (TX only unlessBRD_ALT_CONFIG= 1, then RX available also)
- SERIAL8 = USER = UART5 (RX only, for ESC telemetry)
Serial port protocols (Telem, GPS, etc.) can be adjusted to personal preferences.



---

## archived
**Source URL:** https://ardupilot.org/plane/docs/common-archived-topics.html#common-archived-topics

### Description
This is the parent topic for grouping âarchivedâ topics - topics that
are no longer considered relevant to most users, but which may have some
value to users with old hardware.


---

