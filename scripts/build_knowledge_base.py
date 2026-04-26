#!/usr/bin/env python3
"""
Master Knowledge Base Builder
Runs all scrapers and builders to create complete knowledge base
"""

import sys
import subprocess
import time
from pathlib import Path
from datetime import datetime


class KnowledgeBaseBuilder:
    """
    Master builder that orchestrates all knowledge base creation
    """

    def __init__(self):
        self.scrapers_dir = Path('/workspace/app-b6ukc6ytkow1/backend/scrapers')
        self.data_dir = Path('/workspace/app-b6ukc6ytkow1/backend/data')
        self.results = []

    def print_header(self, text: str):
        """Print formatted header"""
        print("\n" + "=" * 70)
        print(f"  {text}")
        print("=" * 70 + "\n")

    def print_step(self, step: int, total: int, name: str):
        """Print step information"""
        print(f"\n[{step}/{total}] {name}")
        print("-" * 70)

    def run_script(self, script_name: str, description: str) -> bool:
        """Run a Python script and return success status"""
        script_path = self.scrapers_dir / script_name

        if not script_path.exists():
            print(f"❌ Script not found: {script_path}")
            return False

        print(f"Running: {script_name}")
        print(f"Purpose: {description}\n")

        start_time = time.time()

        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                cwd=str(self.scrapers_dir.parent),
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )

            elapsed = time.time() - start_time

            if result.returncode == 0:
                print(f"✅ Success! ({elapsed:.1f}s)")
                if result.stdout:
                    print(result.stdout)
                return True
            else:
                print(f"❌ Failed! ({elapsed:.1f}s)")
                if result.stderr:
                    print(f"Error: {result.stderr}")
                return False

        except subprocess.TimeoutExpired:
            print(f"❌ Timeout! Script took longer than 5 minutes")
            return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False

    def verify_data_files(self):
        """Verify all expected data files exist"""
        expected_files = [
            'ardupilot_parameters.json',
            'ardupilot_hardware.json',
            'equipment_database.json',
            'wing_design_knowledge.json',
            'ai_pilot_knowledge.json'
        ]

        print("\n" + "=" * 70)
        print("  Verifying Knowledge Base Files")
        print("=" * 70 + "\n")

        all_exist = True
        for filename in expected_files:
            filepath = self.data_dir / filename
            if filepath.exists():
                size = filepath.stat().st_size
                print(f"✅ {filename:40} ({size:,} bytes)")
            else:
                print(f"❌ {filename:40} (missing)")
                all_exist = False

        return all_exist

    def print_summary(self):
        """Print build summary"""
        self.print_header("Build Summary")

        total = len(self.results)
        successful = sum(1 for r in self.results if r['success'])
        failed = total - successful

        print(f"Total tasks: {total}")
        print(f"Successful: {successful} ✅")
        print(f"Failed: {failed} ❌\n")

        for result in self.results:
            status = "✅" if result['success'] else "❌"
            print(f"{status} {result['name']}")

        if failed == 0:
            print("\n🎉 All knowledge base components built successfully!")
            print("\nKnowledge base is ready for use.")
            print("Start the server with: python start_server.py")
        else:
            print("\n⚠️  Some components failed to build.")
            print("The system will work with partial knowledge base.")
            print("Check errors above for details.")

    def build_all(self):
        """Build complete knowledge base"""
        self.print_header("Ardupilot Configuration Assistant - Knowledge Base Builder")

        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Data directory: {self.data_dir}")
        print(f"Scrapers directory: {self.scrapers_dir}")

        # Ensure data directory exists
        self.data_dir.mkdir(exist_ok=True)

        # Define build tasks
        tasks = [
            {
                'script': 'scrape_parameters.py',
                'name': 'Ardupilot Parameters',
                'description': 'Scrape Ardupilot parameter documentation'
            },
            {
                'script': 'scrape_hardware.py',
                'name': 'Ardupilot Hardware',
                'description': 'Scrape Ardupilot hardware and autopilot documentation'
            },
            {
                'script': 'build_equipment_db.py',
                'name': 'Equipment Database',
                'description': 'Build comprehensive equipment database (motors, servos, etc.)'
            },
            {
                'script': 'build_wing_design_kb.py',
                'name': 'Wing Design Knowledge',
                'description': 'Build wing design knowledge base (airfoils, materials, physics)'
            },
            {
                'script': 'build_ai_pilot_kb.py',
                'name': 'AI Pilot Assistant',
                'description': 'Build AI pilot assistant knowledge base (flight modes, safety, troubleshooting)'
            }
        ]

        total_tasks = len(tasks)

        # Run all tasks
        for i, task in enumerate(tasks, 1):
            self.print_step(i, total_tasks, task['name'])

            success = self.run_script(task['script'], task['description'])

            self.results.append({
                'name': task['name'],
                'script': task['script'],
                'success': success
            })

            if not success:
                print(f"\n⚠️  Warning: {task['name']} failed, continuing with next task...")

        # Verify files
        self.verify_data_files()

        # Print summary
        self.print_summary()

        # Return success if all tasks completed
        return all(r['success'] for r in self.results)


def main():
    """Main entry point"""
    builder = KnowledgeBaseBuilder()

    try:
        success = builder.build_all()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Build interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
Got