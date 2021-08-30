#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:41:14 2021

@author: chenyuxuan
"""

def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("9 - Quit")
        choice = int(input("Make a choice: ")) # so that can compare against 9 later
        print(type(choice)) #check: choice was a string
        if choice == 9: # double equal sign for comparison
            keep_running = False
        elif choice == 1:
            HDL_Driver()
            
    print(choice)
    return choice

def HDL_Driver():
    HDL_value = hdl_input()
    HDL_character = hdl_analysis(HDL_value)
    hdl_output(HDL_value, HDL_character)
    
def hdl_input():
    hdl_value = int(input(("Enter HDL Value:")))
    return hdl_value

def hdl_analysis(HDL_value):
    if HDL_value >= 60:
        return "Normal"
    elif 40 <= HDL_value < 60:
        return "Borderline Low"
    else:
        return "Low"

def hdl_output(HDL_value, HDL_answer):
    print("The HDl value of {} is considered {}".format(HDL_value, HDL_answer))


interface()