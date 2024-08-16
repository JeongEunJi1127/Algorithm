using System;

public class Solution {
    public int solution(int n, int[,] computers)
    {
        int answer = 0;
        bool[] visited = new bool[n];

        for (int i = 0; i < n; i++)
        {
            if (visited[i] == false)
            {
                answer++;
                DFS(computers, visited, i);
            }
        }
        Console.WriteLine(answer);
        return answer;
    }

    public void DFS(int[,] computers, bool[] visited, int index)
    {
        visited[index] = true;
        for (int i = 0; i < computers.GetLength(0); i++)
        {
            if (computers[index, i] == 1 && !visited[i])
                DFS(computers, visited, i);
        }
    }
    

}