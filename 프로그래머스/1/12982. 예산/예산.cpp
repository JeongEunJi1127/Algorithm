#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    int sum_budget = 0;
    
    sort(d.begin(),d.end());
    
    for(int i : d){
        sum_budget += i;   
        if (sum_budget <= budget){
            answer += 1;
        }
        else{
            break;
        }      
    }
    
    return answer;
}