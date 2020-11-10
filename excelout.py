import re
import os
from openpyxl import load_workbook

path_text = r'C:\Users\ray\OneDrive\test\text\\'

files = os.listdir(path_text)  # txt file directory
pattern_1 = re.compile(r'人材活用 環境 企業統治 社会性\s\w{1,4}\s\w{1,4}\s\w{1,4}\s\w{1,4}\s[^a-zA-Z]{4,20}')  # re pattern
pattern_2 = re.compile(r'人材活用 環境 企業統治 社会性\s.{4,20}')  # re pattern

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
        result = pattern_1.findall(data)

        if len(result) == 0:
            result = pattern_2.findall(data)
            if len(result) == 0:
                print(textfile + 'is empty or different pattern')
                result.append('empty or different pattern')
                text.append(result[0])
            else:
                text.append(result[0])
        else:
            text.append(result[0])

        print(text)
        wb = load_workbook(r'C:/Users/ray/OneDrive/test/excel/appending.xlsx')
        sheet = wb.active
        sheet.append(text)

        wb.save(r'C:/Users/ray/OneDrive/test/excel/appending.xlsx')




