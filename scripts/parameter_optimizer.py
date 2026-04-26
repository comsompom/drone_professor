"""
Parameter Optimizer
Analyzes and optimizes Ardupilot parameters based on aircraft specs and knowledge base
"""

import json
from typing import Dict, List, Any


class ParameterOptimizer:
    """
    Optimizes Ardupilot parameters based on aircraft specifications,
    knowledge base, and best practices
    """

    def __init__(self, knowledge_base, llm):
        self.kb = knowledge_base
        self.llm = llm

    def optimize_parameters(self,
                            aircraft_specs: Dict[str, Any],
                            current_params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze current parameters and suggest optimizations
        """
        suggestions = []

        # Analyze each parameter category
        suggestions.extend(self._optimize_battery_params(aircraft_specs, current_params))
        suggestions.extend(self._optimize_servo_params(aircraft_specs, current_params))
        suggestions.extend(self._optimize_flight_params(aircraft_specs, current_params))
        suggestions.extend(self._optimize_safety_params(aircraft_specs, current_params))

        # Get LLM analysis
        context = self._build_optimization_context(aircraft_specs, current_params, suggestions)
        llm_analysis = self.llm.generate_response(context)

        return {
            'suggestions': suggestions,
            'llm_analysis': llm_analysis,
            'total_suggestions': len(suggestions),
            'critical_count': len([s for s in suggestions if s['priority'] == 'critical']),
            'warning_count': len([s for s in suggestions if s['priority'] == 'warning'])
        }

    def _optimize_battery_params(self,
                                 aircraft_specs: Dict[str, Any],
                                 current_params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Optimize battery-related parameters"""
        suggestions = []

        # Check BATT_CAPACITY
        if 'BATT_CAPACITY' not in current_params or current_params.get('BATT_CAPACITY', 0) == 0:
            suggestions.append({
                'parameter': 'BATT_CAPACITY',
                'current_value': current_params.get('BATT_CAPACITY', 0),
                'suggested_value': 'Set to your battery mAh capacity',
                'reason': 'Battery capacity must be set for accurate remaining capacity estimation',
                'priority': 'critical',
                'category': 'Battery'
            })

        # Check BATT_MONITOR
        if current_params.get('BATT_MONITOR', 0) == 0:
            suggestions.append({
                'parameter': 'BATT_MONITOR',
                'current_value': 0,
                'suggested_value': 4,
                'reason': 'Enable battery monitoring (4 = Analog Voltage and Current)',
                'priority': 'critical',
                'category': 'Battery'
            })

        # Check low voltage threshold
        weight = aircraft_specs.get('weight', 0)
        if weight > 0:
            # Suggest appropriate low voltage based on battery type
            suggested_low_volt = 10.5  # 3S LiPo
            if current_params.get('BATT_LOW_VOLT', 0) < 10.0:
                suggestions.append({
                    'parameter': 'BATT_LOW_VOLT',
                    'current_value': current_params.get('BATT_LOW_VOLT', 0),
                    'suggested_value': suggested_low_volt,
                    'reason': 'Low voltage threshold too low, may damage battery',
                    'priority': 'warning',
                    'category': 'Battery'
                })

        return suggestions

    def _optimize_servo_params(self,
                               aircraft_specs: Dict[str, Any],
                               current_params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Optimize servo-related parameters"""
        suggestions = []

        # Check servo function assignments
        critical_servos = ['SERVO1_FUNCTION', 'SERVO2_FUNCTION', 'SERVO3_FUNCTION', 'SERVO4_FUNCTION']

        for servo in critical_servos:
            if servo not in current_params or current_params.get(servo, 0) == 0:
                suggestions.append({
                    'parameter': servo,
                    'current_value': current_params.get(servo, 0),
                    'suggested_value': 'Assign control surface function',
                    'reason': f'{servo} not assigned. Assign to aileron, elevator, throttle, or rudder',
                    'priority': 'critical',
                    'category': 'Servo'
                })

        # Check servo limits
        for i in range(1, 5):
            min_param = f'SERVO{i}_MIN'
            max_param = f'SERVO{i}_MAX'

            if min_param in current_params and max_param in current_params:
                min_val = current_params[min_param]
                max_val = current_params[max_param]

                if max_val - min_val < 500:
                    suggestions.append({
                        'parameter': f'SERVO{i}_MIN/MAX',
                        'current_value': f'{min_val}/{max_val}',
                        'suggested_value': '1000/2000',
                        'reason': 'Servo range too narrow, may limit control authority',
                        'priority': 'warning',
                        'category': 'Servo'
                    })

        return suggestions

    def _optimize_flight_params(self,
                                aircraft_specs: Dict[str, Any],
                                current_params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Optimize flight performance parameters"""
        suggestions = []

        weight = aircraft_specs.get('weight', 0)
        wingspan = aircraft_specs.get('wingspan', 0)

        # Estimate appropriate cruise speed based on aircraft size
        if wingspan > 0:
            # Rough estimate: larger wingspan = slower cruise speed
            estimated_cruise_speed = 12 + (wingspan * 2)  # m/s
            estimated_cruise_cm = int(estimated_cruise_speed * 100)

            current_cruise = current_params.get('TRIM_ARSPD_CM', 0)

            if abs(current_cruise - estimated_cruise_cm) > 300:
                suggestions.append({
                    'parameter': 'TRIM_ARSPD_CM',
                    'current_value': current_cruise,
                    'suggested_value': estimated_cruise_cm,
                    'reason': f'Cruise speed may be suboptimal for {wingspan}m wingspan aircraft',
                    'priority': 'info',
                    'category': 'Flight Performance'
                })

        # Check throttle settings
        if current_params.get('THR_MAX', 100) == 100:
            suggestions.append({
                'parameter': 'THR_MAX',
                'current_value': 100,
                'suggested_value': 75,
                'reason': 'Consider limiting max throttle to 75% for initial flights',
                'priority': 'info',
                'category': 'Flight Performance'
            })

        # Check airspeed sensor
        if current_params.get('ARSPD_TYPE', 0) == 0:
            suggestions.append({
                'parameter': 'ARSPD_TYPE',
                'current_value': 0,
                'suggested_value': 'Set based on your airspeed sensor',
                'reason': 'Airspeed sensor not configured. Highly recommended for fixed-wing',
                'priority': 'warning',
                'category': 'Sensors'
            })

        return suggestions

    def _optimize_safety_params(self,
                                aircraft_specs: Dict[str, Any],
                                current_params: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Optimize safety-related parameters"""
        suggestions = []

        # Check RTL altitude
        if current_params.get('ALT_HOLD_RTL', 0) < 50:
            suggestions.append({
                'parameter': 'ALT_HOLD_RTL',
                'current_value': current_params.get('ALT_HOLD_RTL', 0),
                'suggested_value': 100,
                'reason': 'RTL altitude too low, increase for safety',
                'priority': 'critical',
                'category': 'Safety'
            })

        # Check geofence
        if current_params.get('FENCE_ENABLE', 0) == 0:
            suggestions.append({
                'parameter': 'FENCE_ENABLE',
                'current_value': 0,
                'suggested_value': 1,
                'reason': 'Enable geofence for safety',
                'priority': 'warning',
                'category': 'Safety'
            })

        # Check failsafe settings
        if current_params.get('FS_SHORT_ACTN', 0) == 0:
            suggestions.append({
                'parameter': 'FS_SHORT_ACTN',
                'current_value': 0,
                'suggested_value': 1,
                'reason': 'Configure short failsafe action (1=RTL recommended)',
                'priority': 'critical',
                'category': 'Safety'
            })

        return suggestions

    def _build_optimization_context(self,
                                    aircraft_specs: Dict[str, Any],
                                    current_params: Dict[str, Any],
                                    suggestions: List[Dict[str, Any]]) -> str:
        """Build context for LLM analysis"""
        context = f"""Analyze these Ardupilot parameter optimization suggestions:

Aircraft Specifications:
{json.dumps(aircraft_specs, indent=2)}

Current Parameters (sample):
{json.dumps(dict(list(current_params.items())[:10]), indent=2)}

Optimization Suggestions:
{json.dumps(suggestions, indent=2)}

Provide a summary of the most critical changes and explain why they are important for this aircraft."""

        return context

    def rate_equipment(self, equipment: Dict[str, Any], aircraft_specs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Rate equipment suitability for aircraft
        """
        weight = aircraft_specs.get('weight', 0)
        wingspan = aircraft_specs.get('wingspan', 0)

        rating = {
            'weight_match': 0,
            'power_match': 0,
            'size_match': 0,
            'price_rating': 0,
            'overall_score': 0
        }

        # Rate based on equipment type
        if 'kv_rating' in equipment:  # Electric motor
            # Lower KV for larger aircraft
            ideal_kv = 1500 - (weight * 100)
            kv_diff = abs(equipment.get('kv_rating', 0) - ideal_kv)
            rating['power_match'] = max(0, 100 - (kv_diff / 10))

        if 'torque' in equipment:  # Servo
            # Extract torque value (e.g., "20kg-cm" -> 20)
            torque_str = equipment.get('torque', '0')
            torque = float(''.join(filter(str.isdigit, torque_str.split('kg')[0])))

            # Heavier aircraft need more torque
            ideal_torque = weight * 5
            torque_diff = abs(torque - ideal_torque)
            rating['power_match'] = max(0, 100 - (torque_diff * 2))

        # Weight rating
        equipment_weight_str = equipment.get('weight', '0g')
        equipment_weight = float(''.join(filter(str.isdigit, equipment_weight_str.split('g')[0]))) / 1000

        # Lighter is better, but must be strong enough
        if equipment_weight < weight * 0.1:
            rating['weight_match'] = 80
        else:
            rating['weight_match'] = 50

        # Price rating (lower is better)
        price_range = equipment.get('price_range', '$0-$0')
        avg_price = self._extract_average_price(price_range)

        if avg_price < 50:
            rating['price_rating'] = 100
        elif avg_price < 100:
            rating['price_rating'] = 80
        elif avg_price < 200:
            rating['price_rating'] = 60
        else:
            rating['price_rating'] = 40

        # Calculate overall score
        rating['overall_score'] = (
                rating['weight_match'] * 0.2 +
                rating['power_match'] * 0.4 +
                rating['price_rating'] * 0.4
        )

        return rating

    def _extract_average_price(self, price_range: str) -> float:
        """Extract average price from price range string"""
        try:
            # Extract numbers from "$15-$30" format
            prices = [float(p.strip('$')) for p in price_range.split('-')]
            return sum(prices) / len(prices)
        except:
            return 0


def main():
    """Test parameter optimizer"""
    print("=== Parameter Optimizer Test ===\n")

    # This would normally use real knowledge base and LLM
    print("Parameter optimizer requires knowledge base and LLM integration.")
    print("Use through Flask API for full functionality.")


if __name__ == '__main__':
    main()
