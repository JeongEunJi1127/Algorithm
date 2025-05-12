#include <string>
#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    set<int> setNumbers;
    
    for(int i=0;i<numbers.size();i++){
        for(int j=i+1;j<numbers.size();j++){
            setNumbers.insert(numbers[i]+numbers[j]);
        }
    }
    
    for (int i : setNumbers) {
        answer.push_back(i);
    }
    
    
    return answer;
}