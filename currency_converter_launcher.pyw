import os
import sys

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

os.system('python currency_converter.py')
