import logging
logging.getLogger("PyPDF2").setLevel(logging.ERROR)

import os
import json
import time
import warnings
from utils import extract_sections_from_pdf
from processor import rank_sections

warnings.filterwarnings("ignore", message="FloatObject.*invalid; use 0.0 instead")
# ...rest of your code...
def main():
    input_dir = "input"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    persona = "PhD Researcher in Computational Biology"
    job = "Prepare a literature review focusing on methodologies, datasets, and performance benchmarks"

    all_sections = []
    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            full_path = os.path.join(input_dir, file)
            all_sections.extend(extract_sections_from_pdf(full_path))
    start = time.time()
    ranked = rank_sections(all_sections, persona, job)
    end = time.time()

    output_data = {
        "metadata": {
            "input_documents": [f for f in os.listdir(input_dir) if f.endswith(".pdf")],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
            "processing_time_sec": round(end - start, 2)
        },
        "extracted_sections": [
            {
                "document": r["document"],
                "page": r["page"],
                "section_title": r["section_title"],
                "importance_rank": round(r["importance_rank"], 4)
            } for r in ranked
        ],
        "subsection_analysis": [
            {
                "document": r["document"],
                "refined_text": r["full_text"][:300],
                "page": r["page"]
            } for r in ranked
        ]
    }

    with open(os.path.join(output_dir, "output.json"), "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

if __name__ == "__main__":
    main()