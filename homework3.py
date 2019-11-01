global Wcamp
global Bcamp
global refBcamp
global refWcamp
global heuristicQueue
global mySymbol
global other

from math import sqrt
from queue import PriorityQueue
import time
import os





def avgDistanceFromGoal(b,c):
    Wc = [b[15][15], b[15][14], b[14][15], b[15][13], b[14][14], b[13][15],
          b[15][12], b[14][13], b[13][14], b[12][15], b[15][11],
          b[14][12], b[13][13], b[12][14], b[11][15],
          b[14][11], b[13][12], b[12][13],
          b[11][14]]
    Bc = [b[0][0], b[0][1], b[1][0], b[0][2], b[1][1],
          b[2][0], b[0][3], b[1][2], b[2][1], b[3][0],
          b[0][4], b[1][3], b[2][2], b[3][1],
          b[4][0], b[1][4], b[2][3],
          b[3][2], b[4][1]]
    if c== 'BLACK':
        mySymbol = 'B'
        other = 'W'
        goal=15
        mycamp = Bc
        othercamp = Wc
    else:
        mySymbol = 'W'
        other = 'B'
        goal=0
        mycamp = Wc
        othercamp = Bc

    myDistance=0
    otherDistance=0
    cnt1=0
    cnt2=0

    for i in range(16):
        for j in range(16):
            if b[i][j]==mySymbol and b[i][j]:# not in othercamp:
                cnt1+=1
                myDistance+=sqrt((goal-i)**2+(goal-j)**2)
        if cnt1==19:
            break
    for i in range(16):
        for j in range(16):
            if b[i][j]==other and b[i][j]:# not in mycamp:
                cnt2+=1
                otherDistance+=sqrt((abs(goal-15)-i)**2+((abs(goal-15)-j)**2))
        if cnt2==19:
            break
    return [myDistance,otherDistance]
