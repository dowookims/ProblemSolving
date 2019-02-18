T = int(input())
for TC in range(1, T + 1):
    nums = int(input())
    costs = list(map(int, input().split()))
    total_sum = 0
    max_number = max(costs)
    max_index = costs.index(max_number)
    start_num = 0
    div_sum = 0
    cnt = 0
    last = len(costs)
    # 값을 받고
    # 포문한번에 될거 같음
    # 1. 맥스 값을 찾는다
    # 2. 맥스값이 여러개 일 수도 있고
    # 3. 최종 맥스값 이후에도 다른 것들이 존재 할 수 있음.
    # 4. 마지막 값이 맥스값이 아니라면?? => 맥스값 이후 다시 케이스들을 구한다.
    # 5. 분할해서 구해보자
    while True:
        if max_index ==0:
            break

        for i in range(start_num, max_index):
            div_sum += i

        total_sum += div_sum
        costs = costs[max_index+1:]
        cnt += max_index
        
        if cnt == last:
            break
        start_num = 0
        div_sum = 0
        max_number = max(costs)
        max_index = costs.index(max_number)

    print(f'#{TC} {total_sum}')