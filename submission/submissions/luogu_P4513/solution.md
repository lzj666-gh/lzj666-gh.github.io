# P4513 题解

我们知道，求一段序列的最大子段和是O（n）的，但是这样是显然会超时的。

我们需要一个数据结构来支持修改和计算的操作，对于这种修改一个而查询区间的问题，考虑使用线段树。

在线段树中，除了左端点，右端点，左儿子指针，右儿子指针之外，新开4个域——max，maxl，maxr，sum，其中sum为该区间的和，max为该区间上的最大子段和，maxl为必须包含左端点的最大子段和，maxr为必须包含右端点的最大子段和。

 可以用线段树来统计了注意求得的最大子段和中至少包含1个元素，所以出现了样例那样的输出负值。

## 修改时：
1、若左儿子的maxr和右儿子的maxl都为负，就从中取较大的为该节点的max（防止一个都不取），反之取二者中正的（都正就都取）。

2、将该节点的max用左右儿子的max更新。

3、该节点的maxl为左儿子的maxl与左儿子sum和右儿子maxl和的最大值。

4、该节点的maxr为右儿子的maxr与右儿子sum和左儿子maxr和的最大值。

5、该节点的sum为左右儿子的sum和。
## 查询时：
1、如果查询区间覆盖这一节点，将该节点信息返回。

2、如果只与一个儿子有交集，就返回在那个儿子中查找到的信息。

3、如果与两个儿子都有交集，就先分别计算出两个儿子的信息，然后按修改的方式将两个信息合并，然后返回。

4、最后返回的max值即为答案。
# 代码
```
#include<cstdio>
#include<algorithm>
using namespace std;
#define N 500001
struct Node{int maxv,maxl,maxr,sumv;}T[N<<2];
inline void pushup(Node &rt,const Node &ls,const Node &rs)
{
	if(ls.maxr<0 && rs.maxl<0)
	  rt.maxv=max(ls.maxr,rs.maxl);
	else
	  {
	  	rt.maxv=0;
	  	if(ls.maxr>0)
	  	  rt.maxv+=ls.maxr;
	  	if(rs.maxl>0)
	  	  rt.maxv+=rs.maxl;
	  }
	rt.maxv=max(rt.maxv,ls.maxv);
	rt.maxv=max(rt.maxv,rs.maxv);
	rt.maxl=max(ls.maxl,ls.sumv+rs.maxl);
	rt.maxr=max(rs.maxr,rs.sumv+ls.maxr);
	rt.sumv=ls.sumv+rs.sumv;
}
void buildtree(int rt,int l,int r)
{
	if(l==r)
	  {
	  	scanf("%d",&T[rt].maxv);
	  	T[rt].sumv=T[rt].maxl=T[rt].maxr=T[rt].maxv;
	  	return;
	  }
	int m=(l+r>>1);
	buildtree(rt<<1,l,m);
	buildtree(rt<<1|1,m+1,r);
	pushup(T[rt],T[rt<<1],T[rt<<1|1]);
}
void update(int p,int v,int rt,int l,int r)
{
	if(l==r)
	  {
	  	T[rt].sumv=T[rt].maxl=T[rt].maxr=T[rt].maxv=v;
	  	return;
	  }
	int m=(l+r>>1);
	if(p<=m) update(p,v,rt<<1,l,m);
	else update(p,v,rt<<1|1,m+1,r);
	pushup(T[rt],T[rt<<1],T[rt<<1|1]);
}
Node query(int ql,int qr,int rt,int l,int r)
{
	if(ql<=l&&r<=qr) return T[rt];
	int m=(l+r>>1);
	if(ql<=m && m<qr)
	  {
	  	Node res;
	  	pushup(res,query(ql,qr,rt<<1,l,m),query(ql,qr,rt<<1|1,m+1,r));
	  	return res;
	  }
	else if(ql<=m) return query(ql,qr,rt<<1,l,m);
	else return query(ql,qr,rt<<1|1,m+1,r);
}
int n,m;
int main()
{
	int op,x,y;
	scanf("%d%d",&n,&m);
	buildtree(1,1,n);
	for(;m;--m)
	  {
	  	scanf("%d%d%d",&op,&x,&y);
	  	if(op==1)
		  {
		  	if(x>y)
		  	  swap(x,y);
		  	printf("%d\n",query(x,y,1,1,n).maxv);
		  }
	  	else update(x,y,1,1,n);
	  }
	return 0;
}
```