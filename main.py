import PyPDF2
import os

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as f:
            merger.append(f)
            print(f"Added: {pdf}")

    with open(output_path, 'wb') as f_out:
        merger.write(f_out)
        print(f"Merged PDF saved to: {output_path}")

# Example usage
if __name__ == "__main__":
    # List of PDF files to merge (ensure the order is correct)
    pdf_files = [
    r"C:\Users\Tamim\Desktop\Linux\1-270.pdf", #copy the pdf file path 
    r"C:\Users\Tamim\Desktop\Linux\271-300.pdf" #copy the pdf file path 
]


    output_file = r"C:\Users\Tamim\Desktop\Linux\1-300.pdf" #writh the file path of the merged pdf where you want to save
    merge_pdfs(pdf_files, output_file)
