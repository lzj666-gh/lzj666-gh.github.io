# P3619 题解

（~~~~这题82分卡了我一个多小时~~~~）

初次审题，就知道应该先做b大于0的任务，因为如果先做小于0的话，会使得t减小，这就可能使得一些比较大的ti不能达到（~~~~到这里大家应该能都想到~~~~）

然后问题来了，b大于0的任务做完了，小于0的呢？如果按照b从大到小排序的话，貌似很正确，但你看这组数据：

做完b大于0的任务后，T=10，剩下2组任务：t1=9，b1=-5；t2=4，b2=-2；显然如果先做第二个的话，会使得第一个任务不能完成

我们可以这样想：对于两组任务t1、b1、t2、b2（其中b1、b2全为负）且当时的时间为T，若先做第一个任务会使得不能做第二个任务而先做第二个任务后还能继续完成第一个任务，则会有

T+b1<t2,T+b2>t1;

移项可得

T<t2-b1,T>t1-b2;

根据不等式的传递性可知

t1-b2<T<t2-b1即t1+b1<t2+b2;

所以我们可以看出按照b+t从大到小的顺序排序可使得答案最优

上代码
```cpp
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#define MAXN 2147483647

using namespace std;
struct node
{
    int tim;
    int b;
}a[100010];    //b大于0的任务
struct ss
{
    int tim;
    int b;
}f[100010];    //b小于等于0的任务
int n,t,z;
int cmp(node &a,node &b)
{
    return a.tim<b.tim;    //由于b大于0，所以先做t小的任务
}
int comp(ss &a,ss &b)
{
    return a.b+a.tim>b.b+b.tim;    //证明如上
}
int main()
{
    scanf("%d",&z);
    for(int i=1;i<=z;i++)
    {
        int s=0,cnt=0,num=0;
        scanf("%d%d",&n,&t);
        for(int j=1;j<=n;j++)
        {
        	int x,y;
        	scanf("%d%d",&x,&y);
        	if(y>0) a[++cnt].tim=x,a[cnt].b=y;
        	else f[++num].tim=x,f[num].b=y;
		}
        sort(a+1,a+cnt+1,cmp);
        sort(f+1,f+num+1,comp);
        for(int j=1;j<=cnt;j++)
        {
            if(t>a[j].tim) t+=a[j].b;
            else{
                s=1;
                break;
            }
		}
        for(int j=1;j<=num;j++)
        {
            if(t>f[j].tim) t+=f[j].b;
            else{
                s=1;
                break;
            }
            if(t<=0){
                s=1;
                break;
            }
        }
        if(s==0) printf("+1s\n");
        else printf("-1s\n");
    }
    return 0;
}
```

