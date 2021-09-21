#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:41:14 2021

@author: chenyuxuan
"""
#print("This is the blood_calculator.py module")
#print("It's name is {}".format(__name__))


def interface():
    print("Blood Calculator")
    keep_running = True
    while keep_running:
        print("Make a choice")
        print("1 - HDL Analysis")
        print("2 - LDL Analysis")
        print("3 - Cholesterol Analysis")
        print("9 - Quit")
        choice = int(input("Make a choice: ")) # so that can compare against 9 later
        print(type(choice)) #check: choice was a string
        if choice == 9: # double equal sign for comparison
            keep_running = False
        elif choice == 1:
            HDL_Driver()
        elif choice == 2:
            LDL_Driver()
        elif choice == 3:
            CHOL_Driver() 
            
    print(choice)
    return choice

# HDL analysis
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
    print("The HDL value of {} is considered {}".format(HDL_value, HDL_answer))

# LDL analysis
def LDL_Driver():
    LDL_value = ldl_input()
    LDL_character = ldl_analysis(LDL_value)
    ldl_output(LDL_value, LDL_character)
    
def ldl_input():
    ldl_value = int(input(("Enter LDL Value:")))
    return ldl_value

def ldl_analysis(LDL_value):
    if LDL_value < 130:
        return "Normal"
    elif 130 <= LDL_value <= 159:
        return "Borderline High"
    elif 160 <= LDL_value <= 189:
        return "High"
    else:
        return "Very High"

def ldl_output(LDL_value, LDL_answer):
    print("The LDL value of {} is considered {}".format(LDL_value, LDL_answer))

# Cholesterol analysis
def CHOL_Driver():
    CHOL_value = chol_input()
    CHOL_character = chol_analysis(CHOL_value)
    chol_output(CHOL_value, CHOL_character)
    
def chol_input():
    chol_value = int(input(("Enter Cholesterol Value:")))
    return chol_value

def chol_analysis(CHOL_value):
    if CHOL_value < 200:
        return "Normal"
    elif 200 <= CHOL_value <= 239:
        return "Borderline High"
    else:
        return "High"

def chol_output(CHOL_value, CHOL_answer):
    print("The Cholesterol value of {} is considered {}".format(CHOL_value, CHOL_answer))


if __name__ == "__main__": #so that it doesn't run if this module is imported ?????????
    interface()

# stores python name for the current module,
# the first script you run is always given "__main__"
# the script you imported is given it actual name 
# so REMEMBER: always start script with those two lines!!!


def check_input(in_string): #check if input length <= 2
    if len(in_string) < 3:
        return True
    else:
        return False



