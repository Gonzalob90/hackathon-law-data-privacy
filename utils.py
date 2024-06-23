"""
utils.py
"""
from PyPDF2 import PdfReader
import io

def read_pdf(uploaded_file):
    bytes_array = uploaded_file.read()
    data_stream = io.BytesIO(bytes_array)
    reader = PdfReader(data_stream)
    number_of_pages = len(reader.pages)
    list_extracted_text = []
    for page_index in range(number_of_pages):
        page = reader.pages[page_index]
        text = page.extract_text()
        list_extracted_text.append(text)

    extracted_text = "\n\n".join(list_extracted_text)
    return extracted_text

