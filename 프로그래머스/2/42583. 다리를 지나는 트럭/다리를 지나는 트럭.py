from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0

    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)

    while trucks or sum(bridge) > 0:
        # 매초 다리 맨 앞의 원소 제거
        bridge.popleft()
        # 다음 트럭 진입 여부 판단
        if trucks and trucks[0]+sum(bridge)<=weight:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
        # 시간 증가
        answer+=1
    return answer