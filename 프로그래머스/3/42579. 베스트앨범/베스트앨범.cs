// 16:38 ~ 17:10

using System;
using System.Linq;
using System.Collections.Generic;

public class Song{
    public int Plays;
    public int ID;
    
    public Song(int plays,int id){
        Plays = plays;
        ID = id;
    }
}
public class Solution {
    public int[] solution(string[] genres, int[] plays) {
        List<int> answer = new List<int>();
        Dictionary<string,int> genre_dict = new Dictionary<string,int>();
        Dictionary<string, List<Song>> plays_dict = new Dictionary<string, List<Song>>();
        
        // 딕셔너리 초기화
        for(int i=0;i<genres.Length; i++){
            // 장르 별 재생 횟수 초기화
            if(genre_dict.ContainsKey(genres[i]))
                genre_dict[genres[i]] += plays[i];
            else
                genre_dict[genres[i]] = plays[i];
            //Console.WriteLine($"장르 딕셔너리 {genres[i]} 키에 재생횟수 {plays[i]} 추가 : {genre_dict[genres[i]]}");
            
            // 노래 별 고유 번호와 재생 횟수 초기화
            if(!plays_dict.ContainsKey(genres[i])){
                plays_dict[genres[i]] = new List<Song>();
            }
            plays_dict[genres[i]].Add(new Song(plays[i],i));
            //Console.WriteLine($"노래 별 딕셔너리 {genres[i]} 키에 고유번호 {i}, 재생횟수 {plays[i]} 추가\n");
        }
        
        // 속한 노래가 많이 재생된 장르를 먼저 수록
        var sorted_list = genre_dict.OrderByDescending(x => x.Value);
        foreach(var sorted in sorted_list){
            //Console.WriteLine($"{sorted.Key}가 가장 큼");
            List<Song> cur_songs = plays_dict[sorted.Key];
            cur_songs.Sort((a, b) => b.Plays.CompareTo(a.Plays));
            answer.Add(cur_songs[0].ID);
            if(cur_songs.Count>1)
                answer.Add(cur_songs[1].ID);
            // Console.WriteLine($"{cur_songs[0].ID}");
            // Console.WriteLine($"{cur_songs[1].ID}");
        }
        
        return answer.ToArray();
    }
}