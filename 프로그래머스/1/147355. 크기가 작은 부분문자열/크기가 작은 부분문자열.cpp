#include <string>
#include <vector>
#include <iostream>

using namespace std;

// stoi 보다 큰 범위를 변환해주는 stoll 사용해야함
// stoi는 int의 : 최소값: -2,147,483,648 (-2^31), 최대값: 2,147,483,647 (2^31 - 1)
// stoll은 long long의 범위 : 최소값: -9,223,372,036,854,775,808 (-2^63), 최대값: 9,223,372,036,854,775,807 (2^63 - 1)

int solution(string t, string p) {
    int answer = 0;
    long long p_int = stoll(p);
    string s = "";
    
    for(int i=0;i<t.size()-p.size()+1;i++){
        for(int j=0;j<p.size();j++){
            s += t[i+j];
        }
        if (stoll(s) <= p_int)
            answer ++;
        s = "";
   }    

    return answer;
}