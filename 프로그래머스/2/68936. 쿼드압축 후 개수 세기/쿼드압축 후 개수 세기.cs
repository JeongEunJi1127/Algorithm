// 17:45 ~ 18:05

using System.Collections.Generic;
using System;

public class Solution {
    public int[] answer = new int[2];
    int zeroCount = 0;
    int oneCount = 0;
    
    public bool IsSame(int[,] arr, int x, int y, int size){
        int value = arr[x,y];      
        for (int i=x; i<x+size; i++)
        {
            for (int j=y; j<y+size; j++)
            {
                if (arr[i, j] != value) 
                    return false;
            }
        }       
        return true;
    }
    
    public void Divide(int[,] arr, int x, int y, int size){
        if(IsSame(arr,x,y,size)){
            if(arr[x,y]==0) 
                zeroCount++;
            else
                oneCount++;
            return;
        }
            
        size /= 2;
        Divide(arr,x, y, size);
        Divide(arr,x, y + size, size);
        Divide(arr,x + size, y, size);
        Divide(arr,x + size, y + size, size);
    }
    
    public int[] solution(int[,] arr) {        
        int n = arr.GetLength(0);
        
        Divide(arr,0,0,n);
        answer[0] = zeroCount;
        answer[1] = oneCount;
        
        return answer;
    }
}