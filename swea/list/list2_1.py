TC = int(input())
for case_num in range(1,TC+1):
    s_c = int(input())

    s_r = [] # 빨강 상자 담아둠
    s_b = [] # 파랑 상자 담아둠
    s_v = [[0 for _ in range(10)] for _ in range(10)] # 보라 색 출력
    cnt = 0
    #값을 받아 온 후 파랑과 빨강을 나눈다
    for _ in range(s_c):
        square = list(map(int, input().split()))
        if square[len(square)-1] == 2:
            s_b.append(square)
        else:
            s_r.append(square)

    # 각 상자를 담아둔 것에서
    # 빈 5x5 배열에 빨간색 상자를 다 그리고(1로 마크)
    # 빨간색이 칠해진 범위(마크가 되어있는 경우)에 파란색을 덧칠(2)
    # 파란색과 빨간색이 칠해진 범위를 카운트해서 반환

    for s in s_r:
        s_min_x, s_min_y, s_max_x, s_max_y = s[0:4]
        for i in range(s_min_x, s_max_x+1):
            for j in range(s_min_y, s_max_y+1):
                s_v[i][j] = 1
    
    for s in s_b:
        s_min_x, s_min_y, s_max_x, s_max_y = s[0:4]
        for i in range(s_min_x, s_max_x+1):
            for j in range(s_min_y, s_max_y+1):
                if s_v[i][j] == 1:
                    cnt += 1

    print(f"#{case_num} {cnt}")
    
    

