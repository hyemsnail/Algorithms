#include <iostream>
using namespace std;

int main() {

	int array[101];
	int n; // 배열 요소 개수
    int v; // 찾는 숫자
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> array[i]; // 배열을 직접 입력
	}
    cin >> v;
	
	int amount = 0; // 그 숫자의 개수
	for (int i = 0; i < n; i++) {
		if (array[i] == v)
			amount++;
	}
	cout << amount;
}