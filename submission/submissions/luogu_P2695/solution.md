# P2695 题解

**这题一看就是标准的贪心！！！将恶龙头的大小与骑士可以杀死的头的大小排序，然后一通乱搞**

**~~注意：you died!要感叹号，本人在此卡了半天。。。~~**
```cpp
#include <stdio.h>
#include <algorithm>//sort头
using namespace std;
inline int read () {//快读
	register int k=0;
	register char c=getchar();
	while (c<'0'||c>'9') c=getchar();
	while (c>='0'&&c<='9') {k=k*10+c-'0';c=getchar();}
	return k;//返回读入的值
}
int main () {
	register int qs[20010],el[20010],m,n,i,ans=0;
	n=read();
	m=read();
	for (i=1;i<=n;i++) el[i]=read();//读入，不必多说
	for (i=1;i<=m;i++) qs[i]=read();
	sort (el+1,el+1+n);//排序
	sort (qs+1,qs+1+m);//排序
	if (n>m) {//如果恶龙数大于骑士的数量，则输出you died!
		printf ("you died!");
		return 0;
	}
	int j=1;
	for (i=1;i<=n;i++) {//枚举答案
		while (el[i]>qs[j]) j++;//找到最小一个大于该头的骑士
		ans+=qs[j];//累加答案
		if (j>m) break;
		j++;
	}
	if (i-1!=n) 
		printf ("you died!");//输出答案
	else
		printf ("%d\n",ans);
	return 0;//好轻松的呢！！！
}
```
谢谢观看，看我这辛苦，总得给个赞再走吧-_-