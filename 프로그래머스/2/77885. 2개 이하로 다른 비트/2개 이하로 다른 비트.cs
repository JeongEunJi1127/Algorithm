// 16:19 ~ 

using System;

public class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.Length];
        
        for (int i = 0; i < numbers.Length; i++) {
            long x = numbers[i];

            if (x % 2 == 0) {
                // 짝수는 그냥 +1 (끝에 0을 1로 바꾸므로 +1)
                answer[i] = x + 1;
            } 
            else {
                long bit = 1;
                while ((x & bit) != 0) { // x의 자리수가 1인지 확인
                    bit <<= 1; // 1이면 넘어가기
                }
                // 0이었던 자리를 1로 바꾸고, 그 바로 앞을 0으로
                answer[i] = x + bit - (bit >> 1);
            }
        }
        
        return answer;
    }
}