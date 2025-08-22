using System;

public class Solution {
    public string solution(int[] food) {
        string left = "";
        string right = "";
        int n = food.Length;
        
        for(int i=0;i<n;i++){
            int cnt = food[i]/2;
            while(cnt>0){
                left = left + i.ToString() ;
                right = i.ToString() + right;
                cnt --;
            }
        }
        
        left += "0";
         
        return left + right;
    }
}