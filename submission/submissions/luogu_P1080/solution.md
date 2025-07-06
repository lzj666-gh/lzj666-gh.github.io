# P1080 题解

本文写作目的为证明P1080贪心算法

-----------------------------------------

我们先来证明

对任意相邻两项，其依照二者$a$、$b$之积升序排列所得的结果小于等于降序排列所得的结果$(\sigma)$

不妨设现有大臣$i,i+1$

设在第$1$到$i-1$位中的最大值为$maximum$，则
 
第$1$到第$i+1$位中的最大值$\alpha$为

$max$
$($
$maximum,$
${\frac{\prod^{i-1}_{p=0}a_p}{b_i}}$
$,$
${\frac{\prod^{i}_{p=0}a_p}{b_{i+1}}}$
$)$

（设$r=\frac{\prod^{i-1}_{p=0}a_p}{b_i}$，$s=\frac{\prod^{i}_{p=0}a_p}{b_{i+1}}$)

要使得$\alpha$小于$i$与$i+1$交换后的最大值$\beta$,当且仅当
$\beta=max(maximum,\frac{\prod^{i-1}_{p=0}a_p}{b_{i+1}},$
$\frac{\prod^{i+1}_{p=0}a_p}{b_i\times{a_i}})<\alpha$

（设$t=\frac{\prod^{i-1}_{p=0}a_p}{b_{i+1}}$，$u=\frac{\prod^{i+1}_{p=0}a_p}{b_i\times{a_i}}$)

若$maximum=\alpha$,则显然有欲达到之效果

否则：

$∵\prod^{i-1}_{p=0}a_p<\prod^{i}_{p=0}a_p$

$∴s>t$

$∴$若$\alpha=s,\beta=t,$则可达到欲达到之效果

$∵\frac{\prod^{i-1}_{p=0}a_p}{a_i}<\prod^{i+1}_{p=0}a_p$

$∴u>r$

$∴$若$\alpha=r$,则不可能达到欲达到之效果

$∴\alpha$只可能等于$s$

又$∵$当$\alpha=s,\beta=t,$可达到欲达到之效果

$∴\alpha<\beta$
$\Longleftrightarrow$
$ s<u \Longleftrightarrow$
$\frac{\prod^{i}_{p=0}a_p}{b_{i+1}}<$
$\frac{\prod^{i+1}_{p=0}a_p}{b_i\times{a_i}
} $

$\Longleftrightarrow \frac{1}{b_{i+1}}<\frac{a_{i+1}}{a_i \times b_{i}} \Longleftrightarrow {a_i} \times {b_i}<{a_{i+1}} \times {b_{i+1}}$

又$∵i+1$位之后的情况与$i,i+1$的排列方式无关

故$(\sigma)$得证

接下来我们证明要使前$n$项奖励的最大值$\lambda$最小,
必有对于所有第$i$项$(i \in \lbrack 1,n \rbrack\bigcap N)$依据$a_i \times b_i$排序

先看一个引理$(*)$:

若长度为$s$的数列$r$不是一个不严格单调递增序列,则必存在$i \in \lbrack 1,s)\bigcap N$
使得$r_i>r_{i+1}$

证明如下：

若不存在这样的$i$,则:

对于任意
$m_1,m_2 \in \lbrack 1,s)\bigcap N$,当$m_1<m_2$时，有$r_{m_1} \leq r_{m_1+1} \leq ...\leq r_{m_2}$

$∴r$是一个不严格单调递增序列(矛盾)

故引理$(*)$得证

若前$n$项没有依照$a_i \times b_i$排序,且$\lambda$取到最小值,则:

由$(*)$,必有$q_1 \in \lbrack 1,n)\bigcap N$,
$q_2=q_1+1$
$st.$

$a_{q_1} \times b_{q_1}>a_{q_2} \times b_{q_2}$

由$(\sigma)$,交换$q_1,q_2$的位置所得的$\lambda'<$现有的$\lambda$(矛盾)

故命题得证.