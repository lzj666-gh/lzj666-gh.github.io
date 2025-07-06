# P4643 题解

## 这道题之所以评价颇高，是因为思路不好得出。

#### zhx巨神告诉我们，边的权值可以均分到两个端点上。简单总结了一下他的证明：

我们先画一条边：

A --------------- C --------------- B

其中C表示边，A，B，为两个端点。设边的权值为c，A点权值为a，B点权值为B。

因为这道题要求的是桃子的得分和阿狸的的分之差，记得分之差为ans（我也不知道为什么），而A，B分别被谁染色，有四种情况：

1.桃子染色A,阿狸染色B,由题意c可以忽略，
    $ans=a-b$ ，而如果把c平分到a,b中,
    $ans=(a+c/2)-(b+c/2)=a-b$ ,相等。
    
2.桃子染色B,阿狸染色A,同上c可以忽略，
    $ans=b-a$ ，而如果把c平分到a,b中,
    $ans=(b+c/2)-(a+c/2)=b-a$ ,同样相等。
    
3.桃子染色A，B，
    由题意，c全部给桃子，
    $ans=a+b+c$ ，而如果把c平分到a,b中,
    $ans=(b+c/2)+(a+c/2)=a+b+c$ ,还是相等。

4.阿里染色A，B，
    由题意，c全部给阿狸，
    $ans=-(a+b+c)=-a-b-c$ ，而如果把c平分到a,b中,
    $ans=-[(b+c/2)+(a+c/2)]=-a-b-c$ ,依然相等。
    
   证毕。
    
   所以我们对边的权值的处理是合理的。

####     代码如下：

    
    #include<cstdio>
    #include<algorithm>
    using namespace std;
    int n,m,x,y,ans,sum,k,z,a[10001];
    int main(){
    	scanf("%d%d",&n,&m);
    	for(int i=1;i<=n;i++){
        		scanf("%d",&k);
        		a[i]=k<<1;
    	}
    	for(int j=1;j<=m;j++){
        		scanf("%d%d%d",&x,&y,&z);
        		a[x]+=z;a[y]+=z;
    	}
    	sort(a+1,a+1+n);
    	for(int i=n;i>=1;i-=2)
        		ans+=a[i]-a[i-1];
    	printf("%d",ans/2);
    	return 0;
    }