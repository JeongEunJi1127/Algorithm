// 18:10 ~ 18:27

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string solution(string s) {
        string answer = "";
        
        List<char> s_list = s.ToList();
        
        int index = 0;
        
        for(int i=0;i<s_list.Count;i++){
            char cur_s = s_list[i];
            
            if(cur_s == ' '){
                answer += cur_s;
                index = 0;
                continue;
            }   
            
            if(index % 2 == 1)
                answer += char.ToLower(cur_s);
            else
                answer += char.ToUpper(cur_s);
            
            index ++;
        }
        
        return answer;
    }
}