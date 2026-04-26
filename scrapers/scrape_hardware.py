"""
Ardupilot Hardware Web Scraper
Scrapes hardware/autopilot data from Ardupilot documentation and saves to JSON
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from typing import Dict, List, Any


class ArdupilotHardwareScraper:
    def __init__(self):
        self.base_url = "https://ardupilot.org/plane/docs/common-autopilots.html"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def scrape_hardware(self) -> List[Dict[str, Any]]:
        """
        Scrape all hardware/autopilot information from Ardupilot documentation
        Returns list of hardware dictionaries
        """
        print(f"Fetching hardware data from {self.base_url}...")

        try:
            response = requests.get(self.base_url, headers=self.headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'lxml')
            hardware_list = []

            # Find all hardware sections
            sections = soup.find_all(['section', 'div'], class_=['section'])

            for section in sections:
                # Get section title (hardware name)
                title_elem = section.find(['h1', 'h2', 'h3', 'h4'])
                if not title_elem:
                    continue

                hardware_name = title_elem.get_text(strip=True)

                # Skip generic section titles
                if hardware_name.lower() in ['autopilots', 'overview', 'introduction']:
                    continue

                # Extract description
                description_parts = []
                for p in section.find_all('p', limit=3):
                    desc_text = p.get_text(strip=True)
                    if desc_text:
                        description_parts.append(desc_text)

                description = ' '.join(description_parts)

                # Extract specifications from lists
                specifications = {}
                spec_lists = section.find_all(['ul', 'ol'])

                for spec_list in spec_lists:
                    items = spec_list.find_all('li')
                    for item in items:
                        spec_text = item.get_text(strip=True)

                        # Parse spec format: "Key: Value"
                        if ':' in spec_text:
                            key, value = spec_text.split(':', 1)
                            specifications[key.strip()] = value.strip()
                        else:
                            specifications[f'feature_{len(specifications)}'] = spec_text

                # Extract pin connections
                pin_connections = self._extract_pin_connections(section)

                # Extract schematic links
                schematics = self._extract_schematics(section)

                # Extract images
                images = []
                for img in section.find_all('img'):
                    img_src = img.get('src', '')
                    if img_src:
                        # Make absolute URL
                        if img_src.startswith('/'):
                            img_src = f"https://ardupilot.org{img_src}"
                        elif not img_src.startswith('http'):
                            img_src = f"https://ardupilot.org/plane/docs/{img_src}"
                        images.append(img_src)

                hardware_list.append({
                    'name': hardware_name,
                    'description': description,
                    'specifications': specifications,
                    'pin_connections': pin_connections,
                    'schematics': schematics,
                    'images': images,
                    'category': self._categorize_hardware(hardware_name, description)
                })

            # Also look for hardware in tables
            hardware_tables = soup.find_all('table', class_='docutils')

            for table in hardware_tables:
                rows = table.find_all('tr')

                # Get headers
                headers = []
                header_row = rows[0] if rows else None
                if header_row:
                    headers = [th.get_text(strip=True) for th in header_row.find_all(['th', 'td'])]

                # Process data rows
                for row in rows[1:]:
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        hardware_data = {}

                        for i, col in enumerate(cols):
                            header = headers[i] if i < len(headers) else f'column_{i}'
                            hardware_data[header] = col.get_text(strip=True)

                        if 'name' in hardware_data or 'Name' in hardware_data:
                            hardware_list.append({
                                'name': hardware_data.get('name') or hardware_data.get('Name', 'Unknown'),
                                'description': hardware_data.get('description') or hardware_data.get('Description', ''),
                                'specifications': hardware_data,
                                'pin_connections': [],
                                'schematics': [],
                                'images': [],
                                'category': 'Autopilot'
                            })

            print(f"Successfully scraped {len(hardware_list)} hardware items")
            return hardware_list

        except Exception as e:
            print(f"Error scraping hardware: {e}")
            return []

    def _extract_pin_connections(self, section) -> List[Dict[str, str]]:
        """Extract pin connection information from section"""
        pin_connections = []

        # Look for tables with pin information
        tables = section.find_all('table')

        for table in tables:
            rows = table.find_all('tr')

            for row in rows:
                cols = row.find_all(['td', 'th'])
                if len(cols) >= 2:
                    pin_text = cols[0].get_text(strip=True).lower()

                    # Check if this looks like pin information
                    if any(keyword in pin_text for keyword in ['pin', 'port', 'connector', 'gpio']):
                        pin_connections.append({
                            'pin': cols[0].get_text(strip=True),
                            'function': cols[1].get_text(strip=True),
                            'notes': cols[2].get_text(strip=True) if len(cols) > 2 else ''
                        })

        return pin_connections

    def _extract_schematics(self, section) -> List[str]:
        """Extract schematic links from section"""
        schematics = []

        # Look for links to PDF or image files
        for link in section.find_all('a'):
            href = link.get('href', '')
            link_text = link.get_text(strip=True).lower()

            if any(keyword in link_text for keyword in ['schematic', 'diagram', 'pinout', 'wiring']):
                # Make absolute URL
                if href.startswith('/'):
                    href = f"https://ardupilot.org{href}"
                elif not href.startswith('http'):
                    href = f"https://ardupilot.org/plane/docs/{href}"

                schematics.append({
                    'title': link.get_text(strip=True),
                    'url': href
                })

        return schematics

    def _categorize_hardware(self, name: str, description: str) -> str:
        """Categorize hardware based on name and description"""
        name_lower = name.lower()
        desc_lower = description.lower()

        if any(keyword in name_lower for keyword in ['pixhawk', 'cube', 'autopilot', 'flight controller']):
            return 'Flight Controller'
        elif any(keyword in name_lower for keyword in ['gps', 'gnss']):
            return 'GPS/GNSS'
        elif any(keyword in name_lower for keyword in ['telemetry', 'radio']):
            return 'Telemetry'
        elif any(keyword in name_lower for keyword in ['power', 'pdb', 'bec']):
            return 'Power Module'
        elif any(keyword in name_lower for keyword in ['sensor', 'imu', 'compass']):
            return 'Sensor'
        else:
            return 'Other'

    def save_to_json(self, hardware_list: List[Dict[str, Any]], filename: str = 'ardupilot_hardware.json'):
        """Save hardware data to JSON file"""
        output_path = f'/workspace/app-b6ukc6ytkow1/backend/data/{filename}'

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'hardware': hardware_list,
                'total_count': len(hardware_list),
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                'source_url': self.base_url
            }, f, indent=2, ensure_ascii=False)

        print(f"Hardware data saved to {output_path}")


def main():
    scraper = ArdupilotHardwareScraper()
    hardware_list = scraper.scrape_hardware()

    if hardware_list:
        scraper.save_to_json(hardware_list)
        print(f"\nSample hardware:")
        for hw in hardware_list[:5]:
            print(f"  - {hw['name']}: {hw['description'][:80]}...")
    else:
        print("No hardware scraped. Please check the URL and HTML structure.")


if __name__ == '__main__':
    main()
