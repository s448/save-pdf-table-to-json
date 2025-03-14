import tabula

pdf_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

dfs = tabula.read_pdf(pdf_path,pages=1, stream=True,output_format="json")
# read_pdf returns list of DataFrames


tabula.convert_into(pdf_path, "test.json", output_format="json", stream=True)