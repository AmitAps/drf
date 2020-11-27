#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 22:55:13 2020

@author: aps
"""

import requests

response = requests.get('https://api.github.com/events')

print(response.text)
print("----------------------------------------------------------------")
print(response.encoding)
print("----------------------------------------------------------------")
response.encoding = 'ISO-8859-1'
print(response.text)
print("----------------------------------------------------------------")
print(response.encoding)

"""
If you change the encoding, Requests will use the new value of response.encoding whenever you call r.text. 
"""

#Binary Response Content
print("----------------------------------------------------------------")
print(response.content)

"""
to create an image from binary data returned by a request, you can use the following code
"""

from PIL import Image
from io import BytesIO
i = Image.open(BytesIO(response.content))

