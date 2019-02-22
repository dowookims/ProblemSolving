'''
포도주 시식
포도주 다 마셔야 하고, 마신후 원위치
연속으로 놓여있는 3잔 못마심
'''
T = int(input())
drink = [0] * T
for i in range(len(drink)):
    drink[i] = int(input())

print(drink)