TNDump
======

Terminal Number Cleanup Export for Nortel/Meridian CS1000 terminal output

The purpose of these files is to help with the cleanup and organization of the output from a CS1000 terminal output. 

Currently there is no way to organize all of the phone programming data from a prt -> dnb ->ENTER ENTER output.

Any questions or comments, feel free to contact me at: jesse.vazquez@trincoll.edu for details or how to get it working.

There are 2 files:

=> LUDNExcel.py - This file will get all of the data for all TN loops and export to Excel

=> LUDN-Custom.py - Allows you to specify a certain loop to export if you don't want them all

How it works: 

=> Copy and paste the terminal output to a .txt file (in my case, dumpFile.txt)

=> Script cleans up the formatting to only include lines with the data we need, then saves to another .txt file (in my case, output.txt)

=> Next it goes through this output.txt fomratted file and exports all of the data to an Excel spreadsheet, choose a file name to save this .xls file as.

How to USE:
    1) Log into the ts1 terminal, ld 20
    2) Run command: prt > dnb > ENTER > ENTER - Let run for a few minutes until complete
    3) Copy this output into a text file, ex: dumpFile.txt
        >> Delete text above the first DN, usually this is the login/initial text
    4) Place this script and dumpFile.txt into same directory
    5) Open terminal to that directory
    6) To Run: python LUDNExcel.py
    7) Enter filename with .txt included: dumpFile.txt
    8) Enter Loop number you want (only one) - ex: 004, 088, 092, 028, 044, 072
    9) Enter the save name of the excel file, .xls included, ex: LUDN-Export-DATE.xls
