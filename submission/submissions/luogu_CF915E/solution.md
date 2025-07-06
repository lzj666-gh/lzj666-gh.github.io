# CF915E 题解

## [更好的阅读](https://www.cnblogs.com/yzhang-rp-inf/p/9775249.html)

#### 原题传送门：[CF915E Physical Education Lessons](https://www.luogu.org/problemnew/show/CF915E)

## 前置芝士：珂朵莉树

### [窝博客里对珂朵莉树的介绍](https://www.cnblogs.com/yzhang-rp-inf/p/9443659.html )

#### 这道题很简单啊

#### 每个操作就是区间赋值0或1，顺带把总和修改一下，跑的飞快

```cpp
#pragma GCC optimize("O3")
#include <bits/stdc++.h>
#define IT set<node>::iterator
using namespace std;
inline int read() //io优化
{
    register int x=0,f=1;register char ch=getchar();
    while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
    while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
    return x*f;
}
struct node
{
    int l,r;
    mutable bool v;
    node(int L, int R=-1, bool V=0):l(L), r(R), v(V) {}
    bool operator<(const node& o) const
    {
        return l < o.l;
    }
};
set<node> s;
int sum=0;
IT split(int pos)
{
    IT it = s.lower_bound(node(pos));
    if (it != s.end() && it->l == pos) 
        return it;
    --it;
    int L = it->l, R = it->r;
    bool V = it->v;
    s.erase(it);
    s.insert(node(L, pos-1, V));
    return s.insert(node(pos, R, V)).first;
}
void assign_val(int l,int r,bool val)
{
    IT itr = split(r+1), itl = split(l), it = itl;
    for( ;itl != itr; ++itl)
        sum-=itl->v*(itl->r-itl->l+1); //过程中顺带计算
    s.erase(it,itr);
    s.insert(node(l,r,val));
    sum+=val*(r-l+1); //过程中顺带计算
}
int main()
{
	int n=read(),m=read();
	s.insert(node(1,n,1));
	sum=n;
	while(m--)
	{
		int l=read(),r=read(),op=read();
		if(op==1) //修改
			assign_val(l,r,0);
		else
			assign_val(l,r,1);
		printf("%d\n",sum); //输出总和
	}
	return 0;
}
```