"""
    @author Jesse Vazquez, Jesse.Vazquez@trincoll.edu
    
    The purpose of this script is to clean up and export to Excel the information provided from the output of a TS1 terminal for prt > ludn. It first cleans up the formatting of the output into a more readable version, then exports that information to Excel.
    
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

"""
import xlwt # Python library for writing to Excel spreadsheet

#### ---Dump File Cleanup--- #####
iFile = raw_input("Enter dump filename with .txt included: ")
inFile = open(iFile, 'r')
outFile = open('output.txt', 'w')

# Boolean needed to prevent a newline from being written to output in first line
first = True

for line in inFile:
    if 'DN' in line:
        if 'TYPE' in line:      # Cases that have "Type: ACDN/LDN"
            pass
        elif 'DNRO' in line:    # Passes on lines with DNRO
            pass
        elif 'DNRI' in line:    # Passes on lines with DNRI
            pass
        elif first is True:     # Prevents newline on first pass
            outFile.write(line)
            first = False
        else:
            outFile.write('\n')
            outFile.write(line)
    if 'NAME' in line:
        outFile.write(line.strip())
        outFile.write('\n')
    if 'TN' in line:
        outFile.write(line)

inFile.close()
outFile.close()

#### ---END CLEANUP---START EXCEL EXPORT--- ####

# Open the output file from clean up in read mode
rFile = open('output.txt', 'r')

# Create Workbook instance to write to
book = xlwt.Workbook()

# Create worksheet for book
sheet1 = book.add_sheet("sheet1", cell_overwrite_ok = True)

# Counter variables needed for DN/Name and TN writing to correct cells
dnx = 1
tnx = 1

# Variables to store DN and NAME fields
storeDN = ''
storeNM = ''
writeDN = True
query = raw_input("Loop number? - '088', '004' etc...>> ")

# Write Column titles
sheet1.write(0, 0, "DN")
sheet1.write(0, 1, "NAME")
sheet1.write(0, 2, "TN")

# Adjust width for NAME column
sheet1.col(1).width = 256 * 20 

# Methods to grab DN/NAME/TN from line
def getDN(dn):
    return dn[5:9]
def getNM(nm):
    return nm[5:].rstrip()
def getTN(tn):
    return tn[5:16]

# Search through each line
for line in rFile:
    if 'DN' in line:
        storeDN = getDN(line)
    
    if 'NAME' in line:
        storeNM = getNM(line)
    
    if 'TN' in line:
        if query in line[:16]:  # Searches only part of the line that has TN in it
            if writeDN is True:
                sheet1.write(dnx, 0, storeDN)
                sheet1.write(dnx, 1, storeNM)
                sheet1.write(tnx, 2, getTN(line))
                writeDN = False
                tnx += 1
            else:
                sheet1.write(tnx, 2, getTN(line))
                tnx += 1
    else:
        dnx = tnx
        writeDN = True
        

# Save Workbook instance to an excel spreadsheet
xlsave = raw_input("Save file name of Excel file - include '.xls': ")
book.save(xlsave)

# Close the output.txt file
rFile.close()    