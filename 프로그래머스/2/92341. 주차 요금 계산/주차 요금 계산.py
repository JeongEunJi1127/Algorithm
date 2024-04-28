import math

def timeToNum(string):
    return int(string[:2]) * 60 + int(string[3:])
     
def solution(fees, records):
    answer = []
    times = {}
    basicTime, basicFee, unitTime, unitFee = fees
    
    cars = {}
    
    for record in records:
        time, num, inout = record.split()
        
        # 딕셔너리에 현재 차번호가 존재하면
        if num in cars.keys():
            # 주차장에 이미 있는 차량이 다시 입차되는 경우는 없으므로 이 경우 inout은 무조건 OUT
            inTime = timeToNum(cars[num][0])
            outTime = timeToNum(time)
            
            cars.pop(num)
            
            if num in times.keys():
                times[num] += outTime-inTime
            else:
                times[num] = outTime-inTime
        # 딕셔너리에 현재 차번호가 존재하지 않으면-> 주차장에 없는 차량이 출차되는 경우는 없으므로 이 경우 inout은 무조건 IN
        else:
            # cars[key] = [들어온시간]
            cars[num] = [time]

    # cars 안에 아직 값이 남아있다면 입차된 후에 출차된 내역이 없어 23:59에 출차된 것
    for key in cars.keys():
        inTime = timeToNum(cars[key][0])
        outTime = timeToNum("23:59")
        
        if key in times.keys():
            times[key] += outTime-inTime
        else:
            times[key] = outTime-inTime
     
    times = dict(sorted(times.items()))

    for i in times.items():
        num, time = i
        
        totalTime = int(time)
        fee = int(basicFee)
        
        if totalTime > int(basicTime):
            fee += math.ceil((totalTime - int(basicTime))/unitTime) * int(unitFee)
            
        answer.append(fee)
    
    return answer