---
date: 2024-03-23 16:51:21
layout: post
---

# [The fundamentals of millimeter wave radar sensors](https://www.tij.co.jp/jp/lit/wp/spyy005a/spyy005a.pdf?ts=1711143374972)

# Introduction

# Range measurement
## Range resolution
- FMCW Radar에서 freq.는 시간에따라 선형적으로 증가하는데, 이 신호 종류를 [chirp](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Linear-chirp.svg/290px-Linear-chirp.svg.png)_Fig.1(b)이라 한다.  
![FIg. 1. Chirp](https://www.researchgate.net/profile/Hua-Jiadong/publication/283811110/figure/fig1/AS:316253492269056@1452412116475/Example-of-an-L-Chirp-signal-a-Trajectory-of-instantaneous-frequency-b-Waveform.png)

Fig.1(a)는 동일한 chirp 신호를 시간의 함수로 나타낸 주파수를 보여준다. chirp의 특징은 start frequency ($f_c$), bandwidth ($B$) and duration ($T_c$)이다. 
chirp의 기울기 (S)는 freq.의 변화율로 포착된다. 
- $f_c$ = 77GHz, B = 4 GHz, $T_s$ = 40$\mu s$, 그리고, s = 100 MH/$\mu s$
- FMCW Radar의 concept는 chirp signal을 전송하고 Obj에 의해 반사된 신호를 캡쳐한다.

# Velocity measurement
## Velocity measurement with two chirps

## Velocity measurement with multiple objects at the same range
- The two-chirp velocity measurement method does not work if multiple moving objects with different velocities are at the time of measurement, both at the same distance from the radar. Since these objects are at the same distance, they will generate reflective chirps with identical IF frequencies. As a consequence, the range-FFT will result in single peak, which represents the combined signal from all of these equi-range objects. A simple phase comparison technique will not work. 
- In this case, in order to measure the speed, the radar system must transmit more than two chirps. It transmits a set of N equally spaced chirps. This set of chirps is called a chirp frame. Figure 7 shows the frequency as a function of time for a chirp frame.

- The processing technique is described below using the example of two objects equidistant from the radar but with different velocities v1 and v2. 
Range-FFT processes the reflected set of chirps, resulting in a set of N identically located peaks, but each with a different phase incorporating the phase contributions from both these objects (the individual phase contributions from each of these objects being represented by the red and blue phasors in Figure 8).  
- A second FFT, called Doppler-FFT, is performed on the N phasors to resolve the two objects, as shown in Figure 9.

- $\omega_1$ and $\omega_2$ correspond to the phase difference between consecutive chirps for the respective objects (Equation 13).


## Velocity resolution

# Angle Detection

## Angle Estimation

## Maximum Angular Field of View
- The maximum angular field of view of the radar is defined by the maximum AoA that the radar can estimate. See Figure 13.  
- The maximum angular field of view of the radar is
defined by the maximum AoA that the radar can
estimate. See Figure 13. 
- Unambiguous measurement of angle requires $\Delta$ < 180$^\circ$. Using Eq.16, this corresponds to $\frac{2\pi sin (\theta)}{\lambda} < n $  
Equation 17 shows that the maximum field of view that two antennas spaced l apart can service is:  
$\theta_{max} = sin^{-1}(frac{\lambda}{2l})$ --- (17)
A spacing between the two antennas of $l = \frac{\lambda}{2}$
results in the largest angular field of view $±90°$  

# TI mmWave sensor solution
- As you can see, an FMCW sensor is able to determine the range, velocity and angle of nearby objects by using a combination of RF, analog and digital electronic components. 
- TI has brought innovation to the field of FMCW sensing by integrating a DSP, MCU and the TX RF, RX RF, analog and digital components into a RFCMOS single chip. 
- TI’s RFCMOS mmWave sensors differentiate themselves from traditional SiGe-based solutions by enabling flexibility and programmability in the mmWave RF front-end and the MCU/HWA/DSP processing back-end. 
Whereas a SiGe-based solution can only store a limited number of chirps and requires real-time intervention to update chirps and chirp profiles during an actual frame, TI’s mmWave sensor solutions are able to store 512 chirps with four profiles before a frame starts. 
This capability allows TI’s mmWave sensors to be easily configured with multiple configurations to maximize the amount of useful data extracted from a scene. 
Individual chirps and the processing back-end can be tailored “on-the-fly” for real-time application needs such as higher range, higher velocities, higher resolution, or specific processing algorithms.

- The TI mmWave Sensor portfolio for “Automotive” scales from high-performance radar front-end to highly-integrated single-chip edge sensors. Designers can address advanced driver assistance systems (ADAS) and autonomous driving safety regulations—including ISO 26262, which enables Automotive Safety Integrity Level (ASIL)-B— with the AWR mmWave portfolio.

- The TI mmWave sensor portfolio for “Industrial” includes both 76-81GHz and 60-64GHz with highly integrated single chip edge sensors . 

- The on-chip DSP provides more flexibility and allows for software integration of high-level algorithms, such as object tracking and classification. 
These single-chip devices provide simple access to the high-accuracy object data including range, velocity and angle that enables advanced sensing in rising applications that demand performance and efficiency such as smart infrastructure, Industry 4.0 in factory and building automation products and autonomous drones.