import os
import zipfile
import tabula
import pandas as pd

# function to convert pdf file into a csv with tabula dependency
def convert_pdf_to_csv(pdf_path: str, csv_path: str):
    """
    Converte um arquivo PDF em um arquivo CSV.
    """
    tabula.convert_into(pdf_path, csv_path, output_format="csv", pages="all")
    print(f"CSV gerado: {csv_path}")

# function to send csv file to a zip file with zipfile dependency
def zip_csv_file(csv_path: str, zip_path: str):
    """
    Compacta um arquivo CSV dentro de um arquivo ZIP.
    """
    #writes the csv file into the zip file
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf: 
        zipf.write(csv_path, os.path.basename(csv_path))
    print(f"Arquivo ZIP criado: {zip_path}")

# main function to convert Anexo_1 pdf tables into a csv structured table 
def main():
    """
    Função principal para executar a conversão e compressão.
    """
    pdf_path = os.path.join("data", "raw", "Anexo_1.pdf")
    csv_path = "Anexo_1_Table.csv"
    zip_path = "Anexo_1_Table.zip"

    convert_pdf_to_csv(pdf_path, csv_path)
    zip_csv_file(csv_path, zip_path)

if __name__ == "__main__":
    main()