// 14:07 ~ 

using System;
using System.Collections.Generic;

public class PriorityQueue{
    List<int> queue;

    public PriorityQueue()
    {
        queue = new List<int>();
    }
    
    public void Add(int num){
        queue.Add(num);
        queue.Sort(); // 여기서 미리 정렬해서 우선순위큐처럼 만듦
    }
    
    public void DeleteMax(){  
        if(queue.Count>0)
            queue.RemoveAt(queue.Count-1);
    }
    
    public void DeleteMin(){
        if(queue.Count>0)
            queue.RemoveAt(0);
    }
    
    public int Min => queue[0];
    public int Max => queue[queue.Count-1];
    public int Count => queue.Count;
}

public class Solution {   
    public PriorityQueue queue = new PriorityQueue();
    
    public void Check_Operation(string oper){
        if(oper == "D 1"){
            queue.DeleteMax();
        }
        else if (oper == "D -1"){
            queue.DeleteMin();
        }
        else{
            string num = oper.Split(" ")[1];
            queue.Add(int.Parse(num));
        }
    }
    
    public int[] solution(string[] operations) {        
        int n = operations.Length;
        
        for(int i=0;i<n;i++){
            Check_Operation(operations[i]);
        }       
        
        if(queue.Count==0)
            return new int[] { 0, 0 };
        else
            return new int[] { queue.Max,queue.Min};
    }
}