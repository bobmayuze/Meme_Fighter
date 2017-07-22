# coding:utf-8

import ocr


print ocr.picpath2words(r'tests/assets/ocr.jpeg')
print ocr.picurl2words('https://test.hi2go.com/ocr.jpeg')
print ocr.picpath2words(r'tests/assets/ocr1.png')
print ocr.picurl2words('https://test.hi2go.com/ocr1.png')
print ocr.picpath2words(r'tests/assets/ocr3.jpg')
print ocr.picurl2words('https://test.hi2go.com/ocr3.jpg')
