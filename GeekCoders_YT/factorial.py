#RECURSION: FACTORIAL OF A GIVEN NUMBER | DATA ENGINEER | TOP MOST PYTHON INTERVIEW QUESTION SERIES |

def fact(n):
    fat = 1
    for i in range(n,0,-1):
        fat*=i
    return fat

print(fact(5))


#recursive
def fact_2(n):
    if n<1:
        return 1
    else:
        return n*fact_2(n-1)

print(fact_2(5))