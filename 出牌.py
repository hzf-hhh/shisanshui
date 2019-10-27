import special
import itertools
import json
import re
import math
import copy

def findcolor(string):
    color = [0, 0, 0, 0, 0]
    p = 0
    for j in range(len(string)):
        if string[j] == '$':
            color[p] = 0
            p = p + 1
        elif string[j] == '&':
            color[p] = 1
            p = p + 1
        elif string[j] == '*':
            color[p] = 2
            p = p + 1
        elif string[j] == '#':
            color[p] = 3
            p = p + 1
    return color
def findd(string):
    num = [0, 0, 0, 0, 0]
    p = 0
    for j in range(len(string)):
        i = j+1
        if string[j] == '$' or string[j] == '&' or string[j] == '#' or string[j] == '*':
            if string[i] == 'A':
                num[p] = 14
            elif string[i] == '2':
                num[p] = 2
            elif string[i] == '3':
                num[p] = 3
            elif string[i] == '4':
                num[p] = 4
            elif string[i] == '5':
                num[p] = 5
            elif string[i] == '6':
                num[p] = 6
            elif string[i] == '7':
                num[p] = 7
            elif string[i] == '8':
                num[p] = 8
            elif string[i] == '9':
                num[p] = 9
            elif string[i] == '1':
                num[p] = 10
            elif string[i] == 'J':
                num[p] = 11
            elif string[i] == 'Q':
                num[p] = 12
            elif string[i] == 'K':
                num[p] = 13
            p = p + 1
    return num
def check1(string):#五张牌的判断牌型
    num = findd(string)
    changenum = sorted(num)
    color = findcolor(string)
    if color[0] == color[1] == color[2] == color[3] == color[4] and changenum[4] == changenum[3]+1 == changenum[2]+2 ==\
        changenum[1]+3 == changenum[0]+4:
        temp = [9,changenum[4]]
        return temp
    if changenum[0] == changenum[1] == changenum[2] == changenum[3] or changenum[1] == changenum[2] == changenum[3] == \
        changenum[4]:
        temp = [8,changenum[2]]
        return temp
    if (changenum[0] == changenum[1] and changenum[2] == changenum[3] == changenum[4]) \
        or (changenum[0] == changenum[1] == changenum[2] and changenum[3] == changenum[4]):
        temp = [7,changenum[2]]
        return temp
    if color[0] == color[1] == color[2] == color[3] == color[4]:
        temp = [6,changenum[4]]
        return temp
    if changenum[4] == changenum[3]+1 == changenum[2]+2 == changenum[1]+3 == changenum[0]+4:
        temp = [5,changenum[4]]
        return temp
    if (changenum[0] == changenum[1] == changenum[2] ) or (changenum[1] == changenum[2] == changenum[3]) or \
            changenum[2] == changenum[3] == changenum[4]:
        temp = [4,changenum[2]]
        return temp
    if changenum[0] == changenum[1] and changenum[2] == changenum[3]:
        if changenum[1]+1 == changenum[3]:
            temp = [2.5,changenum[3]]
        else:
            temp = [2,changenum[3]]
        return temp
    if changenum[0] == changenum[1] and changenum[3] == changenum[4]:
        if changenum[1] + 1 == changenum[3]:
            temp = [2.5, changenum[3]]
        else:
            temp = [2, changenum[3]]
        return temp
    if changenum[1] == changenum[2] and changenum[3] == changenum[4]:
        if changenum[1]+1 == changenum[3]:
            temp = [2.5,changenum[3]]
        else:
            temp = [2,changenum[3]]
        return temp
    if changenum[0] == changenum[1]:
        temp = [2,changenum[0]]
        return temp
    if changenum[1] == changenum[2]:
        temp = [2, changenum[1]]
        return temp
    if changenum[2] == changenum[3]:
        temp = [2, changenum[2]]
        return temp
    if changenum[3] == changenum[4]:
        temp = [2, changenum[3]]
        return temp
    temp = [1,changenum[4]]
    return temp
