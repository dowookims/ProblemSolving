n = 20
f = r = -1
q = [0] * 100
candis = 20
studcan = [1] * 20

sn = 1
nextsn = 2

r += 1
q[r] = sn
print(f"===>%{sn}번 학생 입장하여 줄을선다.")
print(f'학생 줄 : {q[f+1:r+1]}')

while candis >0 :
    if candis > studcan[sn]: candis -= studcan[sn]
    elif studcan[sn] == candis: candis -= studcan[sn]
    print(f"{sn}번 학생 : 선생님한테 사탕 {studcan[sn]}개를 받는다.")
    print(f"======= 남은 사탕의 개수는 {candis}개다.")
    print()
    studcan[sn] += 1

    if candis <= 0:
        print(f"{sn}번 학생이 마지막 사탕을 받아간다.")
        break
    
    r += 1
    q[r] = sn

    print(f"{sn}번 학생 : 다시 줄을 선다.")
    print(f"학생 줄 : {q[f+1:r+1]}")
    print(f"==> {nextsn}번 학생 : 입장하여 줄을 선다")

    r += 1
    q[r] = nextsn
    print(f"학생 줄 : {q[f+1:r+1]} ")

    nextsn +=1
    f += 1
    sn = q[f]
    print(f"{sn}번 학생 : 줄에서 나와...")
    print(f"학생 줄 : {q[f+1:r+1]}")
