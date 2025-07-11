#include <string>
#include <vector>

using namespace std;

int solution(vector<string> babbling) {
    int answer = 0;
    vector<string> can_pronounce = {"aya", "ye", "woo", "ma"};
    
    for(int i=0;i<babbling.size();i++){
        bool is_valid = true;
        for(int j=0;j<babbling[i].size();j++){
            if(babbling[i].substr(j,3) == "aya") j += 2;
            else if(babbling[i].substr(j,2) == "ye") j += 1;
            else if(babbling[i].substr(j,3) == "woo") j += 2;
            else if(babbling[i].substr(j,2) == "ma") j += 1; 
            else{
                is_valid = false;
                break;
            } 
        }
        
        if (is_valid){
            answer ++;
        }
    }
    
    return answer;
}