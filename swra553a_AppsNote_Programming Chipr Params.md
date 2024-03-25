---
date: 2024-03-24 20:22:58
layout: post
---

# [Programming Chirp Parameters in TI Radar Devices](https://www.ti.com/lit/an/swra553a/swra553a.pdf?ts=1615416383966&ref_url=https%253A%252F%252Fwww.ti.com%252Fsensors%252Fmmwave-radar%252Findustrial%252Ftechnical%20-documents.html)

# 1. Chirp Configuration on System Parameters
- 시간에 따라 Tx 신호가 선형적으로 변하는 단일 톤 인 경우를 chirp 이라고 하며, chirp set로 프레임을 형성한다.
  ~~> 레이더 처리를 위한 관찰 장으로 사용.~~
- Fig. 1.은 single chirp과 timing params를, Fig. 2.는 chirp series로 구성된 frame structure를 보인다. 이 경우는 각각의 chirp은 10’s [µs] duration를 가지는 ‘Fast FMCW’ 변조를 나타낸다.
  
![Fig. 1. FMCW Chirp: 단일 처프의 타이밍 매개변수 & Frame Structure: 처프와 프레임 간 프레임 구조](https://img-blog.csdnimg.cn/20210527154953328.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NhbGFkcGll,size_16,color_FFFFFF,t_70)

## 1.1. Measurement Range and Range Resolution
- key parameters: maximum and minimum distance  
- key metrics: range resolution(ability to distinguish two nearby objects)  

### 1.1.1. Maximum Range
- 먼 거리에 위치한 물체를 감지하는 것은 수신 신호의 SNR, 또는 radar IF bandwidth에 의해 제한.  
  : IF bandwidth가 클수록 감지할 수 있는 최대 속도 증가.  
- IF bandwidth과 max range resolution 간의 관계  
> $Range_{max} = \frac{IF_{max}C}{2S}$  
> * $IF_{max}$: 지원되는 Max IF bandwidth (사용되는 ADC sampling freq.에 dependent함)  
>   + complex 1x sampling mode, IF bandwidth는 $0.9 × (ADC_{sampling})$로 제한된다.  
>   + complex 2x and real sampling modes, IF bandwidth는 $\frac {0.9 × (ADC_{sampling})} {2}$ 로 제한된다.
>   + TI radar의 max ADC sampling freq.는 45MHz(AWR22xx)와 37.5MHz(AWR1xxx)
> * $C$: Speed of light  
> * $S$: Slope of the transmitted chirp

- max range를 제한시킬 수 있는 것으로 수신된 신호의 SNR  
> * RF 성능(Tx output power, Rx noise figure), 처프 매개변수(chirp duration, number of chirps in frame)  
> * Tx/Rx antenna gain  
> * Radar Cross Section(RCS, 레이더 단면적)  
> * 물체를 감지하기 위한 감지 알고리즘에 필요한 min SNR.  
> - $Range_{max} &ensp; based &ensp; SNR = ^4\sqrt(\frac{P_t × G_{Rx} × G_{Tx} × C^2 \sigma NT_r}{f_C^2 (4\pi)^3 × kT × NF × SNR_{det}}) $  
>   - $P_t$: tx output power
>   - $G_{Rx}, G_{Tx}$: Ant. gain
>   - $\sigma$: RCS of object
>   - N: number of chirps
>   - $T_r$: chirp time
>   - NF: noise figure
>   - $SNR_{det}$: min SNR
>   - k: Boltzman constant
>   - $T_{det}$: Ambient temperature

### 1.1.2. Range Resolution
- 처프 스윕 대역폭에 따라 변화(비례관계)
- TI’s radar devices support a 4 GHz sweep bandwidth (~4cm)
> - $Range_{resol} = \frac{c}{2 × B}$  
>   * B: sweap bandwidth of FMCW chirp  

## 1.2 Measurement Velocity and Velocity Resolution  
### 1.2.1 Maximum Velocity
- 최대 속도(물체의 상대 속도):  chirp cycle time(두 개의 연속 chirp의 시작점 사이의 시간 차)에 따라 변화
> - 주파수 스윕이 얼마나 빨리 수행될 수 있는지와 허용되는 최소 처프 간 시간에 의존
>   * MMIC가 주파수를 더 빠르게 증가시킬수록 최대 unambiguous velocity가 높다.(TI: max 100MHz/μs 허용)
>   * PLL: 주파수 램프의 매우 빠른 정착을 지원하도록 설계됨
>     * VCO가 램프 주파수 끝에서 다음 램프를 다시 시작하기 위해 점프하는 데 걸리는 시간은 2μsec (최소 유휴 시간 계산은 섹션 5를 참조)
> - $Unambiguousmax velocity = \frac{\lambda}{4T_c}$  
>   * $T_c$: total chirp time  
>   * $\lambda$: wavelength of the signal used  
>   * 실제 측정 가능한 최대 속도는 더 높은 수준의 알고리즘을 사용하여 개선 가능

### 1.2.2 Velocity Resolution
- 속도 차이가 작은 객체(주자 Apps등)를 분리를 위해 속도 분해능이 필요
- 속도 해상도는 전송 프레임 지속 시간에 따라 변화(프레임의 처프 수와 속도 해상도 비례)
> - $Unambiguousmax velocity = \frac{\lambda}{2N_c}$  
>   * $N_c$: Number of Chirp in a frame

## 1.3 Angular Range and Resolution
- 2D 공간에 obj가 위치하기 위해서, 거리와 함께 angle of object가 요구된다.
- angle 추정
  + 지연된 수신 신호 $dsin(\theta)$로부터 위상 shift($\frac{2\pi d sin(\theta)}{\lambda}$) 발생
  + 측정 가능한 angle은 d에 dependent함.
  + $Max unambiguous angular range = sin^{-1}(\frac{\lambda}{2d})$
    > - d : Spacing between receiver antennas
    > - $\lambda$: wavelength
    > - theoretically 가장 넓은 범위의 FOV를 가지려면 Ant. 간격은 $\frac{\lambda}{2}$이며, 이때 $±90°$의 시야 범위를 제공한다.

# 2. Chirp Configurations for Common Applications
- [Ref...](https://e2e.ti.com/support/sensors-group/sensors/f/sensors-forum/971468/awr1843-how-to-configure-the-chirp-setting)  
![Chirp Configuration case of MRR](https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/1023/20210119_5F00_210615886.jpg)

| Parameter | Units | LRR | MRR | SRR | USRR |
| --- | --- | --- | --- | --- | --- |
| Max unambiguous | range | m | 225 | 125 | 45 | 22.5 |
| Sweep bandwidth | MHz | 300 | 540 | 750 | 1500 |
| Ramp slope | MHz/us | 10 | 12 | 15 | 30 |
| Inter-chirp duration | us | 8 | 10 | 12 | 50 |
| Number of chirps | - | 256 | 128 | 128 | 128 |
| Range resolution | m | 0.50 | 0.28 | 0.20 | 0.1 |
| Chirp duration | us | 30 | 45 | 50 | 50 |
| Max umambiguous relative velocity | kmph | 92.28 | 63.75 | 56.56 | 35.3 |
| Max beat frequency | MHz | 15 | 10 | 4.5 | 4.5 |
| ADC sampling rate (complex) | Msps | 16.67 | 11.11 | 5.00 | 5.00 |
| Number of samples per chirp | | 500 | 500 | 250 | 250 |
| Range FFT size | - | 512 | 512 | 256 | 256 | 
| Frame time (total) | ms | 9.728 | 7.04 | 7.94 12.8| 
| Frame time (active) | ms | 7.68 | 5.76 | 6.4 | 6.4| 
| Radar data memory required | KB | 2048 | 1024 | 512 | 512 | 
# 3. Configurable Chirp RAM and Chirp Profiles


# 4. Chirp Timing Parameters


# 5. Advanced Chirp Configurations 


# 6. Basic Chirp Configuration Programming Sequence 


# 7. References