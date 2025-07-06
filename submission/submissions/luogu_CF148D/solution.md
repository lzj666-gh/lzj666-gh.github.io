# CF148D 题解

#### Description

~~翻译君写的清清楚楚明明白白~~

----

#### Solution

- 概率dp
- 设 $f(i,j)$ 表示有 $i$ 只白鼠，$j$ 只黑鼠时A先手胜的概率

- 初始状态
- 全白时，显然先手必胜
- 有一只黑鼠时，先手若抽到黑鼠则后手必胜，所以先手首回合必须抽到白鼠
- $f(i,0)=1,f(i,1)=\frac{i}{i+1}$

- 转移方程 $f(i,j)$
- 先手抽到白鼠，胜：$\frac{i}{i+j}$
- 先手抽到黑鼠，后手抽到白鼠，败： $0$
- 先手抽到黑鼠，后手抽到黑鼠，跑一只白鼠：$\frac{j}{i+j}\times \frac{j-1}{i+j-1}\times \frac{i}{i+j-2}\times f(i-1,j-2)$
- 先手抽到黑鼠，后手抽到黑鼠，跑一只黑鼠：$\frac{j}{i+j}\times \frac{j-1}{i+j-1}\times \frac{j-2}{i+j-2}\times f(i,j-3)$
- $f(i,j)=\frac{i}{i+j}+\frac{j}{i+j}\times \frac{j-1}{i+j-1}\times \frac{i}{i+j-2}\times f(i-1,j-2)+\frac{j}{i+j}\times \frac{j-1}{i+j-1}\times \frac{j-2}{i+j-2}\times f(i,j-3)$

- $O(wb)$

----

#### Code 1
```cpp
//DP
#include<bits/stdc++.h>
using namespace std;

inline int read()
{
    int N=0,C=0;char tf=getchar();
    for(;!isdigit(tf);tf=getchar())C|=tf=='-';
    for(;isdigit(tf);tf=getchar())N=(N<<1)+(N<<3)+(tf^48);
    return C?-N:N;
}

const int N=1010;
int w,b;
double f[N][N];

int main()
{
	w=read(),b=read();
	
	for(int i=1;i<=w;++i)
		f[i][0]=1.0,f[i][1]=1.0*i/(i+1);//全白必胜，一黑首回合必须抽到白鼠
		
	if(!b||b==1)return printf("%.9lf\n",f[w][b]),0;
	for(int i=1;i<=w;++i)
		for(int j=2;j<=b;++j)
		{
			f[i][j]=1.0*i/(i+j);
			f[i][j]+=1.0*j/(i+j)*(j-1)/(i+j-1)*i/(i+j-2)*f[i-1][j-2];//跑白
			if(j^2)f[i][j]+=1.0*j/(i+j)*(j-1)/(i+j-1)*(j-2)/(i+j-2)*f[i][j-3];//跑黑 
		}
	printf("%.9lf\n",f[w][b]);
	
    return 0;
}
```

----

#### Code 2
```cpp
//记忆化搜索
#include<bits/stdc++.h>
using namespace std;

inline int read()
{
    int N=0,C=0;char tf=getchar();
    for(;!isdigit(tf);tf=getchar())C|=tf=='-';
    for(;isdigit(tf);tf=getchar())N=(N<<1)+(N<<3)+(tf^48);
    return C?-N:N;
}

const int N=1010;
int w,b;
double f[N][N];

double dfs(int i,int j)
{
	if(f[i][j])return f[i][j];
	if(!i)return 0;//全黑必败 
	if(!j)return f[i][j]=1.0;//全白必胜 
	if(j==1)return f[i][j]=1.0*i/(i+1);//一黑首回合必须抽到白鼠 
	f[i][j]=1.0*i/(i+j);
	f[i][j]+=1.0*j/(i+j)*(j-1)/(i+j-1)*i/(i+j-2)*dfs(i-1,j-2);//跑白
	if(j>2)f[i][j]+=1.0*j/(i+j)*(j-1)/(i+j-1)*(j-2)/(i+j-2)*dfs(i,j-3);//跑黑 
	return f[i][j];
}

int main()
{
	w=read(),b=read();
	printf("%.9lf\n",dfs(w,b));
	
    return 0;
}
```