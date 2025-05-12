#include <vector>
#include <set>
using namespace std;

int solution(vector<int> nums)
{
    set<int> setNumbers;
    int answer = 0;
    
    for(int num:nums){
        setNumbers.insert(num);
    }
    
    int phoneketmon_size = nums.size()/2;
    
    if(phoneketmon_size >= setNumbers.size()){ 
        answer = setNumbers.size();
    }
    else{
        answer = phoneketmon_size;
    }
    
    return answer;
}