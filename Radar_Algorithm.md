# INDEX 
[1. CFAR](#Constant-False-Alarm-Rate)  
[2. Kalman Filter](#Kalman-Fliter)  

<br>

---


# Constant False Alarm Rate  
- 210915

### Introduction

One important task a radar system performs is target detection. The detection itself is fairly straightforward. It compares the signal to a threshold. Therefore, the real work on detection is coming up with an appropriate threshold. In general, the threshold is a function of both the probability of detection and the probability of false alarm.
    <details>
    <summary> </summary>
    <div markdown="1">
레이더 시스템이 수행하는 중요한 작업 중 하나는 표적 탐지다. 탐지 자체는 매우 간단(신호를 임계값과 비교)하다. 따라서 탐지에 대한 실제 작업은 적절한 임계값을 제시하고 있다. 일반적으로 임계값은 탐지 확률과 오경보 확률의 함수임.
    </div>
    </details>

In many phased array systems, because of the cost associated with a false detection, it is desirable to have a detection threshold that not only maximizes the probability of detection but also keeps the probability of false alarm below a preset level.
    <details>
    <summary> </summary>
    <div markdown="1">
많은 위상 배열 시스템에서 잘못된 탐지와 관련된 비용 때문에 탐지 확률을 최대화할 뿐만 아니라 미리 설정된 수준 아래로 잘못된 경보의 확률을 유지하는 탐지 임계값을 갖는 것이 바람직합니다.
    </div>
    </details>

There is extensive literature on how to determine the detection threshold. Readers might be interested in the [Signal Detection in White Gaussian Noise](https://kr.mathworks.com/help/phased/ug/signal-detection-in-white-gaussian-noise.html) and [Signal Detection Using Multiple Samples](https://kr.mathworks.com/help/phased/ug/signal-detection-using-multiple-samples.html) examples for some well known results. However, all these classical results are based on theoretical probabilities and are limited to white Gaussian noise with known variance (power). In real applications, the noise is often colored and its power is unknown.
    <details>
    <summary> </summary>
        <div markdown="1">      
        감지 임계값을 결정하는 방법에 대한 문헌들:
        독자는 잘 알려진 결과에 대해 White Gaussian Noise의 신호 감지 및 다중 샘플을 사용한 신호 감지 예제에 관심이 있을 수 있습니다. 
        그러나 이러한 모든 고전적 결과는 이론적 확률을 기반으로 하며 알려진 분산(전력)이 있는 white gaussian noise로 제한됩니다. 
        실제 응용 프로그램에서 노이즈는 종종 colored이며 그 전력은 알 수 없습니다.
        </div>
    </details>
      
CFAR technology addresses these issues. In CFAR, when the detection is needed for a given cell, often termed as the cell under test (CUT), the noise power is estimated from neighboring cells.
    <details>
    <summary> </summary>
    <div markdown="1">
CFAR 기술은 이러한 문제를 해결합니다. CFAR에서 CUT(Cell Under Test)라고 하는 주어진 셀에 대해 감지가 필요할 때 노이즈 전력은 인접 셀에서 추정됩니다.
    </div>
    </details>
      
Then the detection threshold, $T$, is given by

$T = αP_n$

where $P_n$ is the noise power estimate and $α$ is a scaling factor called the threshold factor.
    <details>
    <summary> </summary>
    <div markdown="1">
여기서, $P_n$ 은 noise power 추정치이고, $α$ 는 임계값 인자라 불리는 스케일링 인자이다.
    </div>
    </details>
    
From the equation, it is clear that the threshold adapts to the data. It can be shown that with the appropriate threshold factor, $α$, the resulting probability of false alarm can be kept at a constant, hence the name CFAR.

### Cell Averaging CFAR Detection

The cell averaging CFAR detector is probably the most widely used CFAR detector. It is also used as a baseline comparison for other CFAR techniques. In a cell averaging CFAR detector, noise samples are extracted from both leading and lagging cells (called training cells) around the CUT. The noise estimate can be computed as [1]



*P**n*=1*N**N**m*=1*x**m*



where *N* is the number of training cells and *x**m* is the sample in each training cell. If *x**m* happens to be the output of a square law detector, then *P**n* represents the estimated noise power. In general, the number of leading and lagging training cells are the same. Guard cells are placed adjacent to the CUT, both and leading and lagging it. The purpose of these guard cells is to avoid signal components from leaking into the training cell, which could adversely affect the noise estimate.

The following figure shows the relation among these cells for the 1-D case.

![img](https://kr.mathworks.com/help/examples/phased/win64/CFARDetectionExample_01.png)

With the above cell averaging CFAR detector, assuming the data passed into the detector is from a single pulse, i.e., no pulse integration involved, the threshold factor can be written as [1]



*α*=*N*(*P*−1/*N**f**a*−1)



where *P**f**a* is the desired false alarm rate.

### CFAR Detection Using Automatic Threshold Factor

In the rest of this example, we show how to use Phased Array System Toolbox to perform a cell averaging CFAR detection. For simplicity and without losing any generality, we still assume that the noise is white Gaussian. This enables the comparison between the CFAR and classical detection theory.

We can instantiate a CFAR detector using the following command

```
cfar = phased.CFARDetector('NumTrainingCells',20,'NumGuardCells',2);
```

In this detector we use 20 training cells and 2 guard cells in total. This means that there are 10 training cells and 1 guard cell on each side of the CUT. As mentioned above, if we assume that the signal is from a square law detector with no pulse integration, the threshold can be calculated based on the number of training cells and the desired probability of false alarm. Assuming the desired false alarm rate is 0.001, we can configure the CFAR detector as follows so that this calculation can be carried out.

```
exp_pfa = 1e-3;
cfar.ThresholdFactor = 'Auto';
cfar.ProbabilityFalseAlarm = exp_pfa;
```

The configured CFAR detector is shown below.

```
cfar
cfar = 
  phased.CFARDetector with properties:

                   Method: 'CA'
            NumGuardCells: 2
         NumTrainingCells: 20
          ThresholdFactor: 'Auto'
    ProbabilityFalseAlarm: 1.0000e-03
             OutputFormat: 'CUT result'
      ThresholdOutputPort: false
     NoisePowerOutputPort: false
```

We now simulate the input data. Since the focus is to show that the CFAR detector can keep the false alarm rate under a certain value, we just simulate the noise samples in those cells. Here are the settings:

- The data sequence is 23 samples long, and the CUT is cell 12. This leaves 10 training cells and 1 guard cell on each side of the CUT.
- The false alarm rate is calculated using 100 thousand Monte Carlo trials

```
rs = RandStream('mt19937ar','Seed',2010);
npower = db2pow(-10);  % Assume 10dB SNR ratio

Ntrials = 1e5;
Ncells = 23;
CUTIdx = 12;

% Noise samples after a square law detector
rsamp = randn(rs,Ncells,Ntrials)+1i*randn(rs,Ncells,Ntrials);   
x = abs(sqrt(npower/2)*rsamp).^2;
```

To perform the detection, pass the data through the detector. In this example, there is only one CUT, so the output is a logical vector containing the detection result for all the trials. If the result is true, it means that a target is present in the corresponding trial. In our example, all detections are false alarms because we are only passing in noise. The resulting false alarm rate can then be calculated based on the number of false alarms and the number of trials.

```
x_detected = cfar(x,CUTIdx);
act_pfa = sum(x_detected)/Ntrials
act_pfa = 9.4000e-04
```

The result shows that the resulting probability of false alarm is below 0.001, just as we specified.

### CFAR Detection Using Custom Threshold Factor

As explained in the earlier part of this example, there are only a few cases in which the CFAR detector can automatically compute the appropriate threshold factor. For example, using the previous scenario, if we employ a 10-pulses noncoherent integration before the data goes into the detector, the automatic threshold can no longer provide the desired false alarm rate.

```
npower = db2pow(-10);  % Assume 10dB SNR ratio
xn = 0;
for m = 1:10
    rsamp = randn(rs,Ncells,Ntrials)+1i*randn(rs,Ncells,Ntrials);
    xn = xn + abs(sqrt(npower/2)*rsamp).^2;   % noncoherent integration
end
x_detected = cfar(xn,CUTIdx);
act_pfa = sum(x_detected)/Ntrials
act_pfa = 0
```

One may be puzzled why we think a resulting false alarm rate of 0 is worse than a false alarm rate of 0.001. After all, isn't a false alarm rate of 0 a great thing? The answer to this question lies in the fact that when the probability of false alarm is decreased, so is the probability of detection. In this case, because the true false alarm rate is far below the allowed value, the detection threshold is set too high. The same probability of detection can be achieved with our desired probability of false alarm at lower cost; for example, with lower transmitter power.

In most cases, the threshold factor needs to be estimated based on the specific environment and system configuration. We can configure the CFAR detector to use a custom threshold factor, as shown below.

```
release(cfar);
cfar.ThresholdFactor = 'Custom';
```

Continuing with the pulse integration example and using empirical data, we found that we can use a custom threshold factor of 2.35 to achieve the desired false alarm rate. Using this threshold, we see that the resulting false alarm rate matches the expected value.

```
cfar.CustomThresholdFactor = 2.35;
x_detected = cfar(xn,CUTIdx);
act_pfa = sum(x_detected)/Ntrials
act_pfa = 9.6000e-04
```

### CFAR Detection Threshold

A CFAR detection occurs when the input signal level in a cell exceeds the threshold level. The threshold level for each cell depends on the threshold factor and the noise power in that derived from training cells. To maintain a constant false alarm rate, the detection threshold will increase or decrease in proportion to the noise power in the training cells. Configure the CFAR detector to output the threshold used for each detection using the `ThresholdOutputPort` property. Use an automatic threshold factor and 200 training cells.

```
release(cfar);cfar.ThresholdOutputPort = true;cfar.ThresholdFactor = 'Auto';cfar.NumTrainingCells = 200;
```

Next, create a square-law input signal with increasing noise power.

```
rs = RandStream('mt19937ar','Seed',2010);Npoints = 1e4;rsamp = randn(rs,Npoints,1)+1i*randn(rs,Npoints,1);ramp = linspace(1,10,Npoints)';xRamp = abs(sqrt(npower*ramp./2).*rsamp).^2;
```

Compute detections and thresholds for all cells in the signal.

```
[x_detected,th] = cfar(xRamp,1:length(xRamp));
```

Next, compare the CFAR threshold to the input signal.

```
plot(1:length(xRamp),xRamp,1:length(xRamp),th,...  find(x_detected),xRamp(x_detected),'o')legend('Signal','Threshold','Detections','Location','Northwest')xlabel('Time Index')ylabel('Level')
```

![Figure contains an axes. The axes contains 3 objects of type line. These objects represent Signal, Threshold, Detections.](https://kr.mathworks.com/help/examples/phased/win64/CFARDetectionExample_02.png)

Here, the threshold increases with the noise power of the signal to maintain the constant false alarm rate. Detections occur where the signal level exceeds the threshold.

### Comparison Between CFAR and Classical Neyman-Pearson Detector

In this section, we compare the performance of a CFAR detector with the classical detection theory using the Neyman-Pearson principle. Returning to the first example and assuming the true noise power is known, the theoretical threshold can be calculated as

```
T_ideal = npower*db2pow(npwgnthresh(exp_pfa));
```

The false alarm rate of this classical Neyman-Pearson detector can be calculated using this theoretical threshold.

```
act_Pfa_np = sum(x(CUTIdx,:)>T_ideal)/Ntrialsact_Pfa_np = 9.5000e-04
```

Because we know the noise power, classical detection theory also produces the desired false alarm rate. The false alarm rate achieved by the CFAR detector is similar.

```
release(cfar);cfar.ThresholdOutputPort = false;cfar.NumTrainingCells = 20;x_detected = cfar(x,CUTIdx);act_pfa = sum(x_detected)/Ntrialsact_pfa = 9.4000e-04
```

Next, assume that both detectors are deployed to the field and that the noise power is 1 dB more than expected. In this case, if we use the theoretical threshold, the resulting probability of false alarm is four times more than what we desire.

```
npower = db2pow(-9);  % Assume 9dB SNR ratiorsamp = randn(rs,Ncells,Ntrials)+1i*randn(rs,Ncells,Ntrials);x = abs(sqrt(npower/2)*rsamp).^2;   act_Pfa_np = sum(x(CUTIdx,:)>T_ideal)/Ntrialsact_Pfa_np = 0.0041
```

On the contrary, the CFAR detector's performance is not affected.

```
x_detected = cfar(x,CUTIdx);act_pfa = sum(x_detected)/Ntrialsact_pfa = 0.0011
```

Hence, the CFAR detector is robust to noise power uncertainty and better suited to field applications.

Finally, use a CFAR detection in the presence of colored noise. We first apply the classical detection threshold to the data.

```
npower = db2pow(-10);fcoeff = maxflat(10,'sym',0.2);x = abs(sqrt(npower/2)*filter(fcoeff,1,rsamp)).^2;   % colored noiseact_Pfa_np = sum(x(CUTIdx,:)>T_ideal)/Ntrialsact_Pfa_np = 0
```

Note that the resulting false alarm rate cannot meet the requirement. However, using the CFAR detector with a custom threshold factor, we can obtain the desired false alarm rate.

```
release(cfar);cfar.ThresholdFactor = 'Custom';cfar.CustomThresholdFactor = 12.85;x_detected = cfar(x,CUTIdx);act_pfa = sum(x_detected)/Ntrialsact_pfa = 0.0010
```

### CFAR Detection For Range-Doppler Images

In the previous sections, the noise estimate was computed from training cells leading and lagging the CUT in a single dimension. We can also perform CFAR detection on images. Cells correspond to pixels in the images, and guard cells and training cells are placed in bands around the CUT. The detection threshold is computed from cells in the rectangular training band around the CUT.

![img](https://kr.mathworks.com/help/examples/phased/win64/CFARDetectionExample_03.png)

In the figure above, the guard band size is [2 2] and the training band size is [4 3]. The size indices refer to the number of cells on each side of the CUT in the row and columns dimensions, respectively. The guard band size can also be defined as 2, since the size is the same along row and column dimensions.

Next, create a two-dimensional CFAR detector. Use a probability of false alarm of 1e-5 and specify a guard band size of 5 cells and a training band size of 10 cells.

```
cfar2D = phased.CFARDetector2D('GuardBandSize',5,'TrainingBandSize',10,...  'ProbabilityFalseAlarm',1e-5);
```

Next, load and plot a range-doppler image. The image includes returns from two stationary targets and one target moving away from the radar.

```
[resp,rngGrid,dopGrid] = helperRangeDoppler;
```

![Figure contains an axes. The axes with title Range Doppler Map contains an object of type image.](https://kr.mathworks.com/help/examples/phased/win64/CFARDetectionExample_04.png)

Use CFAR to search the range-doppler space for objects, and plot a map of the detections. Search from -10 to 10 kHz and from 1000 to 4000 m. First, define the cells under test for this region.

```
[~,rangeIndx] = min(abs(rngGrid-[1000 4000]));
[~,dopplerIndx] = min(abs(dopGrid-[-1e4 1e4]));
[columnInds,rowInds] = meshgrid(dopplerIndx(1):dopplerIndx(2),...
  rangeIndx(1):rangeIndx(2));
CUTIdx = [rowInds(:) columnInds(:)]';
```

Compute a detection result for each cell under test. Each pixel in the search region is a cell in this example. Plot a map of the detection results for the range-doppler image.

```
detections = cfar2D(resp,CUTIdx);
helperDetectionsMap(resp,rngGrid,dopGrid,rangeIndx,dopplerIndx,detections)
```

![Figure contains an axes. The axes with title Range Doppler CFAR Detections contains an object of type image.](https://kr.mathworks.com/help/examples/phased/win64/CFARDetectionExample_05.png)

The three objects are detected. A data cube of range-doppler images over time can likewise be provided as the input signal to `cfar2D`, and detections will be calculated in a single step.

### Summary

In this example, we presented the basic concepts behind CFAR detectors. In particular, we explored how to use the Phased Array System Toolbox to perform cell averaging CFAR detection on signals and range-doppler images. The comparison between the performance offered by a cell averaging CFAR detector and a detector equipped with the theoretically calculated threshold shows clearly that the CFAR detector is more suitable for real field applications.

### Reference

[1] Mark Richards, **Fundamentals of Radar Signal Processing**, McGraw Hill, 2005




signal을 일정한 간격(Cell)으로 나누고, 임계값을 유동적으로 변경하여 오류할람을 없애는 알고리듬.
target의 위치는 거리에 대한 레이더 신호의 강도가 일정 threshold를 넘어가는 peak에 의해 결정.
만약, 상수 threshold를 사용하면, target이 아닌 장애물dml 신호 강도가 threshold를 넘는 경우가 빈번하게 발생되므로, false alarm이 빈번하게 발생된다.

![img](https://mblogthumb-phinf.pstatic.net/MjAxOTAzMDRfMTQx/MDAxNTUxNjg1NTIwNTcz.5D0iIT84zqxFY7MWYCK8svFTCi58z-1BMizjmc_Ou9gg.NkafQUhq24N7ydpOa0-OaDZp3xsXp7ElFmsXAnl4MV8g.PNG.emcsin/image.png?type=w800)

Frame을 일정한 간격으로 Cell로 나누어 앞과 뒤에 일정한 위도우를 지정 → 윈도우의 Cell들을 평균값을 구하고 일정 가드셀을 두고 센터의 값과 평균값을 비교하여 비교되어진 값이 크기 값에 따라서 0, 1의 값을 도출 → Target 검출




![img](https://mblogthumb-phinf.pstatic.net/MjAxOTAzMDRfMjIx/MDAxNTUxNjg0NzYzNzUx.x8EzI4DhzDXpnWU7EKHwgcIqIb12mI-gBOQ777h3oVkg.nSQw-h47KIuG86A-63BxKMOs5KmRB9pshk3NXf3ueMQg.PNG.emcsin/image.png?type=w800)

CA-CFAR 
- Threshold 값(빨간색 점선)과 실제 검지되는 타겟의 신호와 겹치는 부분을 이용하여 타겟 검지
  + Threshold 값은 테스트 중인 셀(CUT) 주변의 노이즈 플로어 레벨을 추정하여 계산됩니다.
- 종류 : 셀 값들의 어떤 특성을 이용하여 검출하느냐에 따라 CA(Cell Average), GO(Greatest-Of), LO(Least-Of)등


<br>


# Kalman Filter
- https://ko.wikipedia.org/wiki/%EC%B9%BC%EB%A7%8C_%ED%95%84%ED%84%B0

  잡음이 포함되어 있는 측정치(과거에 수행한 측정값)를 바탕으로 선형 역학계의 상태를 추정(현재 상태 변수의 결합분포를 추정)하는 재귀필터.
### 1. Operation
예측과 업데이트 단계로 구성  

  ##### 1.1. 예측  
  현재 상태 변수의 값과 정확도 예측  
  ##### 1.2. 업데이트  
  이전에 추정한 상태 변수를 가반으로 여ㅖ측한 측정치와 실제 측정치의 차이를 반영하여 상태변수 없데이트  

- 추적 레이더에서 적응형 확장 칼만 필터의 성능 분석, 2017
- key : 확장 칼만 필터는 잡음 공분산이 고정되어 있으므로, 거리에 따라 잡음 분산이 변하면서 추적성능이 떨어지게 된다. 거리에 따라 잡음 공분산이 변하는 적응형 칼만 필터를 제시함
  - 각 오류: 정확한 추적을 방해함(각 오류가 커질수록 거리에 배례하여 레이더가 추적한 위치와 목표물 사이의 오차 증가.
  - 적응형 칼만필터 성능 검증
    - KSLV-I의 경로 모델링
    - 열잡음, 글린트 열잡음 고려
  - 



</br>


# [차량용 레이더 시스템에서 주파수 영역의 도래각 추정 기법에 관한 연구](https://www.koreascience.or.kr/article/JAKO201607433788642.pdf)
- The Journal of Korean Institute of Communications and Information Sciences '16-01 Vol.41 No.01
- 22.03.07


fmcw radar에서, 거리와 속도가 다른 물체들은 서로 다른 beat frequency를 가진다.  
MUSIC 알고리즘을 주파수 영역에서 적용하는 방법 제시  

- radar 종류
  - 펄스 도플러 레이더 : 송신된 펄스 신호가 전방의 차량에 반사되어 돌아오는 시간과 도플러 주파수를 측정하여 전방 차량의 거리와 속도를 추정  
  - 잡음 레이더 : 의사 잡음 신호를 송신하여 다중 경로를 통해 되돌아온 수신 신호의 지연 시간을 추출하여 전방 차량의 거리를 추정  
  - FMCW 레이더 : 정현파의 주파수를 변조하여 송신하고 전방 차량에 맞고 되돌아온 수신 신호와의 관계를 통해 전방 차량의 거리와 속도를 동시에 추정  

ㅁ 일반적으로, 단일 안테나를 적용한 레이더는 전방 물처의 각도를 추정할 수 없음  
→ 각도 추정을 위해서 위상배열 안테나와 도래각 추정 알고리듬(고해상도 알고리즘으로  
[MUSIC](https://ieeexplore.ieee.org/document/1164233), [ESPRIT](https://ieeexplore.ieee.org/document/127959) 등)을 통해 각도, 전파 지연 시간, 주파수 등 추정 가능  
→ 그러나, 타겟과 클러터를 구분하지 않고 각도를 추정하므로, 추정된 각도에서 인식해야 할 전방의 물체가 차량인지 고정 물체 등 불필요한 클러터인지 알 수 없다.

![img](https://latex.codecogs.com/gif.latex?%5CDelta%20t) 시간 동안 주파수 BW만큼 선형 주파수를 변조한 송신신호는  
![ㅑimg](https://latex.codecogs.com/gif.latex?y%28t%29%20%3D%20Acos%5Cleft%20%28%202%5Cpi%5Cleft%20%28%20f_c%20-%20%5Cfrac%7BBW%7D%7B2%7D%20%5Cright%20%29t%20&plus;%20%5Cfrac%7BBW%7D%7B2%5CDelta%20t%7Dt%5E2%20%5Cright%20%29)
여기서, A는 송신 신호의 크기,  
![img](https://latex.codecogs.com/gif.latex?f_c)는 반송 주파수, 그리고 BW는 주파수 변조폭 을 나타낸다.

다중 타겟에 의해 반사되어 수신된 신호는 
![img](https://latex.codecogs.com/gif.latex?r%28t%29%20%3D%20%5Csum_%7Bi%20%3D1%7D%5E%7BD%7DB_icos%5Cleft%20%282%5Cpi%20%5Cleft%20%28%20%5Cleft%20%28%20f_c%20-%20%5Cfrac%7BBW%7D%7B2%7D%20&plus;%20f_%7Bd%2Ci%7D%20%5Cright%20%29%20%28t%20-%20t_%7Bd%2Ci%7D%29%20&plus;%20%5Cfrac%7BBW%7D%7B2%5CDelta%20t%7D%20%28t-t_%7Bd%2Ci%7D%29%5E2%20%5Cright%20%29%20%5Cright%20%29%20&plus;%20n%28t%29)  
여기서, D는 타겟의 갯수, B는 수신 신호의 크기, t_d는 지연 시간, 그리고 f_d는 도플러 주파수.

송신 신호와 수신 신호는 믹서를 통과하면서 서로 곱해지고, 믹서 신호는 저역 필터를 통과하며 고주파 대역이 제거된다. 앞으로 믹서 신호는 저역 필터까지 통과한 신호를 뜻한다. 믹서 신호는  
![img](https://latex.codecogs.com/gif.latex?x%28t%29%20%3D%20%5Csum_%7Bi%20%3D1%7D%5E%7BD%7D%20C_i%20cos%5Cleft%20%282%5Cpi%20%5Cleft%20%28%20%5Cfrac%7BBW%7D%7B%5CDelta%20t%7Dt_%7Bd%2Ci%7D%20-%20f_%7Bd%2Ci%7D%20%5Cright%20%29%20t%20&plus;%20%5Cleft%20%28%202%5Cpi%20%5Cleft%20%28%20f_c%20-%20%5Cfrac%7BBW%7D%7B2%7D%20&plus;%20f_%7Bd%2Ci%7D%20%5Cright%20%29t_%7Bd%2Ci%7D%20-%20%5Cfrac%7B%5Cpi%20BW%7D%7B%5CDelta%20t%7Dt_%7Bd%2Ci%7D%5E2%20%5Cright%20%29%20%5Cright%20%29%20&plus;%20w%28t%29)
여기서, C는 믹서 신호의 크기를 나타내며 특히 ![img](https://latex.codecogs.com/gif.latex?%5Cfrac%7BBW%7D%7B%5CDelta%20t%7Dt_%7Bd%7D%20-%20f_%7Bd%7D)를 beat frequency (송신 신호와 수신 신호의 주파수 차, 관측 구간 동안 일정한 값을 가지며, 또한 target마다 서로 다른 일정한 값을 가짐)를 의미하며, 거리에 의한 지연 시간 성분과 속도차에 의한 도플러 주파수 성분으로 이루어져 있다.  

- 비트 주파수 검출은 믹서 신호의 푸리에 변환과 일정 [CFAR 알고리즘](https://ieeexplore.ieee.org/document/60107)을 통해 얻은 문턱 값들을 비교하여 문턱 값보다
높은 값에 해당하는 주파수를 비트 주파수로 추정
- 도플러 주파수의 영향으로 비트 주파수는 주파수 상향 변조구간과 주파수 하향 변조구간에서 각각 다르게 나타난다.  
![img](https://latex.codecogs.com/gif.latex?f_%7Bbu%7D%20%3D%20%5Cfrac%7BBW%20%5Ccdot%20t_d%7D%7B%5CDelta%20t%7Df_%7Bd%7D%2C%20f_%7Bbd%7D%20%3D%20%5Cfrac%7BBW%20%5Ccdot%20t_d%7D%7B%5CDelta%20t%7Df_%7Bd%7D)  
위 식을 거리에 의한 지연 시간 성분과 도플러 성분 ![img](https://latex.codecogs.com/gif.latex?f_%7Br%7D%2C%20f_d)으로 나누어 보면,  ![img](https://latex.codecogs.com/gif.latex?f_%7Br%7D%20%3D%20f_%7Bbu%7D%20&plus;%20f_d%20%3D%20f_%7Bbd%7D%20-%20f_d%20%3D%20%5Cfrac%7Bf_%7Bbu%7D%20&plus;%20f_%7Bbd%7D%7D%7B2%7D%2C%20f_d%20%3D%20%5Cfrac%7Bf_%7Bbu%7D%20-%20f_%7Bbd%7D%7D%7B2%7D)  
따라서, target의 거리는  
![img](https://latex.codecogs.com/gif.latex?R%20%3D%20%5Cfrac%7Bf_%7Br%7D%20%5Ccdot%20c%5CDelta%20t%7D%7B2BW%7D%20%3D%20%5Cfrac%7Bf_%7Bbu%7D%20&plus;%20f_%7Bbd%7D%20%5Ccdot%20%5CDelta%20t%7D%7B4BW%7D)  
속도는  
![img](https://latex.codecogs.com/gif.latex?V_r%20%3D%20%5Cfrac%7Bf_%7Bd%7D%20%7D%7B2f_c%7D%20c%20%3D%20%5Cfrac%7Bf_%7Bbu%7D%20-%20f_%7Bbd%7D%20%5Ccdot%20c%7D%7B4f_c%7D)  
와 깉이 추정할 수 있다(타겟의 추정 거리와 속도가 추정된 비트 주파수에 의해 결정되기 때문에, 비트 주파수를 얼마나 정확히 검출하느냐에 따라 타겟의 거리와 속도의 추정
정확도 결정됨)



