# SP9722 题解

在肝掉这题之间，了解**归并排序**是必不可少的了。

那么，什么是归并排序？

归并排序是利用**二分法**来实现的一种排序算法，主要是将一组数平均分开到不能分的时候，在合并过程中进行排序的一种排序算法。它的时间复杂度为$O(n\ log\ n)$。

下面一张图证明了一切（图片来自网络）：

![](https://cdn.luogu.com.cn/upload/image_hosting/tdwnbw5c.png)

那么，究竟怎样才能把两个序列合并呢？

通过图片可以发现，每次合并两个序列时，它们**本身**都是排好序的。那么合并序列中最小的数一定是两个序列的第一个数较小的那个，第二个数就是剩下的数中最小的······以此类推。

那么，我们就可以艰（yu）难（kuai）地打出代码了：

```cpp
#include<bits/stdc++.h>
using namespace std;
int t,n,a[500001],c[500001];
long long sum;
void msort(int x,int y)
{
    if(x==y) return;//不用排序的情况
    int mid=(x+y)/2,i=x,j=mid+1,k=x;
    msort(x,mid);//二分
    msort(mid+1,y);
    while(i<=mid&&j<=y){
    	if(a[i]<=a[j]) c[k++]=a[i++];
        else c[k++]=a[j++],sum+=mid-i+1;//求逆序对最关键的一步
	}
    while(i<=mid)//合并序列
    c[k++]=a[i++];
    while(j<=y)
    c[k++]=a[j++];
    for(int l=x;l<=y;l++)//存回原来的数组
    a[l]=c[l];
} 
int main()
{
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
    	for(int j=1;j<=n;j++)
    	cin>>a[j];
    	memset(c,0,sizeof(c));//一定要清零！一定要清零！！一定要清零！！！（重要的事情说三遍）
    	sum=0;
    	msort(1,n);
    	cout<<sum<<endl;
	}
    return 0;
}
```

只求两字：

### 过和赞