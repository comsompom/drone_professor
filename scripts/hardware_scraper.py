import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import json
import time

# Main URL containing the list of hardware
MAIN_URL = "https://ardupilot.org/plane/docs/common-autopilots.html"


def get_hardware_links():
    print(f"Fetching main hardware list from {MAIN_URL}...")
    response = requests.get(MAIN_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the Open Hardware section (Sphinx generates IDs for headers)
    open_hw_section = soup.find(id="open-hardware")

    # If the ID changes or isn't found, fallback to the whole page
    container = open_hw_section.parent if open_hw_section else soup

    # Find all internal links (ArduPilot docs use the class 'reference internal')
    links = container.find_all('a', class_='reference internal')

    hw_urls = {}
    for a in links:
        href = a.get('href')
        name = a.get_text(strip=True)
        # Filter out anchor links and ensure it points to a hardware page
        if href and not href.startswith('#') and 'common-' in href:
            full_url = urljoin(MAIN_URL, href)
            if full_url not in hw_urls.values():
                hw_urls[name] = full_url

    print(f"Found {len(hw_urls)} hardware pages to scrape.")
    return hw_urls


def parse_hardware_page(name, url):
    print(f"Scraping: {name}...")
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
    except Exception as e:
        print(f"  [!] Failed to fetch {url}: {e}")
        return None

    soup = BeautifulSoup(res.text, 'html.parser')

    data = {
        "hardware_name": name,
        "source_url": url,
        "description": "",
        "specifications": "",
        "ports_and_uarts": "",
        "other_sections": {}
    }

    # The main text content in Ardupilot docs is usually within a role="main" or div with itemprop="articleBody"
    main_content = soup.find('div', itemprop='articleBody') or soup.find('div', class_='document')
    if not main_content:
        return data

    # 1. Extract Main Description (Paragraphs directly under H1)
    h1 = main_content.find('h1')
    if h1:
        curr = h1.find_next_sibling()
        desc_texts = []
        while curr and curr.name not in ['h1', 'h2', 'h3', 'section']:
            if curr.name == 'p':
                desc_texts.append(curr.get_text(strip=True))
            curr = curr.find_next_sibling()
        data["description"] = "\n".join(desc_texts)

    # 2. Extract Sections (H2 and H3)
    for header in main_content.find_all(['h2', 'h3']):
        section_title = header.get_text(strip=True).replace('¶', '')
        section_content = []

        # Grab elements until the next header
        curr = header.find_next_sibling()
        while curr and curr.name not in ['h1', 'h2', 'h3', 'h4', 'section']:
            if curr.name == 'p':
                section_content.append(curr.get_text(strip=True))
            elif curr.name == 'ul':
                for li in curr.find_all('li'):
                    section_content.append(f"- {li.get_text(strip=True)}")
            elif curr.name == 'table':
                # Parse tables (crucial for UART mappings)
                for row in curr.find_all('tr'):
                    row_data = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                    section_content.append(" | ".join(row_data))
            curr = curr.find_next_sibling()

        text_content = "\n".join(section_content)
        if not text_content.strip():
            continue

        # 3. Categorize into specific KB fields for the LLM
        lower_title = section_title.lower()
        if 'spec' in lower_title or 'feature' in lower_title:
            data["specifications"] += f"**{section_title}**\n{text_content}\n\n"
        elif any(keyword in lower_title for keyword in ['uart', 'port', 'map', 'pin', 'serial']):
            data["ports_and_uarts"] += f"**{section_title}**\n{text_content}\n\n"
        else:
            data["other_sections"][section_title] = text_content

    return data


def build_hardware_kb():
    urls = get_hardware_links()
    kb_data = []

    for name, url in urls.items():
        hw_data = parse_hardware_page(name, url)
        if hw_data:
            kb_data.append(hw_data)
        time.sleep(0.5)  # Be polite to ArduPilot servers

    # Save to JSON
    with open('ardupilot_hardware_kb.json', 'w', encoding='utf-8') as f:
        json.dump(kb_data, f, indent=4)

    # Save to Markdown (Optimized for LLM Context & Vector Databases)
    with open('ardupilot_hardware_kb.md', 'w', encoding='utf-8') as f:
        f.write("# ArduPilot Hardware & Flight Controller Knowledge Base\n\n")
        for hw in kb_data:
            f.write(f"## {hw['hardware_name']}\n")
            f.write(f"**Source URL:** {hw['source_url']}\n\n")
            f.write(f"### Description\n{hw['description']}\n\n")

            if hw['specifications']:
                f.write(f"### Specifications\n{hw['specifications']}\n")

            if hw['ports_and_uarts']:
                f.write(f"### Ports, UARTs & Pin Mapping\n{hw['ports_and_uarts']}\n")

            f.write("\n---\n\n")

    print("\nSuccess! Saved 'ardupilot_hardware_kb.json' and 'ardupilot_hardware_kb.md'.")


if __name__ == "__main__":
    build_hardware_kb()
