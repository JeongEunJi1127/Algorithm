// 16:25 ~ 17:25

using System;
using System.Collections.Generic;
using System.Linq;

// 연속으로 몇칸 False인지 세는게 핵심
class Solution
{
    public int solution(int n, int[] stations, int w){
        int answer = 0;

        List<int> min_list = new List<int>();  // 기지국 설치 안된 시작 구역
        List<int> max_list = new List<int>();  // 기지국 설치 안된 끝 구역
        
        min_list.Add(1);
        for(int i=0;i<stations.Length;i++){
            max_list.Add(stations[i]-w-1);
            min_list.Add(stations[i]+w+1);
        }
        max_list.Add(n);
        
        for (int i = 0; i < min_list.Count; i++)
        {
            //Console.WriteLine($"현재 구역 {min_list[i]} / {max_list[i]}");
            if(min_list[i] > max_list[i]) continue;
            
            int not_installed_length = max_list[i]-min_list[i]+1;
            //Console.WriteLine($"설치안된 구역 길이 {not_installed_length}");
            
            if(not_installed_length%(2*w+1) == 0)
                answer += not_installed_length/(2*w+1);
            else            
                answer += not_installed_length/(2*w+1) +1;
           // Console.WriteLine($"현재 answer {answer}\n");
        }

        return answer;
    }
}