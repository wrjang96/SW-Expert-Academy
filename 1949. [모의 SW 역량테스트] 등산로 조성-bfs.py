T = int(input())
def bfs(x,y, num,tmp_arr):
    global K
    queue = []
    queue.append([x,y,0,[num],[[x,y]]])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    ans = 0
    while queue:
        tx,ty,flag,visited,t_arr = queue.pop(0)
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N  and [nx,ny] not in t_arr:
                if visited[-1] > arr[nx][ny]:
                    queue.append([nx,ny,flag, visited + [arr[nx][ny]], t_arr + [[nx,ny]]])
                else:
                    if flag == 0 and arr[tx][ty] - arr[nx][ny] <= K:
                        for j in range(1, K+1):
                            if arr[nx][ny] - j not in visited and arr[tx][ty] > arr[nx][ny] - j:
                                queue.append([nx, ny, 1, visited + [arr[nx][ny] - j], t_arr + [[nx,ny]]])
                            else:
                                ans = max(ans, len(visited))

                    else:
                        ans = max(ans, len(visited))
        # print(queue)
    return ans






for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    ans = 0
    arr = [[0] * N for i in range(N)]
    visited = [[0] * N for i in range(N)]
    max_num = 0
    for i in range(N):
        arr[i] = list(map(int,input().split()))
        max_num = max(max_num,max(arr[i]))
    final_ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max_num:
                final_ans = max(final_ans, bfs(i,j,arr[i][j],visited))
    print("#" + str(test_case) + " " + str(final_ans))
