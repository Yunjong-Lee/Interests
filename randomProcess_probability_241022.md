---
date: 2024-10-22 11:03:38
layout: post
---





### [Variance, 분산](https://ko.wikipedia.org/wiki/%EB%B6%84%EC%82%B0)
${\displaystyle \operatorname {var} (X)}$ 또는 ${\displaystyle \sigma _{X}^{2}}$, 혹은 간단히 ${\displaystyle \sigma ^{2}\,}$으로 표현한다.  
※ ${\displaystyle \sigma \,}$는 표준편차  

#### 개념
- 변수 $X$가 기대값($\mu = E[X]$)으로부터 얼마나 떨어진 곳에 분포하는지 정도에 대한 수치화[^001]  
  + ${\displaystyle \operatorname {Var} (X) = \operatorname {E} \left[ (X - \mu )^2 \right] } = {\displaystyle \sum _{i=1}^{n}p_{i}x_{i}}$  
  + 기대값에 대해 확장해 보면,  
    ${\displaystyle {\begin{aligned}\operatorname {Var} (X)&=\operatorname {E} \left[(X-\operatorname {E} [X])^{2}\right]\\[4pt]&=\operatorname {E} \left[X^{2}-2X\operatorname {E} [X]+\operatorname {E} [X]^{2}\right]\\[4pt]&=\operatorname {E} \left[X^{2}\right] - 2\operatorname {E} [X]\operatorname {E} [X]+\operatorname {E} [X]^{2}\\[4pt]&=\operatorname {E} \left[X^{2}\right] - \operatorname {E} [X]^{2}\end{aligned}}}$ [^002] 

  + 측정된 데이터에서 평균을 뺀 값(편차)을 제곱하고, 그것을 모두 더한 후 전체 개수로 나누어준다.(차이값의 제곱의 평균, 편차를 모두 더하면 0이므로 제곱해서 더한다)  

- 모분산(population variance, 모집단의 분산) : 관측값에서 모 평균을 빼고 그것을 제곱한 값을 모두 더하여 전체 데이터 수 n으로 나눈 것  
- 표본분산(sample variance, 표본의 분산) : 관측값에서 표본 평균을 빼고 제곱한 값을 모두 더한 것을 n-1로 나눈 것  

- 물리학, 빛이 두 개 이상의 다른 매질을 통과할 때 그 경계면에서 고유 파장에 따라 나뉘는 현상

#### 이산확률변수에서  


#### 연속확률변수에서  



---

[^001]: 기대값은 확률변수의 위치를 나타내고, 분산은 그것이 얼마나 넓게 퍼져 있는지를 나타냄.  
[^002]: 확률변수 $X$의 분산은 $X^2$의 기댓값에서 $X$ 기댓값의 제곱을 뺀 것과 같다.



