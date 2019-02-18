# 가로 길이는 항상 1000이하, 높이는 최대 255
# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다
# 양쪽 모두 거리 2이상의 공간
# 배열로 받을 경우 인덱스 문제 => 맨왼쪽의 경우 두칸이 비어져있다고 생각
# 즉, 양 옆에 2, 2을 추가해서 작업하거나, 아니면 예외 처리를 하거나
# 1,2의 경우, len(a)-1, len(a)의 경우

a = int(input())
for i in range(1, 11):
    b = list(map(int,input().split()))
    w_c = 0
    for j in range(len(b)):
        # j = 0일때
        if j == 0:
            if b[0] > b[1] and b[0] > b[2]:
                w_c += b[0]-abs(b[1]-b[2])
        # j = 1일때 왼쪽 하나만 고려
        elif j == 1:

            if b[1] > b[2] and b[1] > b[3] and b[1]>b[0]:

                if b[0] > b[2] and b[0] > b[3]:
                    w_c += b[1]-b[0]

                else:
                    w_c += b[1]-abs(b[2]-b[3])
        # 
        elif j == len(b)-2:

            if b[j] > b[j+1] and b[j] > b[j-1] and b[j]>b[j-2]:

                if b[j+1] > b[j-1] and b[j+1] >b[j-2]:
                    w_c += b[j]-b[j+1]

                else:
                    w_c += b[j]-abs(b[j-1]-b[j-2])

        elif j == len(b)-1:

            if b[j] > b[j-1] and b[j] > b[j-2]:
                w_c += b[j]-abs(b[j-1]-b[j-2])

        else:
            if b[j] > b[j+1] and b[j] > b[j+2] and b[j] > b[j-1] and b[j] >b[j-2]:
                if abs(b[j-1] - b[j-2]) >= abs(b[j+1] - b[j+2]):
                    if b[j-1] > b[j-2]:
                        w_c += b[j]-b[j-1]
                    else :
                        w_c += b[j]-b[j-2]
                else:
                    if b[j+1]>b[j+2]:
                        w_c += b[j] - b[j+1]
                    else:
                        w_c += b[j] - b[j+2]
    print(f"#{i} {w_c}")