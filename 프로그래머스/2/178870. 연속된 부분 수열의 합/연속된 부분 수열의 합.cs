using System;

public class Solution {
    public int[] solution(int[] sequence, int k) {
        int left = 0, right = 0;
        int sum = 0;

        int startIdx = 0, endIdx = sequence.Length - 1;
        int minLength = int.MaxValue;

        while (right < sequence.Length) {
            sum += sequence[right];

            while (sum > k && left <= right) {
                sum -= sequence[left];
                left++;
            }

            if (sum == k) {
                int length = right - left;
                if (length < minLength) {
                    minLength = length;
                    startIdx = left;
                    endIdx = right;
                }
            }

            right++;
        }

        return new int[] { startIdx, endIdx };
    }
}
