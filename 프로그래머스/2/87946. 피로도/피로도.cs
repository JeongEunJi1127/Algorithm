// 17:40 ~

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    List<int> answer = new List<int>();
    
    // 전체 총량, 현재까지 지나쳐온 던전 개수, 남은 던전들의 조건
    public void Dfs(int total, int cnt, List<(int,int,bool)> dungeons){
        //Console.WriteLine($"현재 총량 {total} 현재까지 지나친 던전 개수 {cnt}");
        for(int i=0;i< dungeons.Count; i++){
            var dungeon = dungeons[i];
            
            if(!dungeon.Item3 && total >= dungeon.Item1){
                //Console.WriteLine($"- 현재 들어가는 던전 {dungeon.Item1} {dungeon.Item2}");
                dungeon.Item3 = true;
                dungeons[i] = dungeon;
                
                Dfs(total-dungeon.Item2, cnt+1, dungeons);
                
                dungeon.Item3 = false;
                dungeons[i] = dungeon;
            }
        }
        
        //Console.WriteLine($"answer에 넣는다 {cnt}\n");
        answer.Add(cnt);
    }
    
    public int solution(int k, int[,] dungeons) {
        int n = dungeons.GetLength(0);
        
        List<(int,int,bool)> dungeons_list = new List<(int,int,bool)>();
        for(int i=0;i<n;i++){
            dungeons_list.Add((dungeons[i,0],dungeons[i,1],false));
        }        
        
        Dfs(k,0,dungeons_list);
        
        return answer.Max();
    }
}