n, m = map(int, input().split())
girl_group = []
for _ in range(n):
    group_name = input()
    members = int(input())
    for _ in range(members):
        member_name.append(input())
    member_name.sort()
    member_name.insert(0, group_name)
    girl_group.append(member_name)

# quiz
for _ in range(m):
    name_containing = input()
    member_or_team = int(input())
    if member_or_team == 0: # if member print
        for i in range(n):
            if name_containing in girl_group[i]:
                for j in name_containing:
                    print(j)
    else: # if team print
        for i in girl_group:
            print("not yet")


# 미완성
# 리스트 활용 방법
# 딕셔너리 활용 방법
# d
