Sure! Based on the new files you’ve provided (the modules for generating questions and incorrect answers), I'll write an updated README that explains the functionality of your project. This will help others (or yourself) understand how to use the application and the overall project structure.

---

### **README.md**

```markdown
# Quiz Generation with Incorrect Answer Options

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
```

### Step 2: Set Up Virtual Environment (Optional, but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Make sure you have all the required dependencies by running:

```bash
pip install -r requirements.txt
```

This will install Flask, NLTK, Gensim, Spacy, and other dependencies required for the application.

### Step 4: Download Spacy Model

The application uses Spacy for Named Entity Recognition (NER). You will need to download the language model for Spacy:

```bash
python -m spacy download en_core_web_md
```

### Step 5: Run the Application

To start the web application, run:

```bash
python app.py
```

The application will be hosted on `http://127.0.0.1:5000/`.

## How the Application Works

### 1. **File Upload**
   - Navigate to the homepage (`/` route).
   - Upload a PDF or TXT document.
   
### 2. **Question Generation**
   - Once the file is uploaded, the content is extracted using PyPDF2 (for PDFs) or directly from the TXT file.
   - The text is processed to extract key entities and terms using Spacy's NER (Named Entity Recognition) and TF-IDF scoring.
   - These key terms are then used to generate quiz questions. For each question, the correct answer is replaced with a blank (underscore).

### 3. **Incorrect Answer Generation**
   - The correct answer is replaced with several incorrect options. These options are generated using the Gensim Word2Vec model by finding semantically similar words to the correct answer. 
   - If the model can't find enough alternatives, fallback logic is used to generate alternatives from the document itself.

### 4. **Answer Submission**
   - Users can answer the quiz questions and submit their responses.
   - The results page will show how many questions the user answered correctly.

## Project Structure

```plaintext
.
├── app.py                        # Main Flask app file
├── workers.py                    # Helper functions for file processing
├── question_extraction.py        # Extracts and ranks candidate keywords for questions
├── incorrect_answer_generation.py# Generates incorrect alternatives for correct answers
├── templates/                    # HTML templates for the web pages
│   ├── index.html                # Landing page (file upload form)
│   ├── quiz.html                 # Page displaying the generated quiz
│   └── result.html               # Page displaying the quiz results
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

### Explanation of Key Files:

- **`app.py`**: The main Flask web application, handling routes like file upload (`/`), quiz generation (`/quiz`), and result submission (`/result`).
- **`workers.py`**: Handles PDF/TXT content extraction and calling the `QuestionGeneration` class to generate questions.
- **`question_extraction.py`**: Implements logic to extract candidate keywords/entities from the document and rank them using TF-IDF scores to generate meaningful questions.
- **`incorrect_answer_generation.py`**: Uses Gensim's Word2Vec model to generate incorrect answers for the questions by finding semantically similar words.
- **`requirements.txt`**: List of required Python packages, including Flask, Spacy, Gensim, and NLTK.

## Libraries and Tools Used

- **Flask**: Web framework for the application.
- **Spacy**: NLP library for Named Entity Recognition (NER).
- **Gensim**: Used for word embeddings and similarity calculations.
- **NLTK**: Used for tokenizing sentences and words, as well as stopword filtering.
- **Scikit-learn**: For calculating TF-IDF scores.
- **PyPDF2**: For reading content from PDF files.

## Running Tests

You can add your test cases to ensure that the document parsing and question generation work as expected. The project currently does not include automated tests, but you can add tests to verify the correctness of:

- Text extraction (PDF or TXT).
- Question and answer generation.
- Incorrect option generation.
