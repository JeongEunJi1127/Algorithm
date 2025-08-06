// 18:06 ~ 18:39

using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[,] sizes) {
        int maxWidth = 0;
        int maxHeight = 0;

        for (int i = 0; i < sizes.GetLength(0); i++) {
            int w = sizes[i, 0];
            int h = sizes[i, 1];

            // 회전해서 가로를 항상 더 긴 쪽으로
            int big = Math.Max(w, h);
            int small = Math.Min(w, h);

            maxWidth = Math.Max(maxWidth, big);
            maxHeight = Math.Max(maxHeight, small);
        }

        return maxWidth * maxHeight;
    }
}