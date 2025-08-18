using System;
using System.Collections.Generic;

public class Solution {
    // dir: 0=Up, 1=Right, 2=Down, 3=Left
    static readonly int[] dy = {-1, 0, 1,  0};
    static readonly int[] dx = { 0, 1, 0, -1};

    public int[] solution(string[] grid) {
        int n = grid.Length;
        int m = grid[0].Length;

        // visited[y, x, dir]
        bool[,,] visited = new bool[n, m, 4];
        List<int> cycles = new List<int>();

        for (int y = 0; y < n; y++) {
            for (int x = 0; x < m; x++) {
                for (int dir = 0; dir < 4; dir++) {
                    if (visited[y, x, dir]) continue;

                    int cy = y, cx = x, cd = dir;
                    int len = 0;

                    while (!visited[cy, cx, cd]) {
                        visited[cy, cx, cd] = true;
                        len++;

                        // 방향 회전
                        char cell = grid[cy][cx];
                        if (cell == 'L') {
                            cd = (cd + 3) % 4; // 왼쪽
                        } else if (cell == 'R') {
                            cd = (cd + 1) % 4; // 오른쪽
                        }
                        // 'S'면 방향 유지

                        // 한 칸 전진 (토러스 wrap)
                        cy = (cy + dy[cd] + n) % n;
                        cx = (cx + dx[cd] + m) % m;
                    }

                    if (len > 0) cycles.Add(len);
                }
            }
        }

        cycles.Sort();
        return cycles.ToArray();
    }
}
