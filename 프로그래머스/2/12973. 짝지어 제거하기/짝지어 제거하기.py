def solution(s):
    answer = 0
    list = []
    for i in s:
        if list:
            if list[-1]==i:
                list.pop(-1)
            else:
                list.append(i)
        else:
            list.append(i)
    if not list:
        answer=1
    return answer