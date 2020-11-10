# This script is for converting CSR PDF into text file.
# pdfplumber is a useful package for cropping pdf and extracting text.
# os is for identifying file path.
import pdfplumber
import os

path_in = r"C:\Users\ray\OneDrive\test\in\\"  # Original CSR PDF file path
path_text = r"C:\Users\ray\OneDrive\test\text\\"  # Afterwards text file path


infiles = os.listdir(path_in)
for infile in infiles:
    text = []  # buckets for text
    with pdfplumber.open(path_in + infile) as pdf:  # open all the files in Original CSR PDF file path
        for page_num in range(len(pdf.pages)):  # crop according the different page number
            #print("*********************"+str(page_num+1)+"********************************")  # from page 1 odd
            if (page_num % 2) == 0:
                page = pdf.pages[page_num]

                left = page.crop((0, 0, 252, 668))  # odd page, left side
                #print("*********************" + str(page_num + 1) + "left ********************************")
                #print(left.extract_text())
                text.append(left.extract_text())

                right = page.crop((252, 0, page.width, page.height))  # odd page, right side
                #print("*********************" + str(page_num + 1) + "right ********************************")
                #print(right.extract_text())
                text.append(right.extract_text())
            else:  # page 2 even
                page = pdf.pages[page_num]

                left = page.crop((0, 0, 262, 668))   # even page, left side
                #print("*********************" + str(page_num + 1) + "left ********************************")
                #print(left.extract_text())
                text.append(left.extract_text())

                right = page.crop((262, 0, page.width, page.height))  # even page, right side
                #print("*********************" + str(page_num + 1) + "right ********************************")
                #print(right.extract_text())
                text.append(right.extract_text())

    # write text to txt.file
    with open(path_text + infile + ".txt","wb+") as f:
            for t in text:
                f.write(str(t).encode('utf8'))







