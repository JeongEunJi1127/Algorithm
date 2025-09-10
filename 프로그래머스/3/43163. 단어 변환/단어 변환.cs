// 16:00 ~ 16:37

using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public string Begin;
    public string Target;
    public string[] Words;
    public int Answer = int.MaxValue;

    public bool Can_Alter(string word1, string word2){
        int different_cnt = 0;

        for(int i=0; i<word1.Length; i++)
        {
            if(word1[i] != word2[i])
                different_cnt++;

            if (different_cnt > 1)
                return false;  // 이미 1개 초과면 바로 false
        }
        return true;
    }
    
    public void Dfs(string cur_word, int cnt, List<string> visited){
        //Console.WriteLine($"\n현재 단어 {cur_word}, 현재 카운트 {cnt}");
        for(int i=0;i<Words.Length;i++){
            if(visited.Contains(Words[i])){
                //Console.WriteLine($"현재 검사중인 단어 {Words[i]}는 visited안에 존재");
                continue;
            }
            
            if(cur_word == Target){ // 타겟과 같은 단어면
                //Console.WriteLine($"현재 단어 {cur_word}는 타겟과 같은 단어");
                Answer = Math.Min(Answer,cnt);
                return;
            }
            else if(Can_Alter(cur_word, Words[i]) && cur_word != Words[i]){
                //Console.WriteLine($"현재 단어 {cur_word}는 {Words[i]}와 교체 가능");
                visited.Add(Words[i]);
                Dfs(Words[i],cnt+1,visited);
                visited.Remove(Words[i]); // 재귀 끝나면 원상복구
            }
        }
        return;
    }
    
    
    public int solution(string begin, string target, string[] words) {
        Begin = begin;
        Target = target;
        Words = words;
        
        if(!words.Contains(target)) // words 안에 타겟 단어가 없으면 0 리턴
            return 0;
        
        List<string> visited = new List<string>();
        Dfs(begin,0,visited);        
        
        return Answer;
    }
}