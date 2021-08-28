# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:50:01 2021

@author: ARJYA
"""

#!pip install tika
from tika import parser
file = 'D:/TechQRT/pdf reading/book_without_pass.pdf'
file_data = parser.from_file(file)
text = file_data['content']
print(text)


s = text.split('\n\n')
print("_____________________________")
print(s)

for i in s:
    print(i)
    print("----------")
    
# 's' = FINAL LIST OF PARAGRAPHS