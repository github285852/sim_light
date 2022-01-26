/***
*mymath.h
*
*       
*
*Purpose:
*       This file defined the functions and variables used by users
*       to fast computation the result of trigonometric functions and
*       the square root.
****/

#ifndef __MYMATH_H__
#define __MYMATH_H__

#define REAL   float
#define TAN_MAP_RES     0.003921569f     /* (smallest non-zero value in table) */
#define RAD_PER_DEG     0.017453293f
#define TAN_MAP_SIZE    256
#define MY_PPPIII   		3.14159f
#define MY_PPPIII_HALF  1.570796f

#define ABS(x) ( (x)>0?(x):-(x) )
#define LIMIT( x,min,max ) ( (x) < (min)  ? (min) : ( (x) > (max) ? (max) : (x) ) )

#ifndef MIN
#define MIN(a, b) ((a) < (b) ? (a) : (b))
#endif

#define MAX(a, b) ((a) > (b) ? (a) : (b))

typedef struct{
	float x;
	float y;
}COORD,coord_f;

typedef struct
{
	float a;
	float b;
	float c;
	float d;
}polyfit;

float my_abs(float f);
REAL fast_atan2(REAL y, REAL x);
float my_pow(float a);
float my_sqrt(float number);
double mx_sin(double rad);
double my_sin(double rad);
float my_cos(double rad);
float my_deathzoom(float x,float zoom);
float my_deathzoom_2(float x,float zoom);
float To_180_degrees(float x);
float my_pow_2_curve(float in,float a,float max);
int InTriangle(COORD point,COORD A,COORD B,COORD C);//判断一个点是否在三角形内
int OnLineSegment(coord_f point,coord_f A,coord_f B);
float fit(polyfit *pf,float x);
signed int add_and_limit(signed int x,signed int add,signed int left,signed int right);
signed int add_and_limit_over(signed int x,signed int add,signed int left,signed int right,int *over);
#endif

