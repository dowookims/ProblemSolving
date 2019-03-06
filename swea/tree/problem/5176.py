import sys
sys.stdin = open("5176.txt", "r")

T = int(input())
def find_height(N):
    h = 1
    maxsize = 1
    while maxsize < N:
        h += 1
        maxsize = 2*maxsize + 1
    return h

for tc in range(1,T+1):
    N = int(input())
    heap = [0 for _ in range(N+1)]
    height = find_height(N)
    current = 1 << (height-1)
    is_included = []
    for value in range(1, N+1):
        heap[current] = value
        is_included.append(current)
        if current*2 + 1 <= N:
            current = current*2 + 1
            while current*2 <= N:
                current = current * 2
        else:
            current = current // 2
            while current // 2 > 0:
                if current in is_included:
                    current = current // 2
                else:
                    break
    print("#{} {} {}".format(tc, heap[1], heap[N//2]))