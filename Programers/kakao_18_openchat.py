'''
(2018년)KAKAO BLIND RECRUITMENT
오픈채팅방
'''
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
userList = {}
rn = len(record)
res = []
for i in range(rn):
    if record[i].split()[0] == "Change":
        userList.update({record[i].split()[1] : record[i].split()[2]})
    elif record[i].split()[0] == "Enter":
        userList.update({record[i].split()[1] : record[i].split()[2]})

for i in range(rn):
    if record[i].split()[0] == "Enter":
        res.append(userList.get(record[i].split()[1])+"님이 들어왔습니다.")
    elif record[i].split()[0] == "Leave":
        res.append(userList.get(record[i].split()[1]) + "님이 나갔습니다.")
    else:
        pass