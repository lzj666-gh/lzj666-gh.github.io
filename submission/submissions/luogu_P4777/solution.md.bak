# P4777 题解

　　中国剩余定理(CRT)不能解决模数不互质情况的模线性同余方程组。这是中国剩余定理的原理所决定的。来看中国剩余定理的形式：
  $$\text{ans} \equiv \sum_{i} r_i \cdot M_i \cdot \text{inv}(M_i, m_i) \pmod M$$
  
　　其中的 $\text{inv}(M_i, m_i)$ 在 $M_i, m_i$ 不互质的情况下，根本不存在。而只要有任意两个模数不互质，就会产生 $M_i, m_i$ 不互质的情况，从而破坏掉整个解。
  
  
　　如果bug比较小，我们能否进行修复？很遗憾，这条路是没有希望的。CRT不能解决模不互质方程组的本质困难在于：CRT最核心的思想是构造一组 $R_i$ ，使得
  $$\begin{cases}R_i \% m_i=1 \\ R_i \% m_k = 0 ~ (i \neq k)\end{cases}$$
  
  
　　$R_i$的性质是如此美好，我们只需要把 $r_1R_1+r_2R_2+\cdots +r_nR_n$ 作为答案输出就行了。很显然，这个和式模 $m_1$ 余 $r_1$， 模 $m_2$ 余 $r_2$……总之完美地满足了我们的需求。但也就是这个 $R_i$ 需要用到逆元，使得CRT无法应对模不互质的情况。这个缺陷是在于CRT的核心思想，给它动小手术是没有用的。我们想找到解模不互质方程组的办法，就必须完全跳出CRT的窠臼。
  
  
　　那么我们应该怎么做呢？方程组是由很多个模线性同余方程构成的。假设我们能把两个模线性同余方程组，等价地合并成一个方程，问题就迎刃而解了——只需要不停地合并这些方程，只到只剩下一个。
  
  
　　理想是美好的，道路是曲折的。首先，未必两个方程可以合并成一个方程（我们可能找不到快速的实现方式）。此外，即使可以把两个方程合并成一个，这个变换也未必是等价变换（可能新方程的解未必是原方程的解，也可能原方程的解被新方程漏掉了）。我们要做的事情是：给出将两个方程合并成一个方程的方法，然后证明这个变换的等价性。
  
---
  
## 数学基础 
　　作为我们接下来讨论的基础，我想先展示几个例子。它们的规模都很小，完全可以手工验证。
  
$$\begin{cases}x \equiv 2 \pmod 4 \\ x \equiv 4 \pmod 6\end{cases} \quad \Rightarrow \quad x\equiv 10 \pmod {12}$$
$$\begin{cases}x \equiv 4 \pmod 6 \\ x \equiv 3 \pmod 5\end{cases} \quad \Rightarrow \quad x\equiv 28 \pmod {30}$$
$$\begin{cases}x \equiv 2 \pmod 4 \\ x \equiv 3 \pmod 6\end{cases} \quad \Rightarrow \quad \varnothing$$

　　可以粗略地总结出几个规律：
- 新方程与原方程具有同样的形式。
- 新方程的模数，是之前两个模数的lcm.
- 可能存在无解的情况

这几条性质是整个算法的基石，我们会在后文详细讨论。这里先一步步摸出 “合并” 的算法。形式化地，考虑这样一组模线性同余方程：

  $$\begin{cases}a \equiv r_1 \pmod {m_1} \\ a \equiv r_2 \pmod {m_2}\end{cases}$$
  
　　这个方程组等价于：
  $$a = k_1m_1 + r_1 = k_2m_2 + r_2$$
　　移一下项，立刻有 
  $$k_1m_1 - k_2m_2 = r_2 - r_1$$
　　左边的$m_1, m_2$，右边的 $r_2-r_1$是已知量。这就是一个典型的不定方程。解不定方程这个任务，我们是熟悉的：可以通过裴蜀定理判断有没有解，可以用扩展欧几里得算法(exgcd)给出 $(k_1, k_2)$ 的整个解系。于是算法有了第一步：
  

- 如果 $\gcd(m_1, m_2) | (r_2-r_1)$，则判断方程有解
- 否则，报告无解

　接下来考虑如何求出一组 $k_1, k_2$. 约定几个记号：记 $d = \gcd(m_1, m_2), ~p_1=\frac{m_1}{d}, ~ p_2=\frac{m_2}{d}$. 显然 $p_1, p_2$ 是互质的。 那么把 $m_1$ 用 $p_1 d$来代替，$m_2$ 用 $p_2 d$来代替，可以把上面的式子写成：
 $$k_1 p_1 - k_2p_2 = \frac{r_2 - r_1}{d}$$
