# 가장 긴 팰린드롬
def solution(s):
    answer = 0
    N = len(s)
    for i in range(N):
        # 홀수 개. 중심을 기준으로 양 사이드가 같은 경우
        j = 1
        cnt_1 = 1
        while 0 <= i - j and i + j < N:
            if s[i - j] == s[i + j]:
                cnt_1 += 2
                j += 1
            else:
                break
        
        # 짝수 개. 양쪽이 일치하는 경우.
        k = 0
        cnt_2 = 0
        while 0 <= i - k and i + k + 1 < N:
            if s[i - k] == s[i + k + 1]:
                cnt_2 += 2
                k += 1
            else:
                break
                
        answer = max(answer, cnt_1, cnt_2)
        
    return answer