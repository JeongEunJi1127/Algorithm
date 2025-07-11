using System;

public class Solution {
    public int solution(string[] babbling) {
        int answer = 0;
            
        for (int i = 0; i < babbling.Length; i++) {
            string bab = babbling[i];
            bab = bab.Replace("aya",".");
            bab = bab.Replace("ye",".");
            bab = bab.Replace("woo",".");
            bab = bab.Replace("ma",".");
            
            Console.WriteLine(bab);
            
            bab = bab.Replace(".","");

            if(bab == "")
            {
                answer++;
            }   
        }

        
        return answer;
    }
}