def WhiteMove(b,r,c,themove,t):
    temprow = r
    tempcol = c
    flag=0
    jumps=[]
    jumps.append((r, c))
    if t==1:
        if c + 1 < 16 and b[r][c + 1] == '.':
            temprow = temprow
            tempcol = tempcol + 1
            jumps.append((temprow, tempcol))
        elif r - 1 >= 0 and c + 1 < 16 and b[r - 1][c + 1] == '.':  # t
            temprow = temprow - 1
            tempcol = tempcol + 1
            jumps.append((temprow, tempcol))
        elif r - 1 >= 0 and b[r - 1][c] == '.':  # t
            temprow = temprow - 1
            tempcol = tempcol
            jumps.append((temprow, tempcol))
        elif r - 1 >= 0 and c - 1 >=0and b[r - 1][c -1] == '.':  # t
            temprow = temprow - 1
            tempcol = tempcol - 1
            jumps.append((temprow, tempcol))
        if c - 1 >= 0 and b[r][c - 1] == '.':  # t
            temprow = temprow
            tempcol = tempcol - 1
            jumps.append((temprow, tempcol))
            #print(1)
        elif r + 1 < 16 and c - 1 >= 0 and b[r + 1][c - 1] == '.':
            temprow = temprow + 1
            tempcol = tempcol - 1
            jumps.append((temprow, tempcol))
            #print(2)
        elif r + 1 < 16 and b[r + 1][c] == '.':
            temprow = temprow + 1
            tempcol = tempcol
            jumps.append((temprow, tempcol))


        themove.append(jumps)
        return [temprow,tempcol]

    while(1):
    #def jumpTopLeft(b,r,c):

        if temprow-2>=0 and tempcol-2>=0 and b[temprow-1][tempcol-1]!='.' and b[temprow-2][tempcol-2]=='.':
            temprow=temprow-2
            tempcol=tempcol-2
            jumps.append((temprow,tempcol))
            #centroidDist.append(sqrt((temprow-r)**2 + (tempcol-c)**2))
            flag = 0
    #def jumpTop(b, r, c):
        elif temprow-2>=0 and b[temprow - 1][tempcol] != '.' and b[temprow - 2][tempcol] == '.':
            temprow = temprow - 2
            tempcol = tempcol
            jumps.append((temprow, tempcol))
            #centroidDist.append(sqrt((temprow - r) ** 2 + (tempcol - c) ** 2))
            flag = 0
    #def jumpLeft(b, r, c):
        elif tempcol-2>=0 and b[temprow][tempcol - 1] != '.' and b[temprow][tempcol - 2] == '.':
            temprow = temprow
            tempcol = tempcol-2
            jumps.append((temprow, tempcol))
            #centroidDist.append(sqrt((temprow - r) ** 2 + (tempcol - c) ** 2))
            flag = 0
        else:
            # def jumpBottomLeft
            if flag==0 and temprow + 2 < 16 and tempcol - 2 >= 0 and b[temprow + 1][tempcol - 1] != '.' and b[temprow + 2][tempcol - 2] == '.':
                temprow = temprow + 2
                tempcol = tempcol - 2
                jumps.append((temprow, tempcol))
                #centroidDist.append(sqrt((temprow - r) ** 2 + (tempcol - c) ** 2))
                flag = 1
            # def jumpTopRight
            elif flag==0 and temprow - 2 >= 0 and tempcol + 2 < 16 and b[temprow - 1][tempcol + 1] != '.' and b[temprow - 2][tempcol + 2] == '.':
                temprow = temprow - 2
                tempcol = tempcol + 2
                jumps.append((temprow, tempcol))
                #centroidDist.append(sqrt((temprow - r) ** 2 + (tempcol - c) ** 2))
                flag = 1
            else:
                if temprow>r or tempcol>c:
                    temprow=r
                    tempcol=c
                    jumps=[]
                    jumps.append((temprow, tempcol))
                break
    if temprow==r and tempcol==c:
        #def topLeft(b, r, c):
        if r - 1 >= 0 and c - 1 >= 0 and b[r - 1][c - 1] == '.':
            temprow = temprow-1
            tempcol = tempcol-1
            jumps.append((temprow, tempcol))

        #def left(b, r, c):
        elif c-1>=0 and b[r][c - 1] == '.':
            temprow = temprow
            tempcol = tempcol - 1
            jumps.append((temprow, tempcol))

        #def top(b, r, c):
        elif r-1>=0 and b[r - 1][c] == '.':
            temprow = temprow - 1
            tempcol = tempcol
            jumps.append((temprow, tempcol))
        else:
            if r+1<16 and c-1>=0 and b[r+1][c-1]=='.':
                temprow = temprow + 1
                tempcol = tempcol-1
                jumps.append((temprow, tempcol))
            elif r-1>=0 and c+1<15 and b[r-1][c+1]=='.': #t
                temprow = temprow - 1
                tempcol = tempcol+1
                jumps.append((temprow, tempcol))
            else:
                if r+1<16 and b[r+1][c]=='.':  #t
                    temprow = temprow + 1
                    tempcol = tempcol
                    jumps.append((temprow, tempcol))
                elif c+1<16 and b[r][c+1]=='.': #t
                    temprow = temprow
                    tempcol = tempcol+1
                    jumps.append((temprow, tempcol))
                else:
                    if r + 1 < 16 and c + 1 < 16 and b[r + 1][c + 1] == '.':
                        temprow = temprow + 1
                        tempcol = tempcol + 1
                        jumps.append((temprow,tempcol))
    themove.append(jumps)
    return [temprow,tempcol]

