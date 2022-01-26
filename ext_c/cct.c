#include "mymath.h"
#include "cct.h"
#include "stdio.h"

#define PI 3.1415926

//得出的RGB比例总和为1,
int coordinate_to_RGB(COORD coord,RGB *rgb)
{
	COORD R,G,B;
	COORD gb_crossp;//gb的交点
	float R_GB_K,G_B_K;//混光比例
	float GB;//GB的亮度
	float temp1;
//特殊点处理
//
	switch(IsSpecialPoint(coord))
	{
		case 1:
		{
			memset(rgb,0,sizeof(RGB));
			rgb->r = 1;
			return 0;
		}
		case 2:
		{
			memset(rgb,0,sizeof(RGB));
			rgb->g = 1;
			return 0;
		}
		case 3:
		{
			memset(rgb,0,sizeof(RGB));
			rgb->b = 1;
			return 0;
		}
		case 4: //在RG线段上
		{
			memset(rgb,0,sizeof(RGB));
			temp1 = (coord.x-GX)/(RX-coord.x);
			rgb->r = temp1/(1+temp1);
			rgb->g = 1 - rgb->r;
			return 0;
		}
		case 5://在RB线段上
		{
			memset(rgb,0,sizeof(RGB));
			temp1 = (coord.x-BX)/(RX-coord.x);
			rgb->r = temp1/(1+temp1);
			rgb->b = 1 - rgb->r;
			return 0;
		}
		case 6://在GB线段上
		{
			memset(rgb,0,sizeof(RGB));
			temp1 = (coord.x-BX)/(GX-coord.x);
			rgb->g = temp1/(1+temp1);
			rgb->b = 1 - rgb->g;
			return 0;
		}
		default :break;
	}
	R.x = RX;
	R.y = RY;
	G.x = GX;
	G.y = GY;
	B.x = BX;
	B.y = BY;
	//求GB的交点。
	TowLineCross(G,B,R,coord,&gb_crossp);
	//求gb交点和R对于coord的比例
	LineSegmentK(gb_crossp,R,coord,&R_GB_K); //混光比和线段比成反比
	LineSegmentK(B,G,gb_crossp,&G_B_K);
	memset(rgb,0,sizeof(RGB));
	//设总亮度为1
	rgb->r = R_GB_K/(1+R_GB_K);
	GB = 1 - rgb->r;
	if(G_B_K == 0)
	{
		rgb->g = GB;
		rgb->b = 0;

	}
	else
	{
		rgb->g = GB*G_B_K/(1+G_B_K);
		rgb->b = GB - rgb->g;
	}
	return 0;
}


void RGB_to_HSI(float r,float g,float b,HSI *hsi)
{
	float min = r;
	float theta;
	float temp1,temp2;
	min = MIN(min,g);
	min = MIN(min,b);
	hsi->s = 1-3*min/(r+g+b);
	temp1 = ((r-g)+(r-b))/2;
	temp2 = pow(r-g,2) + (r-b)*(g-b);
	temp2 = sqrt(temp2);
	if(temp2==0)
	{
		temp2 = 0.00001;
	}
	temp1 = temp1/temp2;
	theta = acosf(temp1);
	if(g>=b)
		hsi->h = theta*180/PI;
	else
		hsi->h = 360 - theta*180/PI;
}

void CCT_to_HSI(int cct,signed grn,HSI *hsi)
{
    printf("CCT:%dK,grn:%d");
    hsi->h = 100;
    hsi->s = 0.5;
    hsi->i = 0.5;
}