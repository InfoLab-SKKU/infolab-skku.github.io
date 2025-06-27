import os
import re
import yaml
from PyPDF2 import PdfReader

def extract_doi_from_text(text):
    # Look for DOI pattern
    match = re.search(r'\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b', text)
    if match:
        return match.group(0)

    # Look for "Digital Object Identifier" followed by a DOI
    match = re.search(r'Digital Object Identifier[:\s]*\b(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)\b', text, re.IGNORECASE)
    if match:
        return match.group(1)

    return None

def extract_doi_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages[:2]:  # Check first 2 pages
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return extract_doi_from_text(text)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def create_yaml_entry(doi, pdf_filename):
    return {
        'id': f'doi:{doi}',
        'image': '',  # Placeholder
        'buttons': [
            {
                'type': 'pdf',
                'link': f'pdf/{pdf_filename}'
            }
        ]
    }

def main(pdf_dir, output_yaml):
    entries = []

    for filename in os.listdir(pdf_dir):
        if filename.lower().endswith('.pdf'):
            file_path = os.path.join(pdf_dir, filename)
            doi = extract_doi_from_pdf(file_path)
            if doi:
                print(f"[✓] Found DOI: {doi} in {filename}")
                entry = create_yaml_entry(doi, filename)
                entries.append(entry)
            else:
                print(f"[✗] No DOI found in {filename}")

    with open(output_yaml, 'w') as f:
        yaml.dump(entries, f, sort_keys=False)

if __name__ == '__main__':
    pdf_directory = '/home/abdenour/Documents/infolab website/academix0.github.io/pdf'  # Your directory
    output_yaml_file = 'papers.yaml'
    main(pdf_directory, output_yaml_file)
