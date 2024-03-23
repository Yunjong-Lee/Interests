


- simple and effective vital sign algorithm
- infineon 24GHz FMCW
- vital signs (breathing and heartbeat)을 얻기 위해 radar의 중간주파수에서 DC를 제거하고, distance-dimensional FFT와 위상처리 진행
- heart와 breath를 분리하기 위한 filter
- 호흡 고조파가 심박주파수 추출 ㅅ; 영향을 제거하기 위해 2차 차분과 notch 필터 사용

[related work] 
- 디지털 헤테로다인 직교 아키텍처 수신기를 구축하여 DC 잡음을 줄였지만 [4] , 하드웨어 비용이 높았습니다. 
- 호흡 고조파가 심장 박동에 미치는 영향을 줄이기 위해 RELAX 알고리즘으로 기저대역 신호를 처리 [5] . 그러나 알고리즘의 복잡성은 높습니다. 
- 기계 학습을 사용하여 호흡 고조파를 제거[6], 훈련을 위해 많은 수의 데이터 세트에 의존해야 합니다.

[principle]  

![FMCW Radar Architecture](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/10275796/10276388/10277450/liu1-p3-liu-small.gif)

- $IF(t) = A_{IF} e^{j 2 \pi f_b t +\frac{4 \pi R(t)}{\lambda _c} } $ &emsp;&emsp; $(1)$    
	+ $A_{IF}$ : the amplitude of IF signal 
	+ the real-time distance between human target and radar $R(t) =R0 + x(t)$ 
	+ $R_0$ : distance between the target and the radar when it is relatively stationary  
	+ $x(t)$ : body surface change caused by breathing and heartbeat  
	+ $f_b$ : frequency of IF signal, and its expression is:  

$f_b = \frac{{2BR(t)}}{{c{T_c}}} $, &emsp;&emsp; $(2)$  
	+ B : radar bandwidth  
	+ c : speed of light  
	+ $T_c$ : time to transmit a chirp.  

[Vital Sign Signal Detection Algorithm]
- Eliminate DC
  - rmcw 레이더는 내부 구성요소로 인해 DC 성분이 생성되며, DC 성분은 vital sign 신호 추출에 영향을 준다.
  - 신호의 DC component는 신호의 average value이다. freq. 에서는 신호의 freq.가 zero인 부분, distance & speed dimension은 모두 zero.
  : DC 성분 제거를 위해 mean value cancellation algorithm 사용
  : 수신된 각 프레임 신호를 평균하여 기준 신호를 구하고, 각 프레임 신호에서 기준 신호를 빼서 타겟 에코 신호를 얻는다.  
  : 기준 수신 신호의 표현  
	+ $C [m] = \frac{1}{N} \displaystyle \sum _{i=1} ^{N} R [m,i]$  
	+ m : the distance dimension sampling point  
	+ i : the velocity dimension sampling point  
	+ $R[m,n]=R[m,n]−C[m] $  

- Distance dimension FFT
  - DC 제거 후 FFT 연산 수행 → 스펙트럼 획득
  - 주파수와 거리의 대응관계를 이용하여 주파수를 거리로 변환 → 거리 스펙트럼 획득
  : ![radar ech signal로부터 얻어낸 거리 스펙트럼]( https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/10275796/10276388/10277450/liu2-p3-liu-small.gif)
- target processing
  : IF 신호의 위상에는 호흡 및 심박 정보가 포함되어 있으므로, range FFT를 통해 얻은 범위 단위의 위상정보를 처리
	+ Phase Unwrapping
	  : 위상 추출에는 MATLAB의 각도 함수 사용 
	  (획득된 위상 값의 진폭 범위는 [-π,π]이므로, 실제 위상 값을 얻으려면 추출된 위상을 풀어야 한다)
	+ 확장된 단계에 대해 1st order difference 수행
	  (fixed phase offset 제거와 heartbeat signal 강화 목적)
	+ 1st order difference 후의 신호는 random body movment에 옇향을 받고, spike 발생
	  : 위와 같은 노이즈 성분을 제거하기 위해 이동 평균 필터링 사용
	  (1st order differential signal smoothing, 평활화) 

![Change of phase with time at different stages](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/10275796/10276388/10277450/liu3-p3-liu-small.gif)  
	: a) is phase change diagram with time before phase unwrapping  
	: b) is phase change diagram with time after phase unwrapping  
	: c) is phase change diagram with time after phase unwrapping difference  
	: d) is phase change diagram with time after phase unwrapping differential moving average filtering  

- Separation of respiration and heartbeat signals  
  : (adults) respiratory rate : 0.1-0.5Hz & heart rate : 0.8-2Hz  
	+ 2-IIR elliptic band-pass filters : other freq. bands and accurately separate breath and heartbeat  
	+ 대역 통과 필터링 후 호흡 및 심박의 시간 영역 파형  
![](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/10275796/10276388/10277450/liu4-p3-liu-small.gif)  
     + a) 에서 필터링된 호흡 신호가 상대적으로 매끄럽고 표준 주기 신호에 근접  
     + b) 의 필터링된 심장박동 신호는 호흡 고조파의 영향으로 인해 주파수 변동이 발생  
     + 심박 수파수 추출 전 고조파의 영향을 제거하는 알고리듬 적용이 필요함  

- Extraction of respiration and heartbeat signals  
     + filtering된 호흡신호는 곧바로 FFT 수행 가능  
     + 심박 신호 추출을 위해서는 호흡 고조파 제거 후 FFT 수행  
        : 위상 2차 difference와 notch 필터의 조합으로 호흡 고조파 제거  
![notch filtering](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/10275796/10276388/10277450/liu5-p3-liu-small.gif)  