def BlackMove(b,r,c,themove,t):
    temprow = r
    tempcol = c
    flag=0
    jumps=[]
    jumps.append((r, c))
    if t==1:

        if r - 1 >= 0 and c + 1 < 16 and b[r - 1][c + 1] == '.':  # t
            temprow = temprow - 1
            tempcol = tempcol + 1
            jumps.append((temprow, tempcol))
        elif c - 1 >= 0 and b[r][c - 1] == '.':  # t
            temprow = temprow
            tempcol = tempcol - 1
            jumps.append((temprow, tempcol))
            #print(1)
        elif r + 1 < 16 and c - 1 >= 0 and b[r + 1][c - 1] == '.':
            temprow = temprow + 1
            tempcol = tempcol - 1
            jumps.append((temprow, tempcol))
            #print(2)
        elif r + 1 < 16 and b[r + 1][c] == '.':
            temprow = temprow + 1
            tempcol = tempcol
            jumps.append((temprow, tempcol))
            #print(3)
        elif r + 1 < 16 and c + 1 < 16 and b[r + 1][c + 1] == '.':
            temprow = temprow + 1
            tempcol = tempcol + 1
            jumps.append((temprow, tempcol))
        elif c + 1 < 16 and b[r][c + 1] == '.':
            temprow = temprow
            tempcol = tempcol + 1
            jumps.append((temprow, tempcol))

        elif r - 1 >= 0 and b[r - 1][c] == '.':  # t
            temprow = temprow - 1
            tempcol = tempcol
            jumps.append((temprow, tempcol))
        themove.append(jumps)
        return [temprow,tempcol]





    while(1):
        #def jumpBottomRght
        if temprow + 2 <16 and tempcol + 2 < 16 and b[temprow+1][tempcol+1]!='.' and b[temprow+2][tempcol+2]=='.':
            temprow = temprow+2
            tempcol = tempcol+2
            jumps.append((temprow, tempcol))
            flag = 0
        # #def jumpDown(b, r, c):
        elif temprow + 2 < 16 and b[temprow + 1][tempcol] != '.' and b[temprow + 2][tempcol] == '.':
            temprow = temprow + 2
            tempcol = tempcol
            jumps.append((temprow, tempcol))
            flag = 0
        #def jumpRight(b, r, c):
        elif tempcol + 2 < 16 and b[temprow][tempcol+ 1] != '.' and b[temprow][tempcol + 2] == '.':
            temprow = temprow
            tempcol = tempcol + 2
            jumps.append((temprow, tempcol))
            flag = 0

        else:
            # def jumpTopRght
            if flag==0 and temprow - 2 >= 0 and tempcol + 2 < 16 and b[temprow-1][tempcol+1]!= '.' and b[temprow-2][tempcol+2]=='.':
                temprow = temprow - 2
                tempcol = tempcol + 2
                jumps.append((temprow, tempcol))
                flag = 1
            # def bottomLeft
            elif flag==0 and temprow + 2 < 16 and tempcol - 2 >= 0 and b[temprow+1][tempcol-1] != '.' and b[temprow+2][tempcol-2]=='.':
                temprow = temprow + 2
                tempcol = tempcol - 2
                jumps.append((temprow, tempcol))
                flag = 1
            else:
                if temprow<r or tempcol<c:
                    temprow=r
                    tempcol=c
                    jumps=[]
                    jumps.append((temprow,tempcol))
                break
    if temprow==r and tempcol==c:
        #def bottomRight(b, r, c):
        if r + 1 < 16 and c + 1 < 16 and b[r + 1][c + 1] == '.':
            temprow = temprow + 1
            tempcol = tempcol + 1
            jumps.append((temprow, tempcol))

        elif c + 1 < 16 and b[r][c + 1] == '.':
            temprow = temprow
            tempcol = tempcol + 1
            jumps.append((temprow, tempcol))
        #def down(b, r, c):
        elif r + 1 < 16 and b[r + 1][c] == '.':
            temprow = temprow+1
            tempcol = tempcol
            jumps.append((temprow, tempcol))
        else:
            if r-1>=0 and c+1<16 and b[r-1][c+1]=='.': #t
                temprow = temprow - 1
                tempcol = tempcol+1
                jumps.append((temprow, tempcol))
            elif r+1<16 and c-1>=0 and b[r+1][c-1]=='.':
                temprow = temprow + 1
                tempcol = tempcol-1
                jumps.append((temprow, tempcol))
            else:
                if c - 1 >= 0 and b[r][c - 1] == '.': #t
                    temprow = temprow
                    tempcol = tempcol - 1
                    jumps.append((temprow, tempcol))
                elif r - 1 >= 0 and b[r - 1][c] == '.': #t
                    temprow = temprow - 1
                    tempcol = tempcol
                    jumps.append((temprow, tempcol))
                else:
                    if r - 1 >= 0 and c - 1 >= 0 and b[r - 1][c - 1] == '.':
                        temprow = temprow - 1
                        tempcol = tempcol - 1
                        jumps.append((temprow, tempcol))

    themove.append(jumps)
    return [temprow,tempcol]



