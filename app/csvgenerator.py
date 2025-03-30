import os
import zipfile
import tabula
import pandas as pd

def convert_pdf_to_csv(pdf_path: str, csv_path: str):
    """
    Converte um arquivo PDF em um arquivo CSV.
    """
    tabula.convert_into(pdf_path, csv_path, output_format="csv", pages="all")
    print(f"CSV gerado: {csv_path}")

def zip_csv_file(csv_path: str, zip_path: str):
    """
    Compacta um arquivo CSV dentro de um arquivo ZIP.
    """
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_path, os.path.basename(csv_path))
    print(f"Arquivo ZIP criado: {zip_path}")

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