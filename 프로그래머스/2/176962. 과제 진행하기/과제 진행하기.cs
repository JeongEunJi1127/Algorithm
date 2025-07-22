// 16:16 ~ 18:11

using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public class Assignment{
        public string Name;
        public int Start;
        public int Playtime;
        
        public Assignment(string name, string start, string playtime){
            Name = name;
            string[] split = start.Split(":");   
            Start = int.Parse(split[0])*60 + int.Parse(split[1]);
            Playtime = int.Parse(playtime);
        }
    }
    
    public string[] DoAssignment(Assignment[] assignment){
        List<string> result = new List<string>();
        
        Stack<Assignment> stack = new Stack<Assignment>();

        int idx = 0;
        
        while(idx < assignment.Length){ 
            Assignment assign = assignment[idx];
            //Console.WriteLine($"현재 진행중인 과제 {assign.Name} {assign.Start} {assign.Playtime}");    
            
            // 마지막 과제인지
            bool isLast = idx == assignment.Length-1;
            // 현재 과제가 사용할 수 있는 시간
            int availableTime = isLast ? int.MaxValue : assignment[idx+1].Start- assign.Start;
 
            stack.Push(assign);           
            while(stack.Count>0){
                Assignment top = stack.Pop();  
                
                // 과제 다 할 수 있으면
                if (availableTime >= top.Playtime){
                    result.Add(top.Name);
                    availableTime -= top.Playtime;
                    
                    if(availableTime <= 0){
                        break;
                    }
                    
                }
                else{
                    top.Start += availableTime;
                    top.Playtime -= availableTime;
                    stack.Push(top);
                    break;
                }
            }
            
            idx ++;
        }
        
        return result.ToArray();
    }
    
    public string[] solution(string[,] plans) {
        int n = plans.GetLength(0);
        Assignment[] assignment = new Assignment[n];
            
        // 먼저 시작해야할 과제 순으로 정렬(2번째 원소 순으로)
        for (int i=0;i<n;i++){   
            assignment[i] = new Assignment(plans[i, 0], plans[i, 1], plans[i, 2]);
        }     
        Array.Sort(assignment, (a, b) => a.Start.CompareTo(b.Start));
        
        string[] answer = DoAssignment(assignment); 
        return answer;
    }
}
