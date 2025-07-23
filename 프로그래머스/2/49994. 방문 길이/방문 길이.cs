// 17:10 ~ 17:42

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public (int x,int y) GetDirection(char dir){
        switch(dir){
            case 'U': return (0,-1);
            case 'D': return (0,1);
            case 'R': return (1,0);
            case 'L': return (-1,0);
            default:  return (0,0);
        }     
    }
    
    public int GetPathLength(string dirs){
        List<char> dir_Commands = dirs.ToList();
        (int x,int y) cur_pos = (0,0);
        HashSet<string> visited = new HashSet<string>();
        
        foreach(char dir in dir_Commands){
            var point = GetDirection(dir);
            
            int nx = cur_pos.x + point.x;
            int ny = cur_pos.y + point.y;
            
            // 범위 벗어나면 무시
            if(nx < -5 || nx > 5 || ny < -5 || ny > 5) 
                continue;
            
            visited.Add($"{cur_pos.x},{cur_pos.y},{nx},{ny}");
            visited.Add($"{nx},{ny},{cur_pos.x},{cur_pos.y}"); //반대의 경우도 해야 같은 선의 중복처리를 할 수 있다(반대 방향으로 그어질 수 잇음)
            
            //Console.WriteLine($"{cur_pos.x},{cur_pos.y},{nx},{ny}");
            cur_pos = (nx,ny);
        }
        
        return visited.Count/2;
    }
    
    public int solution(string dirs) {
        int answer = GetPathLength(dirs);      
        return answer;
    }
}