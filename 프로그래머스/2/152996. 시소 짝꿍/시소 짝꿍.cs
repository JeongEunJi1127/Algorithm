// 16:27 ~ 17:29

using System;
using System.Collections.Generic;

public class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        Dictionary<int, long> dictionary = new Dictionary<int, long>();

        // 가능한 비율 쌍: (기준몸무게, 비교몸무게)
        List<(int, int)> ratios = new List<(int, int)> { (1, 1), (2, 3), (3, 4), (1, 2)};
        Array.Sort(weights);
        
        foreach (int weight in weights) {
            foreach (var item in ratios) {
                int a = item.Item1;
                int b = item.Item2;
                
                if ((weight * a) % b != 0) continue;

                int target = (weight * a) / b;

                if (dictionary.ContainsKey(target))
                    answer += dictionary[target];
            }

            if (!dictionary.ContainsKey(weight))
                dictionary[weight] = 0;
            dictionary[weight]++;
        }

        return answer;
    }
}
