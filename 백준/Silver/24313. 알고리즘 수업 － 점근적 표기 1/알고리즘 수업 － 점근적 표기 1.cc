#include <iostream>
using namespace std;


int main() {
	int a1, a0, c, n0;
	cin >> a1 >> a0;
	cin >> c;
	cin >> n0;

	int fn = a1 * n0 + a0;
	int gn = n0 * c;

	if ((a1 <= c) && (fn <= gn)) {
		cout << 1;
	}
	else
		cout << 0;
	return 0;
}