# P9774 题解

推柿子。~~但是卡了好久谔谔。~~

---

我们设 $f(x)=x!\oplus p$。

展开

$$f(x)=(1\times 2\times \dots \times (x-1)\times x)\oplus p$$

把 $p$ 的倍数提出来并且进行一个变形

$$f(x)=\{[(0\times p+1)\times \dots \times (1\times p-1)]\times[(1\times p+1)\times\dots\times(2\times p-1)]\times\dots\times[(\lfloor\frac{x-p}{p}\rfloor\times p+1)\times\dots\times(\lfloor\frac{x}{p}\rfloor\times p-1)]\times[(\lfloor\frac{x}{p}\rfloor\times p+1)\times \dots \times x]\times(\lfloor \frac{x}{p} \rfloor!\times p) \}\oplus p$$

化简

$$f(x)=\{[1\times 2 \times \dots \times (p-1)]^{\lfloor \frac{x}{p} \rfloor}\times (1\times 2 \times \dots \times (x\bmod p))\times(\lfloor \frac{x}{p} \rfloor!\oplus p)\}\oplus p$$

再化简

$$f(x)=\{[(p-1)!]^{\lfloor \frac{x}{p} \rfloor}\times (x\bmod p)!\times f(\lfloor \frac{x}{p} \rfloor)\}\bmod p$$

根据威尔逊定理化简得

$$f(x)=[(p-1)^{\lfloor \frac{x}{p} \rfloor}\times (x\bmod p)! \times f(\lfloor \frac{x}{p} \rfloor)]\bmod p$$

我们可以快速幂求出 $(p-1)^{\lfloor \frac{x}{p} \rfloor}$，预处理 $(x\bmod p)!$，然后递归计算结果。

做完了。

核心代码：

```cpp
int f(int x){
    if(x<p)return sum[x];
    int ans=qpow(p-1,x/p,p);
    return ans*sum[x%p]%p*f(x/p)%p;
}
```