#include <string>
#include <iostream>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;
    
    for(int i=2;i*i<n;i++){
        if(is_prime[i]){
            for (int j = i*i; j <= n; j += i) {  // i의 배수 지우기 (i*i부터 시작)
                is_prime[j] = false;
            }
        }
    }
    
    for(int i=2;i<n+1;i++){
        if(is_prime[i])
            answer ++;
    }
    
    return answer;
}