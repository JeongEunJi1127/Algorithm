using System;

public class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        int n = A.Length;
        Array.Sort(A);
        Array.Sort(B);
        Array.Reverse(B);
        
        for (int i = 0; i < n; i++)
        {
            answer += A[i] * B[i];
        }

        return answer;
        
    }
}