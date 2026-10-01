from pypdf import PdfReader

pdf_file = input("Enter PDF file name: ")
text_file = input("Enter output text file name: ")

reader = PdfReader(pdf_file)

with open(text_file, "w", encoding="urf-8") as file:
    for page in reader.pages:
        text = page.extract_text()
        if text:
            file.write(text)
            file.write('\n')
            
print("Pdf converted to text successfully!")