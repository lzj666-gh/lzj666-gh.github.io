# P1081 题解

为了通过[提高试炼场](https://www.luogu.com.cn/paste/c6a97wup)的倍增关，被迫做紫题/kel……（[yrz菜菜……](https://www.luogu.com.cn/paste/jsj7y3zb)）

（特别鸣谢：本题解由《算法竞赛进阶指南》赞助播出，《算法竞赛进阶指南》，一本你值得拥有的算法好书！）

刚才一不小心把这个题的方法暴露了呢……没错，这个题的main idea就是：**倍增**！

倍增，字面意思就是“**成倍增长**”，也许你听说过在国际象棋棋盘上摆放麦粒的故事，体验了指数函数爆炸级别的恐怖，也在[快速幂](https://www.luogu.com.cn/problem/P1226)，[ST表](https://www.luogu.com.cn/problem/P3865)和[最近公共祖先LCA](https://www.luogu.com.cn/problem/P3379)中领略到这些高效的算法的神奇

没错，上面的东西都是倍增思想的具体体现

那这个题到底是怎么跟倍增的技巧扯上关系的呢？？？别急，咱们一步一步来，从分析题目开始！

------------
## Part I
>记城市 $i$ 的海拔高度为$h_i$
 ，城市 $i$ 和城市 $j$ 之间的距离 $d_{i,j}$
  恰好是**这两个城市海拔高度之差的绝对值**，即 $d_{i,j}=|h_i-h_j|$。
  
>小 $\text{B}$ 总是**沿着前进方向**选择一个**最近的城市**作为目的地，而小 $\text{A}$ 总是**沿着前进方向**选择**第二近的城市**作为目的地 。

看来，**小$\text{A}$和小$\text{B}$下次到达的城市**是非常重要的，赶紧把它预处理出来！

也就是说，我们要预处理出在城市$i$的时候，**小$\text{A}$要走的城市$ga_i$**和**小$\text{B}$要走的城市$gb_i$**

$gb_i$就是要找一个$j(i<j\le n)$，使得$|h_i-h_j|$最小，而$ga_i$就是使得$|h_i-h_j|$次小

那怎么预处理呢？？？不难想到，$gb_i$就是**离当前的$i$的高度最接近的城市**，我们先给每个城市按高度排个序，这样的话，排序之后**要求的$gb_i$就是$i-1$和$i+1$中，和$i$的高度差更小的那个**

而$ga_i$就同理啦，根据刚才的思路，$ga_i$肯定是$i-1,i-2,i+1,i+2$其中之一，这四个里面肯定有一个是$gb_i$，再从剩下三个里面找个小的就是$ga_i$了

怎么找的问题解决了，但还有一个重要的事情没考虑——每次必须去往**前进方向**的城市，这该怎么办呢？

咱们先从城市$1$来考虑，毕竟从城市$1$出发，哪个城市都能到嘛！找到排序后城市$1$的位置，然后按照刚才说的比较大小，就可以找到$gb_1$和$ga_1$

那$i=2$的时候呢？

$i=2$时，除了城市$1$是不能走的，其它都能畅通无阻，那要不……我们在处理完$i=1$的情况后把城市$1$删掉？问题不就解决了？

完全没有问题！我们就用这种**弄完一个删一个**的方式，这样就可以保证当前要考虑的城市里只有前进方向的城市，因为当一个城市处理过去之后，它就再也不能到达了

那这波操作具体怎么实现呢？既然**要资瓷频繁的删除操作**，开动脑筋想一想，用**双向链表**是更好不过了（没学过双向链表的同学们可以去 [P1160 队列安排](https://www.luogu.com.cn/problem/P1160)）

接下来，让我们开始愉快地写代码吧！虽然双向链表的实现还是挺基础的，但是**要注意的细节和坑还是挺多的**（要不然我为啥光双向链表就调了一晚上），尤其是要注意**判定当前元素的前驱和后继不存在的情况**

```cpp
struct qwq{//存储城市的结构体
	int hi,id;//hi为城市的海拔高度，id为城市的序号
	int pre,nxt;//pre和next是链表的象征！
}h[100005];
bool cmp(qwq x,qwq y){//排序用的cmp函数
	return x.hi<y.hi;//按高度从小到大排
}
int pos[100005],ga[100005],gb[100005];//pos为城市排序后所在的位置，ga和gb就是我们要求的东西
```
```cpp
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&h[i].hi);//输入就不用说了吧
		h[i].id=i;//城市的编号
	}
	sort(h+1,h+1+n,cmp);//排个序
	for(int i=1;i<=n;i++){
		pos[h[i].id]=i;//把pos数组整出来
		h[i].pre=i-1;//用链表把城市串一串
		h[i].nxt=i+1;
	}
	h[1].pre=h[n].nxt=0;//把头部的前驱和尾部的后继（边界部分）搞成0
	for(int i=1;i<n;i++){
		int p=pos[i],p1=h[p].pre,p2=h[p].nxt;  //把当前的城市以及它的前驱和后继都找出来，方便后续操作                                
		if(p1&&(h[p].hi-h[p1].hi<=h[p2].hi-h[p].hi||!p2))//如果当前城市i到p1的距离比到p2的小，或者干脆没有p2只能选p1（选择p1必须保证p1是存在的，切记注意）      
		gb[i]=h[p1].id,ga[i]=choose(h[p1].pre,p2,p);//那gb就当然选p1啦，ga的话就从那两个里面选（怎么选马上就讲）
		else gb[i]=h[p2].id,ga[i]=choose(p1,h[p2].nxt,p);//否则呢，就反过来，gb选p2，ga从p1和p2的后继中选	
		del(p);//弄完了就把它删掉，反正以后都到不了了
	}
```

  ```cpp
int choose(int a,int b,int i){//当前城市为i，从a与b中选择一个更优的
	if(!a)return h[b].id;//如果其中一个城市没有，那就只能被迫选另一个了
	if(!b)return h[a].id;//俺也一样，注意返回的是id
	if(h[i].hi-h[a].hi<=h[b].hi-h[i].hi)//如果城市i与a的高度差比i与b的小
	return h[a].id;//那就选a咯
	else return h[b].id;//要不就是b
}
void del(int pos){//双向链表基本操作——删除链表中的元素
	if(h[pos].nxt)h[h[pos].nxt].pre=h[pos].pre;//连这个都不会的话可以去双向链表入门题回炉重造了
	if(h[pos].pre)h[h[pos].pre].nxt=h[pos].nxt;//如果实在理解不了的话可以画个图，还是很好理解的
}
```
（话说这一步的实现用STL大法中的**set+迭代器**也珂以实现，（~~据说你甚至可以手写平衡树~~），由于本人写set迭代器屡屡出锅，这里就不给大家展示了）

------------
## Part II
对题目分析的第一步完美结束，我们接着来看：
>1、 对于一个给定的 $x=x_0$	
 ，**从哪一个城市出发**，**小 $\text{A}$ 开车行驶的路程总数**与**小 $ \text{B}$ 行驶的路程总数**的比值最小

>2、对任意给定的 $x=x_i$
  和**出发城市 $s_i$** 
 ，**小 $\text{A}$ 开车行驶的路程总数**以及**小 $\text {B}$ 行驶的路程总数**。
 
我们发现，题目中要求的东西跟**到达的城市**，**小 $\text{A}$ 走的路程**和**小 $\text{B}$ 走的路程**

那怎么搞到这些信息呢？我们只需要知道**出发的城市**和**行驶的天数**，哦对了，还有**轮到谁开车**

那我们就一天一天的开，去模拟开车过程？

别忘了数据范围辣么大，他俩有时候开上十天半个月也开不完，怎么办呢？

反手一个**倍增**，闷声发大财！

为啥用倍增就可以呢？因为通过倍增枚举，是将每次把一个数变成它相应的两倍，也就是说：

$\boxed{\begin{aligned}\text{普通的枚举：}1,2,3,4,5,6,7,8,9,10\cdots \qquad\qquad\qquad\ \ \\
\text{用倍增枚举：}1,2,4,8,16,32,64,128,256,512,1024\cdots\end{aligned}}$

这简直快的不是一点半点啊！

领教到倍增的威力之后，我们来看看接下来怎么做，根据刚才说的，我们是**通过已知条件推出新的状态**，也就是说，这是一个**dp**，或者说是**递推**的过程

>**动态规划**需要考虑三件事：**数组**、**方程**、**初始化**
				
> ——  $\text{v\color{red}ectorwyx}$

首先是考虑**状态定义**的问题，根据刚才推出的关键信息，我们分别要定义三个数组——$f$表示走到的城市，$da$表示小$A$走过的距离，$db$表示小$\text{B}$走过的距离

并且，决定这三者的因素在前面也说过了，我们就用$f_{i,j,k}$表示开车$2^i$天（说好的倍增呐），从城市$j$出发到达的城市，$k=0$表示轮到小$\text{A}$先开车，$k=1$表示轮到小$\text{B}$先开车

同样，$da_{i,j,k}$和$db_{i,j,k}$也是这么定义的！

接下来，咱们来考虑**初始化**的问题：

- 对于$f$数组：

$$f_{0,j,0}=ga_j$$

$$f_{0,j,1}=gb_j$$

（很好理解，$2^0$是$1$，开一天之后到达的就是我们刚才预处理出的$ga$和$gb$）

- 对于$da$数组：

$$da_{0,j,0}=|h_j-h_{ga_j}|$$
（第一次会走到$ga_j$，路程就是它俩的距离）
$$da_{0,j,1}=0$$
（小$\text{B}$压根啥也没走）

- 对于$db$数组：
$$db_{0,j,0}=0$$
$$db_{0,j,1}=|h_j-h_{gb_j}|$$
（和刚才$da$的思路完全一样）

我们再来考虑**状态转移方程**：

其实倍增的状态转移还是比较套路的，无非就是**对“前一半”和“后一半”进行处理**

当然这里还有一个坑点：**特判 $i=1$ 的情况**

为啥呢？咱以$f$数组为例分析一下分析一下

当$i=1$时，$2^i=2$，所以我们要分析前$1$天和后$1$天的情况，这两天是由不同的人开，所以：

$$f_{i,j,k}=f_{i-1,(f_{i-1,j,k}),k \mathrm{xor} 1}(i=1)$$

（$\mathrm{xor}$就是异或啦，用来把$k$变成相反的）

当$i>1$时，$2^{i-1}$是个偶数，所以**前后两段是同一个人开车**，因此：

$$f_{i,j,k}=f_{i-1,(f_{i-1,j,k}),k}(i>1)$$

这样我们就把$f$数组的转移写完了，$da$和$db$可以如法炮制：**行驶的总路程=前半段走的路程+后半段走的路程**

$$da_{i,j,k}=\begin{cases}da_{i-1,j,k}+da_{i-1,({f_{i-1,j-1,k}),k \mathrm{xor} 1}}(i=1)\\da_{i-1,j,k}+da_{i-1,({f_{i-1,j-1,k}),k }}(i>1)\end{cases}$$

$$db_{i,j,k}=\begin{cases}db_{i-1,j,k}+db_{i-1,({f_{i-1,j-1,k}),k \mathrm{xor} 1}}(i=1)\\db_{i-1,j,k}+db_{i-1,({f_{i-1,j-1,k}),k }}(i>1)\end{cases}$$

我们发现，$i=1$的时候，除了$k$要取相反，其它压根没啥区别，所以写代码的时候，特判$i=1$时取反，其它照写就行啦！

```cpp
	int f[25][100005][2];
	long long da[25][100005][2],db[25][100005][2];//十年OI一场空，不开long long见祖宗！
    for(int i=1;i<=n;i++){
		if(ga[i]){//预处理的时候一定要注意只有这个东西存在的时候才能预处理
			f[0][i][0]=ga[i];
			da[0][i][0]=abs(h[pos[i]].hi-h[pos[ga[i]]].hi);//注意我们在前面已经将h数组排好了序，所以别忘了取pos
			db[0][i][0]=0;	
		}
		if(gb[i]){//另一边的初始化对称过来即可
			f[0][i][1]=gb[i];
			da[0][i][1]=0;
			db[0][i][1]=abs(h[pos[i]].hi-h[pos[gb[i]]].hi);
		}	
	}
	t=(int)(log(1.0*n)/log(2)+1);//倍增时只需要枚举到log2n就可以，所以要先把它算出来，用的是对数的换底公式：logab=logcb/logca
	for(int i=1;i<=t;i++){//循环顺序很重要！一定要先枚举天数，再枚举城市，这样才能保证后面要用的东西前面已经推出来了
		for(int j=1;j<=n;j++){
			for(int k=0;k<=1;k++){
				int l=(i==1)?k^1:k;//当k=1时，别忘了取相反
				if(f[i-1][j][k])f[i][j][k]=f[i-1][f[i-1][j][k]][l];//递推f数组
				if(f[i][j][k]){//别忘了必须保证存在
					da[i][j][k]=da[i-1][j][k]+da[i-1][f[i-1][j][k]][l];//按照刚才推出的转移方程递推
					db[i][j][k]=db[i-1][j][k]+db[i-1][f[i-1][j][k]][l];
				}
			}
		}
	}
```


------------
## Part III

该推的都推完啦，我们接下来要考虑的，就是如何用我们推出的东西，得到最终的答案

也就是说，我们的首要任务就是计算出$calc(s,x)$，也就是从城市$s$出发，最多走$x$的距离，小$\text{A}$和小$\text{B}$能走的距离$la$和$lb$

那咋办呢？我们可以借鉴倍增求LCA的思路：**从大到小往上跳**

也就是说：我们**按照$i$从大到小枚举**，如果**走完$2^i$天，总路程还是不超过$x$呢**，那就**走过去，更新$la$和$lb$的答案**

没错，就这么简单，我们来把代码写出来！
```cpp
long long da[25][100005][2],db[25][100005][2],la,lb;//再次提醒：十年OI一场空，不开long long见祖宗！
void calc(int s,long long x){
	la=lb=0;//不要忘了初始化哦！
	int k=0;//k依然表示谁先开车
	for(int i=t;i>=0;i--){//从大往小枚举，看看能不能跳
		if(f[i][s][k]&&da[i][s][k]+db[i][s][k]<=x){//如果当前城市存在，并且走完这些天还是超不过x
			x-=da[i][s][k]+db[i][s][k];//剩余路程减去走了的路程
			la+=da[i][s][k],lb+=db[i][s][k];//把新走的路程加到统计的答案里去
			if(!i)k^=1;//别忘了i=0的时候依然要取相反
			s=f[i][s][k];//跳的终点的城市里去
		}
	}
}
```
回到题目，第一问就是要求出对于给定的$x$，从哪个$s$出发，$la$和$lb$的比值最小，而第二问呢，实际上就是让你计算$calc(s,x)$时$la$和$lb$的值

```cpp
	long long x;
	int s;
	scanf("%lld",&x);//第一问：找到一个s使la:lb最小
	int p=0;//p代表最后找到的城市s
	long long ansa=1,ansb=0;//ansa和ansb是找到的比值最小的la和lb
	for(int i=1;i<=n;i++){//枚举每个城市
		calc(i,x);//计算出小A和小B的路程
		if(!lb)la=1;//题目要求：如果lb为0，那就变成1
		if(la*ansb<lb*ansa||(la*ansb==lb*ansa&&h[pos[i]].hi>h[pos[p]].hi))//由于比例的分数算除法会产生玄学的精度问题，所以我们把它换成乘积的形式，除此以外，比值相等时选择高度较高的一个
		ansa=la,ansb=lb,p=i;//更新答案
	} 
	printf("%d\n",p);//找到答案输出
	int m;
	scanf("%d",&m);
	while(m--){
		scanf("%d%lld",&s,&x);
		calc(s,x);//直接计算calc(s,x)就行
		printf("%lld %lld\n",la,lb);
	}
	return 0;
```


------------
## Part IV

上完整代码：
```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
struct qwq{//存储城市的结构体以及cmp
	int hi,id,pre,nxt;
}h[100005];
bool cmp(qwq x,qwq y){
	return x.hi<y.hi;
}
int choose(int a,int b,int i){//选择更优解
	if(!a)return h[b].id;
	if(!b)return h[a].id;
	if(h[i].hi-h[a].hi<=h[b].hi-h[i].hi)
	return h[a].id;
	else return h[b].id;
}
void del(int pos){//删除链表元素
	if(h[pos].nxt)h[h[pos].nxt].pre=h[pos].pre;
	if(h[pos].pre)h[h[pos].pre].nxt=h[pos].nxt;
}
int n,t;
int pos[100005],ga[100005],gb[100005];//一堆变量
int f[25][100005][2];
long long da[25][100005][2],db[25][100005][2],la,lb;
void calc(int s,long long x){//calc函数
	la=lb=0;
	int k=0;
	for(int i=t;i>=0;i--){
		if(f[i][s][k]&&da[i][s][k]+db[i][s][k]<=x){
			x-=da[i][s][k]+db[i][s][k];
			la+=da[i][s][k],lb+=db[i][s][k];
			if(!i)k^=1;
			s=f[i][s][k];
		}
	}
}
int main(){
//Part I——预处理ga和gb                                                   
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%d",&h[i].hi);
		h[i].id=i;
	}
	sort(h+1,h+1+n,cmp);
	for(int i=1;i<=n;i++){
		pos[h[i].id]=i;
		h[i].pre=i-1;
		h[i].nxt=i+1;
	}
	h[1].pre=h[n].nxt=0;
	for(int i=1;i<n;i++){
		int p=pos[i],p1=h[p].pre,p2=h[p].nxt;                                  
		if(p1&&(h[p].hi-h[p1].hi<=h[p2].hi-h[p].hi||!p2))      
		gb[i]=h[p1].id,ga[i]=choose(h[p1].pre,p2,p);
		else gb[i]=h[p2].id,ga[i]=choose(p1,h[p2].nxt,p);	
		del(p);
	}
//Part II——用倍增推出f,da,db                                                         
	for(int i=1;i<=n;i++){
		if(ga[i]){
			f[0][i][0]=ga[i];
			da[0][i][0]=abs(h[pos[i]].hi-h[pos[ga[i]]].hi);
			db[0][i][0]=0;	
		}
		if(gb[i]){
			f[0][i][1]=gb[i];
			da[0][i][1]=0;
			db[0][i][1]=abs(h[pos[i]].hi-h[pos[gb[i]]].hi);
		}	
	}
	t=(int)(log(1.0*n)/log(2)+1);
	for(int i=1;i<=t;i++){
		for(int j=1;j<=n;j++){
			for(int k=0;k<=1;k++){
				int l=(i==1)?k^1:k;
				if(f[i-1][j][k])f[i][j][k]=f[i-1][f[i-1][j][k]][l];
				if(f[i][j][k]){
					da[i][j][k]=da[i-1][j][k]+da[i-1][f[i-1][j][k]][l];
					db[i][j][k]=db[i-1][j][k]+db[i-1][f[i-1][j][k]][l];
				}
			}
		}
	}
// Part III——计算calc得到答案                                  
	long long x;
	int s;
	scanf("%lld",&x);
	int p=0;
	long long ansa=1,ansb=0;
	for(int i=1;i<=n;i++){
		calc(i,x);
		if(!lb)la=1;
		if(la*ansb<lb*ansa||(la*ansb==lb*ansa&&h[pos[i]].hi>h[pos[p]].hi))
		ansa=la,ansb=lb,p=i;
	} 
	printf("%d\n",p);
	int m;
	scanf("%d",&m);
	while(m--){
		scanf("%d%lld",&s,&x);
		calc(s,x);
		printf("%lld %lld\n",la,lb);
	}
	return 0;
}
```
$\color{#4275f5}{\text{yrz 是小珂愛！！！}}$