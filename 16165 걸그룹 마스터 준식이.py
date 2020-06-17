# List 활용 방법
n, m = map(int, input().split())
girl_group = []

# getting input
for _ in range(n):
    group_name = input()
    members = int(input())
    member_name = []
    for _ in range(members):
        member_name.append(input())
    member_name.sort()
    member_name.insert(0, group_name)
    girl_group.append(member_name)

# quiz
for _ in range(m):
    girl = input()  
    member_or_team = int(input())  
    if member_or_team == 0:  # if member print
        for i in range(n):
            if girl == girl_group[i][0]:
                for j in girl_group[i][1:]:
                    print(j)
                break

    else:  # if team print
        for i in range(n):
            if girl in girl_group[i]:
                print(girl_group[i][0])

                
"""
딕셔너리 활용 방법은?
"""
