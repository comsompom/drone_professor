"""
AI Pilot Assistant Knowledge Base Builder
Creates comprehensive database for AI-powered flight assistance and recommendations
"""

import json
from typing import Dict, List, Any
from datetime import datetime


class AIPilotKnowledgeBase:
    """
    Builds knowledge base for AI Pilot Assistant including:
    - Flight modes and their uses
    - Safety recommendations
    - Troubleshooting guides
    - Best practices
    - Common issues and solutions
    """

    def __init__(self):
        self.ai_data = {
            'flight_modes': [],
            'safety_recommendations': [],
            'troubleshooting': [],
            'best_practices': [],
            'common_issues': []
        }

    def build_flight_modes_database(self) -> List[Dict[str, Any]]:
        """Build database of flight modes and recommendations"""
        flight_modes = [
            {
                'name': 'MANUAL',
                'description': 'Full manual control, no stabilization',
                'when_to_use': 'Experienced pilots, aerobatics, testing',
                'requirements': ['Good piloting skills', 'Calm weather', 'Line of sight'],
                'risks': ['High', 'No stabilization', 'Easy to crash'],
                'recommendations': [
                    'Only for experienced pilots',
                    'Test in simulator first',
                    'Have recovery mode ready',
                    'Fly in open area'
                ]
            },
            {
                'name': 'STABILIZE',
                'description': 'Self-leveling when sticks centered',
                'when_to_use': 'Learning, general flying, most situations',
                'requirements': ['Basic piloting skills', 'Calibrated sensors'],
                'risks': ['Low', 'Self-levels', 'Forgiving'],
                'recommendations': [
                    'Best mode for beginners',
                    'Default mode for most flights',
                    'Calibrate accelerometer before flight',
                    'Test at altitude first'
                ]
            },
            {
                'name': 'FLY BY WIRE A (FBWA)',
                'description': 'Stabilized flight with altitude hold',
                'when_to_use': 'Cruising, photography, stable flight',
                'requirements': ['Airspeed sensor', 'Barometer', 'Tuned PID'],
                'risks': ['Low-Medium', 'Altitude hold', 'Speed control'],
                'recommendations': [
                    'Excellent for cruising',
                    'Good for beginners',
                    'Requires airspeed sensor',
                    'Set appropriate speed limits'
                ]
            },
            {
                'name': 'AUTO',
                'description': 'Fully autonomous waypoint navigation',
                'when_to_use': 'Missions, mapping, long-range flights',
                'requirements': ['GPS lock', 'Mission uploaded', 'Tuned navigation', 'Geofence'],
                'risks': ['Medium', 'Autonomous', 'Requires good setup'],
                'recommendations': [
                    'Test in FBWA first',
                    'Set geofence',
                    'Plan safe mission',
                    'Monitor telemetry',
                    'Have manual override ready'
                ]
            },
            {
                'name': 'RTL (Return to Launch)',
                'description': 'Automatic return to launch point',
                'when_to_use': 'Emergency, low battery, lost orientation',
                'requirements': ['GPS lock', 'Home position set', 'RTL altitude configured'],
                'risks': ['Low', 'Automatic return', 'Safe'],
                'recommendations': [
                    'Set appropriate RTL altitude',
                    'Test before long flights',
                    'Ensure clear path home',
                    'Monitor battery during return'
                ]
            },
            {
                'name': 'LOITER',
                'description': 'Circle at current location',
                'when_to_use': 'Waiting, observing, holding position',
                'requirements': ['GPS lock', 'Tuned navigation'],
                'risks': ['Low', 'Holds position', 'Safe'],
                'recommendations': [
                    'Good for photography',
                    'Set appropriate radius',
                    'Monitor wind conditions',
                    'Keep visual contact'
                ]
            },
            {
                'name': 'GUIDED',
                'description': 'GCS-commanded navigation',
                'when_to_use': 'Dynamic missions, follow-me, interactive control',
                'requirements': ['Telemetry link', 'GPS lock', 'GCS software'],
                'risks': ['Medium', 'Requires telemetry', 'Link dependent'],
                'recommendations': [
                    'Ensure strong telemetry',
                    'Have failsafe configured',
                    'Monitor link quality',
                    'Practice in safe area'
                ]
            }
        ]

        return flight_modes

    def build_safety_recommendations(self) -> List[Dict[str, Any]]:
        """Build safety recommendations database"""
        safety = [
            {
                'category': 'Pre-Flight Checks',
                'priority': 'Critical',
                'recommendations': [
                    'Check all control surfaces move correctly',
                    'Verify GPS lock (3D fix, 8+ satellites)',
                    'Confirm battery voltage and capacity',
                    'Test telemetry link',
                    'Verify failsafe settings',
                    'Check weather conditions',
                    'Inspect airframe for damage',
                    'Verify CG position',
                    'Test motor/propeller',
                    'Arm and disarm test on ground'
                ]
            },
            {
                'category': 'Failsafe Configuration',
                'priority': 'Critical',
                'recommendations': [
                    'Set RC failsafe to RTL or LAND',
                    'Configure battery failsafe (RTL at 20%, LAND at 10%)',
                    'Set GCS failsafe to RTL',
                    'Configure geofence with appropriate limits',
                    'Test failsafes on ground',
                    'Set appropriate RTL altitude (50m+ above obstacles)',
                    'Enable crash detection',
                    'Configure throttle failsafe'
                ]
            },
            {
                'category': 'Flight Operations',
                'priority': 'High',
                'recommendations': [
                    'Always maintain visual line of sight',
                    'Fly in open areas away from people',
                    'Respect airspace regulations',
                    'Monitor battery voltage continuously',
                    'Keep telemetry link active',
                    'Have recovery plan for each flight',
                    'Fly in appropriate weather conditions',
                    'Start with conservative settings',
                    'Test new features at altitude',
                    'Land with 20%+ battery remaining'
                ]
            },
            {
                'category': 'Emergency Procedures',
                'priority': 'Critical',
                'recommendations': [
                    'Know how to switch to RTL immediately',
                    'Practice manual recovery',
                    'Have emergency landing sites identified',
                    'Know how to disarm in emergency',
                    'Keep calm and assess situation',
                    'Use FBWA for manual recovery',
                    'Monitor altitude and airspeed',
                    'Communicate with other pilots/observers'
                ]
            },
            {
                'category': 'Maintenance',
                'priority': 'High',
                'recommendations': [
                    'Inspect airframe after each flight',
                    'Check propeller for damage',
                    'Verify all connections are secure',
                    'Clean sensors regularly',
                    'Update firmware carefully',
                    'Keep spare parts available',
                    'Log flight hours and maintenance',
                    'Replace worn components proactively'
                ]
            }
        ]

        return safety

    def build_troubleshooting_database(self) -> List[Dict[str, Any]]:
        """Build troubleshooting guide database"""
        troubleshooting = [
            {
                'issue': 'Aircraft won\'t arm',
                'possible_causes': [
                    'Pre-arm checks failing',
                    'No GPS lock',
                    'Accelerometer not calibrated',
                    'Compass not calibrated',
                    'Safety switch not pressed',
                    'RC not connected',
                    'Battery voltage too low'
                ],
                'solutions': [
                    'Check pre-arm messages in GCS',
                    'Wait for GPS lock (8+ satellites)',
                    'Calibrate accelerometer',
                    'Calibrate compass away from metal',
                    'Press safety switch',
                    'Check RC transmitter and receiver',
                    'Charge or replace battery'
                ]
            },
            {
                'issue': 'Poor GPS performance',
                'possible_causes': [
                    'Obstructed view of sky',
                    'Interference from electronics',
                    'Poor GPS module placement',
                    'Damaged GPS antenna',
                    'GPS not configured correctly'
                ],
                'solutions': [
                    'Ensure clear view of sky',
                    'Move GPS away from power lines and motors',
                    'Mount GPS on top of aircraft',
                    'Check GPS antenna connection',
                    'Verify GPS type in parameters',
                    'Update GPS firmware'
                ]
            },
            {
                'issue': 'Aircraft oscillates or wobbles',
                'possible_causes': [
                    'PID gains too high',
                    'Vibration on flight controller',
                    'Loose components',
                    'CG too far aft',
                    'Control surface flutter'
                ],
                'solutions': [
                    'Reduce P and D gains',
                    'Improve vibration damping',
                    'Secure all components',
                    'Move battery forward',
                    'Stiffen control surfaces',
                    'Run autotune'
                ]
            },
            {
                'issue': 'Compass errors',
                'possible_causes': [
                    'Magnetic interference',
                    'Compass not calibrated',
                    'Compass orientation wrong',
                    'Metal objects nearby',
                    'Power cables near compass'
                ],
                'solutions': [
                    'Calibrate compass away from metal',
                    'Perform compass calibration dance',
                    'Check compass orientation setting',
                    'Move compass away from interference',
                    'Twist power cables',
                    'Use external compass'
                ]
            },
            {
                'issue': 'Telemetry link lost',
                'possible_causes': [
                    'Out of range',
                    'Antenna damaged',
                    'Interference',
                    'Low power',
                    'Incorrect baud rate'
                ],
                'solutions': [
                    'Reduce distance',
                    'Check antenna connections',
                    'Change frequency/channel',
                    'Check power supply',
                    'Verify baud rate matches',
                    'Use higher power radio'
                ]
            },
            {
                'issue': 'Aircraft flies in circles',
                'possible_causes': [
                    'Trim not set correctly',
                    'CG offset',
                    'Compass calibration wrong',
                    'One motor/servo weak',
                    'Wind compensation issue'
                ],
                'solutions': [
                    'Adjust trim in MANUAL mode',
                    'Check CG position',
                    'Recalibrate compass',
                    'Check all motors and servos',
                    'Verify compass orientation',
                    'Check for structural damage'
                ]
            }
        ]

        return troubleshooting

    def build_best_practices(self) -> List[Dict[str, Any]]:
        """Build best practices database"""
        best_practices = [
            {
                'category': 'Initial Setup',
                'practices': [
                    'Read all documentation before first flight',
                    'Use Mission Planner or QGroundControl for setup',
                    'Follow setup wizard completely',
                    'Calibrate all sensors carefully',
                    'Set up failsafes before first flight',
                    'Test on bench before flying',
                    'Start with conservative PID values',
                    'Document your configuration'
                ]
            },
            {
                'category': 'Tuning',
                'practices': [
                    'Use autotune for initial PID values',
                    'Tune in calm weather',
                    'Make small changes incrementally',
                    'Test one parameter at a time',
                    'Log all flights for analysis',
                    'Start with roll, then pitch, then yaw',
                    'Use filter settings to reduce noise',
                    'Document what works'
                ]
            },
            {
                'category': 'Mission Planning',
                'practices': [
                    'Plan missions in GCS before flight',
                    'Set appropriate waypoint altitudes',
                    'Include takeoff and landing sequences',
                    'Set geofence boundaries',
                    'Plan for wind conditions',
                    'Have abort/RTL plan',
                    'Check airspace restrictions',
                    'Verify mission before upload'
                ]
            },
            {
                'category': 'Data Logging',
                'practices': [
                    'Enable comprehensive logging',
                    'Review logs after each flight',
                    'Look for anomalies and warnings',
                    'Track battery performance',
                    'Monitor vibration levels',
                    'Check GPS performance',
                    'Analyze PID performance',
                    'Keep log archive'
                ]
            },
            {
                'category': 'Battery Management',
                'practices': [
                    'Never discharge below 3.5V per cell',
                    'Land with 20% capacity remaining',
                    'Monitor voltage during flight',
                    'Set battery failsafe appropriately',
                    'Balance charge after each flight',
                    'Store at storage voltage',
                    'Check battery health regularly',
                    'Replace degraded batteries'
                ]
            }
        ]

        return best_practices

    def build_common_issues(self) -> List[Dict[str, Any]]:
        """Build common issues and solutions database"""
        common_issues = [
            {
                'issue': 'EKF Variance',
                'severity': 'High',
                'description': 'Extended Kalman Filter reports high variance',
                'impact': 'Poor position estimation, potential flyaway',
                'prevention': [
                    'Ensure good GPS signal',
                    'Calibrate compass properly',
                    'Reduce vibration',
                    'Check for magnetic interference'
                ],
                'immediate_action': 'Land immediately if EKF failsafe triggers'
            },
            {
                'issue': 'Vibration',
                'severity': 'Medium-High',
                'description': 'Excessive vibration affecting sensors',
                'impact': 'Poor flight performance, sensor errors',
                'prevention': [
                    'Balance propellers',
                    'Use vibration damping',
                    'Secure all components',
                    'Check motor bearings'
                ],
                'immediate_action': 'Land and fix vibration source'
            },
            {
                'issue': 'Brownout',
                'severity': 'High',
                'description': 'Voltage drops causing resets',
                'impact': 'Flight controller resets, loss of control',
                'prevention': [
                    'Use adequate power supply',
                    'Check all connections',
                    'Use capacitors on power lines',
                    'Separate power for servos'
                ],
                'immediate_action': 'Land immediately, check power system'
            }
        ]

        return common_issues

    def build_complete_database(self) -> Dict[str, Any]:
        """Build complete AI pilot assistant knowledge base"""
        self.ai_data['flight_modes'] = self.build_flight_modes_database()
        self.ai_data['safety_recommendations'] = self.build_safety_recommendations()
        self.ai_data['troubleshooting'] = self.build_troubleshooting_database()
        self.ai_data['best_practices'] = self.build_best_practices()
        self.ai_data['common_issues'] = self.build_common_issues()

        return self.ai_data

    def save_to_json(self, filename: str = 'ai_pilot_knowledge.json'):
        """Save AI pilot knowledge base to JSON file"""
        output_path = f'/workspace/app-b6ukc6ytkow1/backend/data/{filename}'

        database = self.build_complete_database()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'ai_pilot_assistant': database,
                'created_at': datetime.now().isoformat(),
                'version': '1.0'
            }, f, indent=2, ensure_ascii=False)

        print(f"AI Pilot Assistant knowledge base saved to {output_path}")


def main():
    """Build AI pilot assistant knowledge base"""
    print("=== Building AI Pilot Assistant Knowledge Base ===\n")

    builder = AIPilotKnowledgeBase()
    builder.save_to_json()

    print("\nAI Pilot Assistant knowledge base created successfully!")
    print("Includes:")
    print("  - Flight modes and recommendations")
    print("  - Safety recommendations")
    print("  - Troubleshooting guides")
    print("  - Best practices")
    print("  - Common issues and solutions")


if __name__ == '__main__':
    main()
