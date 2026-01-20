---
date: 2025-12-19 10:49:07
layout: post
---

# DMS 
- evaluates the position of the head and the opening of the eyes  
- recorded data는 
  + SA5AU (Driving Assistant Professional) 
    * 정의: BMW의 '드라이빙 어시스턴트 프로페셔널' 패키지 코드
      기능: 스톱앤고(Stop&Go) 기능이 포함된 액티브 크루즈 컨트롤, 차선 유지 어시스턴트, 스티어링 및 차선 제어 어시스턴트 등 자율주행 보조 기능 제공
  + SA5AR (Traffic Jam Assistant)
    * 정의: '트래픽 잼 어시스턴트' 즉, 정체 구간 주행 지원 기능 코드
    * 기능: 고속도로나 정체된 도로(보통 60km/h 미만)에서 스티어링 휠을 직접 잡지 않아도 운전자의 시선을 감지하여 차로를 유지 기능. SA5AU 패키지에 포함되거나 연동되는 경우가 많습니다. 
  + SAS (SAS Control Unit)
    * 정의: BMW의 주행 지원 시스템을 통합 제어하는 'SPECIAL CONFIGURATION SYSTEM' 또는 ECU  
    * 역할: 사이드 레이더 센서 및 드라이버 카메라 시스템(DCS) 등에서 오는 데이터를 처리하고 5AU/5AR 기능을 구동하기 위한 모듈

