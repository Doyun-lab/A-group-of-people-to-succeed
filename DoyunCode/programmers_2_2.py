import math

day = []
def solution(progresses, speeds):

    for i in range(len(progresses)):
        time = math.ceil((100-progresses[i])/speeds[i])
        day.append(time)

    answer = []
    first = day[0]
    dist = 1

    if len(day) == 1:
        answer = [1]
        return answer
    else:
        for i in range(1, len(day)):
            if first >= day[i]:
                dist += 1
            else:
                answer.append(dist)
                first = day[i]
                dist = 1

        answer.append(dist)
        return answer
