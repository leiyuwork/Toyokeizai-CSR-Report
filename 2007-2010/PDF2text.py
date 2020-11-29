import os
import pyocr.builders
from pdf2image import convert_from_path


# 1.インストール済みのTesseractのパスを通す
path_tesseract = r"C:\\Program Files (x86)\\Tesseract-OCR"
if path_tesseract not in os.environ["PATH"].split(os.pathsep):
    os.environ["PATH"] += os.pathsep + path_tesseract

# 2.OCRエンジンの取得
tools = pyocr.get_available_tools()
tool = tools[0]

# 3.原稿画像の読み込み
images = convert_from_path(r'C:\Users\ray\Desktop\000\in\2007年 サントリー.pdf', poppler_path=r"C:\Program Files\poppler-\bin")
for image in images:
    # 4.ＯＣＲ実行
    builder = pyocr.builders.TextBuilder()
    result = tool.image_to_string(image, lang="jpn", builder=builder)

    print(result)
