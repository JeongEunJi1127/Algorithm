// 15:19 ~ 15:47

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.Length;
        int[] answer = new int[n];
        Stack<int> stack = new Stack<int>();
        
        for(int i=n-1;i>=0;i--){
            int cur_num = numbers[i];
                     
            while(true){          
                if(stack.Count == 0){
                    answer[i] = -1;
                    break;
                }
                if(stack.Peek() > cur_num){
                    answer[i] = stack.Peek();
                    stack.Push(stack.Peek());
                    break;
                }                    
                stack.Pop();
            }
            
            stack.Push(cur_num);
        }
        
        return answer;
    }
}