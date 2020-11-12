def solution(bridge_length, weight, truck_weights):
    now = 0
    bridge = []
    time = []
    
    while truck_weights or bridge:
        now += 1
        if time:
            if time[0] + bridge_length == now:
                bridge.pop(0)
                time.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
                time.append(now)
    
    return now
