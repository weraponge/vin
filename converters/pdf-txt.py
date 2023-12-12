
import sys
import PyPDF2

def pdf_to_text(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if reader.is_encrypted:
            # If encrypted, try decrypting it (assuming no password is set)
            reader.decrypt('')

        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <pdf_file_path>")
        sys.exit(1)

    pdf_file = sys.argv[1]
    pdf_text = pdf_to_text(pdf_file)
    print(pdf_text)
