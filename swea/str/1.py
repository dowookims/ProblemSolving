'''
과제 제출자
제출하지 앟은 사람의 번호를 오름차순으로 출력하라
1. 테스트 케이스
2. 총원 / 제출한 사람
3. 번호
제출하지 않은 사람의 번호 오름차순 출력
'''
T = int(input())
for TC in range(1, T+1):
    total_num, submit_num = list(map(int, input().split()))
    submit_people = list(map(int, input().split()))
    count_list = [0]*total_num
    result =''
    for person in submit_people:
        count_list[person-1] += 1

    for i in range(len(count_list)):
        if count_list[i] == 0:
            result += str(i+1)+' '

    print(f"#{TC} {result}")

