"""
Project Builder
Generates comprehensive build documentation for drone/aircraft projects
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime


class ProjectBuilder:
    """
    Builds complete project documentation including:
    - Equipment list with prices
    - Connection diagrams
    - Step-by-step assembly guide
    - Ardupilot setup instructions
    """

    def __init__(self, knowledge_base):
        self.kb = knowledge_base
        self.output_dir = '/workspace/app-b6ukc6ytkow1/backend/exports'
        os.makedirs(self.output_dir, exist_ok=True)

    def build_project(self,
                      aircraft_specs: Dict[str, Any],
                      selected_hardware: Dict[str, Any],
                      parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Build complete project documentation
        """
        project = {
            'metadata': {
                'project_name': f"{aircraft_specs.get('model', 'Custom')} Build",
                'created_at': datetime.now().isoformat(),
                'aircraft_type': 'Fixed-Wing',
                'specifications': aircraft_specs
            },
            'equipment_list': self._build_equipment_list(selected_hardware),
            'total_cost': self._calculate_total_cost(selected_hardware),
            'connection_diagram': self._generate_connection_guide(selected_hardware),
            'assembly_steps': self._generate_assembly_steps(aircraft_specs, selected_hardware),
            'ardupilot_setup': self._generate_ardupilot_setup(parameters),
            'safety_checklist': self._generate_safety_checklist(),
            'flight_test_plan': self._generate_flight_test_plan()
        }

        return project

    def _build_equipment_list(self, hardware: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Build detailed equipment list with specifications"""
        equipment_list = []

        for category, items in hardware.items():
            if isinstance(items, list):
                for item in items:
                    equipment_list.append({
                        'category': category,
                        'name': item.get('name', 'Unknown'),
                        'specifications': item.get('specifications', {}),
                        'quantity': 1,
                        'price_range': item.get('price_range', 'N/A'),
                        'notes': item.get('description', '')[:100]
                    })

        return equipment_list

    def _calculate_total_cost(self, hardware: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate total project cost"""
        min_cost = 0
        max_cost = 0

        for category, items in hardware.items():
            if isinstance(items, list):
                for item in items:
                    price_range = item.get('price_range', '$0-$0')
                    try:
                        prices = [float(p.strip('$')) for p in price_range.split('-')]
                        min_cost += min(prices)
                        max_cost += max(prices)
                    except:
                        pass

        return {
            'min_cost': round(min_cost, 2),
            'max_cost': round(max_cost, 2),
            'average_cost': round((min_cost + max_cost) / 2, 2),
            'currency': 'USD'
        }

    def _generate_connection_guide(self, hardware: Dict[str, Any]) -> Dict[str, Any]:
        """Generate connection diagram guide"""
        return {
            'overview': 'Connection diagram for all components',
            'connections': [
                {
                    'from': 'Flight Controller',
                    'to': 'ESC',
                    'connection': 'PWM Signal Wire',
                    'pin': 'MAIN OUT 3',
                    'notes': 'Connect ESC signal wire to throttle output'
                },
                {
                    'from': 'Flight Controller',
                    'to': 'Servo 1 (Aileron)',
                    'connection': 'PWM Signal',
                    'pin': 'MAIN OUT 1',
                    'notes': 'Right aileron servo'
                },
                {
                    'from': 'Flight Controller',
                    'to': 'Servo 2 (Elevator)',
                    'connection': 'PWM Signal',
                    'pin': 'MAIN OUT 2',
                    'notes': 'Elevator servo'
                },
                {
                    'from': 'Flight Controller',
                    'to': 'Servo 4 (Rudder)',
                    'connection': 'PWM Signal',
                    'pin': 'MAIN OUT 4',
                    'notes': 'Rudder servo'
                },
                {
                    'from': 'Battery',
                    'to': 'Power Module',
                    'connection': 'XT60 Connector',
                    'notes': 'Main power connection'
                },
                {
                    'from': 'Power Module',
                    'to': 'Flight Controller',
                    'connection': '6-pin Power Cable',
                    'notes': 'Provides power and voltage/current sensing'
                },
                {
                    'from': 'Power Module',
                    'to': 'ESC',
                    'connection': 'XT60 Connector',
                    'notes': 'Motor power'
                },
                {
                    'from': 'RC Receiver',
                    'to': 'Flight Controller',
                    'connection': 'SBUS/PPM',
                    'pin': 'RC IN',
                    'notes': 'RC control input'
                },
                {
                    'from': 'GPS Module',
                    'to': 'Flight Controller',
                    'connection': 'GPS Port',
                    'notes': 'GPS and compass data'
                },
                {
                    'from': 'Telemetry Radio',
                    'to': 'Flight Controller',
                    'connection': 'TELEM Port',
                    'notes': 'Ground station communication'
                }
            ],
            'power_distribution': {
                'battery': '3S-4S LiPo',
                'flight_controller': '5V from power module',
                'servos': '5V from flight controller servo rail or BEC',
                'motor': 'Direct from battery through ESC'
            },
            'wiring_tips': [
                'Use appropriate wire gauge for current requirements',
                'Keep signal wires away from power wires to reduce interference',
                'Use heat shrink tubing for all solder connections',
                'Label all wires for easy troubleshooting',
                'Test continuity before powering on'
            ]
        }

    def _generate_assembly_steps(self,
                                 aircraft_specs: Dict[str, Any],
                                 hardware: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate step-by-step assembly guide"""
        return [
            {
                'step': 1,
                'title': 'Prepare Airframe',
                'description': 'Assemble the aircraft airframe according to manufacturer instructions',
                'tasks': [
                    'Assemble fuselage',
                    'Attach wings',
                    'Install landing gear',
                    'Check all structural connections'
                ],
                'tools_required': ['Screwdriver', 'Allen keys', 'CA glue'],
                'estimated_time': '2-3 hours'
            },
            {
                'step': 2,
                'title': 'Install Flight Controller',
                'description': 'Mount flight controller in center of aircraft',
                'tasks': [
                    'Find center of gravity location',
                    'Mount flight controller with vibration dampening',
                    'Ensure arrow points forward',
                    'Secure with foam tape or rubber standoffs'
                ],
                'tools_required': ['Double-sided foam tape', 'Velcro straps'],
                'estimated_time': '30 minutes'
            },
            {
                'step': 3,
                'title': 'Install Motor and ESC',
                'description': 'Mount motor and connect ESC',
                'tasks': [
                    'Mount motor to motor mount',
                    'Connect motor wires to ESC',
                    'Secure ESC in airframe',
                    'Connect ESC signal wire to flight controller'
                ],
                'tools_required': ['Screwdriver', 'Soldering iron', 'Heat shrink'],
                'estimated_time': '1 hour'
            },
            {
                'step': 4,
                'title': 'Install Servos',
                'description': 'Install and connect control surface servos',
                'tasks': [
                    'Install aileron servos in wings',
                    'Install elevator servo',
                    'Install rudder servo',
                    'Connect all servos to flight controller',
                    'Test servo movement direction'
                ],
                'tools_required': ['Screwdriver', 'Servo arms'],
                'estimated_time': '1-2 hours'
            },
            {
                'step': 5,
                'title': 'Install Power System',
                'description': 'Install battery, power module, and wiring',
                'tasks': [
                    'Mount power module',
                    'Connect battery to power module',
                    'Connect power module to flight controller',
                    'Secure battery compartment',
                    'Install power switch (optional)'
                ],
                'tools_required': ['Velcro straps', 'Wire ties'],
                'estimated_time': '45 minutes'
            },
            {
                'step': 6,
                'title': 'Install GPS and Compass',
                'description': 'Mount GPS module on top of aircraft',
                'tasks': [
                    'Mount GPS on mast or top of fuselage',
                    'Ensure clear view of sky',
                    'Orient arrow forward',
                    'Connect to flight controller GPS port',
                    'Secure cable'
                ],
                'tools_required': ['Mast', 'Foam tape'],
                'estimated_time': '30 minutes'
            },
            {
                'step': 7,
                'title': 'Install RC Receiver',
                'description': 'Install and connect RC receiver',
                'tasks': [
                    'Mount receiver in fuselage',
                    'Connect to flight controller RC IN',
                    'Bind receiver to transmitter',
                    'Test RC connection'
                ],
                'tools_required': ['Foam tape'],
                'estimated_time': '30 minutes'
            },
            {
                'step': 8,
                'title': 'Install Telemetry Radio',
                'description': 'Install telemetry for ground station',
                'tasks': [
                    'Mount telemetry radio',
                    'Connect to TELEM port',
                    'Install antenna',
                    'Test connection with ground station'
                ],
                'tools_required': ['Foam tape'],
                'estimated_time': '20 minutes'
            },
            {
                'step': 9,
                'title': 'Final Wiring Check',
                'description': 'Verify all connections',
                'tasks': [
                    'Check all power connections',
                    'Verify all signal connections',
                    'Secure loose wires',
                    'Test for shorts with multimeter',
                    'Take photos for reference'
                ],
                'tools_required': ['Multimeter', 'Wire ties'],
                'estimated_time': '30 minutes'
            },
            {
                'step': 10,
                'title': 'Configure Ardupilot',
                'description': 'Set up Ardupilot parameters',
                'tasks': [
                    'Connect to Mission Planner',
                    'Load firmware',
                    'Run initial setup wizard',
                    'Configure parameters',
                    'Calibrate sensors'
                ],
                'tools_required': ['Computer', 'USB cable', 'Mission Planner'],
                'estimated_time': '2-3 hours'
            }
        ]

    def _generate_ardupilot_setup(self, parameters: Dict[str, Any]) -> Dict[str, Any]:
        """Generate Ardupilot setup instructions"""
        return {
            'overview': 'Complete Ardupilot configuration guide',
            'steps': [
                {
                    'phase': 'Initial Setup',
                    'tasks': [
                        'Install Mission Planner on computer',
                        'Connect flight controller via USB',
                        'Install Ardupilot firmware (Plane)',
                        'Run Mandatory Hardware setup wizard'
                    ]
                },
                {
                    'phase': 'Sensor Calibration',
                    'tasks': [
                        'Calibrate accelerometer (level calibration)',
                        'Calibrate compass',
                        'Calibrate RC radio',
                        'Set servo output functions',
                        'Calibrate airspeed sensor (if installed)'
                    ]
                },
                {
                    'phase': 'Parameter Configuration',
                    'tasks': [
                        'Set ARSPD_TYPE for airspeed sensor',
                        'Configure BATT_CAPACITY and BATT_MONITOR',
                        'Set SERVO functions for control surfaces',
                        'Configure THR_MIN, THR_MAX, THR_CRUISE',
                        'Set TRIM_ARSPD_CM for cruise speed',
                        'Configure RTL_ALTITUDE',
                        'Enable FENCE if desired'
                    ]
                },
                {
                    'phase': 'Flight Modes',
                    'tasks': [
                        'Configure flight mode switch',
                        'Set up MANUAL mode',
                        'Set up FBWA (Fly-By-Wire A)',
                        'Set up AUTO mode',
                        'Set up RTL (Return to Launch)',
                        'Test mode switching'
                    ]
                },
                {
                    'phase': 'Safety Configuration',
                    'tasks': [
                        'Set failsafe actions',
                        'Configure geofence',
                        'Set battery failsafe thresholds',
                        'Configure RC failsafe',
                        'Test all failsafes on ground'
                    ]
                }
            ],
            'critical_parameters': [
                {'name': 'ARSPD_TYPE', 'value': 'Set based on sensor', 'priority': 'High'},
                {'name': 'BATT_CAPACITY', 'value': 'Battery mAh', 'priority': 'High'},
                {'name': 'SERVO1_FUNCTION', 'value': '4 (Aileron)', 'priority': 'Critical'},
                {'name': 'SERVO2_FUNCTION', 'value': '19 (Elevator)', 'priority': 'Critical'},
                {'name': 'SERVO3_FUNCTION', 'value': '70 (Throttle)', 'priority': 'Critical'},
                {'name': 'SERVO4_FUNCTION', 'value': '21 (Rudder)', 'priority': 'Critical'},
                {'name': 'THR_MAX', 'value': '75', 'priority': 'High'},
                {'name': 'RTL_ALTITUDE', 'value': '100', 'priority': 'High'}
            ]
        }

    def _generate_safety_checklist(self) -> List[Dict[str, Any]]:
        """Generate pre-flight safety checklist"""
        return [
            {
                'category': 'Pre-Flight Checks',
                'items': [
                    'Battery fully charged',
                    'All connections secure',
                    'Propeller secure and undamaged',
                    'Control surfaces move correctly',
                    'GPS lock acquired (6+ satellites)',
                    'Compass calibrated and healthy',
                    'RC link established',
                    'Telemetry link established',
                    'Flight modes tested',
                    'Failsafes configured and tested'
                ]
            },
            {
                'category': 'Range Test',
                'items': [
                    'Perform RC range test',
                    'Walk 50m away with transmitter',
                    'Verify control response',
                    'Check telemetry range'
                ]
            },
            {
                'category': 'Launch Preparation',
                'items': [
                    'Clear flight area',
                    'Check wind conditions',
                    'Set appropriate flight mode',
                    'Arm aircraft',
                    'Verify motor response',
                    'Launch into wind'
                ]
            }
        ]

    def _generate_flight_test_plan(self) -> Dict[str, Any]:
        """Generate flight test plan"""
        return {
            'overview': 'Progressive flight test plan for new aircraft',
            'tests': [
                {
                    'test': 1,
                    'name': 'Ground Tests',
                    'objectives': [
                        'Verify all systems functional',
                        'Test RC range',
                        'Check servo movements',
                        'Verify motor response'
                    ],
                    'success_criteria': 'All systems respond correctly'
                },
                {
                    'test': 2,
                    'name': 'First Flight - Manual Mode',
                    'objectives': [
                        'Hand launch',
                        'Verify aircraft flies straight',
                        'Test control response',
                        'Check trim settings',
                        'Safe landing'
                    ],
                    'duration': '5 minutes',
                    'success_criteria': 'Stable flight, good control response'
                },
                {
                    'test': 3,
                    'name': 'FBWA Mode Test',
                    'objectives': [
                        'Switch to FBWA mode',
                        'Test stabilization',
                        'Verify altitude hold',
                        'Test turns'
                    ],
                    'duration': '10 minutes',
                    'success_criteria': 'Stable flight in FBWA, good stabilization'
                },
                {
                    'test': 4,
                    'name': 'AUTO Mode Test',
                    'objectives': [
                        'Create simple waypoint mission',
                        'Test AUTO mode',
                        'Verify waypoint navigation',
                        'Test RTL function'
                    ],
                    'duration': '15 minutes',
                    'success_criteria': 'Successful waypoint navigation and RTL'
                }
            ]
        }

    def export_project(self, project_data: Dict[str, Any], format: str = 'md') -> str:
        """
        Export project documentation to file
        Formats: md, pdf, doc
        """
        if format == 'md':
            return self._export_markdown(project_data)
        elif format == 'pdf':
            return self._export_pdf(project_data)
        elif format == 'doc':
            return self._export_docx(project_data)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def _export_markdown(self, project_data: Dict[str, Any]) -> str:
        """Export as Markdown"""
        filename = f"ardupilot_project_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {project_data['metadata']['project_name']}\n\n")
            f.write(f"Created: {project_data['metadata']['created_at']}\n\n")

            # Aircraft Specifications
            f.write("## Aircraft Specifications\n\n")
            for key, value in project_data['metadata']['specifications'].items():
                f.write(f"- **{key}**: {value}\n")
            f.write("\n")

            # Equipment List
            f.write("## Equipment List\n\n")
            for item in project_data['equipment_list']:
                f.write(f"### {item['name']}\n")
                f.write(f"- **Category**: {item['category']}\n")
                f.write(f"- **Price Range**: {item['price_range']}\n")
                f.write(f"- **Notes**: {item['notes']}\n\n")

            # Total Cost
            cost = project_data['total_cost']
            f.write(f"**Total Cost**: ${cost['min_cost']} - ${cost['max_cost']} (Average: ${cost['average_cost']})\n\n")

            # Assembly Steps
            f.write("## Assembly Steps\n\n")
            for step in project_data['assembly_steps']:
                f.write(f"### Step {step['step']}: {step['title']}\n\n")
                f.write(f"{step['description']}\n\n")
                f.write("**Tasks:**\n")
                for task in step['tasks']:
                    f.write(f"- {task}\n")
                f.write(f"\n**Tools Required**: {', '.join(step['tools_required'])}\n")
                f.write(f"**Estimated Time**: {step['estimated_time']}\n\n")

            # Ardupilot Setup
            f.write("## Ardupilot Setup\n\n")
            for phase in project_data['ardupilot_setup']['steps']:
                f.write(f"### {phase['phase']}\n\n")
                for task in phase['tasks']:
                    f.write(f"- {task}\n")
                f.write("\n")

            # Safety Checklist
            f.write("## Safety Checklist\n\n")
            for category in project_data['safety_checklist']:
                f.write(f"### {category['category']}\n\n")
                for item in category['items']:
                    f.write(f"- [ ] {item}\n")
                f.write("\n")

        return filepath

    def _export_pdf(self, project_data: Dict[str, Any]) -> str:
        """Export as PDF (requires reportlab)"""
        # Simplified - would use reportlab in real implementation
        filename = f"ardupilot_project_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = os.path.join(self.output_dir, filename)

        # For now, create a text file as placeholder
        with open(filepath.replace('.pdf', '.txt'), 'w') as f:
            f.write("PDF export requires reportlab library\n")
            f.write(json.dumps(project_data, indent=2))

        return filepath.replace('.pdf', '.txt')

    def _export_docx(self, project_data: Dict[str, Any]) -> str:
        """Export as DOCX (requires python-docx)"""
        # Simplified - would use python-docx in real implementation
        filename = f"ardupilot_project_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
        filepath = os.path.join(self.output_dir, filename)

        # For now, create a text file as placeholder
        with open(filepath.replace('.docx', '.txt'), 'w') as f:
            f.write("DOCX export requires python-docx library\n")
            f.write(json.dumps(project_data, indent=2))

        return filepath.replace('.docx', '.txt')


def main():
    """Test project builder"""
    print("=== Project Builder Test ===\n")
    print("Project builder requires knowledge base integration.")
    print("Use through Flask API for full functionality.")


if __name__ == '__main__':
    main()
