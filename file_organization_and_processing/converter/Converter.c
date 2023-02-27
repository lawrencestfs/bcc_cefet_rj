/*
  * File Name: 	Converter.c
  * Authors: Lawrence Fernandes & Vanessa Cavalcanti
  * This program reads an input.txt file containing numbers,
  * convert them to different numerical bases and
  * writes the result in an output.txt file.
  */

// Imports
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

// Global Variables
#define MAX_ALG 7 // Set the maximum size for each number to be read.
#define NUM_AMT 10 // Set amount of numbers to be read and convert.
#define STRLEN 2048 // Statement of the size of the buffer used for conversion.

typedef struct this_number {
        char hexadecimal[MAX_ALG + 1];
	unsigned long long int decimal;
	char binary[(4 * MAX_ALG) + 1];
} number;

typedef struct parser {
	int base;
	char num_read[(4 * MAX_ALG) + 1];
} copia;

char* Convert(unsigned long long int number, int base) {
        static char buffer[STRLEN];
	const char *digits = "0123456789ABCDEF";

	buffer[STRLEN-1] = 0; // To mark the end of the string.
	int i = STRLEN-2;

	do {
		buffer[i--] = digits[number % base];
		number = number / base;
	} while(number > 0);

	return &buffer[i+1];
}

int main() {
	number values[NUM_AMT];
	copia test[NUM_AMT];

	FILE *in = fopen("input.txt", "r");
	if (in == NULL) {
		fprintf(stderr, "\nThe file could not be open for read!\n");
		return 0;
	}

	int i = 0;
	while (fscanf(in, "%d %s\n", &test[i].base, test[i].num_read) == 2) {
		i++;
	}
	
	fclose(in);

	int j;
	for(j=0; j<NUM_AMT; j++) {
		if(test[j].base == 2) {
			strcpy(values[j].binary, test[j].num_read);
			values[j].decimal = strtoull(test[j].num_read, (char **)NULL, 2);
			strcpy(values[j].hexadecimal, Convert(values[j].decimal,16));
		}

		if(test[j].base == 10) {
			values[j].decimal = strtoull(test[j].num_read, (char **)NULL, 10);
			strcpy(values[j].binary, Convert(values[j].decimal,2));
			strcpy(values[j].hexadecimal, Convert(values[j].decimal,16));
		}

		if(test[j].base == 16) {
			strcpy(values[j].hexadecimal, test[j].num_read);
			values[j].decimal = strtoull(test[j].num_read, (char **)NULL, 16);
			strcpy(values[j].binary, Convert(values[j].decimal,2));
		}
    	        printf("%s\t%llu\t%s\n", values[j].hexadecimal, values[j].decimal, values[j].binary);
	}
	
	FILE *out = fopen("output.txt", "w");
	if (out == NULL) {
		fprintf(stderr, "\nThe file could not be open for write!\n");
		return 0;
	}
    
	int k;
	for(k=0; k<NUM_AMT; k++) {
		fprintf(out, "%s\t%llu\t\t%s\n", values[k].hexadecimal, values[k].decimal, values[k].binary);
	}
    
	fclose(out);
	return 0;
}
