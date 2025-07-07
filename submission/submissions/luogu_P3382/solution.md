# P3382 题解

### 粒子群优化（Particle Swarm Optimization,PSO），又称微粒群算法

#### 其重要的迭代用的公式是这条:


## $v_i=v_i×w+c×rand()×(pbest_i+gbest- 2×x_i)$


其中：

$v_i$是速度

$w$是惯性因子((0,1)的实数)，和学习因子相反，就是该粒子原来的速度的 **参考权重** 。比如我的这个程序里取的是0.5，而据说从大到小衰减会更好。因为大的时候会重视每个**个体的价值**，可以更全面的寻找可行解，而越趋于0就越注重**社会的价值**就是所有粒子中的最优解。

$C$是学习因子也就是权重一般取$2$。

我们可以通过这个速度向量来更新位置。

$ b[a].x += b[a].v; $

#### 原理

_PSO算法是基于群体的，根据对环境的适应度将群体中的个体移动到好的区域。然而它不对个体使用演化算子，而是将每个个体看作是D维搜索空间中的一个没有体积的微粒（点），在搜索空间中以一定的速度飞行，这个速度根据它本身的飞行经验和同伴的飞行经验来动态调整。第i个微粒表示为Xi= （xi1, xi2, …, xiD），它经历过的最好位置（有最好的适应值）记为Pi= （pi1, pi2, …, piD），也称为pbest。在群体所有微粒经历过的最好位置的索引号用符号g表示，即Pg，也称为gbest。微粒i的速度用Vi= （vi1, vi2, …, viD）表示。
_

引用自[百度百科](https://baike.baidu.com/item/%E7%B2%92%E5%AD%90%E7%BE%A4%E4%BC%98%E5%8C%96/1352052?fr=aladdin)

#### 粒子群优化算法流程图：

![](https://s2.ax1x.com/2019/02/14/kBtFJA.png)

#### 所以

对于这道题目我们先初始化他个$ 100 $个粒子，随机地在$ \begin{bmatrix}l,r\end{bmatrix} $区间里取x值，接着计算一下这个值对应的函数值且记录一下全局最优（更新时要用到）。

然后通过公式迭代他个$ 100 $次。

那就可以得到答案了。

#### 一些更详细的内容都写在了代码里了。

```cpp
#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
using namespace std;
const int cnt=100;
int n;
double xs[15];//系数
double l,r;//x的范围
double f(double x) {//计算函数值
	double y = 0;
	for (int i=n+1; i>=1; i--) {
		y+=xs[n-i+2]*pow(x,i-1);
	}
	return y;
}
double Rand() {
	return (double)rand()/RAND_MAX;//返回一个[0,1]的随机实数
}
struct node {
	double xv,x,y,besty,bestx;
} b[105];
//xv是速度向量，x是位置，y是当前位置的函数值，besty是该粒子历史最优值，bestx是该粒子历史最优值时的x的值 

double by=-1e233,bx;
//by是全局当前最优值，bbx是取到全局最优值时的自变量x

void update(int a) {
	//更新速度向量
	//速度向量  惯性                 全局最优 局部最优  当前位置
	b[a].xv=b[a].xv*0.5+Rand()*2*(bx+b[a].bestx-b[a].x*2);//更新公式

	//通过速度向量更新位置
	b[a].x+=b[a].xv;

	//位置出界处理	       速度向量方向反转
	if (b[a].x<l) b[a].x=l,b[a].xv=b[a].xv*-1;
	if (b[a].x>r) b[a].x=r,b[a].xv=b[a].xv*-1;

	b[a].y=f(b[a].x);     //计算当前位置函数值
	if (b[a].y>b[a].besty) { //更新局部最优解
		b[a].bestx=b[a].x;
		b[a].besty=b[a].y;
	}
}

int main() {
	scanf("%d%lf%lf",&n,&l,&r);
	for (int i=1; i<=n+1; i++) {
		scanf("%lf",&xs[i]);//读入系数 
	}
	srand(xs[1]+xs[n]);
	//生成粒子
	for (int i=1; i<=cnt; i++) {
		//xv是速度向量，x是位置，y是当前位置的函数值，besty是该粒子历史最优值，bestx是该粒子历史最优值时的x的值 
		b[i].x=b[i].bestx=l+Rand()*(r-l);//初始x的值 为 l~r 的一个实数 
		b[i].xv=0;		//速度向量初始化为0
		b[i].y=b[i].besty=f(b[i].x);	//计算当前函数值
		if (by<b[i].y) { //若当前函数值优于全局最优函数值则更新全局最优
			bx=b[i].bestx;
			by=b[i].besty;
		}
	}
	//开始迭代
	for (int k=1; k<=100; k++) {
		for (int i=1; i<=cnt; i++) {
			//对每个粒子速度和位置更新
			update(i);
			if (by<b[i].besty) {
				//更新全局最优解
				bx=b[i].bestx;
				by=b[i].besty;
			}
		}
	}
	printf("%.5lf\n",bx);//全局最优的x的值即为答案
	return 0;
}
```

点个赞再走吧。