def checkIsolated(b,r,c):
    rdv = [-1, 1, 0, 0, -1, 1, 1, -1]
    cdv = [0, 0, 1, -1, 1, 1, -1, -1]
    for i in range(8):
        new_r=r+rdv[i]
        new_c=c+cdv[i]
        if new_r<0 or new_c<0:
            continue
        if new_r>=16 or new_c>=16:
            continue
        if b[new_r][new_c]!='.':
            return 0

    return 1




def findPossibleMoves(b,c,themove):
    t=0
    Wc = [b[15][15], b[15][14], b[14][15], b[15][13], b[14][14], b[13][15],
          b[15][12], b[14][13], b[13][14], b[12][15], b[15][11],
          b[14][12], b[13][13], b[12][14], b[11][15],
          b[14][11], b[13][12], b[12][13],
          b[11][14]]
    Bc = [b[0][0], b[0][1], b[1][0], b[0][2], b[1][1],
          b[2][0], b[0][3], b[1][2], b[2][1], b[3][0],
          b[0][4], b[1][3], b[2][2], b[3][1],
          b[4][0], b[1][4], b[2][3],
          b[3][2], b[4][1]]
    refW = [(15, 15), (15, 14), (14, 15), (15, 13), (14, 14), (13, 15), (15, 12), (14, 13), (13, 14),
            (12, 15), (15, 11), (14, 12), (13, 13), (12, 14), (11, 15), (14, 11), (13, 12), (12, 13), (11, 14)]
    refB = [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (0, 3), (1, 2), (2, 1), (3, 0), (0, 4), (1, 3),
            (2, 2), (3, 1), (4, 0), (1, 4), (2, 3), (3, 2), (4, 1), ]
    if c=='BLACK':
        mySymbol= 'B'
        other='W'
        f=BlackMove
        destination=(15,15)
        mycamp = refB
        othercamp = refW
        Mc=Bc
        Oc=Wc
    else:
        mySymbol = 'W'
        other='B'
        f=WhiteMove
        destination=(0,0)
        mycamp = refW
        othercamp = refB
        Mc=Wc
        Oc=Bc
    cnt=0

    allMoves=PriorityQueue()
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j]==mySymbol:
                cnt+=1
                if Oc.count(mySymbol)==18:
                    if (i,j) not in othercamp:
                        t=1
                        #continue
                a=f(b,i,j,themove,t)
                row,col=a[0],a[1]
                if (row,col)==(i,j):
                    continue
                if (i,j)==(15,15) or (i,j)==(0,0) or (i,j)==(15,14) or (i,j)==(14,15) or (i,j)==(0,1) or (i,j)==(1,0):
                    continue
                #allMoves.put([15-max(abs(row-i),abs(col-j)),sqrt((row-destination[0])**2+(col-destination[1])**2),[(i,j),(row,col)]])
                allMoves.put([15 - max(abs(row - i), abs(col - j)),
                              sqrt((row - destination[0]) ** 2 + (col - destination[1]) ** 2),[(i,j),(row,col)]])
        if cnt == 19:
            break
    print(allMoves.queue)
    return allMoves



