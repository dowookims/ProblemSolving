# 2050. 알파벳을 숫자로 변환
#
# 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
# [입력]
#알파벳으로 이루어진 문자열이 주어진다.
# [출력]
# 각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다
# 출력 8 7 6 5 4 3 2 1 0
print(' '.join([str(ord(i)-64) for i in input()]))