　　右边那一串东西是整数，因为当且仅当 $d | (r_2-r_1)$ 才会有解。左边满足了 $\gcd(p_1, p_2)$ 互质，因此求出整个解系是很容易的。现在假设我们拿exgcd求出了下面这个方程的解 $(\lambda_1, \lambda_2)$：
  $$\lambda_1p_1 + \lambda_2p_2 = 1$$
　　这是一个非常标准的exgcd. 求出来了 $\lambda_1, \lambda_2$ 之后，可以直接拼出 $k_1, k_2$：
  $$\begin{cases}k_1 = \frac{r_2-r_1}{d}\lambda_1 \\ k_2 = - \frac{r_2-r_1}{d}\lambda 2\end{cases}$$
　　于是
  $$x=r_1+k_1m_1 = r_1 + \frac{r_2-r_1}{d}\lambda_1m_1$$
　　至此，我们成功地构造出了一个 $x$，满足 $\begin{cases}x \equiv r_1 \pmod {m_1} \\ x \equiv r_2 \pmod {m_2}\end{cases}$. 但是整个解系如何给出呢？我们有
  
  
**【定理】** 若有特解 $x^*$, 那么 $\begin{cases}x \equiv r_1 \pmod {m_1} \\ x \equiv r_2 \pmod {m_2}\end{cases}$ 的通解是：$x ^ * + k\cdot \text{lcm}(m_1, m_2)$，亦即
$$x \equiv x^* \pmod {\text{lcm}(m_1, m_2)}$$

　　从线性代数的角度讲，这个通解的构造方式是十分平凡的。对 $\text{lcm}(m_1, m_2)$ 取模的结果，将整个整数集划分成了 $\text{lcm}(m_1, m_2)$ 个等价类，哪个等价类里面有特解，那整个等价类肯定全都是解。一人得道，鸡犬升天。接下来唯一需要说明的事情就是：为什么任意一个完全剩余系里面，只会有一个解？这个问题等价于：为什么 $0, 1,2,\cdots ,\text{lcm}(m_1, m_2)$ 里面，只有一个解？
  
  
　　证明解的唯一性，常常采用这样一种手段：假设 $x, y$ 都是原问题的解，然后经过一系列推理，得到 $x=y$，于是解的唯一性就不言而喻了。我们也采用这种手段来解决唯一性问题。设上述集合里面有 $0\leq x, y \leq \text{lcm}(m_1, m_2)$ 满足 
  $$\begin{cases}x\equiv a_1 \pmod {m_1} \\ x\equiv a_2 \pmod {m_2}\end{cases} ~ , ~ \begin{cases}y\equiv a_1 \pmod {m_1} \\ y\equiv a_2 \pmod {m_2}\end{cases}$$
　　不妨设 $x\geq y$. 那立刻就可以发现
  $$\begin{cases}(x-y) \bmod m_1 = 0 \\ (x-y) \bmod m_2 = 0\end{cases} \quad \Rightarrow \quad\text{lcm}(m_1, m_2) ~ | ~ (x-y) $$
　　$x, y$ 都是小于 $\text{lcm}(m_1, m_2)$ 的数，它们的差也必然要小于  $\text{lcm}(m_1, m_2)$. 但 $(x-y)$ 又要被 $\text{lcm}(m_1, m_2)$ 整除，那怎么办？只有 $x-y=0$，也就是 $x=y$. 到此为止，我们证明了：一个完全剩余系中，有且仅有一个解。以上就是整个 exCRT 算法的全部数学基础。
  

### 算法流程及实现
1. 读入所有方程组。
2. 弹出两个方程，先判断有没有解。
    - 无解：报告异常
    - 有解：合并成同一个方程，然后压进方程组
3. 执行上述步骤(2), 直到只剩下一个方程。这个方程就是解系。 

本题代码如下：
```python
from functools import reduce

def gcd(a, b):
    if b==0: return a
    return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a,b)

def exgcd(a, b):
    if b==0: return 1, 0
    x, y = exgcd(b, a%b)
    return y, x - a//b*y

def uni(P, Q):
    r1, m1 = P
    r2, m2 = Q

    d = gcd(m1, m2)
    assert (r2-r1) % d == 0

    l1, l2 = exgcd(m1//d, m2//d)
    
    return (r1 + (r2-r1)//d*l1*m1) % lcm(m1, m2), lcm(m1, m2)

def CRT(eq):
    return reduce(uni, eq)

if __name__ == "__main__":
    n = int(input())
    eq = [list(map(int, input().strip().split()))[::-1] for x in range(n)]
    print(CRT(eq)[0])
```