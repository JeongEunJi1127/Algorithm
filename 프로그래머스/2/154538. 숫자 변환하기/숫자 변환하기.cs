// 15:42 ~ 16:00

using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int Bfs(int x, int y, int n){
        int convert_cnt = int.MaxValue;

        Queue<(int,int)> queue = new Queue<(int,int)>();
        HashSet<int> visited = new HashSet<int>(); 
        queue.Enqueue((x,0));
        
        while (queue.Count > 0){
            (int cur_x, int cnt) = queue.Dequeue();
            //Console.WriteLine($"현재 x {cur_x} 현재 횟수 {cnt}");
            
            if (cur_x == y){
                //Console.WriteLine($"\n최종 x {cur_x} 최종 횟수 {cnt}");
                convert_cnt= Math.Min(convert_cnt,cnt);
                continue;
            }
            if(cnt > convert_cnt) // 더 검사할 필요 없음
                break;
            
            if (cur_x * 2 <= y && !visited.Contains(cur_x*2)){
                visited.Add(cur_x*2);
                queue.Enqueue((cur_x*2,cnt+1));    
            }      
            if(cur_x * 3 <= y && !visited.Contains(cur_x*3)){
                visited.Add(cur_x*3);
                queue.Enqueue((cur_x*3,cnt+1));    
            }      
            if (cur_x + n <= y && !visited.Contains(cur_x+n)){
                visited.Add(cur_x+n);
                queue.Enqueue((cur_x+n,cnt+1));    
            }      

        }
        
        if(convert_cnt == int.MaxValue)
            convert_cnt = -1;
        return convert_cnt;
    }
    
    public int solution(int x, int y, int n) {
        int answer = Bfs(x,y,n);     
        return answer;
    }
}