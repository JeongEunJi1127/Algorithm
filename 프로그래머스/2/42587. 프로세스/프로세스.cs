// 16:22 ~ 17:04

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        Queue<(int priority, int index)> priorityQueue = new Queue<(int,int)>();
        
        for(int i=0; i<priorities.Length;i++){
            priorityQueue.Enqueue((priorities[i],i));
        }
        
        Dictionary<int,int> dict = new Dictionary<int,int>();
        int cnt = 1;
        while(priorityQueue.Count>0){
            var cur_val = priorityQueue.Dequeue();            
            
            if(priorityQueue.Any(x => x.priority > cur_val.priority)){
                //Console.WriteLine($"더 큰 우선순위 존재 {cur_val.priority}, 값 {cur_val.index}");
                priorityQueue.Enqueue(cur_val);
            }
            else{
                //Console.WriteLine($"이게 가장 높은 우선순위 {cur_val.priority}, 값 {cur_val.index}");
                dict[cur_val.index] = cnt;
                cnt ++;
            }
                        
        }
        
        return dict[location];
    }
}