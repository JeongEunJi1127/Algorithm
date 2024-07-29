def StrToTime(str):
    return int(str[:2])*60 + int(str[3:])  

def solution(fees, records):
    answer = []
    basicTime, basicFee, unitTime, unitFee = fees
    parkingRecords = {}
    timeRecords = {}

    for record in records:
        time, carNum, inOut = record.split()
        
        # 입차면 입차 시간 기록
        if(inOut == "IN"):
            parkingRecords[carNum] = StrToTime(time)
        # 출차면 총 주차 시간 계산
        else:
            parkingTime = StrToTime(time) - parkingRecords[carNum]
            if carNum in timeRecords.keys():
                timeRecords[carNum] += parkingTime
            else:
                timeRecords[carNum] = parkingTime
            parkingRecords.pop(carNum)
    
    # 출차하지 못한 차량 있다면
    if len(parkingRecords.keys()) !=0:
        for i in parkingRecords.keys():    
            parkingTime = StrToTime("23:59") - parkingRecords[i]
            if i in timeRecords.keys():
                timeRecords[i] += parkingTime
            else:
                timeRecords[i] = parkingTime
            
    timeRecords = dict(sorted(timeRecords.items()))
    print(timeRecords)
    
    for timeRecord in timeRecords.keys():
        t = int(timeRecords[timeRecord])
        if t <= basicTime:
            answer.append(basicFee)
        else:
            if (t - basicTime)%unitTime != 0:
                answer.append(basicFee + (int((t - basicTime)/unitTime)+1) * unitFee)
            else:
                answer.append(basicFee + int((t - basicTime)/unitTime) * unitFee)
    return answer