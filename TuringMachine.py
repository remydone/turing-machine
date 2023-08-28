# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:17:05 2021

@author: Remy
"""
# alphabet is list of strings
# strip is list of elements of alphabet

# brain is list of states
# state is list of instructions in order of alphabet
# instruction goes [thing to write, where to move, what next]
# thing to write is index of alphabet
# where to move is -1, 0 or +1
# what next is index of next state


def SolveDemo(brain, strip, alphabet, endstate, pos = 1, state = 0) :
    while state != endstate :
        i = 0
        while strip[pos] != alphabet[i] :
            i += 1
        strip[pos] = alphabet[brain[state][i][0]]
        pos += brain[state][i][1]
        state = brain[state][i][2]
        print("Strip : " + str(strip) + " ; State : " + str(state) + " ; Position : " + str(pos))
    return "end"

def Solve(brain, strip, alphabet, endstate, pos = 1, state = 0) :
    for i in range(len(strip)) :
        j = 0
        while strip[i] != alphabet[j] :
            j += 1
        strip[i] = j
    while state != endstate :
        instruction = strip[pos]
        strip[pos] = brain[state][instruction][0]
        pos += brain[state][instruction][1]
        state = brain[state][instruction][2]
    return strip


alphabet = ["a", "b", "A", "B", "null"]
strip = ["null", "a", "a", "b", "b", "null"] # exo 3.1 du TD
brain3 = [[[2,1,1],[],[],[3,1,0],[4,0,3]],[[0,1,1],[3,-1,2],[],[3,1,1],[]],[[0,-1,2],[],[2,1,0],[3,-1,2],[]]]
print(SolveDemo(brain3, strip, alphabet, 3))

alphabet = ["0", "1", "null"]
strip = ["null", "0", "0", "0", "0", "null"] # exo 4 du TD
brain4 = [[[1,1,1],[1,1,0],[]],[[0,1,4],[1,1,1],[2,1,2]],[],[[0,-1,3],[1,-1,3],[2,1,0]],[[1,1,5],[1,1,4],[2,-1,3]],[[0,1,4],[1,1,5],[]]]
print(SolveDemo(brain4, strip, alphabet, 2))



# Soit un ensemble fini A.
# Soit un ensemble fini S.

# Soit B l ensemble des fonctions injectives de Z dans A

# Soit M = {p, s, n}
# p : x -> x - 1

# Soit la fonction w : B * A * P -> B
#                     (b1, a, p) -> b2 : Z -> A
#                                        x -> { b1(x) si x != p
#                                             { a si x = p


# Une fonction t : A * S -> A * M * S




















