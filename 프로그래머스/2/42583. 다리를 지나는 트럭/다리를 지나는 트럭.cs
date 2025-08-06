// 14:46 ~ 15:36

using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<int> bridge = new Queue<int>();  
        int time = 0;
        int totalWeight = 0;
        int index = 0;

        // 다리 길이만큼 초기화
        for (int i = 0; i < bridge_length; i++)
            bridge.Enqueue(0);

        while (index < truck_weights.Length) {
            time++;
            totalWeight -= bridge.Dequeue(); // 맨 앞 트럭 빠짐

            if (totalWeight + truck_weights[index] <= weight) {
                bridge.Enqueue(truck_weights[index]);
                totalWeight += truck_weights[index];
                index++;
            } else {
                bridge.Enqueue(0); // 트럭 못 들어오면 0으로 채움
            }
        }

        return time + bridge_length;  // 마지막 트럭이 완전히 다리를 건너는 시간 포함
    }
}
