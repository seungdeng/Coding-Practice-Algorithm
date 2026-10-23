def solution(clothes):
    answer = 1
    d = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] not in d:
            d[clothes[i][1]] = 1
        else:
            d[clothes[i][1]] +=1
                   
    for count in d.values():
        answer *= (count+1)
        
    answer -=1
    return answer