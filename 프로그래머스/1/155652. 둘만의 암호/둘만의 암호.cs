// 15:30 ~ 

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string solution(string s, string skip, int index) {
        string answer = "";
        string alphabet = "abcdefghijklmnopqrstuvwxyz";
        char[] alpha_arr = alphabet.ToCharArray();
        
        char[] s_arr = s.ToCharArray();
        
        for (int i=0;i<s_arr.Length;i++){
            char now_s = s_arr[i];
            int now_index = index;
            int idx = Array.IndexOf(alpha_arr, now_s);
            
            while(now_index>0){
                idx = (idx+1) % alphabet.Length;
                if(!skip.Contains(alpha_arr[idx]))
                    now_index --;
            }
            
            answer += alpha_arr[idx];
        }
            
        return answer;
    }
}