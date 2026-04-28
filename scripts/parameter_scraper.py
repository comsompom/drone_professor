import requests
from bs4 import BeautifulSoup
import json

# The specific V4.6.3 Plane parameter URL
URL = "https://ardupilot.org/plane/docs/parameters-Plane-stable-V4.6.3.html"


def scrape_ardupilot_parameters():
    print(f"Downloading ArduPilot documentation from {URL}...")
    response = requests.get(URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    parameters = []

    print("Parsing HTML and extracting parameters...")
    # In Sphinx docs, parameters are usually in <h3> tags (e.g., "BATT_CAPACITY: Battery capacity")
    for h3 in soup.find_all('h3'):
        header_text = h3.get_text(strip=True).replace('¶', '')

        # Ensure it's an actual parameter (contains a colon)
        if ':' not in header_text:
            continue

        param_name, short_desc = header_text.split(':', 1)
        param_name = param_name.strip()

        # Initialize variables for extraction
        desc_lines = []
        metadata = {}

        # Iterate over the next siblings (paragraphs, tables) until the next header
        curr_node = h3.find_next_sibling()
        while curr_node and curr_node.name not in ['h1', 'h2', 'h3', 'section']:
            if curr_node.name == 'p':
                desc_lines.append(curr_node.get_text(strip=True))
            elif curr_node.name == 'table':
                # Extract Range, Increment, Units, Values from the table
                for tr in curr_node.find_all('tr'):
                    tds = tr.find_all(['th', 'td'])
                    if len(tds) >= 2:
                        key = tds[0].get_text(strip=True).replace(':', '')
                        val = tds[1].get_text(strip=True)
                        metadata[key] = val
            elif curr_node.name == 'ul':  # Sometimes values are stored in lists
                for li in curr_node.find_all('li'):
                    desc_lines.append("- " + li.get_text(strip=True))

            curr_node = curr_node.find_next_sibling()

        # Compile the parameter dictionary
        parameters.append({
            "parameter_name": param_name,
            "display_name": short_desc.strip(),
            "description": "\n".join(desc_lines),
            "attributes": metadata
        })

    return parameters


def build_knowledge_base(parameters):
    # 1. Save as JSON (Best for programmatic LLM tool calling)
    with open('ardupilot_kb.json', 'w', encoding='utf-8') as f:
        json.dump(parameters, f, indent=4)

    # 2. Save as Markdown (Best for Local LLM RAG ingestion / Vector DBs)
    with open('ardupilot_kb.md', 'w', encoding='utf-8') as f:
        f.write("# ArduPilot Plane Stable V4.6.3 - Parameter Knowledge Base\n\n")
        for p in parameters:
            f.write(f"## {p['parameter_name']}\n")
            f.write(f"**Display Name:** {p['display_name']}\n\n")
            f.write(f"**Description:**\n{p['description']}\n\n")
            if p['attributes']:
                f.write("**Specifications:**\n")
                for key, val in p['attributes'].items():
                    f.write(f"- **{key}:** {val}\n")
            f.write("\n---\n\n")


if __name__ == "__main__":
    params = scrape_ardupilot_parameters()
    build_knowledge_base(params)
    print(f"Successfully extracted {len(params)} parameters!")
    print("Saved 'ardupilot_kb.json' and 'ardupilot_kb.md'.")
