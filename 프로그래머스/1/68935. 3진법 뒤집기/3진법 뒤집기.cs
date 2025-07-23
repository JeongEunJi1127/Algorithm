// 18:25 ~ 18:37

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string ToTernary(int n){
        string ternary = "";
        
        while(n > 0){
            ternary = (n % 3).ToString() + ternary;
            n /= 3;
        }       
        return ternary;
    }
    
    public int ToDemical(string n){
        int demical = 0;
        int pow = 1;
        
        for(int i = n.Length - 1; i >= 0; i--) {
            int digit = n[i] - '0';
            demical += digit * pow;
            pow *= 3;
        }
        return demical;
    }
    
    
    public int solution(int n) {
        string ternary = ToTernary(n);  
        string reversed = new string(ternary.Reverse().ToArray());
        int reversed_n = ToDemical(reversed);
        
        return reversed_n;
    }
}