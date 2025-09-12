using System;
using System.Collections.Generic;

public class Solution {
    public int solution(string my_string, string is_prefix) {
        List<string> prefix = new List<string>();
        
        string cur_prefix = "";
        
        for(int i=0;i<my_string.Length;i++){
            cur_prefix += my_string[i];
            prefix.Add(cur_prefix);
        }
        
        if(prefix.Contains(is_prefix))
            return 1;
        
        return 0;
    }
}