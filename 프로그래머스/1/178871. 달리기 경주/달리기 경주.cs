using System;
using System.Collections.Generic;

public class Solution {
    public string[] solution(string[] players, string[] callings) {
        int n = players.Length;
        Dictionary<string, int> rank = new Dictionary<string, int>();
        
        // 선수 이름 -> 인덱스 저장
        for(int i=0; i<n; i++) {
            rank[players[i]] = i;
        }

        foreach(string winner in callings) {
            int idx = rank[winner];
            if(idx > 0) {
                string front = players[idx - 1];

                // 자리 바꾸기
                players[idx - 1] = winner;
                players[idx] = front;

                // 인덱스도 갱신
                rank[winner] = idx - 1;
                rank[front] = idx;
            }
        }

        return players;
    }
}
