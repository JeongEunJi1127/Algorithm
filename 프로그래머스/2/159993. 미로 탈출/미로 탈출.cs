using System;
using System.Collections.Generic;

public class Solution
{
    public int solution(string[] maps)
    {
        int[] startPos = { 0, 0 };
        int[] endPos = { 0, 0 };
        int[] leverPos = { 0, 0 };

        for (int i = 0; i < maps.Length; i++)
        {
            for (int j = 0; j < maps[0].Length; j++)
            {
                if (maps[i][j] == 'S')
                {
                    startPos[0] = i;
                    startPos[1] = j;
                }
                else if (maps[i][j] == 'E')
                {
                    endPos[0] = i;
                    endPos[1] = j;
                }
                else if (maps[i][j] == 'L')
                {
                    leverPos[0] = i;
                    leverPos[1] = j;
                }
            }
        }

        int toLever = Bfs(maps, startPos, leverPos);
        if (toLever == -1) return -1;

        int toEnd = Bfs(maps, leverPos, endPos);
        if (toEnd == -1) return -1;

        return toLever + toEnd;
    }

    private int Bfs(string[] maps, int[] startPos, int[] endPos)
    {
        int[] dx = { 0, 0, 1, -1 };
        int[] dy = { 1, -1, 0, 0 };

        int row = maps.Length;
        int column = maps[0].Length;

        int[,] dist = new int[row, column]; // 거리 값 저장
        bool[,] visited = new bool[row, column];

        Queue<int[]> queue = new Queue<int[]>();
        visited[startPos[0], startPos[1]] = true;
        queue.Enqueue(startPos);

        while (queue.Count > 0)
        {
            int[] curPos = queue.Dequeue();

            // 종료 조건
            if (curPos[0] == endPos[0] && curPos[1] == endPos[1])
            {
                return dist[endPos[0], endPos[1]];
            }

            for (int i = 0; i < 4; i++)
            {
                int[] nextPos = { curPos[0] + dx[i], curPos[1] + dy[i] };

                if (0 <= nextPos[0] && nextPos[0] < row && nextPos[1] >= 0 && nextPos[1] < column && maps[nextPos[0]][nextPos[1]] != 'X' && !visited[nextPos[0], nextPos[1]] )
                {
                    visited[nextPos[0], nextPos[1]] = true;
                    dist[nextPos[0], nextPos[1]] = dist[curPos[0], curPos[1]] + 1;
                    queue.Enqueue(nextPos);
                }
            }
        }

        return -1;
    }
}