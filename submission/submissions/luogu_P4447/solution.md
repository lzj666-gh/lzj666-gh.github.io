# P4447 题解

也许是一种奇妙的思路？

------------

我们用类似条形统计图的方式，在数轴上统计各个实力值出现的次数。以样例为例：

![](https://cdn.luogu.com.cn/upload/image_hosting/npj29mfq.png)

题目中的“分组”，就可以理解为在方格中画线——被同一条线相连的方格所对应的同学被分为一组。如：

![](https://cdn.luogu.com.cn/upload/image_hosting/z0820dmk.png)

再演示一个稍微复杂一点的图（删去了数轴）：

![](https://cdn.luogu.com.cn/upload/image_hosting/opl91ep2.png)

也许这样不是特别直观？我们规定，删除被画过线的方格，且总是在最下方一行画线：

![](https://cdn.luogu.com.cn/upload/image_hosting/vd33dlmw.png)

为方便表述，定义一条线所连接的方格数为这条线的长度，某一列当前的方块数为这一列的高度。

至此，“分组”问题被转化成了一个“俄罗斯方块”式的问题。接下来，我们要研究如何使人数最少的组别人数最大——也就是如何使长度最短的线长度最大。

------------

不妨令每一次画线都从最左边一列开始。

每次都画到底，可以吗？

显然，大多数情况下这不是最优解。最后可能会剩下一个方块“一枝独秀”：

![](https://cdn.luogu.com.cn/upload/image_hosting/a3r2wuiw.png)

出现这种情况的根本原因是什么？我们发现，“一枝独秀”的方块总是出现在高度较高的几列。

如何解决？我们需要改变画线的方式：

**如果右边一列的高度不低于当前列，则连接右边一列最下方的方块。反之，停止画线。**

这样，最靠左的一个“峰”相较其右边一列的高度差就不断减小，直到相同。如此反复。记录所画所有线的最短长度，即为答案。

------------

可以用 `std::map` 关键字自动排序的特性来记录图形。

时间复杂度 $O(n\log n)$。

参考代码：

```
#include<cstdio>
#include<map>
std::map<int,int>m;
typedef std::map<int,int>::iterator it;
int main(){
	int n,ans=0x3f3f3f3f;
	scanf("%d",&n);
	for(int i=0;i<n;++i){
		int t;
		scanf("%d",&t);
		++m[t];
		//记录图像。
	}
	while(!m.empty()){
		it i=m.begin(),j=m.begin();
		--(*i).second;
		int t=1;
		for(++j;j!=m.end()&&(*j).first==(*i).first+1&&(*j).second>(*i).second;++i,++j){
   			++t;
			--(*j).second;
		}
		//若 i,j 所对应的能力值是连续的，且 i 对应的那一列高度不高于 j，则继续画线。
		i=m.begin();
		while(i!=m.end()&&(*i).second==0){
			m.erase((*i++).first);
		}
		//高度降为 0 后直接删除，便于计算。
		if(t<ans){
			ans=t;
		}
		//记录答案。
	}
	printf("%d",ans);
	return 0;
}
```