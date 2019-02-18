'''
정곤이의 단조 증가하는 수
k자리 수 X = d1d2…dk 가 d1 ≤ d2 ≤ … ≤ dk 를 만족하면 단조 증가하는 수

양의 정수 N 개 A1, …, AN이 주어진다.

1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값이 단조 증가하는 수인 것들을 구하고 그 중의 최댓값을 출력하는 프로그램을 작성하라.

'''

a = int(input())
for w in range(a):
    b = int(input())
    c = list(map(int, input().split()))
    max_n = 0

    for i in range(len(c)-2):
        for j in range(i+1, len(c)-1):
            k = str(c[i]*c[j])
            t = 0
            for q in range(len(k)-1):
                if k[q] > k[q+1]:
                    break
                else:
                    t += 1
            if t == len(k)-1 and int(k) > max_n:
                max_n = int(k)
    if max_n == 0:
        max_n = -1
    print(f'#{w+1} {max_n}')


'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
 
    ans = -1
    for i in range(N):
        for j in range(i + 1, N):
            num = data[i] * data[j]
            if ans >= num:
                continue
            b = num % 10
            val = num//10
            ok = True
            while val:
                a = val % 10
                if a > b:
                    ok = False
                    break
                val = val//10
                b = a
            if ok:
                ans = max(ans, num)
 
    print("#{} {}".format(test_case, ans))
'''