#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:45:43 2020

@author: aps
"""

import requests
response = requests.get("https://www.thesocialtalks.com")

print("Status Code",response.status_code) #print status code
print("Headers",response.headers) #print headers
print("-------------------------------------------------------------------------")
print('Content Type', response.headers['Content-Type']) #print content type
data = response.text
print("-------------------------------------------------------------------------")
print("Data", data)