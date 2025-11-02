#Лабораторная работа номер 3, вариант 3

def turn(i, sys):
    answ = ''
    while i != 0:
        answ += str(i % sys)
        i //= sys
    answ = list(map(int, answ[::-1]))
    return [0] * (n - len(answ)) + answ

def func(alp, n, i = 0):
    if i == len(alp) ** n:
        return
    print([alp[j] for j in turn(i, len(alp))])
    func(alp, n, i + 1)

alp = input().split()
n = int(input())
func(alp, n)
