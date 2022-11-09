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
    gridList = []
    g1 = []
    g2 = []
    g3 = []

    #grids 1 to 3
    for i in range(9):
        if i == 3 or i == 6:

            gridList.append(g1)
            gridList.append(g2)
            gridList.append(g3)

            g1 = []
            g2 = []
            g3 = []
            
        for j in range(9):
            if j < 3:
                g1.append(sodoku[i][j])

            if j > 2 and j < 6:
                g2.append(sodoku[i][j])

            if j > 5 :
                g3.append(sodoku[i][j])


    gridList.append(g1)
    gridList.append(g2)
    gridList.append(g3)

    return gridList            







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

print()
print("Row Collector : \n")
rowsDict = rowsCollector(solved)
print()

print("Col Collector : \n")
# colsList = []
colsList = colCollector(solved)
print(colsList)

print()
print("Row + colum Tables print as Sodoku :\n")
pySudoku.print_sudoku(rowsDict)
print()
pySudoku.print_sudoku(colsList)


print()
print("GridCollector : \n")
gridList = gridCollector(solved)
print(gridList)

print(gridList[0])
