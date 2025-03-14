import tabula

pdf_path = "https://github.com/s448/save-pdf-table-to-json/blob/main/examle.pdf"

dfs = tabula.read_pdf(pdf_path,pages=1, stream=True,output_format="json")
# read_pdf returns list of DataFrames


tabula.convert_into(pdf_path, "test.json", output_format="json", stream=True)