def evaluate(b,c):
    Wc = [b[15][15], b[15][14], b[14][15], b[15][13], b[14][14], b[13][15],
          b[15][12], b[14][13], b[13][14], b[12][15], b[15][11],
          b[14][12], b[13][13], b[12][14], b[11][15],
          b[14][11], b[13][12], b[12][13],
          b[11][14]]
    Bc = [b[0][0], b[0][1], b[1][0], b[0][2], b[1][1],
          b[2][0], b[0][3], b[1][2], b[2][1], b[3][0],
          b[0][4], b[1][3], b[2][2], b[3][1],
          b[4][0], b[1][4], b[2][3],
          b[3][2], b[4][1]]
    refW=[(15,15),(15,14),(14,15),(15,13),(14,14),(13,15),(15,12),(14,13),(13,14),
              (12, 15),(15,11),(14,12),(13,13),(12,14),(11,15),(14,11),(13,12),(12,13),(11,14)]
    refB=[(0,0),(0,1),(1,0),(0,2),(1,1),(2,0),(0,3),(1,2),(2,1),(3,0),(0,4),(1,3),
              (2,2),(3,1),(4,0),(1,4),(2,3),(3,2),(4,1),]

    if c=='BLACK':
        mySymbol= 'B'
        other='W'
        mycamp=Bc
        othercamp=Wc
        myref=refB
        otherref=refW
    else:
        mySymbol = 'W'
        other = 'B'
        mycamp=Wc
        othercamp=Bc
        myref=refW
        otherref=refB


    evalValue = 0

    # eval for isolated marbles

    d = avgDistanceFromGoal(b, c)
    evalValue=evalValue+d[1]**2-d[0]**2


    dst1=0
    dst2=0

    for i in range(16):
        for j in range(16):
            if i>0 and j>0:
                if b[i][j]==mySymbol:
                    dst1+=(i+j)/sqrt(i**2+j**2)
                if b[i][j]==other:
                    dst2 += (i + j) / sqrt(i ** 2 + j ** 2)
    evalValue=evalValue+(dst2)**2-(dst1)**2

    # if othercamp.count(mySymbol)==17:
    #     print(111)
    #     for i in range(16):
    #         for j in range(16):
    #             if b[i][j]==mySymbol:
    #                 if b[i][j] not in othercamp:
    #                     print(2222)
    #                     evalValue-=200
    # if mycamp.count(other)==18:
    #     for i in range(16):
    #         for j in range(16):
    #             if b[i][j]==other:
    #                 if b[i][j] not in mycamp:
    #                     evalValue+=200


    for i in range(16):
        for j in range(16):
            if b[i][j]==mySymbol:
                if (i,j) not in otherref:
                    for k in otherref:
                        if b[k[0]][k[1]]=='.':
                            evalValue-=(i-k[0])**2-(j-k[1])**2
            elif b[i][j]==other:
                if (i, j) not in myref:
                    for k in myref:
                        if b[k[0]][k[1]]=='.':
                            evalValue+=(i-k[0])**2+(j-k[1])**2
    # for i in range(16):
    #     for j in range(16):
    #         if b[i][j]==other:
    #             if (i,j) not in myref:
    #                 evalValue+=100
    # evalValue=evalValue-(othercamp.count('.'))*200
    # evalValue=evalValue+(mySymbol.count('.'))*200



    if mySymbol=='W':

        for i in  Bc:
            if i==mySymbol:
                evalValue+=100

        for i in Wc:
            if i==other:
                evalValue-=100

    else:

        for i in Wc:
            if i==mySymbol:
                evalValue+=100

        for i in Bc:
            if i == other:
                evalValue -= 100


    return evalValue


def minimax(b,depth,isMax,c,alpha,beta,themove):
    if c=='BLACK':
        mySymbol= 'B'
    else:
        mySymbol = 'W'

    score=evaluate(b,c)
    #print(score)
    # if score==100:
    #     return score
    # if score==100:
    #     return score
    if depth==0:
        return score
    if isMax:
        best=-10000000
        validMoves = findPossibleMoves(b, c,themove)
        while not validMoves.empty():
            bestMove = validMoves.get()
            b[bestMove[2][0][0]][bestMove[2][0][1]] = '.'
            b[bestMove[2][1][0]][bestMove[2][1][1]] = mySymbol
            #b[bestMove[2][1][-1][0]][bestMove[2][1][-1][1]] = mySymbol

            val = minimax(b, depth+1, False,c, alpha, beta,themove)

            best=max(best,val)
            alpha=max(alpha,best)

            b[bestMove[2][0][0]][bestMove[2][0][1]] = mySymbol
            b[bestMove[2][1][0]][bestMove[2][1][1]] = '.'
            #b[bestMove[2][1][-1][0]][bestMove[2][1][-1][1]] = '.'


            if beta<=alpha:
                break
        return best
    else:
        best = 10000000
        validMoves = findPossibleMoves(b, c,themove)
        while not validMoves.empty():
            bestMove = validMoves.get()
            b[bestMove[2][0][0]][bestMove[2][0][1]] = '.'
            b[bestMove[2][1][0]][bestMove[2][1][1]] = mySymbol
            #b[bestMove[2][1][-1][0]][bestMove[2][1][-1][1]] = mySymbol

            val = minimax(b, depth + 1, True,c, alpha, beta,themove)
            best=min(best,val)
            beta=min(beta,best)

            b[bestMove[2][0][0]][bestMove[2][0][1]] = mySymbol
            b[bestMove[2][1][0]][bestMove[2][1][1]] = '.'
            #b[bestMove[2][1][-1][0]][bestMove[2][1][-1][1]] = '.'

            if beta<=alpha:
                break
        return best


