#include<stdio.h>
#include<stdlib.h>
#define PI 3.141592

int my_cos(float*, int*, float*);
int power(float, int);
int factorial(int);
int deg_to_rad(float*, int*, int*);

int check1 = 0, Ic = 0, If = 0, Ip = 0;
float P, F;

int deg_to_rad(float *angle, int *quad, int *symbol)
{
	*angle = (*angle * PI) / 180;
	int type = *angle / PI;
	/*type = *angle - val;
	if(type < 0)
		type *= -1;*/
	if(type % 2 == 0){
		//printf("EVEN");
		if((type * PI) < *angle && ((type + 0.5) * PI) > *angle){
			*quad = 1;
			*symbol = 1;
			if((0 < *angle) && (0.5 * PI > *angle))
				*angle = *angle;
			else
				*angle = *angle - (type * PI);
		}
		else if(((type + 0.5) * PI) < *angle && ((type + 1) * PI) > *angle){
			*quad = 2;
			*symbol = -1;
			*angle = ((type + 1) * PI) - *angle;
		}
	}
	else if (type % 2 == 1){
		//printf("ODD");
		if((type * PI) < *angle && ((type + 0.5) * PI) > *angle){
			*quad = 3;
			*symbol = -1;
			*angle = *angle - (type * PI);
		}
		else if(((type + 0.5) * PI) < *angle && ((type + 1) * PI) > *angle){
			*quad = 4;
			*symbol = 1;
			*angle = ((type + 1) * PI) - *angle;
		}
	}
	return 0;
}

int power(float num, int index)
{
	if(Ip == 0)
		P = 1;
	if (index == 0)
		return P;
	else 
		P *= num;
	if(Ip < (index - 1)){
		++Ip;
		power(num, index);
	}
	else{
		Ip = 0;
		//printf("\nP : %f", P);
		return 0;
	}
}

int factorial(int num)
{
	if(If == 0)
		F = 1;
	if (num == 0)
		return F;
	else 
		F *= (If + 1);
	if(If < (num - 1)){
		++If;
		factorial(num);
	}
	else{
		If = 0;
		//printf("\nF: %f", F);
		return 0;
	}
}

int my_cos(float *angle, int *terms, float *result)
{
	int quad, symbol;
	if (check1 == 0){
		deg_to_rad(angle, &quad, &symbol);
		//printf("\nRAD: %f\nQUAD: %d\nSYMBOL: %d", *angle, quad, symbol);
		check1 = 1;
	}
	
	//Now the real pain begins Danny-boy!!
	if (Ic < *terms){
		power(-1.0, Ic + 1);
		float pow1 = P;
		power(*angle, 2 * Ic);
		float pow2 = P;
		factorial(2 * Ic);
		float pow3 = F;
		*result = *result + (pow1 * pow2) / (pow3);
		++Ic;
		my_cos(angle, terms, result);
	}
	else{
		Ic = 0;
	}
	if (((*result < 0) && (symbol > 0)) || ((*result > 0) && (symbol < 0)))
		*result *= -1;
	return *result;
}

int main()
{
	float angle, result = 0.0;
	int terms;
	printf("Enter the angle in degrees: ");
	scanf("%f", &angle);
	printf("Enter the no. of terms to be considered for computation: ");
	scanf("%d", &terms);
	my_cos(&angle, &terms, &result);
	printf("\n\a>> COS( %f ) = %f", angle, result);
	return 0;
}
