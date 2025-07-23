// 15:50 ~ 

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public long LongJump(int n){
        if(n==1 || n==2)
            return n;
        
        long[] dp = new long[n+1];
        dp[1] = 1;
        dp[2] = 2;
        
        for(int i=3; i<n+1;i++){
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567;
        }
        
        return dp[n];
    }
    
    public long solution(int n) {
        long answer = LongJump(n);          
        return answer;
    }
}