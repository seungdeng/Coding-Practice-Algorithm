from collections import deque

def solution(s):
    answer = True
    left = []
    
    q = deque()
    
    for i in s:
        if i == ')' and not left:
            return False
        if i == '(':
            left.append('(')
        if i == ')' and left:
            left.pop()

    if left:
        return False
    return answer