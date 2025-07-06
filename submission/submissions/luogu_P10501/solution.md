# P10501 题解

前置芝士：[SG 函数](https://zhuanlan.zhihu.com/p/562117547)。

---

分讨写不出来，还是老老实实用 SG 函数做吧。

要两次判断，一次考虑剪长，一次考虑剪宽，剪完后递归求解子局面，结果异或后记录，对记录下来的求 $\operatorname{mex}$ 得出即可得出函数值。

注意不可以剪出一边为 $1$，不然对手直接能赢，所以循环边界条件要注意。

代码：

```cpp
#include<bits/stdc++.h>
#define int long long
using namespace std;
int sg[205][205];
int SG(int n,int m){
	if(sg[n][m]!=-1)return sg[n][m];
	int f[205]={};
	for(int i=2;i<=n-2;i++)f[SG(i,m)^SG(n-i,m)]=1;
	for(int i=2;i<=m-2;i++)f[SG(n,i)^SG(n,m-i)]=1;
  	//注意边界
	for(int i=0;i<=200;i++)
	if(!f[i])return sg[n][m]=i;
}
signed main(){
	memset(sg,-1,sizeof sg);
	int n,m;
	while(cin>>n>>m)
	puts(SG(n,m)?"WIN":"LOSE");
	return 0;
}
//最优解 = 打表
//:-(
```

---

瑞平：写分讨写出 $21$ 次[提交](https://www.luogu.com.cn/record/list?pid=P10501&user=754021)，怒挂 $17$ 发，挤占大量评测姬资源，谴责。