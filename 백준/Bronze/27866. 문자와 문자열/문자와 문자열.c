#include <stdio.h>


int main() {

	char a[1000];
	int index;
	scanf("%s", a);
	scanf("%d", &index);
	printf("%c", a[index-1]);

    return 0;

}
