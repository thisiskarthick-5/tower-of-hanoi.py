disc = int(input("ENTER THE NUMBER OF DISC  :"))
source = 'A'
aux = 'B'
dest = 'C'

def towerofhanoi(disc,source,dest,aux):
    if disc == 1:
        print(f"MOVE DISC {source} from {dest}")
    else:
        towerofhanoi(disc-1,source,aux,dest)
        print(f"MOVE DISC {source} from {dest}")
        towerofhanoi(disc-1,aux,dest,source)


towerofhanoi(disc,source,dest,aux)

