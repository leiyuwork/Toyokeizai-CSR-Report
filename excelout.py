import re
import os
from openpyxl import load_workbook

path_text = r'C:\Users\ray\OneDrive\test\text\\'
files = os.listdir(path_text)  # txt file directory
pattern = re.compile(r'人材活用 環境 企業統治 社会性\s\w{1,4}\s\w{1,4}\s\w{1,4}\s\w{1,4}\s[^a-zA-Z]{4,20}')  # re pattern

for textfile in files:  # for every txt file
    print(textfile)
    with open(path_text + textfile, "r", encoding="utf-8_sig") as f:

        text = []
        line = f.readlines()
        stock_code = line[0]
        name = line[1]

        text.append(stock_code)
        text.append(name)

        f.seek(0)  # read txt file again by other read method

        data = f.read()
        result = pattern.findall(data)
        text.append(result[0])

        print(text)
        wb = load_workbook(r'C:/Users/ray/OneDrive/test/excel/appending.xlsx')
        sheet = wb.active
        sheet.append(text)

        wb.save(r'C:/Users/ray/OneDrive/test/excel/appending.xlsx')




