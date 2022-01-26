#ifndef _CCT_H
#define _CCT_H

typedef struct{
	float r;
	float ww;
	float g;
	float cw;
	float b;
	float a;
	float l;
	float y;
	float w;
}RGB,LEDK;

typedef struct{
  short h;
	float s;
	float i;
}HSI;

#define LEDWX_DEFAULT		0.3278
#define LEDWY_DEFAULT		0.3332
#define LEDRX_DEFAULT		0.6809
#define LEDRY_DEFAULT		0.3074
#define LEDGX_DEFAULT		0.1398
#define LEDGY_DEFAULT		0.6553
#define LEDBX_DEFAULT		0.1592 //
#define LEDBY_DEFAULT		0.0458


#define RX 	LEDRX_DEFAULT	// 0.7
#define RY 	LEDRY_DEFAULT	// 0.28
#define GX	LEDGX_DEFAULT//0.08
#define GY	LEDGY_DEFAULT//0.83
#define BX	LEDBX_DEFAULT	//0.1
#define BY	LEDBY_DEFAULT//0.1


int coordinate_to_RGB(COORD coord,RGB *rgb);
void RGB_to_HSI(float r,float g,float b,HSI *hsi);

#endif



