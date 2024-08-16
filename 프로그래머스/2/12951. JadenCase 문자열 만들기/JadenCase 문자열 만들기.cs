using System;
using System.Text;

public class Solution
{
    public string solution(string s)
    {
        string answer = "";

        char[] charArr = s.ToLower().ToCharArray();
        
        for(int i=0; i<charArr.Length ; i++){
            charArr[0] = Char.ToUpper(charArr[0]);
            if(charArr[i] == ' ' && i+1 < charArr.Length)
            {
                charArr[i+1] = Char.ToUpper(charArr[i+1]);
            }
        }
        for(int i=0; i<charArr.Length; i++)
        {
            answer += charArr[i];
        }

        return answer;
    }
}