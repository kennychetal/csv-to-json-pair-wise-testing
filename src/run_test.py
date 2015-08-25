#Authors: Kenny Chetal kca48@sfu.ca, Erick Costigan ejc6@sfu.ca
import os
import filecmp

#Code will execute code that we are testing
def runFunctionality():
    for i in range(1,8):
        os.system("python main.py t" + str(i))

#Code will run comparisons and give us results between files
def runComparisons():
    for i in range(1,8):
        errors = False
        try:
            result = filecmp.cmp('t'+str(i)+'.json','../expected_output/t'+str(i)+'.json')
        except WindowsError:
            errors = True
        if(result==True and errors==False):
            print "Test " + str(i) + " files are same \n"
        elif(result==False):
            print "Test " + str(i) + " files are different \n"
        elif(errors==True):
            print "Test " + str(i) + " missing csv files thus json was not created \n"
            
def Main():
    runFunctionality()
    runComparisons()

Main()
