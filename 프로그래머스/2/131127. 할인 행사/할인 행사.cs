using System;
using System.Collections.Generic;

public class Solution {
    public int answer = 0;
    
    public void Check_Product(string[] want, int[] number, string[] discount, int start){
        int n = want.Length;
        Dictionary<string,int> dict = new Dictionary<string,int>();
        bool isValid = true;
        
        for(int i=0; i<n; i++)
        {
            dict[want[i]] = 0;            
        }   
        
        // discount 배열에서 start 인덱스부터 start+10 인덱스까지 검사/ dict 만족하는지 검사
        for(int i = start; i<start+10; i++){
            if(dict.ContainsKey(discount[i])){
                dict[discount[i]] += 1;
            }          
        }
        
        for(int i=0; i<n; i++)
        {
            if(number[i] != dict[want[i]]){
                isValid= false;
                break;
            }
        } 
        
        if(isValid)
            answer ++;
    }
    
    public int solution(string[] want, int[] number, string[] discount) {     
        int n = discount.Length;
        
        for(int i=0; i<=n-10; i++)
        {
            Check_Product(want, number, discount,i);
        }   
        
        return answer;
    }
}