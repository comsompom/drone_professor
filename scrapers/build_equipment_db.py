"""
Equipment Database Scraper
Scrapes information about engines, servos, and other drone equipment
"""

import json
import time
from typing import Dict, List, Any


class EquipmentDatabaseBuilder:
    """
    Builds a comprehensive equipment database for drones and small planes
    Includes engines (gasoline and electric), servos, ESCs, batteries, etc.
    """

    def __init__(self):
        self.equipment_data = {
            'engines': {
                'electric': [],
                'gasoline': []
            },
            'servos': [],
            'escs': [],
            'batteries': [],
            'propellers': [],
            'optical_flow': [],
            'gimbals': [],
            'transmitters': [],
            'telemetry': []
        }

    def build_electric_motors_database(self) -> List[Dict[str, Any]]:
        """Build database of electric motors with specifications"""
        electric_motors = [
            {
                'name': 'Brushless Outrunner 2212 920KV',
                'type': 'Brushless Electric',
                'kv_rating': 920,
                'max_current': '20A',
                'max_power': '200W',
                'weight': '55g',
                'shaft_diameter': '3.17mm',
                'recommended_prop': '10x4.5',
                'voltage_range': '11.1V - 14.8V (3-4S LiPo)',
                'applications': ['Small planes', 'Quadcopters', 'Fixed-wing'],
                'price_range': '$15-$30'
            },
            {
                'name': 'Brushless Outrunner 2830 1000KV',
                'type': 'Brushless Electric',
                'kv_rating': 1000,
                'max_current': '30A',
                'max_power': '350W',
                'weight': '85g',
                'shaft_diameter': '4mm',
                'recommended_prop': '11x7',
                'voltage_range': '11.1V - 14.8V (3-4S LiPo)',
                'applications': ['Medium planes', 'Large quadcopters'],
                'price_range': '$25-$45'
            },
            {
                'name': 'High-Power Brushless 4250 500KV',
                'type': 'Brushless Electric',
                'kv_rating': 500,
                'max_current': '60A',
                'max_power': '800W',
                'weight': '180g',
                'shaft_diameter': '5mm',
                'recommended_prop': '14x8',
                'voltage_range': '14.8V - 22.2V (4-6S LiPo)',
                'applications': ['Large planes', 'Heavy-lift drones'],
                'price_range': '$60-$120'
            }
        ]

        return electric_motors

    def build_gasoline_engines_database(self) -> List[Dict[str, Any]]:
        """Build database of gasoline engines with specifications"""
        gasoline_engines = [
            {
                'name': 'DLE-20 Gasoline Engine',
                'type': 'Gasoline 2-Stroke',
                'displacement': '20cc',
                'max_power': '2.5HP @ 8000 RPM',
                'weight': '650g',
                'fuel_consumption': '400ml/hour',
                'recommended_prop': '16x6 - 18x6',
                'applications': ['Medium to large planes', 'Long-range aircraft'],
                'price_range': '$200-$300',
                'flight_time': '45-60 minutes'
            },
            {
                'name': 'DLE-30 Gasoline Engine',
                'type': 'Gasoline 2-Stroke',
                'displacement': '30cc',
                'max_power': '3.5HP @ 7500 RPM',
                'weight': '950g',
                'fuel_consumption': '550ml/hour',
                'recommended_prop': '18x8 - 20x8',
                'applications': ['Large planes', 'Heavy aircraft'],
                'price_range': '$300-$450',
                'flight_time': '60-90 minutes'
            },
            {
                'name': 'DLE-55 Gasoline Engine',
                'type': 'Gasoline 2-Stroke',
                'displacement': '55cc',
                'max_power': '6HP @ 7000 RPM',
                'weight': '1800g',
                'fuel_consumption': '800ml/hour',
                'recommended_prop': '22x10 - 24x10',
                'applications': ['Very large planes', 'Scale models'],
                'price_range': '$500-$750',
                'flight_time': '90-120 minutes'
            }
        ]

        return gasoline_engines

    def build_servos_database(self) -> List[Dict[str, Any]]:
        """Build database of servos with specifications"""
        servos = [
            {
                'name': 'Standard Servo 9g',
                'type': 'Analog',
                'torque': '1.8kg-cm @ 4.8V',
                'speed': '0.12sec/60° @ 4.8V',
                'weight': '9g',
                'voltage_range': '4.8V - 6V',
                'applications': ['Small control surfaces', 'Light aircraft'],
                'price_range': '$3-$8'
            },
            {
                'name': 'Digital Servo 20kg',
                'type': 'Digital',
                'torque': '20kg-cm @ 6V',
                'speed': '0.16sec/60° @ 6V',
                'weight': '60g',
                'voltage_range': '4.8V - 7.4V',
                'applications': ['Medium to large control surfaces', 'Retractable landing gear'],
                'price_range': '$15-$35'
            },
            {
                'name': 'High-Voltage Servo 35kg',
                'type': 'Digital High-Voltage',
                'torque': '35kg-cm @ 7.4V',
                'speed': '0.13sec/60° @ 7.4V',
                'weight': '68g',
                'voltage_range': '6V - 8.4V',
                'applications': ['Large aircraft', 'Heavy control surfaces'],
                'price_range': '$35-$70'
            }
        ]

        return servos

    def build_escs_database(self) -> List[Dict[str, Any]]:
        """Build database of ESCs (Electronic Speed Controllers)"""
        escs = [
            {
                'name': '30A Brushless ESC',
                'max_current': '30A',
                'burst_current': '40A',
                'voltage_range': '2-4S LiPo',
                'bec_output': '5V 2A',
                'weight': '25g',
                'features': ['BEC', 'Low voltage cutoff', 'Brake'],
                'price_range': '$12-$25'
            },
            {
                'name': '60A Brushless ESC',
                'max_current': '60A',
                'burst_current': '80A',
                'voltage_range': '2-6S LiPo',
                'bec_output': '5V 3A',
                'weight': '45g',
                'features': ['BEC', 'Low voltage cutoff', 'Brake', 'Programmable'],
                'price_range': '$25-$50'
            }
        ]

        return escs

    def build_optical_flow_database(self) -> List[Dict[str, Any]]:
        """Build database of optical flow sensors"""
        optical_flow = [
            {
                'name': 'PX4FLOW Optical Flow Sensor',
                'type': 'Optical Flow',
                'resolution': '752x480',
                'frame_rate': '250 FPS',
                'field_of_view': '16°',
                'weight': '20g',
                'interface': 'I2C',
                'voltage': '5V',
                'applications': ['Indoor navigation', 'Position hold', 'Precision landing'],
                'price_range': '$80-$150',
                'features': ['Sonar sensor', 'Gyroscope', 'USB interface']
            },
            {
                'name': 'Mateksys 3901-L0X Optical Flow',
                'type': 'Optical Flow',
                'resolution': '640x480',
                'frame_rate': '126 FPS',
                'field_of_view': '42°',
                'weight': '8g',
                'interface': 'I2C',
                'voltage': '3.3-5V',
                'applications': ['Indoor flight', 'Position hold', 'Low altitude'],
                'price_range': '$35-$50',
                'features': ['VL53L0X rangefinder', 'PMW3901 sensor', 'Lightweight']
            },
            {
                'name': 'Holybro PMW3901 Optical Flow',
                'type': 'Optical Flow',
                'resolution': '640x480',
                'frame_rate': '126 FPS',
                'field_of_view': '42°',
                'weight': '10g',
                'interface': 'I2C/UART',
                'voltage': '3.3-5V',
                'applications': ['Indoor navigation', 'GPS-denied environments'],
                'price_range': '$40-$60',
                'features': ['VL53L1X rangefinder', 'Plug and play', 'Ardupilot compatible']
            }
        ]

        return optical_flow

    def build_gimbals_database(self) -> List[Dict[str, Any]]:
        """Build database of camera gimbals"""
        gimbals = [
            {
                'name': '2-Axis Brushless Gimbal',
                'axes': 2,
                'max_camera_weight': '300g',
                'control': 'PWM',
                'weight': '180g',
                'tilt_range': '±90°',
                'roll_range': '±45°',
                'applications': ['GoPro', 'Small action cameras'],
                'price_range': '$50-$120',
                'features': ['Brushless motors', 'Lightweight', 'Easy installation']
            },
            {
                'name': '3-Axis Brushless Gimbal',
                'axes': 3,
                'max_camera_weight': '500g',
                'control': 'PWM/SBUS',
                'weight': '350g',
                'tilt_range': '±90°',
                'roll_range': '±45°',
                'yaw_range': '±320°',
                'applications': ['DSLR', 'Professional cameras', 'Cinema'],
                'price_range': '$150-$400',
                'features': ['Full 3-axis stabilization', 'High precision', 'Multiple control modes']
            },
            {
                'name': 'Storm32 BGC 3-Axis Gimbal',
                'axes': 3,
                'max_camera_weight': '400g',
                'control': 'PWM/SBUS/MAVLink',
                'weight': '280g',
                'tilt_range': '±90°',
                'roll_range': '±45°',
                'yaw_range': '±320°',
                'applications': ['GoPro', 'Action cameras', 'FPV'],
                'price_range': '$80-$180',
                'features': ['Storm32 controller', 'MAVLink support', 'Ardupilot integration']
            },
            {
                'name': 'Tarot T-2D Brushless Gimbal',
                'axes': 2,
                'max_camera_weight': '350g',
                'control': 'PWM',
                'weight': '200g',
                'tilt_range': '±90°',
                'roll_range': '±45°',
                'applications': ['GoPro Hero', 'Xiaomi Yi'],
                'price_range': '$60-$100',
                'features': ['Plug and play', 'Lightweight', 'Durable']
            }
        ]

        return gimbals

    def build_transmitters_database(self) -> List[Dict[str, Any]]:
        """Build database of RC transmitters"""
        transmitters = [
            {
                'name': 'FrSky Taranis X9D Plus',
                'channels': 16,
                'protocol': 'ACCST',
                'range': '1.5km',
                'telemetry': True,
                'display': 'LCD',
                'battery': '2S LiPo or 6x AA',
                'weight': '680g',
                'price_range': '$200-$250',
                'features': ['Voice alerts', 'Haptic feedback', 'SD card logging', 'Trainer port']
            },
            {
                'name': 'RadioMaster TX16S',
                'channels': 16,
                'protocol': 'Multi-protocol (ACCST, ACCESS, AFHDS, etc.)',
                'range': '2km',
                'telemetry': True,
                'display': 'Color touchscreen',
                'battery': '2S LiPo',
                'weight': '650g',
                'price_range': '$180-$220',
                'features': ['EdgeTX firmware', 'Hall sensor gimbals', 'Wireless trainer', 'USB-C']
            },
            {
                'name': 'FlySky FS-i6X',
                'channels': 10,
                'protocol': 'AFHDS 2A',
                'range': '1km',
                'telemetry': True,
                'display': 'LCD',
                'battery': '4x AA',
                'weight': '392g',
                'price_range': '$50-$70',
                'features': ['Budget friendly', 'Reliable', 'Easy to use', 'Firmware upgradable']
            },
            {
                'name': 'Spektrum DX6e',
                'channels': 6,
                'protocol': 'DSMX',
                'range': '1km',
                'telemetry': False,
                'display': 'LCD',
                'battery': '4x AA',
                'weight': '454g',
                'price_range': '$120-$150',
                'features': ['Spektrum quality', 'Simple interface', 'Reliable', 'Bind-N-Fly compatible']
            }
        ]

        return transmitters

    def build_telemetry_database(self) -> List[Dict[str, Any]]:
        """Build database of telemetry systems"""
        telemetry = [
            {
                'name': 'RFD900x Telemetry Radio',
                'frequency': '900MHz',
                'range': '40km',
                'data_rate': '250kbps',
                'power_output': '1W',
                'weight': '18g',
                'voltage': '5V',
                'interface': 'UART',
                'price_range': '$200-$280',
                'features': ['Long range', 'High data rate', 'Encryption', 'Frequency hopping']
            },
            {
                'name': 'HolyBro SiK Telemetry Radio V3',
                'frequency': '433MHz / 915MHz',
                'range': '1km',
                'data_rate': '57.6kbps',
                'power_output': '100mW',
                'weight': '15g',
                'voltage': '5V',
                'interface': 'UART',
                'price_range': '$40-$70',
                'features': ['Plug and play', 'Ardupilot compatible', 'Reliable', 'Affordable']
            },
            {
                'name': 'RFD900+ Telemetry Radio',
                'frequency': '900MHz',
                'range': '15km',
                'data_rate': '250kbps',
                'power_output': '1W',
                'weight': '20g',
                'voltage': '5V',
                'interface': 'UART',
                'price_range': '$150-$200',
                'features': ['Long range', 'Reliable', 'Frequency hopping', 'Error correction']
            },
            {
                'name': 'ESP8266 WiFi Telemetry',
                'frequency': '2.4GHz',
                'range': '100m',
                'data_rate': '1Mbps',
                'power_output': '20dBm',
                'weight': '5g',
                'voltage': '3.3V',
                'interface': 'UART',
                'price_range': '$5-$15',
                'features': ['WiFi', 'Low cost', 'Easy setup', 'Short range']
            },
            {
                'name': 'Microhard pDDL900 Telemetry',
                'frequency': '900MHz',
                'range': '60km',
                'data_rate': '230kbps',
                'power_output': '1W',
                'weight': '25g',
                'voltage': '5V',
                'interface': 'UART',
                'price_range': '$400-$600',
                'features': ['Professional grade', 'Very long range', 'Encryption', 'Reliable']
            }
        ]

        return telemetry

    def build_complete_database(self) -> Dict[str, Any]:
        """Build complete equipment database"""
        self.equipment_data['engines']['electric'] = self.build_electric_motors_database()
        self.equipment_data['engines']['gasoline'] = self.build_gasoline_engines_database()
        self.equipment_data['servos'] = self.build_servos_database()
        self.equipment_data['escs'] = self.build_escs_database()
        self.equipment_data['optical_flow'] = self.build_optical_flow_database()
        self.equipment_data['gimbals'] = self.build_gimbals_database()
        self.equipment_data['transmitters'] = self.build_transmitters_database()
        self.equipment_data['telemetry'] = self.build_telemetry_database()

        return self.equipment_data

    def save_to_json(self, filename: str = 'equipment_database.json'):
        """Save equipment database to JSON file"""
        output_path = f'/workspace/app-b6ukc6ytkow1/backend/data/{filename}'

        database = self.build_complete_database()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'equipment': database,
                'created_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                'version': '1.0'
            }, f, indent=2, ensure_ascii=False)

        print(f"Equipment database saved to {output_path}")


def main():
    builder = EquipmentDatabaseBuilder()
    builder.save_to_json()
    print("Equipment database created successfully!")


if __name__ == '__main__':
    main()
