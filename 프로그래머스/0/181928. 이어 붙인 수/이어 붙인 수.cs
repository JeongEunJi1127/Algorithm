using System;

public class Solution {
    public int solution(int[] num_list) {
        string odd = "";
        string even = "";
        
        foreach(int num in num_list){
            if(num%2 == 1)
                odd += num.ToString();
            else
                even += num.ToString();
        }
        
        return int.Parse(odd)+int.Parse(even);
    }
}