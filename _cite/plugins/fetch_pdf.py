
import os
import yaml
import requests

# Paths
INPUT_FILE = '/home/abdenour/Documents/infolab website/academix0.github.io/_data/citations.yaml'
OUTPUT_FILE = '/home/abdenour/Documents/infolab website/academix0.github.io/_data/sources.yaml'
PDF_DIR = 'pdf'
UNPAYWALL_API = 'https://api.unpaywall.org/v2/{}?email=abdenour@skku.edu'  # Replace with your email

# Ensure pdf directory exists
os.makedirs(PDF_DIR, exist_ok=True)

# Load YAML input
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    papers = yaml.safe_load(f)

sources = []

def download_pdf_from_unpaywall(doi):
    try:
        url = UNPAYWALL_API.format(doi)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        pdf_url = None
        if data.get('best_oa_location') and data['best_oa_location'].get('url_for_pdf'):
            pdf_url = data['best_oa_location']['url_for_pdf']

        if not pdf_url:
            print(f"[!] No open access PDF found for {doi}")
            return None

        filename = f"{doi.split('/')[-1].replace('.', '_')}.pdf"
        pdf_path = os.path.join(PDF_DIR, filename)

        print(f"[*] Downloading PDF for {doi} from {pdf_url}")
        pdf_response = requests.get(pdf_url)
        pdf_response.raise_for_status()

        with open(pdf_path, 'wb') as f:
            f.write(pdf_response.content)

        return filename

    except Exception as e:
        print(f"[!] Error for DOI {doi}: {e}")
        return None

# Process each paper
for paper in papers:
    doi = paper.get('id', '').replace('doi:', '')
    filename = download_pdf_from_unpaywall(doi)
    if filename:
        sources.append({
            'id': f"doi:{doi}",
            'image': '',
            'buttons': [
                {
                    'type': 'pdf',
                    'link': f'pdf/{filename}'
                }
            ]
        })

# Save to sources.yaml
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    yaml.dump(sources, f, sort_keys=False, allow_unicode=True)

print(f"\n[✓] Updated '{OUTPUT_FILE}' with {len(sources)} entries.")
