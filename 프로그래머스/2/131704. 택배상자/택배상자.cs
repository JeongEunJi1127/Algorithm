// 15:20 ~ 15:46

using System;
using System.Collections.Generic;

public class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int n = order.Length;
        int cur_idx = 0;

        Stack<int> stack = new Stack<int>();
        
        for(int i=1;i<n+1;i++){
            stack.Push(i);
            
            while(stack.Count >0 && stack.Peek() == order[cur_idx]){
                stack.Pop();
                cur_idx++;
            }
        }  
        
        return cur_idx;
    }
}