using System;
using System.Collections.Generic;

public class Solution
{
    public int solution(int[,] maps)
    {
        int answer = 0;
        bool[,] visited = new bool[maps.GetLength(0), maps.GetLength(1)];
        BFS(maps, visited, (0, 0));
        if (maps[maps.GetLength(0) - 1, maps.GetLength(1) - 1] == 1)
            answer = -1;
        else
            answer = maps[maps.GetLength(0) - 1, maps.GetLength(1) - 1];
        return answer;
    }

    public void BFS(int[,] maps, bool[,] visited, (int,int) start)
    {
        Queue<(int,int)> q = new Queue<(int, int)>();
        // 남 동 북 서
        int[] dx = new int[] { 0, 1, 0, -1 };
        int[] dy = new int[] { 1, 0, -1, 0 };
        q.Enqueue(start);
        visited[start.Item1, start.Item2] = true;

        while(q.Count > 0)
        {
            (int x, int y) = q.Dequeue();
            for (int i = 0; i < 4; i++)
            {
                int nx = dx[i] + x;
                int ny = dy[i] + y;

                // nx,ny가 범위 안이고 벽이 아니고 방분하지 않은 곳일 때
                if(nx >= 0 && ny >= 0 && nx < maps.GetLength(0) && ny < maps.GetLength(1) && maps[nx, ny] != 0 && !visited[nx, ny])
                {
                    if (nx == maps.GetLength(0) && ny == maps.GetLength(1))
                    {
                        return;
                    }
                    visited[nx, ny] = true;
                    q.Enqueue((nx, ny));
                    maps[nx, ny] = maps[x, y] + 1;
                }
            }
        }
    }
}