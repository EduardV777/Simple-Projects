#include <cstdio>
#include <cstdlib>
using namespace std;

void output(int **A,int o,int i) {
	for (int k = 0; k < o; k++) {
		for (int j = 0; j < i; j++) {
			printf("%4d",A[k][j]);
		}
		printf("\n");
	}
}

int main() {
	int r=3, c = 5, s=1, num=1;
	int** Arr = new int* [r];
	for (int k = 0; k < r; k++) {
		Arr[k] = new int [c];
		for (int j = 0; j < c; j++, num++) {
			Arr[k][j] = num;
		}
	}
	printf("Contents of array:\n");
	output(Arr, r, 5);
	system("pause>nul");
	return 0;
}