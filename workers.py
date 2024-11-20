from PyPDF2 import PdfFileReader
from question_generation_main import QuestionGeneration

# The pdf2text function takes in the path of a file and its extension as arguments.
# It identifies the file type and extracts its contents. 
# If the file is a PDF, it uses the PdfReader module from the PyPDF2 library to read the contents of each page of the PDF 
# and concatenate them into a single string. 

def pdf2text(file_path: str, file_exten: str) -> str:
    """ Converts a given file to text content """

    _content = ''

    # Identify file type and get its contents
    if file_exten == 'pdf':
        with open(file_path, 'rb') as pdf_file:
            _pdf_reader = PdfFileReader(pdf_file)
            for p in range(_pdf_reader.numPages):
                _content += _pdf_reader.getPage(p).extractText()
            # _content = _pdf_reader.getPage(0).extractText()
            print('PDF operation done!')

    elif file_exten == 'txt':
        with open(file_path, 'r') as txt_file:
            _content = txt_file.read()
            print('TXT operation done!')

    return _content

def txt2questions(doc: str, n=5, o=4) -> dict:
    """ Get all questions and options """


    qGen = QuestionGeneration(n, o)
    q = qGen.generate_questions_dict(doc)
    for i in range(len(q)):
        temp = []
        for j in range(len(q[i + 1]['options'])):
            temp.append(q[i + 1]['options'][j + 1])
        q[i + 1]['options'] = temp
    return q

workers.py
Displaying app.py.
