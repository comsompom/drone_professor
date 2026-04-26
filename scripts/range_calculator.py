"""
Range Calculator
Calculates flight range based on aircraft specifications and power system
"""

import math
from typing import Dict, Any


class RangeCalculator:
    """
    Calculates flight range for electric and gasoline-powered aircraft
    """

    def __init__(self):
        # Constants
        self.AIR_DENSITY = 1.225  # kg/m³ at sea level
        self.GRAVITY = 9.81  # m/s²

        # Efficiency factors
        self.ELECTRIC_MOTOR_EFFICIENCY = 0.85
        self.GASOLINE_ENGINE_EFFICIENCY = 0.25
        self.PROPELLER_EFFICIENCY = 0.75

        # Energy densities
        self.LIPO_ENERGY_DENSITY = 150  # Wh/kg
        self.GASOLINE_ENERGY_DENSITY = 12000  # Wh/kg

    def calculate_range(self, aircraft_specs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Calculate flight range based on aircraft specifications
        """
        engine_type = aircraft_specs.get('engine_type', 'electric')

        if engine_type == 'electric':
            return self._calculate_electric_range(aircraft_specs)
        elif engine_type == 'gasoline':
            return self._calculate_gasoline_range(aircraft_specs)
        else:
            return {'error': 'Unknown engine type'}

    def _calculate_electric_range(self, specs: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate range for electric aircraft"""
        weight = specs.get('weight', 0)  # kg
        wingspan = specs.get('wingspan', 0)  # m
        battery_capacity = specs.get('battery_capacity', 0)  # mAh
        battery_voltage = specs.get('battery_voltage', 11.1)  # V (default 3S)
        cruise_speed = specs.get('cruise_speed', 15)  # m/s

        if weight == 0 or wingspan == 0 or battery_capacity == 0:
            return {'error': 'Insufficient specifications'}

        # Calculate battery energy
        battery_wh = (battery_capacity / 1000) * battery_voltage
        usable_energy = battery_wh * 0.8  # 80% usable capacity for safety

        # Estimate power required for cruise flight
        # Simplified drag model
        wing_area = wingspan * wingspan * 0.5  # Rough estimate
        drag_coefficient = 0.03  # Typical for small aircraft

        # Drag force
        drag = 0.5 * self.AIR_DENSITY * cruise_speed ** 2 * wing_area * drag_coefficient

        # Power required (drag * speed)
        power_required = drag * cruise_speed

        # Account for inefficiencies
        total_power = power_required / (self.ELECTRIC_MOTOR_EFFICIENCY * self.PROPELLER_EFFICIENCY)

        # Flight time
        flight_time_hours = usable_energy / total_power if total_power > 0 else 0
        flight_time_minutes = flight_time_hours * 60

        # Range
        range_km = (cruise_speed * flight_time_hours * 3.6)  # Convert m/s to km/h
        range_m = cruise_speed * flight_time_hours * 3600

        return {
            'engine_type': 'electric',
            'range_km': round(range_km, 2),
            'range_m': round(range_m, 2),
            'flight_time_minutes': round(flight_time_minutes, 1),
            'battery_energy_wh': round(battery_wh, 2),
            'usable_energy_wh': round(usable_energy, 2),
            'estimated_power_w': round(total_power, 2),
            'cruise_speed_ms': cruise_speed,
            'cruise_speed_kmh': round(cruise_speed * 3.6, 1),
            'safety_margin': '20% reserve included',
            'coordinates': self._generate_range_circle(range_m)
        }

    def _calculate_gasoline_range(self, specs: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate range for gasoline aircraft"""
        weight = specs.get('weight', 0)  # kg
        wingspan = specs.get('wingspan', 0)  # m
        fuel_capacity = specs.get('fuel_capacity', 0)  # liters
        cruise_speed = specs.get('cruise_speed', 15)  # m/s

        if weight == 0 or wingspan == 0 or fuel_capacity == 0:
            return {'error': 'Insufficient specifications'}

        # Gasoline properties
        gasoline_density = 0.75  # kg/L
        fuel_weight = fuel_capacity * gasoline_density

        # Energy available
        fuel_energy_wh = fuel_weight * self.GASOLINE_ENERGY_DENSITY
        usable_energy = fuel_energy_wh * 0.9  # 90% usable

        # Estimate power required
        wing_area = wingspan * wingspan * 0.5
        drag_coefficient = 0.03

        drag = 0.5 * self.AIR_DENSITY * cruise_speed ** 2 * wing_area * drag_coefficient
        power_required = drag * cruise_speed

        # Account for inefficiencies
        total_power = power_required / (self.GASOLINE_ENGINE_EFFICIENCY * self.PROPELLER_EFFICIENCY)

        # Flight time
        flight_time_hours = usable_energy / total_power if total_power > 0 else 0
        flight_time_minutes = flight_time_hours * 60

        # Range
        range_km = cruise_speed * flight_time_hours * 3.6
        range_m = cruise_speed * flight_time_hours * 3600

        # Fuel consumption
        fuel_consumption_lh = fuel_capacity / flight_time_hours if flight_time_hours > 0 else 0

        return {
            'engine_type': 'gasoline',
            'range_km': round(range_km, 2),
            'range_m': round(range_m, 2),
            'flight_time_minutes': round(flight_time_minutes, 1),
            'fuel_capacity_l': fuel_capacity,
            'fuel_energy_wh': round(fuel_energy_wh, 2),
            'fuel_consumption_lh': round(fuel_consumption_lh, 2),
            'estimated_power_w': round(total_power, 2),
            'cruise_speed_ms': cruise_speed,
            'cruise_speed_kmh': round(cruise_speed * 3.6, 1),
            'safety_margin': '10% reserve included',
            'coordinates': self._generate_range_circle(range_m)
        }

    def _generate_range_circle(self, range_m: float, center_lat: float = 37.7749,
                               center_lon: float = -122.4194, num_points: int = 64) -> list:
        """
        Generate coordinates for range circle on map
        """
        # Earth radius in meters
        earth_radius = 6371000

        coordinates = []

        for i in range(num_points + 1):
            angle = (2 * math.pi * i) / num_points

            # Calculate offset in degrees
            lat_offset = (range_m / earth_radius) * (180 / math.pi) * math.cos(angle)
            lon_offset = (range_m / earth_radius) * (180 / math.pi) * math.sin(angle) / math.cos(
                center_lat * math.pi / 180)

            coordinates.append({
                'lat': center_lat + lat_offset,
                'lon': center_lon + lon_offset
            })

        return coordinates

    def compare_power_systems(self, specs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compare electric vs gasoline for given aircraft
        """
        # Calculate for electric
        electric_specs = {**specs, 'engine_type': 'electric'}
        electric_range = self._calculate_electric_range(electric_specs)

        # Calculate for gasoline
        gasoline_specs = {**specs, 'engine_type': 'gasoline'}
        gasoline_range = self._calculate_gasoline_range(gasoline_specs)

        return {
            'electric': electric_range,
            'gasoline': gasoline_range,
            'comparison': {
                'range_advantage': 'gasoline' if gasoline_range.get('range_km', 0) > electric_range.get('range_km',
                                                                                                        0) else 'electric',
                'flight_time_advantage': 'gasoline' if gasoline_range.get('flight_time_minutes',
                                                                          0) > electric_range.get('flight_time_minutes',
                                                                                                  0) else 'electric',
                'weight_advantage': 'electric',  # Electric typically lighter
                'cost_advantage': 'electric',  # Electric typically cheaper to operate
                'maintenance_advantage': 'electric'  # Electric has less maintenance
            }
        }


def main():
    """Test range calculator"""
    print("=== Range Calculator Test ===\n")

    calculator = RangeCalculator()

    # Test electric aircraft
    electric_specs = {
        'weight': 3.5,
        'wingspan': 1.8,
        'engine_type': 'electric',
        'battery_capacity': 5000,  # mAh
        'battery_voltage': 14.8,  # 4S
        'cruise_speed': 15
    }

    print("Electric Aircraft Range:")
    electric_range = calculator.calculate_range(electric_specs)
    print(f"  Range: {electric_range.get('range_km')} km")
    print(f"  Flight Time: {electric_range.get('flight_time_minutes')} minutes")
    print(f"  Power Required: {electric_range.get('estimated_power_w')} W")

    # Test gasoline aircraft
    print("\nGasoline Aircraft Range:")
    gasoline_specs = {
        'weight': 5.0,
        'wingspan': 2.0,
        'engine_type': 'gasoline',
        'fuel_capacity': 1.5,  # liters
        'cruise_speed': 18
    }

    gasoline_range = calculator.calculate_range(gasoline_specs)
    print(f"  Range: {gasoline_range.get('range_km')} km")
    print(f"  Flight Time: {gasoline_range.get('flight_time_minutes')} minutes")
    print(f"  Fuel Consumption: {gasoline_range.get('fuel_consumption_lh')} L/h")


if __name__ == '__main__':
    main()
