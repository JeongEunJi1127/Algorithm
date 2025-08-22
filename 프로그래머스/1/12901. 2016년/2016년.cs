using System;

public class Solution {
    public string solution(int a, int b) {
        string answer = "";
        DateTime date = new DateTime(2016, a, b);
        answer = date.DayOfWeek.ToString();
        answer = answer.Substring(0, 3);
        return answer.ToUpper();
    }
}