n, m = map(int, input().split())
start = input()
S = [(ord(start[0]) - 96 - 1, int(start[1]) - 1)]
end = input()
end = (ord(end[0]) - 96 - 1, int(end[1]) - 1)

dx = [2, 1, 2, -1, 1, -1, -2, -2]
dy = [1, 2, -1, 2, -2, -2, 1, -1]

def Print(S):
    for i in S:
        print("{}{}".format(chr(i[0] + 97), i[1] + 1), end = ' ')

def backtracking(i, m, n, S):
    if i == m * n:
        x = S[len(S) - 1]
        if x == end:
            Print(S)
            exit()
    else:
        locate = S[len(S) - 1]
        for j in range(8):
            x = locate[0] + dx[j]
            y = locate[1] + dy[j]
            if 0 <= x and x < m and 0 <= y and y < n:
                if (x, y) not in S:
                    S.append((x, y))
                    backtracking(i + 1, m, n, S[:])
                    S.pop()

backtracking(1, m, n, S)
if len(S) == 1:
    print('Not Found')
