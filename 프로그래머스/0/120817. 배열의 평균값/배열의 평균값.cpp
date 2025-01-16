#include <string>
#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    for(int i = 0; i < size(numbers); i++){
        answer += numbers[i];
    }
    answer = answer / size(numbers);
    return answer;
}