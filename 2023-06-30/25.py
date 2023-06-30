# 풍선 터트리기
def solution(a):
    answer = set()
    N = len(a)
    INF = int(1e9) + 1
    # 자신의 숫자를 기준으로 양쪽 모두 자기보다 작은 수가 존재하면 불가능 아니면 가능
    # left
    min_number = INF
    for i in range(N):
        if min_number > a[i]:
            min_number = a[i]
            answer.add(a[i])     
    # right
    min_number = INF
    for i in range(N - 1, -1, -1):
        if min_number > a[i]:
            min_number = a[i]
            answer.add(a[i])
    
    answer = len(answer)
            
    return answer
    