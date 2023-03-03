'''
201989 - Tomas Gael P. Estrera IV
205294 - Luis Ishmael Valera

Certification:

I hereby certify that the submission described in this document abides by the principles stipulated in the DISCS Academic Integrity Policy document.

I further certify that I am the author of this submission and that any assistance I received in its preparation is fully acknowledged and disclosed in the documentation.

I have also cited all sources from which I obtained data, ideas, or words that are directly copied or paraphrased in this document.

Sources are properly credited according to accepted standards for professional publication.

Sources:

https://www.freecodecamp.org/news/demystifying-dynamic-programming-3efafb8d4296/#:~:text=Dynamic%20Programming%20Defined,example%20of%20a%20sub%2Dproblem.'''


def LCS(text1, text2):
    CS = [[0 for j in range(len(text1)+1)] for i in range(len(text2)+1)]

    for i in range (len(text1)-1,-1,-1):
        for j in range (len(text2)-1,-1,-1):
            if text1[i] == text2[j]:
                CS[i][j] = 1 + CS[i + 1][j + 1]
                
            else:
                CS[i][j] = max(CS[i][j + 1], CS[i + 1][j])
    
                
    i = 0
    j = 0
    word = []
  
    while i < len(text1) and j < len(text2):
        down = CS[i+1][j]
        right = CS[i][j+1]
        if text1[i] == text2[j]:
            word.append(text1[i])
            i += 1
            j += 1
        else:
            if down > right:
                i += 1
            else:
                j += 1
    

    yes = ''.join(word)
    
    
    return yes



'''Initialization of Matrix




The Longest Common Subsequence Code starts with the initialization of the graph using a matrix wherein the matrix is composed of L1 x L2 wherein L1 is the length of the first string, and L2 is the length of the second string.

Hence, the length of the columns were initialized to be the number of elements of the first string + 1. The length of the rows were initialized to be the length of the second string plus 1.




Logic Behind range + 1 for both columns and rows

The logic behind adding +1 for both rows and columns is because of the marking algorithm's tendency to search for something out of index. One of the algorithm uses a checker for the right cell of the matrix. If there is no +1 space allocation for both rows and columns, then the algorithm will search the cells that are in the right and bottom of the bottom-most and right-most cells (which then results in an out-of-index range error). Hence, we need these 0 space allocations for the checker to work.




How does the Algorithm work?


Marking the Cells with Numbers


The first part of the LCS algorithm will start from the bottom to the top. This will be accomplished by looping through the first and second string starting from the last-most elements of these strings. Hence, we would use a for loop that uses the parameters (string length - 1, -1, -1) in order to inverse the loop order to make the loop descending.


For every cell, the algorith will check if the cell is at intersection with two list indexes with the same letter. For example, A is the matrix with a and b as its indexes (a representing element from String1 and b representing element from second String2). If String1[a] is equal to String2[b], then it means that the cell is at the intersection of a an identical string element from both strings. Then, the cell would have a value of = 1 + diagonal cell below it. This algorithm iterate until the upper-left-most cell is filled, which is Matrix[0][0].


Recording the longest common subsequence by tracking the recorded numbers


In order to record the longest common subsequence, the values of the cells will be used to track and update the longest common subsequence.


This algorithm will start from the top in Matrix[0][0].


The algorithm will iterate through the matrix by constantly comparing the values of the cells below it and at the right of it. If the cell's string indices doesn't match (element a of string1 is not equal to element b of string2), then comparisons will then occur. These 2 comparisons are:


If the cell below current cell is greater than the cell at the right of the current cell, then we increase our row index by 1 in order to move to the next row while still being in the same column position.

If the opposite is true (right of current cell > bottom of current cell) or (right of current cell == bottom of current cell), then we increase our column index by 1 in order to proceed to the right column while retaining the same row index.


However, if the cell's string indices does match, then we will append the element of the string associated with our current cell to an arraylist. From here, we increase our column and row index by 1 in order to move to a diagonal cell below our current cell.


Eventually, this algorithm will continue until the row and column indexes have passed through all possible cells of the matrix. The arraylist will then be joined through the join() function in order to form the new string of longest common subsequence'''