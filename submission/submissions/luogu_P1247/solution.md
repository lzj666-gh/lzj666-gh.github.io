# P1247 题解

感觉题解的证明都不是很详细啊。。。。。。那本蒟蒻来发一下从网上+自己理解的证明吧。

设$(a,b,c)$为三堆石子的个数$(a>=0,b>=0,c>=0)$，先手为 甲；后手为乙。

必败局势，一般称为奇异局势，显然$(0,0,0)$是一个奇异局势（因为谁面对这种局势，都无法做到游戏给出的条件：每次最少取一个）

讨论局势是必败还是必胜，都是相对于首先面对此局势者来说。因此站在甲的角度来讨论。甲面对$(0,0,0)$必输。

当甲面对$(a,a,0)$，甲每次拿$x$，乙随后也跟着拿$x$，因此甲面对的局势始终是$(a-x,a-x,0)$。因此转化为甲最终都会面对$(0,0,0)$，因此甲必输。

因为游戏是两个人交替进行。由此可得，如果局势（a,b,c）是必胜局势，那么甲就有策略，使得拿走某堆中的$x$个物品后，一般地设为$(a-x,b,c)=(a',b,c)$。此时$(a',b,c)$就是一个必败的局面。反之，必败的局面可以变为必胜的局面。

更一般地，考虑$N>=2$堆石子的情况。每堆数量为$(a_1,a_2,...,a_N)$ 

定理：$(a_1,a_2,...,a_N)$为奇异局势当且仅当$a_1\oplus a_2\oplus ...\oplus a_N=0$   

证明：$(a_1,a_2,...,a_N)=(0,0,...0)$时显然成立。

当$(a_1,a_2,...,a_N)$不为$(0,0,...0)$时，若$a_1\oplus a_2\oplus ...\oplus a_N=k\neq0$   ，显然$k$的最高位为$1$。

则一定存在一个$a_i(1<=i<=N)$，它在$k$的最高位的值为$1$。（若$a_1,a_2,...,a_N$在$k$的最高位处都为$0$，那么异或运算规则，不可能得到$k$的最高位为$1$）

因此，$a_i\oplus k<a_i$（因为最高位变为$0$了）

设$a_{i'}=a_i\oplus k$，则$a_1\oplus a_2 \oplus...\oplus a_{i'}...\oplus a_N=a_1\oplus a_2\oplus ...\oplus a_N \oplus k$ (代入$a_{i'}=a_i\oplus k$，并由异或的交换律得到)      $=k\oplus k=0$

因此当$a_1\oplus a_2\oplus ...\oplus a_N=k\neq0$时，存在移动$a_i->a_{i'}$ （即$a_i-a_{i'}>0$）使得$a_1\oplus a_2 \oplus...\oplus a_i...\oplus a_N=0$

若$a_1\oplus a_2 \oplus...\oplus a_i...\oplus a_N=0$，则不存在合法移动，使得$a_1\oplus a_2 \oplus...\oplus a_{i'}...\oplus a_N=0$。

因为若$a_1\oplus a_2 \oplus...\oplus a_{i'}...\oplus a_N=a_1\oplus a_2 \oplus...\oplus a_{i'}...\oplus a_N=0$，则两边同时异或$a_1$,可得$a_2\oplus ...a_i\oplus ...\oplus a_N=a_2\oplus ...a_{i'}\oplus ...\oplus a_N$，
继续两边异或$a_3...a_N$(除了共有的$a_i,a_{i'}$)，由此可推出$a_i=a_{i'}$。显然这不是合法的移动。

由以上证明得出

- $a_1\oplus a_2\oplus ...\oplus a_N=k\neq0$，一定存在一步特定移动使得$a_1\oplus a_2\oplus ...\oplus a_N=0$；

- $a_1\oplus a_2 \oplus...\oplus a_i...\oplus a_N=0$，不存在一步合法移动使得$a_1\oplus a_2 \oplus...\oplus a_{i'}...\oplus a_N$再次为$0$，       
- 当$a_1\oplus a_2 \oplus...\oplus a_i...\oplus a_N=0$时，下一步必然为$a_1\oplus a_2 \oplus...\oplus a_{i'}...\oplus a_N\neq0$，再下一步可以变为$a_1\oplus a_2 \oplus...\oplus a_{i''}...\oplus a_N=0$。

必要性：由$(a_1,a_2,...,a_N)$为奇异局势（必败局势），考虑甲先乙后。

假设$a_1\oplus a_2 \oplus...\oplus a_i...\oplus a_N\neq0$,那么甲通过移动，可使$a_1\oplus a_2 \oplus...\oplus a_{i'}...\oplus a_N=0$。如此一直下去，每次乙都只能面对$a_1\oplus a_2\oplus ... a_i\oplus ...\oplus a_N=0$的局势。

由于游戏的结束点必然为$(0,0,...0)$，因此乙最终将面对$(0,0,0)$。在乙面对$(0,0,0)$的上一步，设为$(b_1,...b_N)$,此时$b_1\oplus ... \oplus b_N\neq0$。

但乙最终先面对了$(0,0,...0)$，显然是甲胜，这与$(a_1,a_2,...,a_N)$为奇异局势（必败局势，甲必败）矛盾。

因此必有$a_1\oplus a_2 \oplus...\oplus a_i...\oplus a_N=0$。

充分性：由$a_1\oplus a_2\oplus ...\oplus a_N=0$ ，由上，乙始终有办法让甲面对的局势始终是$x_1\oplus x_2\oplus ...\oplus x_N=0$。因此甲最终面对的必然是$(0,0,...0)$的局势，而$(0,0,...0)$就是个奇异局势。

证毕。

理解了奇异局势的判定后，这道题就很好做了。代码也超级简单。

```c++
#include <cstdio>

int n;
int a[500005];

int main()
{
    scanf("%d",&n);
    int check=0;
    for(int i=1; i<=n; i++)
    {
        scanf("%d",&a[i]);
        check^=a[i];
    }
    if(!check)
    {
        printf("lose\n");
        return 0;
    }
    for(int i=1; i<=n; i++)
    {
        if((check^a[i])<a[i])
        {
            printf("%d %d\n",a[i]-(check^a[i]),i);
            for(int j=1; j<=n; j++)
                if(j!=i)
                    printf("%d ",a[j]);
                else    printf("%d ",check^a[i]);
            break;
        }
    }
    return 0;
}
```