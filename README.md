TNDump
======

Terminal Number Cleanup Export for Nortel/Meridian CS1000 terminal output

The purpose of these files is to help with the cleanup and organization of the output from a CS1000 terminal output. 

Currently there is no way to organize all of the phone programming data from a prt -> dnb ->ENTER ENTER output.

Any questions or comments, feel free to contact me at: jesse.vazquez@trincoll.edu for details or how to get it working.

How it works: 

=> Copy and paste the terminal output to a .txt file (in my case, dumpFile.txt)

=> Script cleans up the formatting to only include lines with the data we need, then saves to another .txt file (in my case, output.txt)

=> Next it goes through this output.txt fomratted file and exports all of the data to an Excel spreadsheet, choose a file name to save this .xls file as.
