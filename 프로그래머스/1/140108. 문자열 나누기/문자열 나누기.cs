// 15:07 ~ 15:22

using System;
using System.Collections.Generic;

public class Solution {
    public int solution(string s) {
        int answer = 0;
        Queue<char> queue = new Queue<char>(s);
        
        while(queue.Count > 0){                     
            char x = queue.Dequeue();
            int x_cnt = 1;
            int x_ncnt = 0;
            int n = queue.Count;
            
            for(int i=0;i<n; i++){
                char tmp = queue.Dequeue();
                if(tmp == x)
                    x_cnt ++;
                else
                    x_ncnt ++;
                
                if(x_cnt == x_ncnt){
                    answer ++;
                    break;                    
                }          
            }

            if(queue.Count == 0 && x_cnt != x_ncnt){
                answer ++;
                break;                    
            }  
        }
                  
        return answer;
    }
}