// useful macros and functions for avoiding re-typing everything
#include<stdio.h>
#include<stdlib.h>

// Memory allocation
#define Malloc(p,n) \
	if(!((p) = malloc(sizeof(*(p))*(n)))){\
		fprintf(stderr, "Insufficient memory");\
		exit(EXIT_FAILURE);\
	}
#define Calloc(p,n) \
	if(!((p) = calloc(n, sizeof(*(p))))){\
		fprintf(stderr, "Insufficient memory");\
		exit(EXIT_FAILURE);\
	}

#define Realloc(p,n) \
	if(!((p) = realloc((p),sizeof(*(p))*(n)))){\
		fprintf(stderr, "Insufficient memory");\
		exit(EXIT_FAILURE);\
	}

// useful stuff
// strlen: in ios: https://opensource.apple.com/source/Libc/Libc-583/arm/string/strlen.s 
//((x - 0x01010101) & ~x & 0x80808080) == hasnull(word) 

# define SWAP(x,y,t)((t)=(x),(x)=(y),(y)=(t))
// w/o tmp var ver. for basic types
void swap(int *a, int *b){
	*a ^= *b;
	*b ^= *a;
	*a ^= *b;
}

# define Compare(x,y)((x)>(y)?1:(x)==(y)?0:-1)

#define isFull(ptr) (!(ptr))

unsigned int int_to_bit(unsigned int k) {
    return (k == 0 || k == 1 ? k : ((k & 1) + 10 * int_to_bit(k >> 1)));
}


// to pass compiling process
int main(void){
	printf("\nrun passed");
	return 0;
}

