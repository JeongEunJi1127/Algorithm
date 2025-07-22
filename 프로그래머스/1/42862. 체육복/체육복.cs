// 14:36 ~ 15:06

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        List<int> lost_list = lost.ToList();
        List<int> reserve_list = reserve.ToList();
        
        // 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우 미리 처리
        for(int i=1; i<n+1; i++){
            if(lost_list.Contains(i) && reserve_list.Contains(i)){
                lost_list.Remove(i);
                reserve_list.Remove(i);
            }
        }
        
        for(int i=1; i<n+1; i++){
            // i번 학생이 체육복을 도난당한 사람일 때
            if(lost_list.Contains(i)){
                
                // 순수하게 도난당한 경우에 앞 뒤 사람에게 빌릴 수 있는 경우
                if(reserve_list.Contains(i-1)){
                    reserve_list.Remove(i-1);
                    answer ++;
                }
                else if(reserve_list.Contains(i+1)){
                    reserve_list.Remove(i+1);
                    answer ++;
                }  
                
                //Console.WriteLine(i);
            }
            else
                answer ++;
        }
        // Console.WriteLine($"도난당한 사람 중 체육복 빌린 사람 수 {answer}");
        return answer;
    }
}