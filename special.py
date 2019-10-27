def zzql(card):
    for i in range(4):
        temp = 0
        for j in range(13):
            temp = temp + card[i][j]
        if temp==13:
            return 1
    return 0
def ytl(card):
    for i in range(13):
        temp = card[0][i]+card[1][i]+card[2][i]+card[3][i]
        if temp != 1:
            return 0
    return 1
def sftx(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    temp = 0
    for j in range(13):
        if num[j] == 4:
            temp = temp + 1
    if temp == 3:
        return 1
    else:
        return 0
def sth(card):
    num = [0, 0, 0, 0]
    for i in range(4):
        for j in range(13):
            num[i] = num[i] + card[i][j]
    temp1 = 0
    temp2 = 0
    temp3 = 0
    for i in range(4):
        if num[i] >= 5:
            temp1 = 1
            num[i] = num[i] - 5
            break
    if temp1 == 0:
        return 0
    for i in range(4):
        if num[i] >= 5:
            temp2 = 1
            num[i] = num[i] - 5
            break
    if temp2 == 0:
        return 0
    for i in range(4):
        if num[i] >= 3:
            temp3 = 1
            num[i] = num[i] - 3
            break
    if temp3 == 1:
        return 1
    else:
        return 0
def sths(card):
    card1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
    card1[0] = card[0]
    card1[1] = card[1]
    card1[2] = card[2]
    card1[3] = card[3]
    temp1 = 0
    temp2 = 0
    temp3 = 0
    for j in range(4):
        for i in range(9):
            if card1[j][i] == 1 and card1[j][i + 1] == 1 and card1[j][i + 2] == 1 and card1[j][i + 3] == 1 \
                    and card1[j][i + 4] == 1:
                card1[j][i] = 0
                card1[j][i + 1] = 0
                card1[j][i + 2] = 0
                card1[j][i + 3] = 0
                card1[j][i + 4] = 0
                temp1 = 1
                break
        if temp1 == 1:
            break
    if temp1 == 0:
        return 0
    print(card)
    for j in range(4):
        for i in range(9):
            if card1[j][i] == 1 and card1[j][i + 1] == 1 and card1[j][i + 2] == 1 and card1[j][i + 3] == 1 and card1[j][
                i + 4] == 1:
                card1[j][i] = 0
                card1[j][i + 1] = 0
                card1[j][i + 2] = 0
                card1[j][i + 3] = 0
                card1[j][i + 4] = 0
                temp2 = 1
                break
        if temp2 == 0:
            break
    if temp2 == 0:
        return 0
    for j in range(4):
        for i in range(11):
            if card1[j][i] == 1 and card1[j][i + 1] == 1 and card1[j][i + 2] == 1:
                card1[j][i] = 0
                card1[j][i + 1] = 0
                card1[j][i + 2] = 0
                card1[j][i + 3] = 0
                card1[j][i + 4] = 0
                temp3 = 1
                break
    if temp3 == 1:
        return 1
    else:
        return 0
def ssz(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    temp1 = 0
    temp2 = 0
    temp3 = 0
    for i in range(9):
        if num[i] > 0 and num[i + 1] > 0 and num[i + 2] > 0 and num[i + 3] > 0 and num[i + 4] > 0:
            num[i] = num[i] - 1
            num[i + 1] = num[i + 1] - 1
            num[i + 2] = num[i + 2] - 1
            num[i + 3] = num[i + 3] - 1
            num[i + 4] = num[i + 4] - 1
            temp1 = 1
            break
    if temp1 == 0:
        return 0
    for i in range(9):
        if num[i] > 0 and num[i + 1] > 0 and num[i + 2] > 0 and num[i + 3] > 0 and num[i + 4] > 0:
            num[i] = num[i] - 1
            num[i + 1] = num[i + 1] - 1
            num[i + 2] = num[i + 2] - 1
            num[i + 3] = num[i + 3] - 1
            num[i + 4] = num[i + 4] - 1
            temp2 = 1
            break
    if temp2 == 0:
        return 0
    for i in range(11):
        if num[i] > 0 and num[i + 1] > 0 and num[i + 2] > 0:
            num[i] = num[i] - 1
            num[i + 1] = num[i + 1] - 1
            temp3 = 1
            break
    if temp3 == 0:
        return 0
    else:
        return 1
def wdst(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    temp1 = 0
    temp2 = 0
    for j in range(13):
        if num[j] == 3:
            temp1 = temp1 + 1
        if num[j] == 2:
            temp2 = temp2 + 1
    if temp1 == 1 and temp2 == 5:
        return 1
    else:
        return 0
def qd(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp = 0
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    for j in range(6):
        temp = temp + num[j]
    if temp == 0:
        return 1
    else:
        return 0
def qx(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp = 0
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    for j in range(7):
        temp = temp + num[j]
    if temp == 13:
        return 1
    else:
        return 0
def ldb(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    temp1 = 0
    for j in range(13):
        if num[j] == 2:
            temp1 = temp1 + 1
    if temp1 == 6:
        return 1
    else:
        return 0
def cys(card):
    num = [0, 0, 0, 0]
    for i in range(4):
        for j in range(13):
            num[i] = num[i] + card[i][j]
    if num[0] + num[1] == 13:
        return 1
    elif num[2] + num[3] == 13:
        return 1
    else:
        return 0
def sehz(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    if num[9] + num[10] + num[11] + num[12] >= 12:
        return 1
    else:
        return 0
def sgcs(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    temp1 = 0
    temp2 = 0
    for j in range(13):
        if num[j] == 3:
            temp1 = temp1 + 1
        if num[j] == 2:
            temp2 = temp2 + 1
    if temp1 == 2 and temp2 == 3:
        return 1
    else:
        return 0
def stst(card):
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(13):
        num[i] = card[0][i] + card[1][i] + card[2][i] + card[3][i]
    temp1 = 0
    for j in range(13):
        if num[j] == 3:
            temp1 = temp1 + 1
    if temp1 == 4:
        return 1
    else:
        return 0
