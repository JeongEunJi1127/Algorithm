using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int[] answers) {  
        int[] pattern1 = new int[] {1,2,3,4,5};
        int[] pattern2 = new int[] {2,1,2,3,2,4,2,5};
        int[] pattern3 = new int[] {3,3,1,1,2,2,4,4,5,5};
        
        int answer1 = 0;
        int answer2 = 0;
        int answer3 = 0;
        
        for(int i=0; i<answers.Length;i++){
            if (answers[i] == pattern1[i%5]) answer1 += 1;
            if (answers[i] == pattern2[i%8]) answer2 += 1;
            if (answers[i] == pattern3[i%10]) answer3 += 1;
        }
        
        Console.WriteLine($"{answer1},{answer2},{answer3}");
        
        int maxNumber = Math.Max(answer1,Math.Max(answer2,answer3));
        List<int> lst = new List<int>();
        if (answer1 == maxNumber) lst.Add(1);
        if (answer2 == maxNumber) lst.Add(2);
        if (answer3 == maxNumber) lst.Add(3);
        
        return lst.ToArray();
    }
}