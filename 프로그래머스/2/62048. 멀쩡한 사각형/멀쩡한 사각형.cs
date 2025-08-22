using System;
using System.Collections.Generic;

public class Solution {
    public long GCD(long a, long b) { //최소공약수
        if (b == 0) {
            return (long)a;
        }
        return GCD(b, a%b);
    }
    
    public long solution(int w, int h) {
        long answer = (long)w * (long)h - (w+h-GCD(w,h));

        return answer;
    }
}