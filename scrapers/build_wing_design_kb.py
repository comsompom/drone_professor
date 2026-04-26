"""
Wing Design Knowledge Base Builder
Creates comprehensive database for wing design including aerodynamics, materials, and physics
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime


class WingDesignKnowledgeBase:
    """
    Builds knowledge base for wing design including:
    - Airfoil profiles
    - Wing configurations
    - Materials
    - Physics calculations
    - Design guidelines
    """

    def __init__(self):
        self.wing_data = {
            'airfoils': [],
            'wing_types': [],
            'materials': [],
            'physics_formulas': [],
            'design_guidelines': []
        }

    def build_airfoils_database(self) -> List[Dict[str, Any]]:
        """Build database of airfoil profiles"""
        airfoils = [
            {
                'name': 'NACA 2412',
                'type': 'Cambered',
                'max_camber': '2%',
                'max_camber_position': '40%',
                'max_thickness': '12%',
                'applications': ['General aviation', 'Trainers', 'Light aircraft'],
                'characteristics': {
                    'lift_coefficient': '1.4-1.6',
                    'drag_coefficient': '0.006-0.008',
                    'stall_angle': '14-16°',
                    'reynolds_number': '500,000-3,000,000'
                },
                'advantages': ['Good lift', 'Gentle stall', 'Forgiving'],
                'disadvantages': ['Moderate drag', 'Not for high speed']
            },
            {
                'name': 'Clark Y',
                'type': 'Flat bottom',
                'max_camber': '3.5%',
                'max_camber_position': '30%',
                'max_thickness': '11.7%',
                'applications': ['Vintage aircraft', 'Sport planes', 'RC models'],
                'characteristics': {
                    'lift_coefficient': '1.5-1.7',
                    'drag_coefficient': '0.007-0.009',
                    'stall_angle': '15-17°',
                    'reynolds_number': '300,000-2,000,000'
                },
                'advantages': ['High lift', 'Easy to build', 'Stable'],
                'disadvantages': ['Higher drag', 'Not efficient at high speed']
            },
            {
                'name': 'NACA 0012',
                'type': 'Symmetrical',
                'max_camber': '0%',
                'max_camber_position': 'N/A',
                'max_thickness': '12%',
                'applications': ['Aerobatic', 'Vertical stabilizers', 'Symmetrical flight'],
                'characteristics': {
                    'lift_coefficient': '0 at 0° AOA',
                    'drag_coefficient': '0.006-0.007',
                    'stall_angle': '12-14°',
                    'reynolds_number': '500,000-5,000,000'
                },
                'advantages': ['Symmetrical performance', 'Low drag', 'Aerobatic'],
                'disadvantages': ['Lower lift', 'Requires higher speed']
            },
            {
                'name': 'Eppler 193',
                'type': 'High lift',
                'max_camber': '4.5%',
                'max_camber_position': '35%',
                'max_thickness': '9.5%',
                'applications': ['Gliders', 'Sailplanes', 'Slow flight'],
                'characteristics': {
                    'lift_coefficient': '1.8-2.0',
                    'drag_coefficient': '0.005-0.006',
                    'stall_angle': '16-18°',
                    'reynolds_number': '200,000-1,000,000'
                },
                'advantages': ['Very high lift', 'Low drag', 'Excellent glide'],
                'disadvantages': ['Sensitive to roughness', 'Complex to build']
            }
        ]

        return airfoils

    def build_wing_types_database(self) -> List[Dict[str, Any]]:
        """Build database of wing configurations"""
        wing_types = [
            {
                'name': 'Rectangular Wing',
                'description': 'Constant chord wing, simplest design',
                'aspect_ratio': '4-8',
                'taper_ratio': '1.0',
                'advantages': ['Easy to build', 'Simple structure', 'Predictable stall'],
                'disadvantages': ['Higher induced drag', 'Less efficient'],
                'applications': ['Trainers', 'Simple aircraft', 'RC models'],
                'design_notes': 'Good for beginners, easy to repair'
            },
            {
                'name': 'Tapered Wing',
                'description': 'Wing with reducing chord from root to tip',
                'aspect_ratio': '6-10',
                'taper_ratio': '0.4-0.6',
                'advantages': ['Lower induced drag', 'Better efficiency', 'Lighter'],
                'disadvantages': ['More complex to build', 'Tip stall tendency'],
                'applications': ['Sport aircraft', 'Aerobatic', 'Performance planes'],
                'design_notes': 'Use washout to prevent tip stall'
            },
            {
                'name': 'Elliptical Wing',
                'description': 'Elliptical planform, optimal lift distribution',
                'aspect_ratio': '7-12',
                'taper_ratio': 'Variable',
                'advantages': ['Minimum induced drag', 'Optimal efficiency', 'Beautiful'],
                'disadvantages': ['Very complex to build', 'Expensive'],
                'applications': ['High performance', 'Racing', 'Historic aircraft'],
                'design_notes': 'Theoretical optimum, rarely used due to complexity'
            },
            {
                'name': 'Delta Wing',
                'description': 'Triangular wing, swept back',
                'aspect_ratio': '2-4',
                'taper_ratio': '0-0.2',
                'advantages': ['High speed capable', 'Strong structure', 'Large area'],
                'disadvantages': ['High induced drag at low speed', 'Poor low speed performance'],
                'applications': ['High speed aircraft', 'Jets', 'Experimental'],
                'design_notes': 'Requires high landing speed'
            },
            {
                'name': 'Flying Wing',
                'description': 'No fuselage, all-wing design',
                'aspect_ratio': '8-15',
                'taper_ratio': '0.3-0.5',
                'advantages': ['Very efficient', 'Low drag', 'Lightweight'],
                'disadvantages': ['Stability challenges', 'Complex design', 'CG critical'],
                'applications': ['Long endurance', 'Surveillance', 'Experimental'],
                'design_notes': 'Requires careful design and tuning'
            }
        ]

        return wing_types

    def build_materials_database(self) -> List[Dict[str, Any]]:
        """Build database of wing construction materials"""
        materials = [
            {
                'name': 'Balsa Wood',
                'type': 'Natural wood',
                'density': '120-220 kg/m³',
                'tensile_strength': '10-20 MPa',
                'youngs_modulus': '3-4 GPa',
                'cost': 'Low-Medium',
                'advantages': ['Lightweight', 'Easy to work', 'Good strength-to-weight', 'Traditional'],
                'disadvantages': ['Variable quality', 'Moisture sensitive', 'Fragile'],
                'applications': ['RC models', 'Small aircraft', 'Ribs and spars'],
                'working_notes': 'Select straight grain, seal against moisture'
            },
            {
                'name': 'Plywood',
                'type': 'Engineered wood',
                'density': '500-700 kg/m³',
                'tensile_strength': '40-80 MPa',
                'youngs_modulus': '6-10 GPa',
                'cost': 'Low',
                'advantages': ['Strong', 'Consistent', 'Affordable', 'Easy to work'],
                'disadvantages': ['Heavier', 'Moisture sensitive'],
                'applications': ['Ribs', 'Spars', 'Fuselage', 'Control surfaces'],
                'working_notes': 'Use aircraft-grade plywood, seal edges'
            },
            {
                'name': 'Carbon Fiber',
                'type': 'Composite',
                'density': '1500-1600 kg/m³',
                'tensile_strength': '3500-6000 MPa',
                'youngs_modulus': '230-600 GPa',
                'cost': 'High',
                'advantages': ['Very strong', 'Very stiff', 'Lightweight', 'Durable'],
                'disadvantages': ['Expensive', 'Requires skill', 'Brittle', 'Conductive'],
                'applications': ['High performance', 'Spars', 'Skins', 'Racing'],
                'working_notes': 'Use proper safety equipment, vacuum bagging recommended'
            },
            {
                'name': 'Fiberglass',
                'type': 'Composite',
                'density': '1800-2000 kg/m³',
                'tensile_strength': '1000-2000 MPa',
                'youngs_modulus': '35-45 GPa',
                'cost': 'Medium',
                'advantages': ['Strong', 'Durable', 'Moldable', 'Affordable'],
                'disadvantages': ['Heavier than carbon', 'Requires skill', 'Messy'],
                'applications': ['Fuselage', 'Cowlings', 'Fairings', 'Skins'],
                'working_notes': 'Use epoxy resin, work in ventilated area'
            },
            {
                'name': 'Foam (EPP/EPO)',
                'type': 'Polymer foam',
                'density': '20-40 kg/m³',
                'tensile_strength': '1-3 MPa',
                'youngs_modulus': '0.01-0.05 GPa',
                'cost': 'Low',
                'advantages': ['Very lightweight', 'Impact resistant', 'Easy to shape', 'Cheap'],
                'disadvantages': ['Weak', 'Not durable', 'UV sensitive'],
                'applications': ['RC models', 'Cores', 'Trainers', 'Parkflyers'],
                'working_notes': 'Use hot wire cutter, reinforce with tape or carbon'
            },
            {
                'name': 'Aluminum',
                'type': 'Metal',
                'density': '2700 kg/m³',
                'tensile_strength': '200-500 MPa',
                'youngs_modulus': '70 GPa',
                'cost': 'Medium',
                'advantages': ['Strong', 'Durable', 'Easy to work', 'Repairable'],
                'disadvantages': ['Heavy', 'Corrosion', 'Fatigue'],
                'applications': ['Spars', 'Fittings', 'Landing gear', 'Full-scale aircraft'],
                'working_notes': 'Use aircraft-grade aluminum (2024, 6061, 7075)'
            }
        ]

        return materials

    def build_physics_formulas(self) -> List[Dict[str, Any]]:
        """Build database of aerodynamic physics formulas"""
        formulas = [
            {
                'name': 'Lift Force',
                'formula': 'L = 0.5 × ρ × V² × S × CL',
                'variables': {
                    'L': 'Lift force (N)',
                    'ρ': 'Air density (kg/m³)',
                    'V': 'Velocity (m/s)',
                    'S': 'Wing area (m²)',
                    'CL': 'Lift coefficient'
                },
                'description': 'Calculates the lift force generated by a wing',
                'typical_values': {
                    'ρ': '1.225 kg/m³ at sea level',
                    'CL': '0.4-1.6 depending on angle of attack'
                }
            },
            {
                'name': 'Drag Force',
                'formula': 'D = 0.5 × ρ × V² × S × CD',
                'variables': {
                    'D': 'Drag force (N)',
                    'ρ': 'Air density (kg/m³)',
                    'V': 'Velocity (m/s)',
                    'S': 'Reference area (m²)',
                    'CD': 'Drag coefficient'
                },
                'description': 'Calculates the drag force acting on the aircraft',
                'typical_values': {
                    'CD': '0.02-0.05 for clean aircraft'
                }
            },
            {
                'name': 'Wing Loading',
                'formula': 'WL = W / S',
                'variables': {
                    'WL': 'Wing loading (kg/m²)',
                    'W': 'Aircraft weight (kg)',
                    'S': 'Wing area (m²)'
                },
                'description': 'Weight per unit wing area, affects stall speed and maneuverability',
                'typical_values': {
                    'WL': '10-30 kg/m² for small aircraft, 50-100 kg/m² for jets'
                }
            },
            {
                'name': 'Aspect Ratio',
                'formula': 'AR = b² / S',
                'variables': {
                    'AR': 'Aspect ratio',
                    'b': 'Wingspan (m)',
                    'S': 'Wing area (m²)'
                },
                'description': 'Ratio of wingspan to average chord, affects induced drag',
                'typical_values': {
                    'AR': '4-8 for trainers, 10-20 for gliders, 2-4 for jets'
                }
            },
            {
                'name': 'Stall Speed',
                'formula': 'Vs = √(2 × W / (ρ × S × CLmax))',
                'variables': {
                    'Vs': 'Stall speed (m/s)',
                    'W': 'Weight (N)',
                    'ρ': 'Air density (kg/m³)',
                    'S': 'Wing area (m²)',
                    'CLmax': 'Maximum lift coefficient'
                },
                'description': 'Minimum speed at which aircraft can maintain level flight',
                'typical_values': {
                    'CLmax': '1.2-1.8 for most airfoils'
                }
            },
            {
                'name': 'Reynolds Number',
                'formula': 'Re = ρ × V × c / μ',
                'variables': {
                    'Re': 'Reynolds number',
                    'ρ': 'Air density (kg/m³)',
                    'V': 'Velocity (m/s)',
                    'c': 'Chord length (m)',
                    'μ': 'Dynamic viscosity (Pa·s)'
                },
                'description': 'Ratio of inertial to viscous forces, affects airfoil performance',
                'typical_values': {
                    'Re': '50,000-500,000 for RC models, 1,000,000+ for full-scale'
                }
            }
        ]

        return formulas

    def build_design_guidelines(self) -> List[Dict[str, Any]]:
        """Build design guidelines and best practices"""
        guidelines = [
            {
                'category': 'Wing Sizing',
                'guidelines': [
                    'Wing area: 50-80 dm²/kg for trainers',
                    'Wing area: 30-50 dm²/kg for sport aircraft',
                    'Wing area: 20-30 dm²/kg for fast aircraft',
                    'Aspect ratio: Higher AR = more efficient but less maneuverable',
                    'Chord: Minimum 10cm for structural integrity'
                ]
            },
            {
                'category': 'Airfoil Selection',
                'guidelines': [
                    'Trainers: Use forgiving airfoils (NACA 2412, Clark Y)',
                    'Aerobatic: Use symmetrical airfoils (NACA 0012)',
                    'Gliders: Use high-lift airfoils (Eppler series)',
                    'Speed: Use thin airfoils (8-10% thickness)',
                    'Consider Reynolds number for your application'
                ]
            },
            {
                'category': 'Structural Design',
                'guidelines': [
                    'Spar depth: Minimum 10% of chord',
                    'Rib spacing: 10-15cm for balsa, 15-25cm for foam',
                    'Use washout (2-3°) to prevent tip stall',
                    'Dihedral: 3-5° for stability',
                    'Safety factor: Minimum 4x for manned aircraft'
                ]
            },
            {
                'category': 'Center of Gravity',
                'guidelines': [
                    'CG position: 25-33% of mean aerodynamic chord',
                    'Start at 30% and adjust for stability',
                    'Forward CG = more stable, less maneuverable',
                    'Aft CG = less stable, more maneuverable',
                    'Never exceed aft CG limit'
                ]
            },
            {
                'category': 'Control Surfaces',
                'guidelines': [
                    'Aileron area: 15-20% of wing area',
                    'Elevator area: 20-25% of horizontal stabilizer',
                    'Rudder area: 25-30% of vertical stabilizer',
                    'Control throws: Start conservative, increase gradually',
                    'Use exponential for smoother control'
                ]
            }
        ]

        return guidelines

    def build_complete_database(self) -> Dict[str, Any]:
        """Build complete wing design knowledge base"""
        self.wing_data['airfoils'] = self.build_airfoils_database()
        self.wing_data['wing_types'] = self.build_wing_types_database()
        self.wing_data['materials'] = self.build_materials_database()
        self.wing_data['physics_formulas'] = self.build_physics_formulas()
        self.wing_data['design_guidelines'] = self.build_design_guidelines()

        return self.wing_data

    def save_to_json(self, filename: str = 'wing_design_knowledge.json'):
        """Save wing design knowledge base to JSON file"""
        output_path = f'/workspace/app-b6ukc6ytkow1/backend/data/{filename}'

        database = self.build_complete_database()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'wing_design': database,
                'created_at': datetime.now().isoformat(),
                'version': '1.0'
            }, f, indent=2, ensure_ascii=False)

        print(f"Wing design knowledge base saved to {output_path}")


def main():
    """Build wing design knowledge base"""
    print("=== Building Wing Design Knowledge Base ===\n")

    builder = WingDesignKnowledgeBase()
    builder.save_to_json()

    print("\nWing design knowledge base created successfully!")
    print("Includes:")
    print("  - Airfoil profiles")
    print("  - Wing configurations")
    print("  - Construction materials")
    print("  - Physics formulas")
    print("  - Design guidelines")


if __name__ == '__main__':
    main()
