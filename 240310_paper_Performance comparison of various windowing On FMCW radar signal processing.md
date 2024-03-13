---
date: 2024-02-16 11:09:07
layout: post
---


# Performance comparison of various windowing On FMCW radar signal processing
- [2016 International Symposium on Electronics and Smart Devices (ISESD)](https://ieeexplore.ieee.org/document/7886743)

# Abstract  
- signal processing of FMCW radar. 
  + to translate the signal from the time domain to distance 
  + optimization of defining the target using windowing(Blackmann, Hamming, Hanning, and Bartlet are the types of windowing used in this research)
  + new method for windowing by separating the data in near and far distance. 
    - suppress the signal from short distance and strengthen the signal in far distance. 
    - algorithm : to combine complex data I and Q then apply windowing, and FFT the signal to take the range of target. 
    - comparison of signal processing (@ 70.896 km or 38 nautical miles (nmi))

# FMCW Radar Parameters
- data form:  I + jQ complex form (demodulator can get I/Q signal from radar receiver)
  + I/Q data는 pulse에 따라 수집되어 2차원 배열 구성  
  ![Triangle modulation_transmitted, received, and beat frequencies as a function of time for a moving target](https://ieeexplore.ieee.org/mediastore_new/IEEE/content/media/7883473/7886681/7886743/7886743-fig-2-source-small.gif)
  
  > Sampling Frequency = 1 MHz  
    Number of N sample = 1024  
    Bandwidth = = 1 MHz  
    Carrier Frequency = = 9.4 GHz  

# Algorithm
- I/Q data save → combine I/Q data (complex array, 90x1024) → "Blackman, Hamming, Hanning 및 Bartlet의 윈도잉"
- time domain plot 작성
- FFT all data (per sequence) (as an array of 90 x 1024) & save FFT result
- Choose the half of data (array of 90 x 512) & Calculate the mean of the half (Resulting an array data of 1 x 512)
  + range target인 1 x 512 배열 데이터로 plot 작성
- threshold로 smoothing signal
- 90x1024 배열의 windowing (Blackman, Hamming, Hanning, and Bartlet)에 5~10 단계 적용 및 결과 비교

# Results and Discussion


# Conclusion









