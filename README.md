# NLP Classic Text Analysis

A Natural Language Processing (NLP) project that performs syntax parsing and chunk frequency analysis on classic literature using NLTK.

This project analyzes texts such as *The Picture of Dorian Gray* and *The Iliad* by:

- Loading and preprocessing text
- Sentence and word tokenization
- Part-of-speech (POS) tagging
- Noun Phrase (NP) chunking
- Verb Phrase (VP) chunking
- Chunk frequency analysis
- Automated report generation
- CSV exports
- Visualization generation

---

## Project Overview

The goal of this project is to demonstrate a complete NLP pipeline that transforms raw literary text into meaningful syntactic insights.

Rather than manually reading thousands of lines of text, the application automatically identifies frequently occurring noun phrases and verb phrases, helping uncover narrative patterns, recurring themes, and important concepts.

---

## Features

### Text Processing

- Load text from Project Gutenberg sources
- Convert text to lowercase
- Sentence tokenization
- Word tokenization

### Linguistic Analysis

- Part-of-speech tagging using NLTK
- Noun phrase chunking
- Verb phrase chunking
- Frequency analysis

### Automated Outputs

- Console summaries
- Text reports
- CSV exports
- Frequency visualization charts

---

## Project Structure

nlp-classic-text-analysis/
│
├── archive/
│   └── Discover Insights into Classic Texts_Solution.ipynb
│
├── data/
│   ├── raw/
│   │   ├── dorian_gray.txt
│   │   ├── the_iliad.txt
│   │   └── my_text.txt
│   │
│   └── processed/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_tokenization.ipynb
│   └── 03_chunk_analysis.ipynb
│
├── outputs/
│   ├── figures/
│   │   ├── noun_phrase_frequency.png
│   │   └── verb_phrase_frequency.png
│   │
│   ├── reports/
│   │   └── chunk_analysis_report.txt
│   │
│   └── results/
│       ├── noun_phrase_counts.csv
│       └── verb_phrase_counts.csv
│
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── chunk_counters.py
│   ├── chunking.py
│   ├── preprocessing.py
│   └── utils.py
│
├── tests/
│
├── .gitignore
├── CHANGELOG.md
├── LICENSE
├── README.md
├── main.py
└── requirements.txt

---

## NLP Pipeline

Raw Text
    ↓
Load Text
    ↓
Sentence Tokenization
    ↓
Word Tokenization
    ↓
POS Tagging
    ↓
Noun Phrase Chunking
    ↓
Verb Phrase Chunking
    ↓
Frequency Analysis
    ↓
Reports / CSVs / Visualizations

---

## Technologies Used

- Python
- NLTK
- Pandas
- Matplotlib
- Pytest
- Jupyter Notebook

---

## Installation

Clone the repository:

git clone <repository-url>
cd nlp-classic-text-analysis

Create a virtual environment:

python -m venv venv

Activate the virtual environment:

### Windows

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## Required NLTK Resources

Run Python:

import nltk

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("averaged_perceptron_tagger")
nltk.download("averaged_perceptron_tagger_eng")

---

## Running the Project

Execute:

python main.py

Example output:

Tokenized 6492 sentences.
POS tagged 6492 sentences.

Top Noun Phrase Chunks:
----------------------------------------
965 | ('i')
202 | ('henry')
198 | ('lord')

Results saved successfully.

---

## Generated Outputs

### Report

outputs/reports/chunk_analysis_report.txt

Contains:

- Top noun phrase chunks
- Top verb phrase chunks
- Frequency statistics

### CSV Exports

outputs/results/noun_phrase_counts.csv
outputs/results/verb_phrase_counts.csv

Useful for additional analysis in:

- Excel
- Power BI
- Python
- Tableau

### Visualizations

outputs/figures/noun_phrase_frequency.png
outputs/figures/verb_phrase_frequency.png

Generated automatically after each execution.

---

## Key Findings from The Picture of Dorian Gray

The analysis identified several dominant noun phrases, including:

- Henry
- Lord
- Dorian Gray
- Life
- Basil

This suggests a strong focus on character-driven interactions and recurring philosophical themes throughout the novel.

---

## Future Improvements

Potential enhancements include:

- Improved chunk grammars
- Named Entity Recognition (NER)
- Character relationship analysis
- Sentiment analysis
- Multi-novel comparison dashboards
- Interactive visualizations

---

## Testing

Run tests using:

python -m pytest

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

## Author

**Wayne Franz**

Portfolio project created as part of an NLP and Machine Learning learning journey, demonstrating practical Natural Language Processing techniques, software engineering best practices, and reproducible analytical workflows.
