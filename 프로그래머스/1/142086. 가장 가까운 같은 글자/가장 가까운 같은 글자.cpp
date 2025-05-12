#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    map<int,int> dist;
    
    for(int i=0;i<s.length();i++){
        if (dist.find(s[i]) == dist.end()){ //dist의 키에 해당 문자가 없으면
            answer.push_back(-1);
        }
        else{
            int pos = i-dist[s[i]];
            answer.push_back(pos);
        }    
        dist[s[i]] = i;
    }
    
    return answer;
}