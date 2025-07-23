// 15:04 ~ 15:18

using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] prices) {
        int n = prices.Length;
        int[] answer = new int[n];
        
        for(int i=0;i<n-1;i++){
            int cnt = 0;
            for(int j=i+1;j<n;j++){
                // Console.WriteLine($"{i} {j}");
                if(prices[i] <= prices[j]){
                    cnt ++;
                }   
                else if (prices[i] > prices[j]){
                    cnt ++;
                    break;   
                }              
            }    
            answer[i] = cnt;
        }
        
        return answer;
    }
}