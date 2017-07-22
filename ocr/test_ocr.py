# coding:utf-8

import ocr


print 'Should pass ========================================'
print ocr.picpath2words(r'tests/assets/ocr.jpeg')
print ocr.picurl2words('https://test.hi2go.com/ocr.jpeg')
print ocr.picpath2words(r'tests/assets/ocr1.png')
print ocr.picurl2words('https://test.hi2go.com/ocr1.png')
print ocr.picpath2words(r'tests/assets/ocr2.jpg')
print ocr.picurl2words('https://test.hi2go.com/ocr2.jpg')

print "\nShould fail ========================================"
ocr.picpath2words(r'tests/assets/no_ocr.png')
ocr.picurl2words('https://test.hi2go.com/no_ocr.png')
