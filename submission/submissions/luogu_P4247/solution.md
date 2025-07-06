# P4247 题解

终于把欠下几个月的大坑填上了……

一道比较经典的线段树维护区间问题。

考虑~~众所周知的~~线段树五问：

1、每个区间需要记录哪些值？

区间维护任选c个数的乘积之和可能比较棘手，不过注意到c只有20，我们不妨暴力地把选0~20个数的答案全都记下来。

2、需要哪些标记？

区间加标记，区间取反标记。

3、如何叠加标记（在原有标记的区间增加新的标记？）

区间加标记直接叠加就行了。

处理取反标记时，与原先的标记xor。

为了方便处理，我们钦定取反标记的优先级高于区间加标记。这样的话别忘了在加一个取反标记时把原来的区间加标记也取反。

4、如何对区间进行整体修改？

先考虑取反。

由于奇数个-1相乘是-1，偶数个-1相乘是1，所以对于区间内奇数个数的答案要取反，偶数个数的答案不变。

区间加处理起来可能比较麻烦：

设区间大小为p。

原先区间内的数是a1,a2……,ap,区间加x后变成了(a1+x),(a2+x),……,(ap+x)。

考虑对区间的第i项进行修改，我们取任意一组乘积(a1+x)·(a2+x)·……·(ai+x)

把它展开：

原式=a1·a2·……·ai + x·(a1·a2·……·ai-1+a1·a2·……·ai-2·ai + ……) + x^2·(a1·a2·……·ai-2+……) + …… 

可以观察到，这个式子对答案的贡献相当于 sigma (j=1~i) x^(i-j)·(从这i个数中选出j个数的乘积之和)。

仍然不怎么好处理，不过我们可以转而去算这样一个东西：

对于一个j个数的乘积的式子，对i个数的乘积的贡献有多少。

即：这个式子在计算第i项答案时被算过多少次。

就相当于：有多少个从p个数中选i个数的方案，包含了某特定的j个数。

相当于这j个数必须选，还要从剩余(p-j)个数中任意选出(i-j)个数。

答案是C(p-j,i-j)。

那么我们就有了式子：ans[i] = sigma(j=0~i) x^(i-j)·ans[j]·C(p-j,i-j)。

杨辉三角预处理出(n,20)以内的组合数，更新答案时注意要从大到小更新。

5、如何合并区间？

ans[now][i]= sigma (j=0~i) ans[ls][j] * ans[rs][i-j]。

即：大区间选了i个数，可以是左区间选0个，右区间选i个；左区间选1个，右区间选(i-1)个，……，左区间选i个，右区间选0个。

注意特判一下选0个的情况(应该乘1而不是乘0)，在这里wa了好几次。

于是这题就做完了，~~是不是非常简单~~。

