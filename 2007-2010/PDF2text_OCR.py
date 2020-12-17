import os
import pyocr.builders
from pdf2image import convert_from_path

path_in = r"C:\Users\Ray94\Downloads\in\\"  # Original CSR PDF file path
path_text = r"C:\Users\Ray94\Downloads\out\\"  # Text file path

# 1.インストール済みのTesseractのパスを通す
path_tesseract = r"C:\\Program Files (x86)\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

# 2.OCRエンジンの取得
tools = pyocr.get_available_tools()
tool = tools[0]

# 3.pdf原稿から画像への変換
infiles = os.listdir(path_in)
for infile in infiles:
    text = []
    print(infile)
    images = convert_from_path(path_in+infile, poppler_path=r"C:\Program Files\poppler-\bin")

    for image in images:
        # 4.ＯＣＲ実行

        image_left = image.crop((0, 0, 715.5, 2023))
        builder = pyocr.builders.TextBuilder()
        result_left = tool.image_to_string(image_left , lang="jpn", builder=builder)
        text.append(result_left)

        image_right = image.crop((715.5, 0, 1431, 2023))
        builder = pyocr.builders.TextBuilder()
        result_right = tool.image_to_string(image_right, lang="jpn", builder=builder)
        text.append(result_right)

    with open(path_text + infile + ".txt","wb+") as f:
        for t in text:
            f.write(str(t).encode('utf8'))
