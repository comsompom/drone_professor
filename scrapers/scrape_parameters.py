"""
Ardupilot Parameters Web Scraper
Scrapes parameter data from Ardupilot documentation and saves to JSON
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from typing import Dict, List, Any


class ArdupilotParameterScraper:
    def __init__(self):
        self.base_url = "https://ardupilot.org/plane/docs/parameters-Plane-stable-V4.6.3.html"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def scrape_parameters(self) -> List[Dict[str, Any]]:
        """
        Scrape all parameters from Ardupilot documentation
        Returns list of parameter dictionaries
        """
        print(f"Fetching parameters from {self.base_url}...")

        try:
            response = requests.get(self.base_url, headers=self.headers, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'lxml')
            parameters = []

            # Find all parameter sections
            # Parameters are typically in tables or definition lists
            param_tables = soup.find_all('table', class_='docutils')

            for table in param_tables:
                rows = table.find_all('tr')

                for row in rows[1:]:  # Skip header row
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        param_name = cols[0].get_text(strip=True)
                        param_desc = cols[1].get_text(strip=True)

                        # Extract values if available
                        param_values = []
                        if len(cols) >= 3:
                            values_text = cols[2].get_text(strip=True)
                            param_values = [v.strip() for v in values_text.split(',') if v.strip()]

                        parameters.append({
                            'name': param_name,
                            'description': param_desc,
                            'values': param_values,
                            'category': self._extract_category(param_name)
                        })

            # Also look for definition lists (dl/dt/dd structure)
            param_lists = soup.find_all('dl', class_='docutils')

            for dl in param_lists:
                terms = dl.find_all('dt')
                descriptions = dl.find_all('dd')

                for term, desc in zip(terms, descriptions):
                    param_name = term.get_text(strip=True)
                    param_desc = desc.get_text(strip=True)

                    # Extract possible values from description
                    param_values = self._extract_values_from_description(param_desc)

                    parameters.append({
                        'name': param_name,
                        'description': param_desc,
                        'values': param_values,
                        'category': self._extract_category(param_name)
                    })

            # Look for section-based parameters
            sections = soup.find_all(['section', 'div'], class_=['section'])

            for section in sections:
                section_title = section.find(['h1', 'h2', 'h3', 'h4'])
                category = section_title.get_text(strip=True) if section_title else 'General'

                # Find parameters in this section
                param_elements = section.find_all(['p', 'div'], class_=['parameter', 'param'])

                for elem in param_elements:
                    param_text = elem.get_text(strip=True)

                    # Parse parameter format: PARAM_NAME: description
                    if ':' in param_text:
                        parts = param_text.split(':', 1)
                        param_name = parts[0].strip()
                        param_desc = parts[1].strip() if len(parts) > 1 else ''

                        param_values = self._extract_values_from_description(param_desc)

                        parameters.append({
                            'name': param_name,
                            'description': param_desc,
                            'values': param_values,
                            'category': category
                        })

            print(f"Successfully scraped {len(parameters)} parameters")
            return parameters

        except Exception as e:
            print(f"Error scraping parameters: {e}")
            return []

    def _extract_category(self, param_name: str) -> str:
        """Extract category from parameter name prefix"""
        if '_' in param_name:
            return param_name.split('_')[0]
        return 'General'

    def _extract_values_from_description(self, description: str) -> List[str]:
        """Extract possible values from parameter description"""
        values = []

        # Look for common patterns like "0:Disabled, 1:Enabled"
        if ':' in description and ',' in description:
            parts = description.split(',')
            for part in parts:
                if ':' in part:
                    value = part.split(':')[0].strip()
                    if value.replace('.', '').replace('-', '').isdigit():
                        values.append(value)

        # Look for range patterns like "0 to 100"
        if ' to ' in description.lower():
            import re
            range_match = re.search(r'(\d+(?:\.\d+)?)\s+to\s+(\d+(?:\.\d+)?)', description, re.IGNORECASE)
            if range_match:
                values.append(f"Range: {range_match.group(1)} to {range_match.group(2)}")

        return values

    def save_to_json(self, parameters: List[Dict[str, Any]], filename: str = 'ardupilot_parameters.json'):
        """Save parameters to JSON file"""
        output_path = f'/workspace/app-b6ukc6ytkow1/backend/data/{filename}'

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump({
                'parameters': parameters,
                'total_count': len(parameters),
                'scraped_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                'source_url': self.base_url
            }, f, indent=2, ensure_ascii=False)

        print(f"Parameters saved to {output_path}")


def main():
    scraper = ArdupilotParameterScraper()
    parameters = scraper.scrape_parameters()

    if parameters:
        scraper.save_to_json(parameters)
        print(f"\nSample parameters:")
        for param in parameters[:5]:
            print(f"  - {param['name']}: {param['description'][:80]}...")
    else:
        print("No parameters scraped. Please check the URL and HTML structure.")


if __name__ == '__main__':
    main()
