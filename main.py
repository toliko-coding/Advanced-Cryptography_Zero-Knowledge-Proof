from Verifier import *
from Prover import *
     
def sudoku_pazzle_board():
    puzzle = [
        0,0,0,2,6,0,7,0,1, 
        6,8,0,0,7,0,0,9,0, 
        1,9,0,0,0,4,5,0,0, 
        8,2,0,1,0,0,0,4,0, 
        0,0,4,6,0,2,9,0,0, 
        0,5,0,0,0,3,0,2,8, 
        0,0,9,3,0,0,0,7,4, 
        0,4,0,0,5,0,0,3,6, 
        7,0,3,0,1,8,0,0,0 
    ]
    return puzzle 


def solve_sudoku_puzzle(puzzle):
    solution = [
        4,3,5,2,6,9,7,8,1, 
        6,8,2,5,7,1,4,9,3, 
        1,9,7,8,4,4,5,6,2, 
        8,2,6,1,9,5,3,4,7, 
        3,7,4,6,8,2,9,1,5, 
        9,5,1,7,4,3,6,2,8, 
        5,1,9,3,2,6,8,7,4, 
        2,4,8,9,5,7,1,3,6, 
        7,6,3,4,1,8,2,5,9 
    ]
    return solution

def PrintTable(puzzle):
    print("Suduku Table : \n")

    #Top frame
    def lineframe():
        for i in range(9):
            print("__" , end="__")    
    lineframe()
    print("\n")

    counter = 1
    row = 1
    for card in puzzle:
        if counter < 10:
            if counter % 3 == 0:
                print(card, end=" | ")
                counter +=1
            else:
                print(card, end=" , ")
                counter +=1

            
        else:
            print("\n") 
            print(card, end=" , ")
            counter = 2

    print("\n")
    lineframe()
    print("\n")

        
unsolveTable = sudoku_pazzle_board()
solvedTable = solve_sudoku_puzzle(unsolveTable)

#PrintTable(unsolveTable)
#PrintTable(solvedTable)
#print(solvedTable[1])