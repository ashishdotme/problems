#include <stdlib.h>  
#include <iostream>
using namespace std;

// Time: O(n+m)
// Space: O(1)

int main()
{
	int a = 0, b = 0, N = 10, M = 10;    
	for (int i = 0; i < N; i++) {
			a = a + rand();  // O(n)
	}
	for (int j = 0; j < M; j++) {
			b = b + rand();	// O(m)
	}
	return 0;
}
