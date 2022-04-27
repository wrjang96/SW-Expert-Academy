T = int(input())
move = [[-1,1],[1,1],[1,-1],[-1,-1]]
# def dfs
def search(x,y):
    global arr
    queue = [[0, x,y,1,[arr[x][y]]]]
    return_ans = 0
    while queue:
        # print(queue)
        flag, tx, ty, cnt, ans_queue = queue.pop(0)
        if cnt !=1 and flag < 3:
            nx = tx + move[flag+1][0]
            ny = ty + move[flag+1][1]
            if 0 <= nx < N and 0 <= ny < N:
                if nx == x and ny == y and cnt != 1:
                    # print(ans_queue)
                    return_ans = max(len(ans_queue), return_ans)
                if arr[nx][ny] not in ans_queue:
                    queue.append([flag+1, nx, ny, 2, ans_queue + [arr[nx][ny]]])
        nx = tx + move[flag][0]
        ny = ty + move[flag][1]
        if 0 <= nx < N and 0 <= ny < N:
            if nx == x and ny == y and cnt != 1:
                # print(ans_queue)
                return_ans = max(len(ans_queue), return_ans)

            if arr[nx][ny] not in ans_queue:
                queue.append([flag, nx, ny, cnt + 1, ans_queue + [arr[nx][ny]]])
    return return_ans
for test_case in range(1, T + 1):
    ans = -1
    N = int(input())
    arr = [[0] * N for i in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            ans = max(ans,search(i,j))
    if ans == 0:
        ans = -1
    print("#"+ str(test_case)+" "+ str(ans))
