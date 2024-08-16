using System;

public class Solution
{
    public int solution(int[] numbers, int target)
    {
        int answer = Dfs(numbers, target, 0, 0);
        Console.WriteLine(answer);
        return answer;
    }

    public int Dfs(int[] numbers, int target, int depth, int answer)
    {
        if (depth == numbers.Length)
        {
            if (answer == target)
                return 1;
            return 0;
        }
        else
        {
            return Dfs(numbers, target, depth + 1, answer + numbers[depth]) + Dfs(numbers, target, depth + 1, answer - numbers[depth]);
        }
    }
}