```cpp
#include<bits/stdc++.h>
#define ln q << 1
#define rn (q << 1) | 1
#define lson ln,l,mid
#define rson rn,mid + 1,r
#define md int mid = l + r >> 1
#define lint long long
using namespace std;
const int mo = 19940417;
int n,m;
int zuhe[50010][21];
struct node{
	lint c[21],c1;
	int sz;
	bool c2;
	node(){c1 = sz = c2 = 0;memset(c,0,sizeof(c));}
}t[200010];
int a[50010];
lint tmp[21];
int read(){
	int x = 0,y = 1;
	char c;
	c = getchar();
	while(c < '0' || c > '9'){
		if(c == '-') y = -1;
		c = getchar();
	}
	while(c >= '0' && c <= '9'){
		x = (x << 1) + (x << 3) + c - '0';
		c = getchar();
	}
	return x * y;
}
void print(lint q){
	if(q >= 10) print(q / 10);
	putchar(q % 10 + '0');
}
void upd(int q){//向上更新节点 
	register int i,j;
	memset(t[q].c,0,sizeof(t[q].c));
	for(i = 0;i <= 20 && i <= t[ln].sz;++i){
		for(j = 0;j + i <= 20 && j <= t[rn].sz;++j){
			t[q].c[i + j] += t[ln].c[i] * t[rn].c[j];
		}
	}
	for(i = 0;i <= 20 && i <= t[q].sz;++i) t[q].c[i] %= mo;
}
void build(int q,int l,int r){//初始化 
	t[q].sz = r - l + 1;
	if(l == r) {
		t[q].c[0] = 1;
		t[q].c[1] = (a[l] % mo + mo) % mo; 
		return;
	}
	md;
	build(lson);
	build(rson);
	upd(q);
}
void add(int q,int x){//区间加的更新 
	if(!q || !x) return;
	register int i,j;
	tmp[0] = 1;
	for(i = 1;i <= 20 && i <= t[q].sz;++i) tmp[i] = tmp[i - 1] * x % mo;
	for(i = min(20,t[q].sz);i;--i){
		for(j = 0;j < i;++j){
			t[q].c[i] = (t[q].c[i] + t[q].c[j] * tmp[i - j] % mo * zuhe[t[q].sz - j][i - j]) % mo;
		}
	}
	t[q].c1 = (t[q].c1 + x) % mo;
}
void rev(int q){//区间取反的更新 
	if(!q) return;
	for(int i = 1;i <= 20 && i <= t[q].sz;++i) t[q].c[i] = (i & 1) ? mo - t[q].c[i] : t[q].c[i];
	t[q].c1 = mo - t[q].c1;
	t[q].c2 ^= 1;
}
void psc(int q){//下传标记 
	if(t[q].c2){
		rev(ln);
		rev(rn);
		t[q].c2 = 0;
	}
	if(t[q].c1){
		add(ln,t[q].c1);
		add(rn,t[q].c1);
		t[q].c1 = 0;
	}
}
void md1(int q,int l,int r,int al,int ar,int ax){//区间加 
	if(l >= al && r <= ar){
		add(q,ax);
		return;
	}
	psc(q);
	md;
	if(mid >= al) md1(lson,al,ar,ax);
	if(mid < ar) md1(rson,al,ar,ax);
	upd(q);
}
void md2(int q,int l,int r,int al,int ar){//区间取反 
	if(l >= al && r <= ar) {
		rev(q);
		return;
	}
	psc(q);
	md;
	if(mid >= al) md2(lson,al,ar);
	if(mid < ar) md2(rson,al,ar);
	upd(q);
}
node mg(node q,node w){//合并两段区间 
	node e;
	register int i,j;
	e.sz = q.sz + w.sz;
	for(i = 0;i <= 20 && i <= q.sz;++i){
		for(j = 0;j + i <= 20 && j <= w.sz;++j){
			e.c[i + j] = (e.c[i + j] + q.c[i] * w.c[j]) % mo;
		}
	}
	return e;
}
node query(int q,int l,int r,int al,int ar){//区间查询 
	if(l >= al && r <= ar) return t[q];
	psc(q);
	md;
	if(ar <= mid) return query(lson,al,ar);
	else if(al > mid) return query(rson,al,ar);
	else return mg(query(lson,al,ar),query(rson,al,ar));
}
int main(){
	int i,j,k,l,r,x;
	char c;
	n = read();
	m = read();
	for(i = 1;i <= n;++i) a[i] = read();
	t[0].c[0] = 1; 
	zuhe[0][0] = 1;
	for(i = 1;i <= n;++i){
		zuhe[i][0] = 1;
		for(j = 1;j <= 20 && j <= i;++j) zuhe[i][j] = (zuhe[i - 1][j] + zuhe[i - 1][j - 1]) % mo;
	}//预处理组合数 
	build(1,1,n);
	for(i = 1;i <= m;++i){
		c = getchar();
		while(c != 'I' && c != 'Q' && c != 'R') c = getchar();
		l = read();
		r = read();
		if(c == 'I'){
			x = read();
			x = (x % mo + mo) % mo;
			md1(1,1,n,l,r,x);
		}
		else if(c == 'R'){
			md2(1,1,n,l,r);
		}
		else{
			x = read();
			print((query(1,1,n,l,r).c[x] % mo + mo) % mo);
			putchar('\n');
		}
	}
	return 0;
}
```

