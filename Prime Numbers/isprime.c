/*
 * Praneet Kapoor
 * 16.04.2021
 *
 * Program to check whether a number is prime or not
 * */

#include<stdio.h>

int isprime(unsigned long int);

int main(void)
{
	    unsigned long int num;
	        printf("Enter the number: ");
		    scanf("%lu", &num);
		        if(isprime(num) == 0) printf("\nIt is a prime.\n");
			    else printf("\nIt is not a prime.\n");
			        return 0;
}

int isprime(unsigned long int num)
{
	    int check = 0;
	        for(int i = 2; (i <= num/2) && (check < 1); ++i){
			        printf("\n\t\ti-> %d check-> %d", i, check);
				        if(num % i == 0)
						            ++check;
					    }    
		    if(check < 1) return 0;
		        else return 1;
}
