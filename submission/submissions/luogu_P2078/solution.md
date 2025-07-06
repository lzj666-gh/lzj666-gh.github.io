# P2078 题解

**map轻松AC**
map库最大的优势，就是它可以定义任意类型下标，那么女人编号是负数的问题就迎刃而解了

代码
```
```C++
#include<bits/stdc++.h>
#define r(i,a,b) for(int i=a;i<=b;i++)
using namespace std;int n,m,p,q,u,v,tat,tot;
map<int,int>f;//STl大法好
int find(int x){return x==f[x]?x:f[x]=find(f[x]);}
void judge(int x,int y){f[find(x)]=find(y);}
bool too(int x,int y){return find(x)==find(y);}
int main()
{
	scanf("%d%d%d%d",&n,&m,&p,&q);//输入
	r(i,-1*m,n) f[i]=i;//初始化
	r(i,1,p+q)//直接一起做
	 {
	 	scanf("%d%d",&u,&v);
	 	judge(u,v);
	 }
	r(i,-1*m,-1)
	 if(too(f[i],-1)) tat++;//找连接在一起的
	r(i,1,n)
	 if(too(f[i],1)) tot++;//同理
	printf("%d",min(tat,tot));//几对朋友就是最小值
}
```