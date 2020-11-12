import re  # this module let you check if a particular string matches a given regular expression
import os  # os is for identifying file path.
from openpyxl import load_workbook  # A Python library to read/write Excel xlsx/xlsm files

path_text = r'C:\Users\ray\OneDrive\test\text\\'

files = os.listdir(path_text)  # txt file path
pattern_1 = re.compile(r'人材活用 環境 企業統治 社会性\s.{4,20}\s[^a-zA-Z]{4,20}')  # re pattern 01
pattern_2 = re.compile(r'人材活用 環境 企業統治 社会性\s.{4,20}')  # re pattern 02

for textfile in files:  # for each txt file
    print(textfile)  # confirm file name
    with open(path_text + textfile, "r", encoding="utf-8_sig") as f:
        # open files; "with open" method is convenient cuz there is no need to close file every time

        text = []  # List for matching result
        line = f.readlines()  # read txt file by lines
        stock_code = line[0]  # stock_code always in first line
        name = line[1]  # company name always in second line
        text.append(textfile)  # append file name in text
        text.append(stock_code)  # append stock_code in text
        text.append(name)   # append company name in text

        f.seek(0)  # read txt file again by other read method

        data = f.read()  # read whole txt
        result = pattern_1.findall(data)  # match pattern 01

        if len(result) == 0:  # if no result for pattern 01
            result = pattern_2.findall(data)  # then try another pattern
            if len(result) == 0:  # if still no result
                print("matching result in" + textfile + 'is null or need a different pattern')
                result.append('null or different pattern')
                text.append(result[0])
            else:  # if pattern 02 succeeded
                text.append(result[0])  # append matching result(02)
        else:  # if pattern 01 succeeded
            text.append(result[0])  # append matching result(02)

        print(text)  # confirm the matching result
        wb = load_workbook(r'C:/Users/ray/OneDrive/test/excel/appending.xlsx')  # open excel
        sheet = wb.active  # get the currently active sheet
        sheet.append(text)  # append matching result to excel sheet

        wb.save(r'C:/Users/ray/OneDrive/test/excel/appending.xlsx')  # save excel