def findBestMove(b,c,themove):
    Wc = [b[15][15], b[15][14], b[14][15], b[15][13], b[14][14], b[13][15],
          b[15][12], b[14][13], b[13][14], b[12][15], b[15][11],
          b[14][12], b[13][13], b[12][14], b[11][15],
          b[14][11], b[13][12], b[12][13],
          b[11][14]]
    Bc = [b[0][0], b[0][1], b[1][0], b[0][2], b[1][1],
          b[2][0], b[0][3], b[1][2], b[2][1], b[3][0],
          b[0][4], b[1][3], b[2][2], b[3][1],
          b[4][0], b[1][4], b[2][3],
          b[3][2], b[4][1]]
    moves=[]
    if c=='BLACK':
        mySymbol= 'B'
        mycamp = Bc
        othercamp = Wc
    else:
        mySymbol = 'W'
        mycamp = Wc
        othercamp = Bc
    bestVal=-10000000
    moveFrom=0
    moveTo=0
    if c=='WHITE':
        if 'W' in Wcamp:
            isEmpty=False
        else:
            isEmpty=True
    else:
        if 'B' in Bcamp:
            isEmpty=False
        else:
            isEmpty=True

    if not isEmpty:
        if c=='BLACK':
            # finding the first B that is inside the camp
            for i in range(len(Bcamp)):
                moves=[]
                if Bcamp[i]=='B':
                    #print(i)
                    row=refBcamp[i][0]
                    col=refBcamp[i][1]
                    #print(row,col)
                # checking for available moves while prioritizing jump over empty moves preferably..
                # towards the middle of the board
                    temprow=row
                    tempcol=col
                    moves.append((temprow,tempcol))
                    while(1):
                        if b[temprow+1][tempcol+1]!='.' and b[temprow+2][tempcol+2]=='.':
                            temprow=temprow+2
                            tempcol=tempcol+2
                            moves.append((temprow, tempcol))
                        elif b[temprow+1][tempcol]!='.' and b[temprow+2][tempcol]=='.':
                            temprow=temprow+2
                            tempcol=tempcol
                            moves.append((temprow, tempcol))
                        elif b[temprow][tempcol+1]!='.' and b[temprow][tempcol+2]=='.':
                            temprow=temprow
                            tempcol=tempcol+2
                            moves.append((temprow, tempcol))
                        else:
                            break
                    if temprow==row and tempcol==col:
                        if b[temprow+1][tempcol+1]=='.':
                            temprow = temprow + 1
                            tempcol = tempcol+1
                            moves.append((temprow, tempcol))

                        elif b[temprow+1][tempcol]=='.':
                            temprow=temprow+1
                            tempcol=tempcol
                            moves.append((temprow, tempcol))
                        elif b[temprow][tempcol + 1] == '.':
                            temprow = temprow
                            tempcol = tempcol + 1
                            moves.append((temprow, tempcol))
                        else:
                            temprow = row
                            tempcol = col

                    if temprow==row and tempcol==col:
                        continue
                    heuristicQueue.put([sqrt((temprow-7.5)**2+(tempcol-7.5)**2),0,[(row,col),(temprow,tempcol)]])
                    themove.append(moves)
        elif c=='WHITE':
            # finding the first B that is inside the camp
            for i in range(len(Wcamp)):
                moves=[]
                if Wcamp[i]=='W':
                    row=refWcamp[i][0]
                    col=refWcamp[i][1]
                    #print(row,col)
                # checking for available moves while prioritizing jump over empty moves preferably..
                # towards the middle of the board
                    temprow=row
                    tempcol=col
                    moves.append((temprow,tempcol))
                    while(1):
                        if b[temprow-1][tempcol-1]!='.' and b[temprow-2][tempcol-2]=='.':
                            temprow=temprow-2
                            tempcol=tempcol-2
                            moves.append((temprow, tempcol))
                        elif b[temprow-1][tempcol]!='.' and b[temprow-2][tempcol]=='.':
                            temprow=temprow-2
                            tempcol=tempcol
                            moves.append((temprow, tempcol))
                        elif b[temprow][tempcol-1]!='.' and b[temprow][tempcol-2]=='.':
                            temprow=temprow
                            tempcol=tempcol-2
                            moves.append((temprow, tempcol))
                        else:
                            break
                    if temprow==row and tempcol==col:
                        if b[temprow-1][tempcol-1]=='.':
                            temprow = temprow - 1
                            tempcol = tempcol-1
                            moves.append((temprow, tempcol))
                        elif b[temprow-1][tempcol]=='.':
                            temprow=temprow-1
                            tempcol=tempcol
                            moves.append((temprow, tempcol))
                        elif b[temprow][tempcol - 1] == '.':
                            temprow = temprow
                            tempcol = tempcol - 1
                        else:
                            temprow=row
                            tempcol=col

                    if temprow==row and tempcol==col:
                        continue
                    heuristicQueue.put([sqrt((temprow-7.5)**2+(tempcol-7.5)**2),15-row,[(row,col),(temprow,tempcol)]])
                    themove.append(moves)
        if len(heuristicQueue.queue)==0:
            moves=[]
            maxx=-1
            maxy=-1
            for m in range(16):
                for n in range(16):
                    if b[m][n]==mySymbol:
                        if m>=maxx and n>=maxy:
                            maxx=m
                            maxy=n
            moves.append((maxx,maxy))
            moves.append((maxx+1,maxy+1))
            themove.append(moves)

            return [(maxx,maxy),(maxx+1,maxy+1)]





        tempy=heuristicQueue.get()


        return tempy[2]
    else:
        validMoves=findPossibleMoves(b,c,themove)
        while not validMoves.empty():
            bestMove=validMoves.get()
            b[bestMove[2][0][0]][bestMove[2][0][1]] = '.'
            b[bestMove[2][1][0]][bestMove[2][1][1]] = mySymbol
            #b[bestMove[2][1][-1][0]][bestMove[2][1][-1][1]] = mySymbol


            val=minimax(b,0,False,c,-1000,1000,themove)
            #print((bestMove[2][0][0],bestMove[2][0][1]),(bestMove[2][1][0],bestMove[2][1][1]))
            #print(val,end="\n")

            b[bestMove[2][0][0]][bestMove[2][0][1]] = mySymbol
            b[bestMove[2][1][0]][bestMove[2][1][1]] = '.'
            #b[bestMove[2][1][-1][0]][bestMove[2][1][-1][1]] = mySymbol
            print(othercamp.count(mySymbol))


            if val>bestVal and (bestMove[2][0][0],bestMove[2][0][1])!=(bestMove[2][1][0],bestMove[2][1][1]):
                bestVal=val
                moveFrom=(bestMove[2][0][0],bestMove[2][0][1])
                moveTo=(bestMove[2][1][0],bestMove[2][1][1])
                #moveTo=bestMove[2][1]
                # print("--",moveFrom,moveTo)
                # print(bestVal)

        return (moveFrom,moveTo)
