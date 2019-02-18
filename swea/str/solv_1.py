T = int(input())
for TC in range(1, T+1):
    pattern = input()
    sentence = input()
    
    p = len(pattern)
    p1 = pattern[0]
    noValue = True
    for i in range(len(sentence)):
        if sentence[i] == p1:
            c = sentence[i:i+p]
            if c == pattern:
                print(f"#{TC} 1")
                noValue = False
                break
    if noValue:
        print(f"#{TC} 0")