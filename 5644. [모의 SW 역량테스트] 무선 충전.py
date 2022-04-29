T = int(input())
def cal(A,B):
    ans = 0
    if len(arr[A[0]][A[1]]) > 0 and len(arr[B[0]][B[1]]) > 0:
        if len(arr[A[0]][A[1]]) == 1 and len(arr[B[0]][B[1]]) == 1:
            if arr[A[0]][A[1]][0][0] == arr[B[0]][B[1]][0][0]:
                ans += arr[A[0]][A[1]][0][1]
            else:
                ans += (arr[A[0]][A[1]][0][1] + arr[B[0]][B[1]][0][1])
        elif len(arr[A[0]][A[1]]) == 1 and len(arr[B[0]][B[1]]) == 2:
            tmp = []
            for j in range(len(arr[B[0]][B[1]])):
                if arr[A[0]][A[1]][0][0] == arr[B[0]][B[1]][j][0]:
                    tmp.append(arr[B[0]][B[1]][j][1])
                else:
                    tmp.append(arr[A[0]][A[1]][0][1] + arr[B[0]][B[1]][j][1])
            ans += max(tmp)
        elif len(arr[A[0]][A[1]]) == 2 and len(arr[B[0]][B[1]]) == 1:
            tmp = []
            for j in range(len(arr[A[0]][A[1]])):
                if arr[A[0]][A[1]][j][0] == arr[B[0]][B[1]][0][0]:
                    tmp.append(arr[A[0]][A[1]][j][1])
                else:
                    tmp.append(arr[A[0]][A[1]][j][1] + arr[B[0]][B[1]][0][1])
            ans += max(tmp)
        else:
            tmp = []
            for j in range(len(arr[A[0]][A[1]])):
                for k in range(len(arr[B[0]][B[1]])):
                    if arr[A[0]][A[1]][j][0] == arr[B[0]][B[1]][k][0]:
                        tmp.append(arr[A[0]][A[1]][j][1])
                    else:
                        tmp.append(arr[A[0]][A[1]][j][1] + arr[B[0]][B[1]][k][1])
            ans += max(tmp)
    elif len(arr[A[0]][A[1]]) > 0:
        if len(arr[A[0]][A[1]]) == 1:
            ans += arr[A[0]][A[1]][0][1]
        else:
            tmp = []
            for j in range(len(arr[A[0]][A[1]])):
                tmp.append(arr[A[0]][A[1]][j][1])
            ans += max(tmp)
    elif len(arr[B[0]][B[1]]) > 0:
        if len(arr[B[0]][B[1]]) == 1:
            ans += arr[B[0]][B[1]][0][1]
        else:
            tmp = []
            for j in range(len(arr[B[0]][B[1]])):
                tmp.append(arr[B    [0]][B[1]][j][1])
            ans += max(tmp)
    return ans

def fill(sx,sy,arr,C,k,P):
    queue = [[sx,sy,0]]
    dx = [0,-1,0,1,0]
    dy = [0,0,1,0,-1]
    arr[sx][sy].append([k,P])
    visited = [[0] * 10 for i in range(10)]
    visited[sx][sy] = 1
    while queue:
        tx,ty,cnt = queue.pop(0)
        if cnt >= C:
            break
        for i in range(1,5):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0<=nx <10 and 0<=ny <10 and visited[nx][ny] == 0:
                queue.append([nx,ny,cnt +1])
                arr[nx][ny].append([k,P])
                visited[nx][ny] = 1

def move(ax,ay,bx,by,am,bm):
    dx = [0, -1, 0, 1, 0]
    dy = [0, 0, 1, 0, -1]

    return [ax + dx[am],ay + dy[am]], [bx + dx[bm] , by + dy [bm]]


for test_case in range(1, T + 1):
    arr = [[[] for i in range(10)] for i in range(10)]
    M, A = map(int,input().split())
    A_move = list(map(int,input().split()))
    B_move = list(map(int,input().split()))
    for i in range(A):
        sx,sy,C,P =map(int, input().split())
        fill(sy-1,sx-1,arr,C,i+1,P)
    A = [0,0]
    B = [9,9]
    # for i in range(10):
    #     print(arr[i])
    ans = 0
    ans += cal(A, B)
    for i in range(M):
        A,B = move(A[0],A[1],B[0],B[1],A_move[i], B_move[i])
        # print(len(arr[A[0]][A[1]]),len(arr[B[0]][B[1]]))
        ans += cal(A,B)
    print("#" + str(test_case) + " " + str(ans))