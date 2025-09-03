# P2894 题解

区间操作，考虑用线段树维护，需要维护每一段区间的最大连续空房的数量sum，但是只维护这一个值是不够的，因为这时当我们更新节点信息时没法直接让父亲节点的sum等于两个儿子的sum和，比如左儿子在1~4中有三个连续空房1、2、3，右儿子在5~8中有三个连续空房6、7、8，这时父亲的sum显然不等于6而等于3。

因此在新建线段树时需要维护如下信息（懒标记会在下面的区间修改中用到）：
```cpp
struct Segment_Tree{
	int sum;//区间最大连续空房数
	int len;//区间长度 
	int lmax,rmax;//从左开始或从右开始的最大连续空房数
	int lazy;//懒标记 
}t[4*MAXX];
```

然后是建树过程，维护上述信息。
```cpp
void build(int p,int l,int r)
{
	t[p].lazy=0;//懒标记清零
	t[p].sum=t[p].len=t[p].lmax=t[p].rmax=r-l+1;
	//初始均为空房，所以连续空房长度都整个区间长度
	if(l==r)return;
	int mid=(l+r)/2;
	build(p*2,l,mid);
	build(p*2+1,mid+1,r); 
}
```
懒标记下放：
```cpp
void spread(int p)
{
	if(t[p].lazy==0)return;
    //没有标记直接返回
	if(t[p].lazy==1){
    //如果要新开房
	    t[p*2].lazy=t[p*2+1].lazy=1;
    //下放懒标记
		t[p*2].sum=t[p*2].lmax=t[p*2].rmax=0;
		t[p*2+1].sum=t[p*2+1].lmax=t[p*2+1].rmax=0;
    //这一段区间没有剩余房间
	}
	if(t[p].lazy==2){
    //如果退房
		t[p*2].lazy=t[p*2+1].lazy=2;
		t[p*2].sum=t[p*2].lmax=t[p*2].rmax=t[p*2].len;
		t[p*2+1].sum=t[p*2+1].lmax=t[p*2+1].rmax=t[p*2+1].len;
    //这一段房间全部是空的
	}
	t[p].lazy=0;//懒标记清零
}
```
更新节点信息：
```cpp
void renew(int p)
{
	if(t[p*2].sum==t[p*2].len)//左区间全为空房 
	 t[p].lmax=t[p*2].len+t[p*2+1].lmax;
    //那么左区间全部可住，在加上右区间从左开始的最长区间
	else t[p].lmax=t[p*2].lmax;
    //否则父节点的lmax等于左区间的lmax
	if(t[p*2+1].sum==t[p*2+1].len)//右区间全为空房，同理
	 t[p].rmax=t[p*2+1].len+t[p*2].rmax; 
	else t[p].rmax=t[p*2+1].rmax;
	t[p].sum=max(max(t[p*2].sum,t[p*2+1].sum),t[p*2].rmax+t[p*2+1].lmax);
    //p节点的sum有三种：全在左边的，全在右边的，跨越左右区间的，取个max就好了
} 
```
现在线段树的基本操作已经完成，再看题，题目要求我们在线段树上支持两种操作：区间修改，查询max(sum)的左端点

区间修改（修改分两种：退房和开房）：
```cpp
void change(int p,int l,int r,int tag,int L,int R)
//tag=1代表没人住，tag=2代表有人住，[L,R]是要修改的区间 
{
	spread(p);//下放懒标记
	if(L<=l&&r<=R){//如果要修改的区间完全覆盖了当前节点所代表的区间 
    	if(tag==1)t[p].sum=t[p].lmax=t[p].rmax=0;
    //如果要开房，这一段房间全部不可用
		else t[p].sum=t[p].lmax=t[p].rmax=t[p].len; 
    //如果要退房，这一段区间全部可用
		t[p].lazy=tag;//更新懒标记
		return;
	}
	int mid=(l+r)/2;
	if(L<=mid)change(p*2,l,mid,tag,L,R);
	if(R>mid)change(p*2+1,mid+1,r,tag,L,R);
    //修改左右儿子
	renew(p);//更新节点信息
}
```
查询：
```cpp
int ask(int p,int l,int r,int length)
{
	spread(p);//下放懒标记
	if(l==r)return l;//如果找到对应区间，返回左端点
	int mid=(l+r)/2;
	if(t[p*2].sum>=length)return ask(p*2,l,mid,length);
    //如果左区间即可找到足够多的房间，就在左区间找
	if(t[p*2].rmax+t[p*2+1].lmax>=length)return mid-t[p*2].rmax+1;
    //如果在中间能找到足够多的房间，答案就是左区间从右开始的最长连续区间的左端点
	else return ask(p*2+1,mid+1,r,length);
    //否则就在右边找
}
```
最后的主函数：
```cpp
int main()
{
	n=read();m=read();
	build(1,1,n);//建树
	for(int i=1;i<=m;i++) 
	{
		int act,x,y;
		act=read();
		if(act==1){
			x=read();
			if(t[1].sum>=x){
        //如果存在这么长的区间才找
				int left=ask(1,1,n,x);
				printf("%d\n",left);
				change(1,1,n,1,left,left+x-1);
                //找到之后记得修改
			}
			else printf("0\n");//否则找不到
		}
		else{
			x=read();y=read();
			change(1,1,n,2,x,x+y-1);//退房	
		}
	}
	return 0;
} 
```