# Learning Game - Quiz generator

This project involves the generation of quiz questions from a given text document, where the document can either be a PDF or TXT file. It uses various NLP (Natural Language Processing) techniques, such as Named Entity Recognition (NER), TF-IDF, and word embeddings, to automatically generate multiple-choice questions with incorrect alternative answers.

The project consists of multiple modules:

1. **Question Extraction**: Extracts meaningful keywords and entities from the document, ranks them based on their significance, and formulates them into quiz questions.
2. **Incorrect Answer Generation**: Generates incorrect alternative answers for each quiz question using semantic similarity and word embeddings.
3. **Flask Web Application**: A web interface that allows users to upload a document (PDF or TXT), processes it, and generates quiz questions with multiple-choice options.

## Features

- Upload a document (PDF or TXT).
- Extract key information from the document.
- Generate multiple-choice quiz questions.
- Provide incorrect alternatives to the correct answer based on semantic similarity.
- Display the questions and options in a user-friendly web interface.

## Requirements

- Python 3.7+
- The application uses Flask for the web interface and other Python libraries for NLP tasks.

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/quiz-generator.git
cd quiz-generator
