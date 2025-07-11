using System;
using System.Text; // stringbuilder

public class Solution {
    public string solution(string X, string Y) {   
        int[] countX = new int[10];
        int[] countY = new int[10];
        int[] common = new int[10];
        
        for(int i = 0; i < X.Length; i++) { 
            countX[X[i] - '0'] += 1;
        }
        for(int i = 0; i < Y.Length; i++) { 
            countY[Y[i] - '0'] += 1;
        }
        
        for(int i = 0; i < 10; i++) { 
            if (countX[i] >0 && countY[i] >0){
                common[i] = Math.Min(countX[i],countY[i]);
            }
        }
        
        // 겹치는 숫자 없을 때
        bool is_all_zero = true;
        for(int i = 0; i < 10; i++) { 
            if (common[i] != 0){
                is_all_zero = false;
                break;
            }
        }
        if(is_all_zero)
            return "-1";
        
        // 겹치는 숫자 0만 있을 때
        bool is_only_zero = true;
        for(int i=9; i>=1 ; i--){
            if (common[i] != 0){
                is_only_zero = false;
                break;
            }
        }
        if(is_only_zero)
            return "0";
        
        // 일반적인 경우
        StringBuilder sb = new StringBuilder();
        for(int i=9; i>=0 ; i--){
            if(common[i]!=0){
                sb.Append(new string((char)(i + '0'), common[i]));
            }
        }   
        return sb.ToString();
    }
}