#include <iostream>
#include <string>
using namespace std;

int main() {
	int n;
	string s;
	cin >> n;
	while (n > 0) {
		cin >> s;
		cout << s[0]<< s[size(s) - 1] << endl;
		n--;

	}
	return 0;
}
