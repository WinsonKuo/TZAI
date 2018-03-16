# -*- coding: UTF-8 -*-
import pyperclip
import re
import random

def replace(m):
    text = ''
    count = 0
    EOS = len(m)
    for piece in m:
        count = count + 1
        seed = random.randint(0,1)
        if seed:
            x = '再'
        else:
            x = '在'
        if count == EOS:
            text = text + piece
        else:
            text = text + piece + x
    return text

text = pyperclip.paste()
m = re.split('在|再', text)
text = replace(m)
print(text)
