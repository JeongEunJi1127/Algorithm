using System;
using System.Collections.Generic;

public class Solution {
    public string solution(string[] cards1, string[] cards2, string[] goal) {
        string answer = "";
        Queue<string> c1 = new Queue<string>();
        Queue<string> c2 = new Queue<string>();
        
        for(int i=0;i<cards1.Length;i++){
            c1.Enqueue(cards1[i]);
        }
        
        for(int i=0;i<cards2.Length;i++){
            c2.Enqueue(cards2[i]);
        }
        
        int idx = 0;
        bool isValid = true;
        while(idx < goal.Length){
            string cur_goal = goal[idx];
            
            if(c1.Count>0 && cur_goal == c1.Peek()){
                c1.Dequeue();
            }
            else if(c2.Count>0 && cur_goal == c2.Peek()){
                c2.Dequeue();
            }
            else{
                isValid = false;
                break;
            }
            
            idx ++;
        }
        
        if(isValid)
            answer=  "Yes";
        else
            answer = "No";
        
        return answer;
    }
}