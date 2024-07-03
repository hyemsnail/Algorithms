#include<iostream>
using namespace std;

int a[1000001] = {0};
int main() {

	int M, N;
	cin >> M >> N;

	for (int i = 2; i <= N; i++)
		for (int j = 2; i * j <= N; j++)
			a[i * j] = 1;

	for (int i = M; i <= N; i++)
		if (a[i] == 0) cout << i << '\n';


	return 0;
}
