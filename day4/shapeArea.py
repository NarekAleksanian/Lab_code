def solution(n):
    count = 0
    for i in range(n, n-2, -1):
        count += i * i
    return count

