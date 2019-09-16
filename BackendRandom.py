import random

#Global Var
map = []
moveAIList = [1,2,3,4,5,6,7]
def main():
    initMap() #tes
    playing = True
    while(playing):
        cmd = int(input("Enter input : "))
        playerMove(cmd)
        aiMove()
        printMap()

def playerMove(cmd):
    for i in reversed(range(6)):
        # print(i*7 + cmd -1)
        if(map[i * 7 + cmd-1] == '-'):
            map[i * 7 + cmd-1] = '0'
            break

def aiMove():
    cmdAi = random.choice(moveAIList)
    for i in reversed(range(6)):
        # print(i*7 + cmd -1)
        if(map[i * 7 + cmdAi-1] == '-'):
            map[i * 7 + cmdAi-1] = '1'
            break

def initMap():
    for i in range(6):
        for j in range(7):
            map.append('-')
    printMap()

def printMap():
    for i in range(6):
        for j in range (7):
            print(map[i*7 + j],end= ' ')
        print()


if __name__ == "__main__":
    main()