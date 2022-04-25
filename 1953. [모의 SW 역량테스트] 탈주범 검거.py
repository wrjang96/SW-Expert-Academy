T = int(input())

move = [[],[[-1,0],[1,0],[0,1],[0,-1]],[[-1,0],[1,0]],[[0,1],[0,-1]],[[-1,0],[0,1]],[[1,0],[0,1]],[[1,0],[0,-1]],[[-1,0],[0,-1]]]
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [[0] * M for i in range(N)]
    visited = [[0] * M for i in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    queue =[]
    queue.append([R,C,0])
    visited[R][C] = 1
    for i in range(L):
        while queue:
            if queue[0][2] > i-1:
                break
            x,y,cnt = queue.pop(0)
            for j in range(len(move[arr[x][y]])):
                nx = x + move[arr[x][y]][j][0]
                ny = y + move[arr[x][y]][j][1]
                if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] ==0:
                    for j in range(len(move[arr[nx][ny]])):
                        tx = nx + move[arr[nx][ny]][j][0]
                        ty = ny + move[arr[nx][ny]][j][1]
                        if tx == x and ty == y:
                            queue.append([nx, ny, cnt + 1])
                            visited[nx][ny] = 1
                            break
    ans = 0
    for i in range(N):
        ans += sum(visited[i])
    print("#"+ str(test_case)+" "+ str(ans))