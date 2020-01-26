#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 22:57:36 2020

@author: laurafinger
"""

import random

messages = ['It is certain', 
            'It is decidely so',
            'Yes, defiiately',
            'Reply hazy, try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful',]
print(messages[random.randint(0, len(messages) - 1)])
spam = [0,1,2,3,4,5]