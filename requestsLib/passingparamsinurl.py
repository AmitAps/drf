#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:52:59 2020

@author: aps
"""

import requests

payload = {'Username': 'username', 'Password': 'password'}
r = requests.post('https://www.facebook.com/login', params=payload)
print(r.status_code)
print(r.headers)
print('--------------------------------------------------------------------')
print(r.headers['Content-Type'])

print('--------------------------------------------------------------------')

print(r.text)
print('--------------------------------------------------------------------')
print(r.url)

#You can also pass a list of items as a value:

payload_01 = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('https://httpbin.org/get', params=payload_01)
print(r.url)