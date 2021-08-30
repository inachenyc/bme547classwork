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
            
    print(choice)
    return choice


interface()