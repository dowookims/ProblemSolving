'''
회문
100*100배열에서 가장 긴 회문 구하기
주어지는 글자는 'A','B','C'
글자판은 정사각형
1. 100 x 100 배열을 받고
2. row / col 별로 펠린드롬을 조사한다.
3. 초기 max_length를 0으로 잡고
4. 비교하면서 조사.
'''
# def isPal(text):
#     if len(text) == 1:
#         return True
#     if text[0] == text[len(text)-1]:
#         if len(text) == 2:
#             return True
#         else:
#             text = text[1:len(text)-1]
#     return isPal(text)

def isPal(text):
    while True:
        if len(text) == 1:
            return True
        if text[0] == text[len(text)-1]:
            if len(text) == 2:
                return True
            else:
                text = text[1:len(text)-1]
        else:
            return False



T = 10
for _ in range(T):
    TC = int(input())
    alpha_list = [0]*100

    for i in range(100):
        alpha_list[i] = list(input().split())
    pass_count = 0
    max_length = 0

    for r in range(100):
        

    for c in range(100):


    print(f"#{TC} {max_length}")
