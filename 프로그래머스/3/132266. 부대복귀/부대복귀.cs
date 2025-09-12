// 17:40 ~ 18:08

using System;
using System.Collections.Generic;

public class Solution {
    public int[] solution(int n, int[,] roads, int[] sources, int destination) {
        int[] answer = new int[sources.Length];
            
        List<int>[] graph = new List<int>[n+1];
        // 그래프 초기화
        for (int i=0; i<=n; i++) {
            graph[i] = new List<int>();
        }
        
        for(int i=0;i<roads.GetLength(0);i++){
            int start = roads[i,0];
            int end = roads[i,1];
            
            graph[start].Add(end);
            graph[end].Add(start);
            
            // Console.WriteLine($"{start} -> {end} / {end} -> {start} 초기화");
        }
    
        // BFS -> destination에서 각 노드까지의 최단 거리 리스트 dist를 구해놓기
        int m = graph.Length; // 노드 개수
        bool[] visited = new bool[m+1];
        int[] dist = new int[m+1];
        
        Queue<int> queue = new Queue<int>();
        queue.Enqueue(destination); 
        visited[destination] = true;
        dist[destination] = 0; 
        
        while(queue.Count>0){
            int cur_node = queue.Dequeue();
            
            foreach(var node in graph[cur_node]){
                if(!visited[node]){
                    visited[node] = true;
                    dist[node] = dist[cur_node] + 1;
                    queue.Enqueue(node);
                }
            }
        }
        
        // 각 Source에서 Destination까지의 최단 거리 구하기
        for(int i=0;i<sources.Length;i++){
            if(!visited[sources[i]])
                answer[i] = -1;
            else
                answer[i] = dist[sources[i]];
        }
        
        return answer;
    }
}