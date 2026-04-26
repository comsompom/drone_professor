#!/usr/bin/env python3
"""
Knowledge Base Status Checker
Verifies and reports on knowledge base completeness
"""

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any


class KnowledgeBaseChecker:
    """Check knowledge base status and completeness"""

    def __init__(self):
        self.data_dir = Path('/workspace/app-b6ukc6ytkow1/backend/data')
        self.files = {
            'ardupilot_parameters.json': {
                'name': 'Ardupilot Parameters',
                'description': 'Parameter documentation from Ardupilot',
                'required_keys': ['parameters', 'total_count']
            },
            'ardupilot_hardware.json': {
                'name': 'Ardupilot Hardware',
                'description': 'Hardware and autopilot documentation',
                'required_keys': ['hardware', 'total_count']
            },
            'equipment_database.json': {
                'name': 'Equipment Database',
                'description': 'Motors, servos, ESCs, and other equipment',
                'required_keys': ['equipment']
            },
            'wing_design_knowledge.json': {
                'name': 'Wing Design Knowledge',
                'description': 'Airfoils, materials, physics, and design guidelines',
                'required_keys': ['wing_design']
            },
            'ai_pilot_knowledge.json': {
                'name': 'AI Pilot Assistant',
                'description': 'Flight modes, safety, troubleshooting, best practices',
                'required_keys': ['ai_pilot_assistant']
            }
        }

    def check_file(self, filename: str, info: Dict[str, Any]) -> Dict[str, Any]:
        """Check a single knowledge base file"""
        filepath = self.data_dir / filename

        result = {
            'filename': filename,
            'name': info['name'],
            'exists': False,
            'size': 0,
            'valid_json': False,
            'has_required_keys': False,
            'item_count': 0,
            'created_at': None,
            'status': 'missing'
        }

        # Check if file exists
        if not filepath.exists():
            return result

        result['exists'] = True
        result['size'] = filepath.stat().st_size

        # Try to load JSON
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)

            result['valid_json'] = True

            # Check required keys
            has_all_keys = all(key in data for key in info['required_keys'])
            result['has_required_keys'] = has_all_keys

            # Get item count
            if 'parameters' in data:
                result['item_count'] = len(data.get('parameters', []))
            elif 'hardware' in data:
                result['item_count'] = len(data.get('hardware', []))
            elif 'equipment' in data:
                equipment = data.get('equipment', {})
                result['item_count'] = sum(
                    len(v) if isinstance(v, list) else sum(len(vv) for vv in v.values() if isinstance(vv, list))
                    for v in equipment.values()
                )
            elif 'wing_design' in data:
                wing_data = data.get('wing_design', {})
                result['item_count'] = sum(len(v) for v in wing_data.values() if isinstance(v, list))
            elif 'ai_pilot_assistant' in data:
                ai_data = data.get('ai_pilot_assistant', {})
                result['item_count'] = sum(len(v) for v in ai_data.values() if isinstance(v, list))

            # Get creation date
            result['created_at'] = data.get('created_at', data.get('scraped_at'))

            # Determine status
            if has_all_keys and result['item_count'] > 0:
                result['status'] = 'complete'
            elif has_all_keys:
                result['status'] = 'empty'
            else:
                result['status'] = 'incomplete'

        except json.JSONDecodeError:
            result['status'] = 'invalid'
        except Exception as e:
            result['status'] = f'error: {e}'

        return result

    def check_all(self) -> Dict[str, Any]:
        """Check all knowledge base files"""
        results = {}

        for filename, info in self.files.items():
            results[filename] = self.check_file(filename, info)

        return results

    def print_report(self):
        """Print detailed status report"""
        print("=" * 80)
        print("  Knowledge Base Status Report")
        print("=" * 80)
        print(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Data directory: {self.data_dir}\n")

        results = self.check_all()

        # Print individual file status
        print("-" * 80)
        print(f"{'Component':<30} {'Status':<12} {'Items':<8} {'Size':<12}")
        print("-" * 80)

        total_items = 0
        total_size = 0
        complete_count = 0

        for filename, result in results.items():
            status_icon = {
                'complete': '✅',
                'empty': '⚠️ ',
                'incomplete': '⚠️ ',
                'invalid': '❌',
                'missing': '❌'
            }.get(result['status'], '❓')

            status_text = result['status'].upper()
            items = str(result['item_count']) if result['item_count'] > 0 else '-'
            size = f"{result['size']:,} B" if result['size'] > 0 else '-'

            print(f"{status_icon} {result['name']:<28} {status_text:<12} {items:<8} {size:<12}")

            if result['status'] == 'complete':
                complete_count += 1

            total_items += result['item_count']
            total_size += result['size']

        print("-" * 80)
        print(f"{'TOTAL':<30} {complete_count}/{len(results)} complete {total_items:<8} {total_size:,} B")
        print("-" * 80)

        # Print summary
        print("\n" + "=" * 80)
        print("  Summary")
        print("=" * 80 + "\n")

        if complete_count == len(results):
            print("🎉 Knowledge base is complete!")
            print(f"   Total items: {total_items:,}")
            print(f"   Total size: {total_size:,} bytes ({total_size / 1024:.1f} KB)")
        elif complete_count > 0:
            print(f"⚠️  Knowledge base is partially complete ({complete_count}/{len(results)} components)")
            print(f"   Total items: {total_items:,}")
            print(f"   Total size: {total_size:,} bytes ({total_size / 1024:.1f} KB)")
            print("\n   Missing or incomplete components:")
            for filename, result in results.items():
                if result['status'] != 'complete':
                    print(f"   - {result['name']}: {result['status']}")
        else:
            print("❌ Knowledge base is empty or missing")
            print("   Run: python build_knowledge_base.py")

        # Print recommendations
        print("\n" + "=" * 80)
        print("  Recommendations")
        print("=" * 80 + "\n")

        if complete_count < len(results):
            print("To build complete knowledge base:")
            print("  1. Ensure Python dependencies are installed:")
            print("     pip install -r requirements.txt")
            print("  2. Run the knowledge base builder:")
            print("     python build_knowledge_base.py")
            print("  3. Or run individual builders:")
            print("     python scrapers/scrape_parameters.py")
            print("     python scrapers/scrape_hardware.py")
            print("     python scrapers/build_equipment_db.py")
            print("     python scrapers/build_wing_design_kb.py")
            print("     python scrapers/build_ai_pilot_kb.py")
        else:
            print("✅ Knowledge base is complete and ready to use!")
            print("   Start the server with: python start_server.py")

        print("\n" + "=" * 80)

        return results

    def get_statistics(self) -> Dict[str, Any]:
        """Get knowledge base statistics"""
        results = self.check_all()

        stats = {
            'total_files': len(results),
            'complete_files': sum(1 for r in results.values() if r['status'] == 'complete'),
            'total_items': sum(r['item_count'] for r in results.values()),
            'total_size_bytes': sum(r['size'] for r in results.values()),
            'files': results
        }

        return stats


def main():
    """Main entry point"""
    checker = KnowledgeBaseChecker()
    checker.print_report()


if __name__ == '__main__':
    main()
