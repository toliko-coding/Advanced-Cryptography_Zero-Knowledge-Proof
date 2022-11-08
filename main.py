from Verifier import *
from Prover import *
import pySudoku

#Function that take imput from text and Build a list size 9 to org
def buildTable(text,org):
    while len(text) > 0:
        l = []

        # Get a row of numbers
        while len(l) < 9:
            if text[0].isdigit():
                l.append(int(text[0]))
            text = text[1:]

        # Insert that row into the Sudoku grid
        org.append(l)
        if len(org) == 9:
            break            

#Create List of all the rows
def rowsCollector(sodoku):
    rows = {}
    for i in range(9):
        print(sodoku[i])
        rows[i] = sodoku[i]
        
    return rows

#Create List of all the colums
def colCollector(sodoku):
    cols = ""
    colsList = []
    for i in range(9):
        for j in range(9):
           cols += str(sodoku[j][i])
    
    buildTable(cols , colsList)
    return colsList

    #print(cols)

#Create List of all the grids[3x3] inside the table
def gridCollector(sodoku):
    pass






'''
import input(sodoku table) from .txt file -> create sodoku -> solve
   this functuion returns 2 values [ Solve , Original]
'''
x  = pySudoku.main()

solved = x[0]
#print(s)
#print(type(s))

#print("x1\n")
text = x[1]
#print(text)

org = []
buildTable(text,org)
print(org)

print("Row Collector : \n")
rowsDict = rowsCollector(solved)

print("Col Collector : \n")
colsList = []
colsList = colCollector(solved)
print(colsList)

# pySudoku.print_sudoku(s)
# pySudoku.print_sudoku(org)
