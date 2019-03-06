import sys
sys.stdin = open("dasol.txt", "r")

for TC in range(1, int(input())+1):
    word = input()
    n = len(word)
    o = '..#.'
    e = '.#.#'
    print(o*n+'.')
    print(e*n+'.')
    for i in range(len(word)):
        d = '#.{}.'.format(word[i])
        print(d,end="")
    print('#')
    print(e * n + '.')
    print(o * n + '.')
