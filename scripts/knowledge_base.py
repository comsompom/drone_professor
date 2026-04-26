"""
Knowledge Base Manager
Manages the Ardupilot knowledge base including parameters, hardware, and equipment
"""

import json
import os
from typing import Dict, List, Any, Optional


class KnowledgeBase:
    def __init__(self, data_dir: str = '/workspace/app-b6ukc6ytkow1/backend/data'):
        self.data_dir = data_dir
        self.parameters = []
        self.hardware = []
        self.equipment = {}
        self.load_all_data()

    def load_all_data(self):
        """Load all knowledge base data from JSON files"""
        try:
            # Load parameters
            params_file = os.path.join(self.data_dir, 'ardupilot_parameters.json')
            if os.path.exists(params_file):
                with open(params_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.parameters = data.get('parameters', [])
                print(f"Loaded {len(self.parameters)} parameters")

            # Load hardware
            hardware_file = os.path.join(self.data_dir, 'ardupilot_hardware.json')
            if os.path.exists(hardware_file):
                with open(hardware_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.hardware = data.get('hardware', [])
                print(f"Loaded {len(self.hardware)} hardware items")

            # Load equipment
            equipment_file = os.path.join(self.data_dir, 'equipment_database.json')
            if os.path.exists(equipment_file):
                with open(equipment_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.equipment = data.get('equipment', {})
                print(f"Loaded equipment database")

        except Exception as e:
            print(f"Error loading knowledge base: {e}")

    def search_parameters(self, query: str, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search parameters by name or description"""
        query_lower = query.lower()
        results = []

        for param in self.parameters:
            # Check category filter
            if category and param.get('category', '').lower() != category.lower():
                continue

            # Search in name and description
            if (query_lower in param.get('name', '').lower() or
                    query_lower in param.get('description', '').lower()):
                results.append(param)

        return results

    def get_parameter_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get specific parameter by exact name"""
        for param in self.parameters:
            if param.get('name', '').upper() == name.upper():
                return param
        return None

    def get_parameters_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get all parameters in a category"""
        return [p for p in self.parameters if p.get('category', '').lower() == category.lower()]

    def search_hardware(self, query: str, category: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search hardware by name or description"""
        query_lower = query.lower()
        results = []

        for hw in self.hardware:
            # Check category filter
            if category and hw.get('category', '').lower() != category.lower():
                continue

            # Search in name and description
            if (query_lower in hw.get('name', '').lower() or
                    query_lower in hw.get('description', '').lower()):
                results.append(hw)

        return results

    def get_hardware_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Get all hardware in a category"""
        return [h for h in self.hardware if h.get('category', '').lower() == category.lower()]

    def search_equipment(self, equipment_type: str, query: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Search equipment by type and optional query
        Types: electric, gasoline, servos, escs, optical_flow, gimbals, transmitters, telemetry
        """
        results = []

        # Handle nested structure for engines
        if equipment_type in ['electric', 'gasoline']:
            equipment_list = self.equipment.get('engines', {}).get(equipment_type, [])
        else:
            equipment_list = self.equipment.get(equipment_type, [])

        if not query:
            return equipment_list

        query_lower = query.lower()
        for item in equipment_list:
            # Search in name and other fields
            item_str = json.dumps(item).lower()
            if query_lower in item_str:
                results.append(item)

        return results

    def get_all_categories(self) -> Dict[str, List[str]]:
        """Get all available categories"""
        param_categories = list(set(p.get('category', 'General') for p in self.parameters))
        hardware_categories = list(set(h.get('category', 'Other') for h in self.hardware))
        equipment_categories = list(self.equipment.keys())

        return {
            'parameters': sorted(param_categories),
            'hardware': sorted(hardware_categories),
            'equipment': sorted(equipment_categories)
        }

    def get_statistics(self) -> Dict[str, Any]:
        """Get knowledge base statistics"""
        return {
            'total_parameters': len(self.parameters),
            'total_hardware': len(self.hardware),
            'equipment_types': len(self.equipment),
            'parameter_categories': len(set(p.get('category') for p in self.parameters)),
            'hardware_categories': len(set(h.get('category') for h in self.hardware))
        }

    def recommend_hardware_for_aircraft(self, aircraft_specs: Dict[str, Any]) -> Dict[str, Any]:
        """
        Recommend hardware based on aircraft specifications
        """
        weight = aircraft_specs.get('weight', 0)  # in kg
        wingspan = aircraft_specs.get('wingspan', 0)  # in meters

        recommendations = {
            'flight_controller': [],
            'motor': [],
            'servos': [],
            'esc': [],
            'telemetry': [],
            'additional': []
        }

        # Recommend flight controllers (from hardware)
        flight_controllers = self.get_hardware_by_category('Flight Controller')
        recommendations['flight_controller'] = flight_controllers[:3] if flight_controllers else []

        # Recommend motors based on weight
        if weight < 2:  # Small aircraft
            motors = self.search_equipment('electric', '920KV')
        elif weight < 5:  # Medium aircraft
            motors = self.search_equipment('electric', '1000KV')
        else:  # Large aircraft
            motors = self.search_equipment('electric', '500KV')

        recommendations['motor'] = motors

        # Recommend servos based on weight
        if weight < 2:
            servos = self.search_equipment('servos', '9g')
        elif weight < 5:
            servos = self.search_equipment('servos', '20kg')
        else:
            servos = self.search_equipment('servos', '35kg')

        recommendations['servos'] = servos

        # Recommend ESC based on motor
        if weight < 2:
            escs = self.search_equipment('escs', '30A')
        else:
            escs = self.search_equipment('escs', '60A')

        recommendations['esc'] = escs

        # Recommend telemetry
        telemetry = self.search_equipment('telemetry')
        recommendations['telemetry'] = telemetry

        return recommendations

    def recommend_parameters_for_aircraft(self, aircraft_specs: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Recommend parameter configurations based on aircraft specifications
        """
        recommendations = []

        weight = aircraft_specs.get('weight', 0)
        wingspan = aircraft_specs.get('wingspan', 0)

        # Get critical parameters for configuration
        critical_categories = ['ARSPD', 'BATT', 'SERVO', 'RC', 'THR', 'TRIM']

        for category in critical_categories:
            params = self.get_parameters_by_category(category)
            recommendations.extend(params)

        return recommendations


def main():
    """Test the knowledge base"""
    kb = KnowledgeBase()

    print("\n=== Knowledge Base Statistics ===")
    stats = kb.get_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n=== Available Categories ===")
    categories = kb.get_all_categories()
    for cat_type, cat_list in categories.items():
        print(f"{cat_type}: {', '.join(cat_list[:5])}...")

    print("\n=== Test Aircraft Recommendations ===")
    test_aircraft = {
        'model': 'Test Plane',
        'weight': 3.5,
        'wingspan': 1.8
    }

    recommendations = kb.recommend_hardware_for_aircraft(test_aircraft)
    print(f"Recommended motors: {len(recommendations['motor'])}")
    print(f"Recommended servos: {len(recommendations['servos'])}")


if __name__ == '__main__':
    main()
Got