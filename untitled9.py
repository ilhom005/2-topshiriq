# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FcHdD1e9oObCW9R_00Z_At3RB3_pFDwk
"""

import time

def svetafor():
    while True:
        print("Qizil")
        time.sleep(10)

        print("Sariq")
        time.sleep(3)

        print("Yashil")
        time.sleep(10)

        user_input = input("Dastur to'xtatilsinmi? (ha/yo'q): ")
        if user_input.lower() == "ha":
            print("Svetafor to'xtatildi.")
            break

if __name__ == "__main__":
    svetafor()