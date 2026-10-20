def solution(board, moves):
    answer = 0
    bag= []
    for i in range(len(moves)):
        for k in range(len(board)):
            if board[k][moves[i]-1]==0: 
                continue;
            else:
                bag.append(board[k][moves[i]-1])
                board[k][moves[i]-1]=0
        
            if len(bag)>=2:
                if bag[-1] == bag[-2]:
                    bag.pop()
                    bag.pop()
                    answer+=2
            break
    

    return answer