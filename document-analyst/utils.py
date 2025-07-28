from PyPDF2 import PdfReader

def extract_sections_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    sections = []
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            lines = text.split("\n")
            for line in lines:
                if is_section_heading(line):
                    sections.append({
                        "document": pdf_path.split("/")[-1],
                        "page": page_num + 1,
                        "section_title": line.strip(),
                        "full_text": text
                    })
    return sections

def is_section_heading(line):
    # Simple heading detection logic (customize as needed)
    return line.strip().lower().startswith((
        "introduction", "method", "dataset", "conclusion", "results", "background", "related work"
    ))