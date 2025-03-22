using System;
using System.Linq;

public class Solution {
    public string solution(string s) {
        string answer = "";
        int[] input = s.Split().Select(int.Parse).ToArray();
        System.Console.WriteLine(input);
        
        int minNum = input.Min();
        int maxNum = input.Max();
        
        answer = minNum.ToString()+" "+maxNum.ToString();
        return answer;
    }
}