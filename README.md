# 📚 Document Analyst – Smart PDF Section Extractor & Ranker

![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg?logo=python)
![License](https://img.shields.io/github/license/turagavishnusahitya/document-analyst)
![Issues](https://img.shields.io/github/issues/turagavishnusahitya/document-analyst)

**Document Analyst** is an intelligent tool designed to analyze multiple PDF documents and extract the most relevant sections based on user intent. Whether you're a researcher or data analyst, this tool helps you skip the fluff and focus only on the content that truly matters.

---

## 🧠 What This Project Does (In Simple Terms)

Imagine a user says:

> “I’m a PhD researcher in computational biology. I want to prepare a literature review and need sections from documents that talk about methodologies, datasets, and benchmarks.”

This system:

- Reads through all PDFs in the input folder
- Extracts structured sections and paragraphs
- Matches content against the **persona** and **job-to-be-done**
- Ranks each section based on **text similarity**
- Returns the **most relevant sections in a JSON file**

---

## ⚙️ How It Works (Approach)

### 1️⃣ Extraction Module

- Loads PDFs from `/input` folder  
- Extracts headings, sections, and paragraphs using font styles  
- Labels sections with heading levels (H1, H2, etc.) and page numbers  

### 2️⃣ Ranking Module

- Uses `persona` and `goal` (defined in `app.py`)  
- Applies **TF-IDF vectorization** to compute similarity  
- Ranks sections and outputs top results to `results.json`  

---

## 🧰 Tools & Libraries Used

| Library / Tool      | Purpose                                      |
|---------------------|----------------------------------------------|
| **PyMuPDF (fitz)**  | Extract text and structure from PDFs         |
| **scikit-learn**    | TF-IDF vectorization for similarity scoring  |
| **Python 3.10**     | Core programming language                    |
| **Docker**          | Easy deployment and isolated environment     |

> 💡 **Note:** The system runs fully **offline**—no cloud or API dependencies.

---

## 📁 Folder Structure

```
document-analyst1/
├── input/            # Put your PDFs here
├── output/           # Final results appear here (results.json)
├── app.py            # Main runner script
├── utils.py          # PDF reading & section extraction
├── processor.py      # TF-IDF scoring & ranking
├── Dockerfile        # Docker setup for containerization
├── requirements.txt  # Python dependencies
```

---

## 🐳 How to Use with Docker

### 🏗️ Step 1: Build the Docker Image

```bash
docker build -t doc-analyst .
```

### ▶️ Step 2: Run the App

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  doc-analyst
```

✅ Place your PDF files in the `input/` folder  
📝 Edit the `persona` and `goal` inside `app.py`  
📄 Final results will appear in `output/results.json`

---

## 📤 Sample Output (`results.json`)

```json
[
  {
    "title": "Methodology Overview",
    "page_number": 4,
    "score": 0.92,
    "snippet": "This section describes the algorithms and tools used in the analysis..."
  },
  {
    "title": "Benchmark Datasets Used",
    "page_number": 6,
    "score": 0.87,
    "snippet": "We evaluated our model on several public datasets such as BioMed and GenBank..."
  }
]
```

---

## 💡 Key Benefits

- 🔍 Automatically extracts **only relevant sections**
- 📄 Supports **multiple PDFs (3–10 files)**
- 🧪 Works offline, no internet required
- 🐳 Dockerized and easy to run anywhere
- ⚡ Fast: Outputs in **under 60 seconds**
- 🧩 Easily extendable for other **personas/goals**

---

## 🧑‍🎓 Persona & Goal (Editable in app.py)

```python
persona = "PhD Researcher in Computational Biology"
job_to_be_done = "Prepare a literature review focusing on methodologies, datasets, and performance benchmarks"
```

Modify these fields in `app.py` to suit your own needs!

---

## 🤝 Contributing

We welcome contributions to make this better!  
To contribute:

1. Fork this repository  
2. Create a feature branch (`git checkout -b feature-xyz`)  
3. Commit your changes (`git commit -m 'Add new feature'`)  
4. Push and create a pull request  

---

## 🧑‍💻 Author

**Turaga Vishnu Sahitya**  
📫 [turagavishnusahitya@gmail.com](mailto:turagavishnusahitya@gmail.com)  
🔗 [GitHub Profile](https://github.com/turagavishnusahitya)

