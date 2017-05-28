def answer(members, teamsFormedAlready):
    membersJoined=2*teamsFormedAlready
    membersRemaining=members-membersJoined
    if membersRemaining%2==0:
        return 'yes'
    else:
        return 'no'

testcases=int(input())
for i in range(testcases):
    members, teams = input().strip().split()
    members, teams= [int(members), int(teams)]
    for i in range(teams):
        a, b=input().strip().split()
    print(answer(members, teams))