![BMW DMS Camera](https://g30.bimmerpost.com/forums/attachment.php?s=62f39c5f8969b71f7d16f3e1bee3a494&attachmentid=2060063&stc=1&d=1558535505)

※ DCS (Driver Camera System, ACC off or unavailable touch detection of the steering wheel up to 60km/h)  

※ [Magna's DMS](https://www.newsweek.com/magnas-driver-monitoring-system-can-tell-when-youre-phone-1712612)


![new Magna driver monitor](https://assets.newsweek.com/wp-content/uploads/2025/08/2051111-magna-driver-monitoring-system.jpg?w=1600&quality=80&webp=1)  

![Magna Driver Monitoring System in the rearview mirror](https://assets.newsweek.com/wp-content/uploads/2025/08/2051115-magna-driver-monitoring-system.jpg?w=1600&quality=80&webp=1)



# DMS Algorithms  
- DMS를 위해서는 Vital sign estimation algorithm 이외에 "head position"과 "gaze"에 대한 estimation algorithm이 필요하다.



- monitoring driver's Head movement proposed  
- index
  + One‐shot learning‐based driver's head movement identification using a millimetre-wave radar sensor
  + Head Pose Estimation via mmWave Radar
  + Human Multi-Activities Classification Using mmWave Radar: Feature Fusion in Time-Domain and PCANet

# [One‐shot learning‐based driver's head movement identification using a millimetre-wave radar sensor](https://scholarworks.bwise.kr/cau/bitstream/2019.sw.cau/70053/1/One-shot%20learning-based%20driver%27s%20head%20movement%20identification%20using%20a%20millimetre-wave%20radar%20sensor.pdf), IET, 2021  


+ 비트센싱과 협업 진행
  
+ AI를 적용하는 이유  
  : supervised learning based approaches : require a huge amount of data to be labelled.  

+ radar related ref
  * Jung, J., et al.: CNN‐based driver monitoring using millimeter wave radar sensor. IEEE Sens. Lett. 3, 1–4 (2021)
  * Bresnahan, D.G., Li, Y.: Classification of driver head motions using a mm‐Wave FMCW radar and deep convolutional neural network. IEEE Access 9, 100472–100479 (2021)

+ AI related ref 
  * Fei‐Fei, L., Fergus, R., Perona, P.: One‐shot learning of object categories. IEEE Trans. Pattern Anal. Mach. Intell. 28(4), 594–611 (2006)
  * Wu, D., Zhu, F., Shao, L.: One‐shot learning gesture recognition from RGBD images. In: 2012 IEEE Computer Society Conference on Computer Vision and Pattern Recognition Workshops, pp. 7–12. (2012)
  * Vinyals, O., et al.: Matching Networks For One‐Shot Learning. arXiv:1606.04080 (2016)
  * Altae‐Tran, H., et al.: Low data drug discovery with one‐shot learning. ACS Central Sci. 3(4), 283–293 (2017). https://doi.org/10.1021/acscentsci.6b00367.pMID: 28470045
  * Zhang, A., et al.: Limited data rolling bearing fault diagnosis with few‐shot learning. IEEE Access 7, 110895–110904 (2019)
  * Chauhan, J., Nathani, D., Kaul, M.: Few‐shot learning on graphs via super‐classes based on graph spectral measures. ArXiv:2002.12815(2020)
  * Tuyet‐Doan, V.‐N., et al.: One‐shot learning for partial discharge diagnosis using ultra‐high‐frequency sensor in gas‐insulated switchgear. Sensors 20(19), 5562 (2020). https://www.mdpi.com/1424‐8220/20/19/5562  

--- 

## 2. Signal analysis for the FMCW radar system   
: signal analysis  
+ transmitted signal, $f(t)$  
  &emsp; &emsp; $= cos(2 \pi f_c t + \pi \frac{\Delta B}{\Delta T} t^2)$  
  . $f_c$ is the carrier frequency  
  . $\Delta B$ are the operating bandwidth of the transmitted signal  
  . $\Delta T$ are the duration of transmission in one frame  

  + received signal, $r(t)$  
  &emsp; &emsp; $= \alpha f (t - t_{td})$  
  &emsp; &emsp; $= \alpha cos(2\pi f_c (t-t_{td}) + \pi \frac{\Delta B}{\Delta T} (t-t_{td})^2 )$   
  . α : the attenuation factor owing to the path loss  
  . $t_{td}$ ( $= \frac{2R}{c}$) : time delay    
  . $R$ : distance to the target  

+ base-band signal, $m(t)$   
  &emsp; &emsp; $m(t) = \frac{\alpha}{2}cos 2 \pi (\frac{\Delta B R}{\Delta T c} + \frac{2f R}{c})$  
  &emsp; &emsp; ※ ~~$f(t)$와 $r(t)$ 사이의 different signal이 포함되어 있으므로 beat signal이라고도 한다.~~   
  
+ sampling process 후의 신호, $m(t)$    
  &emsp; &emsp; $m[n] = \frac{\alpha}{2} cos(2 \pi \frac{Delta B R}{\Delta T c} nT_s + 2 \pi \frac{2f_c R}{c} + \phi) $  
    . $T_s N_s, \phi$ : sampling period, number of samples, and the phase offset  
+ beat signal (frequency‐domain), $M[k]$  
  &emsp; &emsp; $M[k] = \displaystyle \sum ^{N_s-1} _{n=0} m|n|exp (\frac{-j2\pi k m}{N_s})$  

+ peak value는 index $k$에서 나타나며, peak value로부터 target의 거리(추정) $\^{R}$는  
  &emsp; &emsp; $\^{R} = \frac{c \Delta T}{2\Delta B} f_b$  

## 3. 환경  
: 60GHz (bandwidth of 6 GHz.)  
: set up at the centre of the steering wheel  
  - (a) Case 1: when staring at the front
  - (b) Case 2: when shaking head up and down
  - (c) Case 3: when shaking head side to side
  - (d) Case 4: when lowering the head  
  
: distance between the driver's head and the steering wheel : 40 cm (20~60 cm)  
: remove clutter (multi-path reflection) : 
  - Pittella, E., et al.: Measurement of breath frequency by body‐worn UWB radars: a comparison among different signal processing techniques. IEEE Sens. J. 17(6), 1772–1780 (2017)  


---

# [Head Pose Estimation via mmWave Radar](https://ieeexplore.ieee.org/document/10901471)
- fft & static interference removal(extract head pose features) and a novel human head posture estimation (CNN)  

## realted work
- 7. Haipeng Liu, Yuheng Wang, Anfu Zhou, Hanyue He, Wei Wang, Kunpeng Wang, Peilin Pan, Yixuan Lu, Liang Liu, and Huadong Ma. “real-time arm gesture recognition in smart home scenarios via millimeter wave sensing ”. Proceedings of the ACM on interactive, mobile, wearable and ubiquitous technologies, 4 : 1–28, 2020.
- 8. Haowen Wei, Ziheng Li, Alexander D Galvan, Zhuoran Su, Xiao Zhang, Kaveh Pahlavan, and Erin T Solovey. “indexpen: Two-finger text input with millimeter-wave radar ”. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 6 : 1–39, 2022.
- 9. Yadong Li, Dongheng Zhang, Jinbo Chen, Jinwei Wan, Dong Zhang, Yang Hu, Qibin Sun, and Yan Chen. “towards domain-independent and real-time gesture recognition using mmwave signal ”. IEEE Transactions on Mobile Computing, 22 : 7355–7369, 2023.


- 10. Mingmin Zhao, Tianhong Li, Mohammad Abu Alsheikh, Yonglong Tian, Hang Zhao, Antonio Torralba, and Dina Katabi. “through-wall human pose estimation using radio signals ”. In Proceedings of the IEEE conference on computer vision and pattern recognition, pages 7356–7365, 2018.
  + wifi 대역의 신호는 벽은 통과하고 인체는 반사하는 특징을 이용

- 11. Soo Min Kwon, Song Yang, Jian Liu, Xin Yang, Wesam Saleh, Shreya Patel, Christine Mathews, and Yingying Chen. “hands-free human activity recognition using millimeter-wave sensors ”. In 2019 IEEE International Symposium on Dynamic Spectrum Access Networks (DySPAN), pages 1–2, 2019.

# [Human Multi-Activities Classification Using mmWave Radar: Feature Fusion in Time-Domain and PCANet](https://www.mdpi.com/1424-8220/24/16/5450#Introduction)

- Parameters  
  + range profile, Time-Frequency, Range–Azimuth Time,  
  + mean, variance, standard deviation, kurtosis, skewness, and central moment  
    : The kurtosis [38] measures the signal probability distribution tailedness.  
    : 확률분포의 꼬리에 있는 값의 분포 정도, 데이터가 평균에서 얼마나 멀리 퍼져 있는지를 수치화한 값  
    : 정규분포(평균이 0안 경우)에서는 0 or 3  
    : 값이 높을 수록, 이상치가 많음(위험 평가 등에 활용됨)  
    : The skewness [39] measures the asymmetry of the signal probability distribution about its mean.  
    : 실수값 확률변수의 확률분포 비대칭도를 나타내는 지표, 분포가 한쪽으로 얼마나 치우쳤는지 수치화  
    : The central moment [40] measures the moment of the signal probability distribution about its mean, and we applied a two-order central moment in the following computation.  

---  

# [RadEye: Tracking Eye Motion Using FMCW Radar](https://dl.acm.org/doi/10.1145/3706598.3713775)
- sub-6GHz FMCW radar
- DNN to refine the detection accuracy

## ...
- Existing contactless eye tracking solutions : camera, acoustic, radar
  + camera : high accuracy / privacy concerns, poor lighting conditions
  + acoustic : small distance (due to the propagation nature of sounds)
  + radar : mm level detection (small wavelength)

## signal processing
- 아래의 절차를 이용하여 100 ms 미만으로 깜박이는 눈 움직임을 걸러낼 수 있음

![system overview of RadEye](https://dl.acm.org/cms/10.1145/3706598.3713775/asset/343be76d-8741-40e3-96ed-adf644d3fa24/assets/images/medium/chi25-689-fig7.jpg)  
※ selection of the range bin and the extraction of eye motions  

Range-FFT - Filtering (Range-FFT) - FFT Bin Selection - Eye Motion Detection  

### Range-FFT
- chirp duration : 1ms
- sample rate : 2.5Msps (in each cycle, 1500 complex numbers are acquired)
  + sample 끝에 zero padding을 추가, 다른 range에서, 신호를 얻기위해 4096-point range-FFT 실행  
  + 4096 bin에서 첫 256 bin만 사용한다. ---why???  

### Filtering for Range-FFT  
- 2차 Butterworth bandpass filter: suppress noise and out-of-band interference
  + pass band : 1 ~ 5 Hz [46](Tianfang Zhang, Zhengkun Ye, Ahmed Tanvir Mahdad, Md Mojibur Rahman Redoy Akanda, Cong Shi, Yan Wang, Nitesh Saxena, and Yingying Chen. 2023. FaceReader: Unobtrusively Mining Vital Signs and Vital Sign Embedded Sensitive Info via AR/VR Motion Sensors. In Proceedings of the 2023 ACM SIGSAC Conference on Computer and Communications Security. Association for Computing Machinery, New York, NY, USA, 446–459.) and [50](Xi Zhang, Yu Zhang, Zhenguo Shi, and Tao Gu. 2023. mmFER: Millimetre-wave Radar based Facial Expression Recognition for Multimedia IoT Applications. In Proceedings of the 29th Annual International Conference on Mobile Computing and Networking. Association for Computing Machinery, New York, NY, USA, 1–15.)
    * eye blinking freq.와 chest breathing freq. (0.1 Hz ∼ 0.5 Hz)가 overlap되지만, eye blinking의 freq.가 높기때문에 필터에 영향을 주지 않는다
    * 심장의 박동이 눈의 미세한 움직을 유발하는 것에 대해서도 영향 없음 (HBR은 매우 약함, 머리의 흔들림의 원인이되지 않음)  

### FFT Bin Selection  
- 눈 움직임 특징을 가진 FFT bin을 찾는 것은 어려운 일임
- amplitude dynamic range (동적범위, 측정할 수 있는 max와 min의 비율)를 indicator로 이용하여 bin을 찾는다
  + 눈을 감고 뜰 때 blinking motion은 반사면이 전환(watar-textured eyeball에서 skin-textured eyelid로)되는 원인이 된다.
  + 레이더 IF 신호의 amplitude의 변화 원인
- algorithms
  + 각각의 Range-FFT bin i에 대해 window-slides variance 계산  
  $v_i(j) = \frac{1}{W} \displaystyle \sum_{m=j} ^{j+W-1} (|y_i(m)| - \tilde{y_i})^2$  
    * $\tilde{y_i} = \frac{1}{W} \displaystyle \sum_{m=j} ^{j+W-1} |y_i(m)|$  
    * $W$ : window size (200, eye blinking에 맞춤)
  + $v_i (j)$가 시전 정의된 threshold $T$보다 크면, timestamp $j$는 $t_n$으로 기록
    * $T = 0.05$ (empirically, 경험치)
  + the next detected timestamp $j$ satisfies the $2000 < j − t_n < 3000$ (fit in the interval of blink), it will be counted as the continuous blink.
  + 연속 3회 깜박임 감지 시, Range-FFT bin을 candidate bin으로 기록한다.  

  ![Fig 8. The signal amplitude variance for different Range-FFT bins during eye blinks. (b) Eye motion detected based on signal phase (with the camera-based ground truth marked). (c) Comparison of Eye motions and interfering motions from the target person’s head.](https://dl.acm.org/cms/10.1145/3706598.3713775/asset/6fe911c7-7b98-485c-81af-3ccd31bd3972/assets/images/medium/chi25-689-fig8.jpg)  

    * 이 경우, 알고리듬은 가장 작은 index를 가진 bin을 선택한다.
      - smallest index range-FFT bin은 가장 짧은 signal travel path (best reflects the eye motion pattern)를 나타냄  

### Eye Motion Detection
- Range-FFT bin이 구분되면 bin을 관찰하고, bin을 기반으로 eye motion 추정  
- 각각의 eye motion은 3-단계로 구분 (detect 3 positions for each eye motion)  
  + move eyeball / edge eyeball / eyeball backs to the start position  
  ※ 눈 회전 검출동안 위상에서 중요한 패턴을 보임  
  + Eyeball rotations은 반복적인 움직임(edge에 도달하면, eyeball은 central point로 돌아간다)을 포함한다.
    * 반복적인 위상변화 패턴이 발생됨
  + 극소 위상 극값의 위치(positions of local phase extremums)는 눈 움직임의 가장자리에 도달하는 위치와 일치
    * feature 추출  
      -. identifying local peaks : searches local max/min phase with 1 sec.  
      -. search along the gradients of samples before/after the peak (피크 앞/뒤의 spl들의 gradient를 따라 검색, gradient의 position이 0과 같으면, start/stop 위치)
  + 신체의 다른 부분 (head/mouth)의 간섭 제거, Fig.8(c) 참조
    * pahse shifter, time duration to refine in detection result
      -.위상 차가 임계값을 초과하면, 신호는 버려짐
      -. 움직임이 임계값으로 떨어지면, time duration이 고려된다.
      duration range내 (200 ~ 600 ms) 신호는 타당한 eye motion 신호임


  




  



## References
- [Radar-Based Eyeblink Detection Under Various Conditions](https://dl.acm.org/doi/abs/10.1145/3587828.3587855)




--- 

# [Eye-Gaze Tracking Based on Head Orientation Estimation Using FMCW Radar Sensor](https://ieeexplore.ieee.org/document/10723245)  
- 센서 모듈설계, Robot system팀(SEC)
- eye-gaze tracking method based on head orientation estimation (eye gaze direction and the orientation of the human head) that uses a single FMCW(60GHz) radar.
- algorithm은 multiple bolck으로 구분
  + signal analysis methods : range-angle map을 이용하여 human 존재 추정
  + If human is detected, 수신 signal는 관심있는 하위 공간으로 투영(projected).
    * 
  + 투영된 신호에서 target spectrum 분리 : super-resolution multiple signal classification (MUSIC) algorithm 이용 사람의 머리 크기를 정확히 추정 가능
  + MobileNet을 통해 사람 머리 방향에 따라 신호를 분류 
  + 
- 

## Introduction
- Existing radar-based studies are limited to topics (eye blinking, ...)
- Eye tracking의 category는  
  + Eye gaze detection and eye-gaze tracking  
    * Contact sensors(렌즈, EEG, EOG, ...) : high accuracy/discomfort  
    * noncontact sensors (vision) : outstanding estimation (recognition of gaze and facial expressions)/privacy, low-light conditions  
    * noncontact sensors (radar) : privacy, low-light conditions, do not require physical contact with the body/lower resolution  



### Target Detection

#### A. Range Estimation  
- radar signal $s(t)$  
  $s(t) = A_T e^{j2\pi f_{c} t} e^{j \pi_{\gamma} t^2} rect(\frac{t}{T_c} )$  
  $A_T$ is the amplitude  
  $f_c$ is the carrier frequency  
  $γ = \frac{B}{T_c}$ is the frequency slope  
  $B$ is the bandwidth  
  $T_c$ is the chirp duration  
  $rect(⋅)$ is rectangular function    

  $rect(\frac{t}{T_c}) = {1,	if 0 < t < T_c  
			              0,	otherwise.


$^a if 0 < t < t_c, _b$  

$\left{ \frac{a}{b} \right.$





   




BlinkRadar: Non-intrusive driver eye-blink detection with UWB radar, in Proc. IEEE 42nd Int. Conf. Distrib. Comput. Syst. (ICDCS), Bologna, Italy, Jun. 2022, pp. 1040–1050.

Detection of eye blinking using Doppler sensor with principal component analysis, IEEE Antennas Wireless Propag. Lett., vol. 14, pp. 123–126, 2015.


---

# [Eye-Gaze Tracking Based on Head Orientation Estimation Using FMCW Radar Sensor](https://ieeexplore.ieee.org/document/10723245)  
- 센서 모듈설계, Robot system팀(SEC)
- eye-gaze tracking method based on head orientation estimation (eye gaze direction and the orientation of the human head) that uses a single FMCW(60GHz) radar.
- algorithm은 multiple bolck으로 구분
  + signal analysis methods : range-angle map을 이용하여 human 존재 추정
  + If human is detected, 수신 signal는 관심있는 하위 공간으로 투영(projected).
    * 
  + 투영된 신호에서 target spectrum 분리 : super-resolution multiple signal classification (MUSIC) algorithm 이용 사람의 머리 크기를 정확히 추정 가능
  + MobileNet을 통해 사람 머리 방향에 따라 신호를 분류 
  + 
- 

## Introduction
- Existing radar-based studies are limited to topics (eye blinking, ...)
- Eye tracking의 category는
  + Eye gaze detection and eye-gaze tracking
    * Contact sensors(렌즈, EEG, EOG, ...) : high accuracy/discomfort
    * noncontact sensors (vision) : outstanding estimation (recognition of gaze and facial expressions)/privacy, low-light conditions
    * noncontact sensors (radar) : privacy, low-light conditions, do not require physical contact with the body/lower resolution

### Target Detection

#### A. Range Estimation
- radar signal $s(t)$ 
  $s(t) = A_T e^{j2\pi f_{c} t} e^{j \pi_{\gamma} t^2} rect(\frac{t}{T_c} )$
  $A_T$ is the amplitude
  $f_c$ is the carrier frequency
  $γ = \frac{B}{T_c}$ is the frequency slope
  $B$ is the bandwidth
  $T_c$ is the chirp duration
  $rect(⋅)$ is rectangular function  

  $rect(\frac{t}{T_c}) = {1,	if 0 < t < T_c 
			  0,	otherwise.




  

###  



연관성 낮음
30. S. Lim, J. Jung, E. Lee, J. Choi, and S.-C. Kim, “In-vehicle passenger occupancy detection using 60-GHz FMCW radar sensor,” IEEE Internet Things J., vol. 11, no. 4, pp. 7002–7012, Feb. 2024.
  
  algorithm: 
  - raw radar signal (convert to range-angle map from raw signal) -> to supress clutter signal, two clutter suppression methods are proposed.
  - to classify various arrangements of passengers inside the vehicle by applying three classification algorithms: 1) SVM; 2) MLP; and 3) CNN.
  - transform data structure





---

###











