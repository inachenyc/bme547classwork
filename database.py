#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 12:15:37 2021

@author: chenyuxuan
"""

#print("This is the database.py module")
#print("It's name is {}".format(__name__))

import blood_calculator as bc #so that can type less everytime you call a function in this module later
#from blood_calculator import hdl_analysis # only imports hdl function
#from blood_calculator import * # this is easier but bad, b/c if import multiple modules, latter will override
#answer = hdl_analysis(55)
#print("The analysis of 55 HDL is {}".format(answer))
#answer2 = ldl_analysis(200)

answer = bc.hdl_analysis(55)
print("The analysis of 55 HDL is {}".format(answer))

answer2 = bc.ldl_analysis(200)