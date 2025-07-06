# P1016 题解

这道题目应该算是妥妥的贪心+模拟吧……

算法原理如下：

1.枚举途中经过的加油站，每经过一个加油站，计算一次花费；

2.在一个加油站所需要加的油，就是能够支持它到达下一个油价比它低的加油站的量；

3.如果在这个加油站即使加满油，都不能到达一个比它油价低的加油站，就把油箱加满，前往能够到达的加油站中油价最低的那个；

4.如果在这个加油站即使加满油，都不能到达任意一个加油站，也不能到达终点城市，说明无解；


**第三点：为什么要加满油？**因为这样可以减少在下一个加油站（价格更贵）所需要加的油量。

AC代码：

```cpp
#include<bits/stdc++.h>
using namespace std;
double maxx,mo=0,d2,temlen=0,d1,c,p;
//temlen：油箱中在到达了下一个加油站时油箱中的剩余油量可以继续走的路程
int n;
struct add
{
    double co;
    double dis;
}pl[10000];//加油站结构体：dis-距离起点的距离，co：油价
int move(int now)//1.now:现在到达的加油站
{
    int can=99999;
    int f=pl[now].dis;
    for(int i=now+1;i<=n&&pl[i].dis-f<=maxx;i++)
    {
        if(pl[i].co<pl[now].co)//2.
        {
            mo+=((pl[i].dis-f-temlen)/d2)*pl[now].co;
            temlen=0;
            return i;
        }
        if(can==99999||pl[i].co<pl[can].co)can=i;
    }
    if(d1-pl[now].dis<=maxx)
        {
            mo+=((d1-pl[now].dis-temlen)/d2)*pl[now].co;
            return 9999;
        }
    if(can==99999)//4.
    {
        cout<<"No Solution";
        return -1;
    }
    else//3.
    {
        mo+=c*pl[now].co;
        temlen+=(maxx-pl[can].dis+f);
        return can;
    }
}
int cmp(add a,add b)
{
    return a.dis<b.dis;
}
int main()
{
    cin>>d1>>c>>d2>>p>>n;
    pl[0].dis=0;
    pl[0].co=p;
    for(int i=1;i<=n;i++)cin>>pl[i].dis>>pl[i].co;
    sort(pl,pl+n,cmp);
    maxx=c*d2;
    int k=0,t;
    do
    {
        t=move(k);
        k=t;
        if(t==-1)return 0;
    }while(t!=9999);
    printf("%.2f",mo);
    return 0;
}
```

Update：
	时隔一年之后偶然翻到，竟然有137个赞QAQ！感谢大家，但由于之前的写法上有一些不足（太丑啦！），现在贴一份新的代码上来。
    
```cpp
#include <bits/stdc++.h>
using namespace std;
#define maxn 100000
#define db double
#define INF 9999999 
int n;
db D1, D2, C, P, res, ans, maxx;

struct node
{
	db co, dis;
	bool friend operator <(const node& a, const node& b)
	{ return a.dis < b.dis; }
}pl[maxn];

int Solve(int now)
{
	int flag = INF; db d = pl[now].dis; 
	for(int i = now + 1; i <= n && pl[i].dis - d <= maxx; i ++)
	{
		if(pl[i].co < pl[now].co)
		{
			ans += ((pl[i].dis - d - res) / D2) * pl[now].co;
			res = 0; return i;
		}
		if(flag == INF || pl[i].co < pl[flag].co) flag = i;
	}
	if(D1 - pl[now].dis <= maxx)
	{
		ans += ((D1 - pl[now].dis - res) / D2) * pl[now].co;
		return INF;
	}
	if(flag == INF) { printf("No Solution\n"); return -1; }
	else
	{
		ans += C * pl[now].co; res += (maxx - (pl[flag].dis - d));
		return flag;
	}
}

int main()
{
	scanf("%lf%lf%lf%lf%d", &D1, &C, &D2, &P, &n);
	pl[0].dis = 0, pl[0].co = P;
	for(int i = 1; i <= n; i ++) 
		scanf("%lf%lf", &pl[i].dis, &pl[i].co);
	sort(pl, pl + n + 1);
	maxx = C * D2;
	int k = 0, t;
	do
	{
		t = Solve(k), k = t;
		if(t == -1) return 0;
	}while(t != INF);
	printf("%.2lf", ans);
	return 0;
}
```