def check2(string):#三张牌的判断牌型
    num = findd(string)
    if num[0] == num[1] == num[2]:
        temp = [4,num[0]]
        return temp
    elif num[0] == num[1]:
        temp = [2,num[0]]
        return temp
    elif num[0] == num[2]:
        temp = [2,num[0]]
        return temp
    elif num[1] == num[2]:
        temp = [2,num[1]]
        return temp
    elif num[0] != num[1] and num[0] != num[2] and num[1] != num[2]:
        temp = [1,max(num[0],num[1],num[2])]
        return temp
def find(string):
    card = [[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
    for j in range(len(string)):
        i = j+1
        if string[j] == '$':
            if string[i] == 'A':
                card[0][12] = 1
            elif string[i] == '2':
                card[0][0] = 1
            elif string[i] == '3':
                card[0][1] = 1
            elif string[i] == '4':
                card[0][2] = 1
            elif string[i] == '5':
                card[0][3] = 1
            elif string[i] == '6':
                card[0][4] = 1
            elif string[i] == '7':
                card[0][5] = 1
            elif string[i] == '8':
                card[0][6] = 1
            elif string[i] == '9':
                card[0][7] = 1
            elif string[i] == '1':
                card[0][8] = 1
            elif string[i] == 'J':
                card[0][9] = 1
            elif string[i] == 'Q':
                card[0][10] = 1
            elif string[i] == 'K':
                card[0][11] = 1
        elif string[j] == '&':
            if string[i] == 'A':
                card[1][12] = 1
            elif string[i] == '2':
                card[1][0] = 1
            elif string[i] == '3':
                card[1][1] = 1
            elif string[i] == '4':
                card[1][2] = 1
            elif string[i] == '5':
                card[1][3] = 1
            elif string[i] == '6':
                card[1][4] = 1
            elif string[i] == '7':
                card[1][5] = 1
            elif string[i] == '8':
                card[1][6] = 1
            elif string[i] == '9':
                card[1][7] = 1
            elif string[i] == '1':
                card[1][8] = 1
            elif string[i] == 'J':
                card[1][9] = 1
            elif string[i] == 'Q':
                card[1][10] = 1
            elif string[i] == 'K':
                card[1][11] = 1
        elif string[j] == '*':
            if string[i] == 'A':
                card[2][12] = 1
            elif string[i] == '2':
                card[2][0] = 1
            elif string[i] == '3':
                card[2][1] = 1
            elif string[i]== '4':
                card[2][2] = 1
            elif string[i] == '5':
                card[2][3] = 1
            elif string[i] == '6':
                card[2][4] = 1
            elif string[i] == '7':
                card[2][5] = 1
            elif string[i] == '8':
                card[2][6] = 1
            elif string[i] == '9':
                card[2][7] = 1
            elif string[i] == '1':
                card[2][8] = 1
            elif string[i] == 'J':
                card[2][9] = 1
            elif string[i] == 'Q':
                card[2][10] = 1
            elif string[i] == 'K':
                card[2][11] = 1
        elif string[j] == '#':
            if string[i] == 'A':
                card[3][12] = 1
            elif string[i] == '2':
                card[3][0] = 1
            elif string[i] == '3':
                card[3][1] = 1
            elif string[i] == '4':
                card[3][2] = 1
            elif string[i] == '5':
                card[3][3] = 1
            elif string[i] == '6':
                card[3][4] = 1
            elif string[i] == '7':
                card[3][5] = 1
            elif string[i] == '8':
                card[3][6] = 1
            elif string[i] == '9':
                card[3][7] = 1
            elif string[i] == '1':
                card[3][8] = 1
            elif string[i] == 'J':
                card[3][9] = 1
            elif string[i] == 'Q':
                card[3][10] = 1
            elif string[i] == 'K':
                card[3][11] = 1
    return card
def specialcard(string):
    list = [' ',' ',' ']
    list1 = string.split()
    string1 = list1[0] + ' ' + list1[1] + ' ' + list1[2]
    string2 = list1[3] + ' ' + list1[4] + ' ' + list1[5] + ' ' + list1[6] + ' ' + list1[7]
    string3 = list1[8] + ' ' + list1[9] + ' ' + list1[10] + ' ' + list1[11] + ' ' + list1[12]
    list[0] = string1
    list[1] = string2
    list[2] = string3
    return list
def pickcard(string):
    card = find(string)
    if special.zzql(card)!=0 or special.ytl(card)!=0 or special.sftx(card)!=0 or special.sth(card)!=0 or special.sths(card)!=0 \
        or special.ssz(card)!=0 or special.wdst(card)!=0 or special.qd(card)!=0 or special.qx(card)!=0 or special.ldb(card)!=0 \
        or special.cys(card)!=0 or special.sehz(card)!=0 or special.sgcs(card)!=0 or special.stst(card)!=0:
        list = specialcard(string)
        return list
    else:
        list = string.split()
        list1 = [' ', ' ', ' ']
        front = ' '
        middle = ' '
        bottom = ' '
        temp1 = [-1, -1]
        temp2 = [-1, -1]
        temp3 = [-1, -1]
        for i in itertools.combinations(list,5):
            xxx = copy.deepcopy(list)
            for y in i:
                xxx.remove(y)
            for j in itertools.combinations(xxx,5):
                p = copy.deepcopy(xxx)
                for t in j:
                    p.remove(t)
                string1 = ' '.join(i)
                string2 = ' '.join(j)
                string3 = ' '.join(p)
                frontvalue = check1(string1)
                middlevalue = check1(string2)
                bottomvalue = check2(string3)
                if frontvalue[0] > middlevalue[0] or (frontvalue[0] == middlevalue[0] and frontvalue[1] >= middlevalue[1]):
                    if middlevalue[0] > bottomvalue[0] or (middlevalue[0] == bottomvalue[0] and middlevalue[1] >= bottomvalue[1]):
                        if front == ' ':
                            front = string1
                            middle = string2
                            bottom = string3
                            temp1 = frontvalue
                            temp2 = middlevalue
                            temp3 = bottomvalue
                        else:
                            win1 = 0
                            win2 = 0
                            win3 = 0
                            if frontvalue[0] > temp1[0]:
                                win1 = 1
                            elif frontvalue[0] == temp1[0]:
                                if frontvalue[1] > temp1[1]:
                                    win1 = 1
                                elif frontvalue[1] == temp1[1]:
                                    win1 = 0
                                elif frontvalue[1] < temp1[1]:
                                    win1 = -1
                            elif frontvalue[0] < temp1[0]:
                                win1 = -1
                            if middlevalue[0] > temp2[0]:
                                win2 = 1
                            elif middlevalue[0] == temp2[0]:
                                if middlevalue[1] > temp2[1]:
                                    win2 = 1
                                elif middlevalue[1] == temp2[1]:
                                    win2 = 0
                                elif middlevalue[1] < temp2[1]:
                                    win2 = -1
                            elif middlevalue[0] < temp2[0]:
                                win2 = -1
                            if bottomvalue[0] > temp3[0] :
                                win3 = 1
                            elif bottomvalue[0] == temp3[0]:
                                if bottomvalue[1] > temp3[1]:
                                    win3 = 1
                                elif bottomvalue[1] == temp3[1]:
                                    win3 = 0
                                elif bottomvalue[1] < temp3[1]:
                                    win3 = -1
                            elif bottomvalue[0] < temp3[0]:
                                win3 = -1
                            if win1 + win2 + win3 > 0:
                                front = string1
                                middle = string2
                                bottom = string3
                                temp1 = frontvalue
                                temp2 = middlevalue
                                temp3 = bottomvalue
        list1[0] = bottom
        list1[1] = middle
        list1[2] = front
        return list1
def cp(string):
    list = pickcard(string)
    return list