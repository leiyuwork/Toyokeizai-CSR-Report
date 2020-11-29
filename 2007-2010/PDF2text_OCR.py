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

# 3.pdf原稿から画像への変換
images = convert_from_path(r'C:\Users\ray\Desktop\000\in\2007年 サントリー.pdf', poppler_path=r"C:\Program Files\poppler-\bin")
print(images)
for image in images:
    # 4.ＯＣＲ実行

    image_left = image.crop((0, 0, 715.5, 2023))
    builder = pyocr.builders.TextBuilder()
    result_left = tool.image_to_string(image, lang="jpn", builder=builder)

    image_right = image.crop((715.5, 0, 1431, 2023))
    builder = pyocr.builders.TextBuilder()
    result_right = tool.image_to_string(image, lang="jpn", builder=builder)

    result = result_left + result_right
    print(result)
