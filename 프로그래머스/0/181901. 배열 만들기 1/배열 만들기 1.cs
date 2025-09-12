using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n, int k) {
        List<int> answer = new List<int>();
        for(int i=1;i<=n/k;i++){
            answer.Add(k*i);
        }
        return answer.ToArray();
    }
}