start_time = time.clock()

# Driver code
if __name__ == "__main__":
    totalMoves=0
    while(1):
        start_time = time.clock()

        f = open('input.txt', 'r')
        # file read starts
        mode = f.readline()
        color = f.readline()
        timeGiven = f.readline()
        Board = []
        temp = []
        heuristicQueue = PriorityQueue()
        themove = []

        for i in range(16):
            line = f.readline()
            line.strip()
            temp.append([str(n) for n in line.split()])

        f.close()
        myDepth = 0

        for i in temp:
            for j in i:
                Board.append(list(j))

        Wcamp = [Board[15][15], Board[15][14], Board[14][15], Board[15][13], Board[14][14], Board[13][15],
                 Board[15][12], Board[14][13], Board[13][14], Board[12][15], Board[15][11],
                 Board[14][12], Board[13][13], Board[12][14], Board[11][15],
                 Board[14][11], Board[13][12], Board[12][13],
                 Board[11][14]]
        Bcamp = [Board[0][0], Board[0][1], Board[1][0], Board[0][2], Board[1][1],
                 Board[2][0], Board[0][3], Board[1][2], Board[2][1], Board[3][0],
                 Board[0][4], Board[1][3], Board[2][2], Board[3][1],
                 Board[4][0], Board[1][4], Board[2][3],
                 Board[3][2], Board[4][1]]
        refWcamp = [(15, 15), (15, 14), (14, 15), (15, 13), (14, 14), (13, 15), (15, 12), (14, 13), (13, 14),
                    (12, 15), (15, 11), (14, 12), (13, 13), (12, 14), (11, 15), (14, 11), (13, 12), (12, 13), (11, 14)]
        refBcamp = [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (0, 3), (1, 2), (2, 1), (3, 0), (0, 4), (1, 3),
                    (2, 2), (3, 1), (4, 0), (1, 4), (2, 3), (3, 2), (4, 1), ]

        color = color.strip()
        mode = mode.strip()
        wr = 0
        timeGiven = timeGiven.strip()
        if mode == 'SINGLE':
            myDepth = 0
        else:
            if float(timeGiven) > 50:
                myDepth = 3
            # elif float(timeGiven)<=150 and float(timeGiven)>100:
            #     myDepth=4
            elif float(timeGiven) <= 50 and float(timeGiven) > 20:
                myDepth = 2
            # elif float(timeGiven)<=50 and float(timeGiven)>20:
            #     myDepth=2
            elif float(timeGiven) <= 20 and float(timeGiven) > 7:
                myDepth = 1
            elif float(timeGiven) <= 7:
                myDepth = 0

        if color == 'BLACK':
            mySymbol = 'B'
            other = 'W'
            wr = 'WHITE'
        else:
            mySymbol = 'W'
            other = 'B'
            wr = 'BLACK'
        f.close()
        val = findBestMove(Board, color, themove)

        print(mySymbol,val)
        # print(themove)
        myMove = []
        # print(themove)
        for i in themove:
            # print(i)
            if i == []:
                continue
            if i[0] == (val[0][0], val[0][1]) and i[-1] == (val[1][0], val[1][1]):
                myMove = i
                break
        # print(myMove)



        # write to file

        ff = open('output.txt', 'w')
        if abs(val[0][0] - val[1][0]) == 1 or abs(val[0][1] - val[1][1]) == 1:
            ff.write('E')
            ff.write(' ')
            ff.write(str(val[0][1]))
            ff.write(',')
            ff.write(str(val[0][0]))
            ff.write(' ')
            ff.write(str(val[1][1]))
            ff.write(',')
            ff.write(str(val[1][0]))
        else:
            for i in range(len(myMove) - 1):
                ff.write('J')
                ff.write(' ')
                ff.write(str(myMove[i][1]))
                ff.write(',')
                ff.write(str(myMove[i][0]))
                ff.write(' ')
                ff.write(str(myMove[i + 1][1]))
                ff.write(',')
                ff.write(str(myMove[i + 1][0]))
                ff.write('\n')
        ff.close()

        Board[val[0][0]][val[0][1]] = '.'
        Board[val[1][0]][val[1][1]] = mySymbol
        f1 = open('input.txt', 'w')
        # f1.write("hello")
        f1.write(mode)
        f1.write("\n")
        # f1.write('BLACK')
        f1.write(wr)
        f1.write("\n")
        f1.write(str(float(timeGiven) - time.clock() + start_time))
        f1.write("\n")
        for bb in Board:
            for cc in bb:
                f1.write(str(cc))
            f1.write("\n")
        f1.close()
        print(Board)
        totalMoves += 1
        #os.system("cls")



        if Wcamp.count('B')==19 or Bcamp.count('W')==19:
            break
    print(totalMoves)



print(time.clock() - start_time, "seconds")
########################################################################################











