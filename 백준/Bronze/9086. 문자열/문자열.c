#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	int n;
	char s[999];
	scanf("%d", &n);
	while (n > 0) {
		scanf("%s", s);
		printf("%c%c\n", s[0], s[strlen(s) - 1]);
		n--;
	}
	return 0;
 
}
