using System;

class Solution
{
    public int solution(int n)
    {
        int answer = 0;

        while(n>0){
            int remain = n%2==0 ? 0 : 1;
            answer += remain;
            n /= 2;
            //Console.WriteLine(n);
        }

        return answer;
    }
}