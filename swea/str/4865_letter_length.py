import sys
sys.stdin = open("sample_input3.txt","r")
for TC in range(1, int(input())+1):
    case = set(input())
    exam = input()
    count = {}
    for item in case:
        count.update({item:0})

    for letter in exam:
        if letter in count:
            count.update({letter:count.get(letter)+1})
    print(f"#{TC} {max(count.values())}")