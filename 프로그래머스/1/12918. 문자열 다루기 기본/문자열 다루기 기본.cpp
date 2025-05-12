#include <string>
#include <vector>
#include <cctype>

using namespace std;

bool solution(string s) {
    bool answer = true;
    if (s.length() != 4 and s.length() != 6)
        answer = false;
    for (char s_string : s)
        if (!isdigit(s_string)){
            answer = false;
            break;
        }
            
    
    return answer;
}