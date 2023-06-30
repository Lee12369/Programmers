# 자물쇠와 열쇠
def solution(key, lock):
    answer = True
    N = len(lock)
    M = len(key)
    def rotate(arr):
        arr = list(map(list, zip(*arr[::-1])))
        return arr
    
    # sliding window를 위한 범위 설정
    min_height = 20
    min_width = 20
    max_height = 0
    max_width = 0
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                min_height = min(min_height, i)
                min_width = min(min_width, j)
                max_height = max(max_height, i)
                max_width = max(max_width, j)
                
    lock = [lock[i][min_width: max_width + 1] for i in range(min_height, max_height + 1)]
    
    height = max_height - min_height + 1
    width = max_width - min_width + 1
    
    # 빈 공간 영역에 맞는 key인 target을 설정. 공간이 0 이면 target은 1이다. 반대로 공간이 1이면 target은 0이다.    
    target = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if lock[i][j] == 0:
                target[i][j] = 1
            else:
                target[i][j] = 0
    
    # key 영역에 target과 일치하는 영역이 있는지 확인 
    def func_check(key, target):
        for i in range(M - height + 1):
            for j in range(M - width + 1):        
                key_slice = [key[k][j: j + width] for k in range(i, i + height)]
                if key_slice == target:
                    return True
        return False
    
    # key 영역을 회전하여 확인.
    answer = False
    for _ in range(4):
        answer = func_check(key, target)
        if answer == True:
            break
        key = rotate(key)
    
    return answer