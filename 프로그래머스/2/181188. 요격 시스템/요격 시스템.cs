// 14:20 ~ 15:03

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[,] targets) {
        int answer = 0;
        int n = targets.GetLength(0);
        
        List<(int start,int end)> points = new List<(int,int)>();
        // 2차원 배열 -> 리스트로 변환
        for(int i=0;i<n;i++){
            points.Add((targets[i,0],targets[i,1]));
        }
        // end 위치로 정렬
        points.Sort((a, b) => a.end.CompareTo(b.end));
                     
        int lastShot = -1;
        foreach(var point in points){
            if(point.start >= lastShot){
                answer++;
                lastShot = point.end;
            }
            //Console.WriteLine($"{point.start} {point.end}");
        }
        
        
        
        return answer;
    }
}