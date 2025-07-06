# P1885 题解

先模拟长度，L(i)=L(i-1)*2+k;（其中k为m+oooo……oo的个数）  
当超出n时，再模拟n在什么位置上。  
1：在L(i-1)上迭代处理  
2：在m+oooo……oo上，第一个是m，其他都是o  
3：在第二个L(i-1)上，那就不要n-L(i-1)-k，就回到L(i-1)上了  
```cpp
#include<cstdio>

int n,t=0,k=3;

int main()
{
	scanf("%d",&n);int m=n;
	while(t<=n) t=t*2+k,k++;
	k--;
	while(t>0)
	{
		t=(t-k)/2;
		if(m>t)
		{
			if(m<=t+k)
			{
				if(m==t+1) return printf("m"),0;
				else printf("o"),0;
			}
			else m=m-(t+k);
		}
		k--;
	}
	return 0;
}
```