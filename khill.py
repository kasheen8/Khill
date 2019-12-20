Alphabet = 'АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
lngt = len(Alphabet)
T = {'А':1,'Б':2,'В':6,'Г':7,'Д':8,'Е':5,'Ж':9,'З':10,'И':3,'К':11,'Л':12,'М':13,'Н':4,'О':14,'П':15,'Р':16,'С':17,
     'Т':18,'У':19,'Ф':20,'Х':21,'Ц':22,'Ч':23,'Ш':24,'Щ':25,'Ъ':26,'Ы':27,'Ь':28,'Э':29,'Ю':30,'Я':0}
sampleK = [[14,15,6,16],[17,11,13,5],[19,11,1,1],[10,1,0,25]]
sampleInvK = [[2,16,28,13],[1,9,1,0],[25,8,26,26],[19,23,21,6]]

import numpy as np

def printmat(M):
    for row in M:
        print(' '.join([str(elem) for elem in row]))
    print('\n')

def determ3(M):
    det = (M[0][0] * M[1][1] * M[2][2] + M[0][1] * M[1][2] * M[2][0] + M[0][2] * M[1][0] * M[2][1] -
           M[0][0] * M[1][2] * M[2][1] - M[0][1] * M[1][0] * M[2][2] - M[0][2] * M[1][1] * M[2][0])
    return det

def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
        return d, y, x - y * (a // b)

def invMat(M):
    invM = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(4):
        for j in range(4):
            matr = M[:][:]
            a = np.delete(matr,i,axis=0)
            a = np.delete(a,j,axis=1)
            invM[i][j] =  (((-1) ** (i+j))* determ3(a)) % lngt
    invM = np.array(invM)
    invM = invM.transpose()
    d,x,y = gcdex(determ(M),lngt)
    for i in range(4):
        for j in range(4):
            invM[i][j] = invM[i][j] * x % lngt
    return invM

def determ(M):
    det = (M[0][0] * (M[1][1] * M[2][2] * M[3][3] + M[1][2] * M[2][3] * M[3][1] + M[1][3] * M[2][1] * M[3][2] -
    M[1][3] * M[2][2] * M[3][1] - M[1][1] * M[2][3] * M[3][2] - M[1][2] * M[2][1] * M[3][3]) -
    M[0][1] * (M[1][0] * M[2][2] * M[3][3] + M[1][2] * M[2][3] * M[3][0] + M[1][3] * M[2][0] * M[3][2] -
    M[1][3] * M[2][2] * M[3][0] - M[1][0] * M[2][3] * M[3][2] - M[1][2] * M[2][0] * M[3][3]) +
    M[0][2] * (M[1][0] * M[2][1] * M[3][3] + M[1][1] * M[2][3] * M[3][0] + M[1][3] * M[2][0] * M[3][1] -
    M[1][3] * M[2][1] * M[3][0] - M[1][0] * M[2][3] * M[3][1] - M[1][1] * M[2][0] * M[3][3]) -
    M[0][3] * (M[1][0] * M[2][1] * M[3][2] + M[1][1] * M[2][2] * M[3][0] + M[1][2] * M[2][0] * M[3][1] -
    M[1][2] * M[2][1] * M[3][0] - M[1][0] * M[2][2] * M[3][1] - M[1][1] * M[2][0] * M[3][2]))
    return det

def readText():
    a = input('Выберете способ ввода текста:\n1)Напечатать вручную\n2)Из файла\n')
    while a!='1' and a!='2':
        a = input('Выберете способ ввода текста:\n1)Напечатать вручную\n2)Из файла\n')
    if a == '1':
        text = input()
    else:
        a = open('Текст.txt')
        text = a.read()
    print(text + '\n')
    return text

from random import randint
def genMatrix():
    K1 = [[randint(0, lngt), randint(0, lngt), randint(0, lngt), randint(0, lngt)],
          [randint(0, lngt), randint(0, lngt), randint(0, lngt), randint(0, lngt)],
          [randint(0, lngt), randint(0, lngt), randint(0, lngt), randint(0, lngt)],
          [randint(0, lngt), randint(0, lngt), randint(0, lngt), randint(0, lngt)]]
    while determ(K1) == 0:
        K1 = [[randint(0,lngt),randint(0,lngt),randint(0,lngt),randint(0,lngt)],
          [randint(0, lngt), randint(0, lngt), randint(0, lngt), randint(0, lngt)],
          [randint(0, lngt), randint(0, lngt), randint(0, lngt), randint(0, lngt)],
          [randint(0, lngt), randint(0, lngt), randint(0, lngt), randint(0, lngt)]]
    return K1


def editText():
    text = readText()
    text = text.upper()
    text = text.replace('Й','И')
    text = text.replace('Ё','Е')
    for char in text:
        if Alphabet.find(char) == -1:
            text = text.replace(char,'')
    while len(text)%4 != 0:
        text += 'Ъ'
    print(text + '\n')
    text = codeText(text)
    return text

def codeText(text):
    L = [[T[text[i]],T[text[i+1]],T[text[i+2]],T[text[i+3]]] for i in range(0,len(text),4)]
    return L

def decodeText(decodeText):
    text = ''
    for string in decodeText:
        for number in string:
            for keys in T:
                if T[keys]==number:
                    text += keys
                    break
    return text

def encrypt(codeText,codeMatrix):
    for string in codeText:
        newstring = string[:]
        string[0]=(newstring[0] * codeMatrix[0][0] + newstring[1] * codeMatrix[0][1] + newstring[2] * codeMatrix[0][2] + newstring[
            3] * codeMatrix[0][3]) % lngt
        string[1] = (newstring[0] * codeMatrix[1][0] + newstring[1] * codeMatrix[1][1] + newstring[2] * codeMatrix[1][2] + newstring[
            3] * codeMatrix[1][3]) % lngt
        string[2] = (newstring[0] * codeMatrix[2][0] + newstring[1] * codeMatrix[2][1] + newstring[2] * codeMatrix[2][2] + newstring[
            3] * codeMatrix[2][3]) % lngt
        string[3] = (newstring[0] * codeMatrix[3][0] + newstring[1] * codeMatrix[3][1] + newstring[2] * codeMatrix[3][2] + newstring[
            3] * codeMatrix[3][3]) % lngt
    return codeText

def delEr(text):
    if text[-1]=='Ъ':
        text=text.rstrip('Ъ')
    return text

def mainLoop(matrix,invMatrix):
    choice = '0'
    myMatrix = 0
    while choice != '1' and choice != '2' and choice != '3':
        choice = input('Выберите режим\n1)Шифрование\n2)Расшифровывание\n3)Выход\n')
    if choice == '1':
        myMatrix = matrix
    elif choice == '2':
        myMatrix = invMatrix
    elif choice == '3':
        return 0
    codeText = editText()
    codeText = encrypt(codeText,myMatrix)
    codeText = decodeText(codeText)
    codeText = delEr(codeText)
    print(codeText + '\n')
    mainLoop(matrix,invMatrix)

if __name__ == "__main__":
    choice = '0'
    while choice!='1' and choice !='2':
        choice = input('Выберите способ получения ключевой матрицы:\n1)Сгенерировать случайно\n2)Использовать матрицу из задания\n')
    if choice == '1':
        K = genMatrix()
        invK = invMat(K)
        while determ(invK) == 0:
            K = genMatrix()
            invK = invMat(K)
    else:
        K = sampleK
        invK = sampleInvK
    print('Ключевая матрица:\n')
    printmat(K)
    print('Обратная матрица:\n')
    printmat(invK)
    mainLoop(K,invK)

