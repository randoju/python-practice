#RECURSION: COUNT OF ELEMENTS IN A LIST | DATA ENGINEER | TOP MOST PYTHON INTERVIEW QUESTION SERIES |

def count(l):
    if not l:
        return 0
    return 1+count(l[1:])

a= [1,2,3,4,5,6,7]
print(count(a))
