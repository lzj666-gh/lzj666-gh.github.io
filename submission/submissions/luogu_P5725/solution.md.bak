# P5725 题解

Update:之前过审过后由于文章转移博客链接没了，现在重交。真的麻烦管理了，特此说明QAQ。

A掉这道题后，我第一次惊叹地说出了：

**我谔谔**。

咳咳，进入正题了。

[原题传送门](https://www.luogu.com.cn/problem/P5725)。
[在窝的博客中食用更佳](https://www.luogu.com.cn/blog/MZY666/solution-p5725)。

### 【 题意概括 】

观察样例，根据输入输出不同的正方形和三角形矩阵。

没错，就这样。

### 【 思路 】

要一步一步来。

令输入为 $n$ 。

在正方形中，对于第 $i$ 行的第 $j$ 个数，这个数的值为 $(i-1) \times n+j$.

在三角形矩阵中，先令 $where=1$.

当 $n-j<i$ 时，此处输出 $where$ 的值，随后 $where$ 值 $+1$.

否则，此处用空格补齐。

记得每一个数都要补零哦。

好的，下面进入代码环节。

### 【 代码实现 + 注释 】

```cpp
#include<bits/stdc++.h>//万能头文件好 
using namespace std;
int main(){
	int n,i,j,wei=0,weii,where;
	scanf("%d",&n);//输入n
	//wei表示n*n的位数，weii表示当前数的位数（好补零）
	while(pow(10,wei)<=n*n)wei++;//算出n*n的位数
	if(n==0)return 0;//特判 
//	printf("%d",wei);//测试用 
	//下面进入正方形的输出
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			weii=0;//初始化为0
			while(pow(10,weii)<=n*(i-1)+j)weii++;//算当前数的位数
			while(weii<wei){
				printf("0");
				weii++;
			}//补零
			printf("%d",n*(i-1)+j);//输出该数
		}
		printf("\n");//记得换行
	}
	//下面进入三角形的矩阵的输出
	printf("\n");//记得换行
	where=1;//初始化，第一个数为1
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			weii=0;//初始化为0
			while(pow(10,weii)<=where)weii++;//同理，算当前数的位数
			if(n-j<i){//如果这个数应该输出来
				while(weii<wei){
					printf("0");
					weii++;
				}
				printf("%d",where);
				where++;//记得加1
			}//同上理
			else{//否则
				weii=0;//把这个数当成0位
				while(weii<wei){
					printf(" ");
					weii++;
				}//输出空格
			}
		}
		printf("\n");//记得换行
	}
	return 0;//over~
}
```

打完后暗想：这是不是该一道橙题把（指码量）

结果 [WA$ \times 2$](https://www.luogu.com.cn/record/31839826)。QAQ

无奈之下看了看别人的题解。我谔谔！竟然说只要小于 $10$ 直接补一个 $0$ ！

这不是我的错了好伐，这是没给数据范围的锅（强行甩锅）QWQ.

那咱们直接把 $n \times n$ 的位数改成 $2$ 不就好了嘛。

最后附上最终AC代码：

```cpp
#include<bits/stdc++.h>//万能头文件好 
using namespace std;
int main(){
	int n,i,j,wei=0,weii,where;
	scanf("%d",&n);
	
//	while(pow(10,wei)<=n*n)wei++;
	wei=2;//唯一不同的地方就是这两行
	if(n==0)return 0;//特判 
//	printf("%d",wei);//测试用 
	
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			weii=0;
			while(pow(10,weii)<=n*(i-1)+j)weii++;
			while(weii<wei){
				printf("0");
				weii++;
			}
			printf("%d",n*(i-1)+j);
		}
		printf("\n");
	}
	
	printf("\n");
	where=1;
	for(i=1;i<=n;i++){
		for(j=1;j<=n;j++){
			weii=0;
			while(pow(10,weii)<=where)weii++;
			if(n-j<i){
				while(weii<wei){
					printf("0");
					weii++;
				}
				printf("%d",where);
				where++;
			}
			else{
				weii=0;
				while(weii<wei){
					printf(" ");
					weii++;
				}
			}
		}
		printf("\n");
	}
	return 0;
}
```
然而尴尬的是，当我把这份题解写完后数据范围才加了上去
QAQ。（不过好像还是没说超过10就补0？

对了，如果有建议请私信，作者自愿禁言了。否则将**无法**回复您哦！

完结撒花~（疯狂暗示 AWA.