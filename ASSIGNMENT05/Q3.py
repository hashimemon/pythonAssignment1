l=[1,4,44,55,78,99,97,114,118]

def printEvenNo(List):
    print('Given List ',List)
    print('Even Numbers In A List Are:')
    for i in List:
        if i%2==0:
            print(i)

printEvenNo(l)
