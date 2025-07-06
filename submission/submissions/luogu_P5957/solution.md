# P5957 题解

-   _Solution 1:_

 	对每个横坐标进行搜索（上/下）。
    
 	时间复杂度：$O(2^X)$
    
-   _Solution 2:_
	
	$DP$：令 $f_{i,j}$ 表示飞到点 $\left({i,j}\right) $ 最少需要点击屏幕的次数。
    
    根据飞行规则，点 $\left({i,j}\right) $ 可能且仅可能在点 $\left({i-1,j+1}\right) $ 时不点击屏幕和在点 $\left({i-1,j-1}\right) $ 点击屏幕抵达，即可得：
    
    状态转移方程：$f_{i,j}= min\left\{f_{i-1,j+1},f_{i-1,j-1}+1\right\} $ 
    
 	时间复杂度：$O(kX),k$ 为选取的 $j$ 的上界。

-   _Solution 3:_

	设$x$为上升的次数（即点击屏幕的次数），$y$为下降的次数，则从起点到到点$\left({a,b}\right)$时，满足
    
    $\begin{cases}x+y=a\\x-y=b\end{cases}$
    
    故有 $x=\dfrac{a+b}{2}$
    
    所以只需求出 $x=x_n$ 时，纵坐标的最小值。
    
    考虑记录当前可走区间的端点。
    
    由 $x=\dfrac{a+b}{2}$ 可得
    
    $\triangle x=\dfrac{\triangle a+\triangle b}{2}$
    
    即可得可走区间中的点必须和端点的奇偶性相同。
    
    转移：最低点 $l$ 一直不跳，最高点 $r$ 一直跳，新区间与可通行范围（障碍物）的交集即为新的可走区间。
    
    每次转移从一根障碍物，跳到相邻的另一根障碍物，为 $O(1)$ ,共 $n$ 次。
    
    时间复杂度：$O(n)$
#  **代码**
```
#include<bits/stdc++.h>
using namespace std;
int x,a,b,l,r,ll,n,X;
int main()
{
	scanf("%d%d",&n,&X);
	for(int i=1;i<=n;i++)
	{
		scanf("%d%d%d",&x,&a,&b);
		if (r+(x-ll)>=b)r=(r-(x-ll)-b)&1?b-1:b-2;
		else r+=(x-ll);
		if (l-(x-ll)<=a)l=(a-l+(x-ll))&1?a+1:a+2;
		else l-=(x-ll);
		if(r<l){cout<<"NIE";return 0;}
		else ll=x;
	}
	cout<<((x+l)>>1);
}
```

