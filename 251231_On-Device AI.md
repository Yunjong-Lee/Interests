---
date: 2025-12-31 11:22:25
layout: post
---


# On Device AI  
## 개요  
- 스마트폰의 얼굴 인식, 자율주행차의 실시간 상황 판단, 스마트 스피커의 음성 명령 처리, 웨어러블 기기의 건강 분석 등에서 쓰이며, 기기 자체에서 데이터를 처리해 개인정보 보호 강화, 빠른 반응 속도, 인터넷 연결 없이도 사용 가능한 장점을 제공하는 기술  


## 적용 사례  

|     |     |  예  |
| --- | --- | --- |
| 스마트폰 | 얼굴 인식 잠금 해제, 사진 편집, 실시간 번역, AI 기반 카메라 기능 강화 등 | S24(통화 중 실시간 통역/메시지 번역/음성 녹음 요약&번역/Circle to Search(화면 이미지 즉시 검색)) </br> 애플 인텔리전스 (텍스트 재작성/스마트 이미지 생성/지능형 siri) |  
| 자율주행차 | 주변 환경(보행자, 차량) 데이터를 기기 내에서 실시간 분석하여 즉각적인 반응 및 제어 |  | 
| 스마트홈 기기 | 스마트 스피커가 클라우드 연결 없이 음성 명령을 직접 처리하여 음악 재생, 기기 제어 |  |
| 웨어러블 기기 | 스마트워치에서 심박수, 수면 패턴 등을 실시간 분석하여 개인 건강 관리. | | 
| 노트북 | 소형언어모델(sLM)을 탑재해 기기 내에서 문서 요약, 글쓰기 등 생성형 AI 기능 제공 | 페르소나AI 협력 노트북 |    
| 로봇 | 공장 및 서비스 로봇에서 비전, 내비게이션 등을 온디바이스 AI로 처리하여 반응 속도 향상 | 현대차, 딥엑스 NPU 활용 | 
| IoT 기기 | 저전력 AI 칩을 활용해 대규모 IoT 장치에서 실시간 데이터 분석 및 AI 기능 구현 |  | 


## Global Market
- 16.6조원에서 31년 1,181억 달러(약 167조),연평균 27.95%T씩 성장 예상
  + 출처: Verified Market Research, 딜로이트 인사이트 재구성
- 
![2023~2030년 글로벌 온디바이스 AI 시장 규모, 단위 10억$](https://postfiles.pstatic.net/MjAyNTAyMTFfMzAg/MDAxNzM5MjMyOTg4ODE1.XK1FGkUO-fZOdlCE_pYLR2tmKRHEXvinpC0cSh1Djr4g.TLiZIVeV4pRKWHChFUXE__WhT21YCE-Pu4clo7I340Qg.PNG/%EA%B7%B8%EB%A6%BC_1-1.png?type=w966)  
[※ "온디바이스 AI 기술동향 및 발전방향", 이슈리포트 2024-06호, 한국전자정보통신산업진흥회, 2024.06.28](https://www.gokea.org/core/?cid=53&uid=50549&page=&role=view&cate1=%EC%82%B0%EC%97%85%EC%9D%BC%EB%B0%98)  

![Healthcare 분야에서 AI 시장 규모, 단위 10억$](https://postfiles.pstatic.net/MjAyNTAyMTFfNzMg/MDAxNzM5MjM0MTQ1ODQ1.xNmCrWS7K6tRsnyBAppln4kihQuSGgFbRkGpqrsupqUg.Dsv2axceNHxT3XDbiVQdBwuXKvV-tY5uifcM3aUd6AUg.PNG/%EA%B7%B8%EB%A6%BC_1-5.png?type=w966)  
[※ "Artificial Intelligence in Healthcare Market Size, Report 2034", Precedence Research, 2024.08.09](https://www.precedenceresearch.com/artificial-intelligence-in-healthcare-market)  


## System Architecture  
![엑시노스 AI SDK 구조조](https://image.semiconductor.samsung.com/image/samsung/p6/semiconductor/newsroom/techblog/ondeviceai-251212/pc-contents-01.png?$ORIGIN_PNG$)
- Exynos AI Studio High Level Toolchain (EHT) 과 Exynos AI Studio Low Level Toolchain (ELT)으로 구성
- 각각 모델 레벨에서 고급 그래프 최적화 및 양자화 수행
- EHT는 
  + 오픈소스 프레임워크 (ONNX, TFLite 등) IR을 입력받아 IR (Intermediate Representation) Converter를 통해 내부 IR로 변환하고, 그래프 최적화를 통해 NPU 실행에 적합한 모델 구조로 조정한다. 
  + 양자화를 통해 모델 크기를 경량화 (온디바이스 환경에서 실행될 수 있도록) 한다.

- ELT는 
  + 각 NPU 세대에 최적화된 로어링 작업을 수행해 모델을 하드웨어에서 실행 가능한 형태로 변환한다. 
  + 컴파일러 단계를 거쳐 NPU에서 구동 가능한 온디바이스 AI 모델로 생성

- 다양한 AI 모델 IR 포맷 지원을 위한 SDK (ONNX, TFLite 등 오픈소스 프레임워크 IR)

![Fig 2. 다양한 AI 입력 모델 IR 처리 방식](https://image.semiconductor.samsung.com/image/samsung/p6/semiconductor/newsroom/techblog/ondeviceai-251212/pc-contents-02.png?$ORIGIN_PNG$)  
  + SDK 내부의 IR Converter를 거친 다양한 입력 IR은 Exynos 온디바이스 AI 개발에 최적화된 내부 IR로 변환

- Simulator/Emulator  
  + 로어링 과정 시, 각 모듈의 기능을 강화하고 정확도 손실을 최소화하기 위한 단계별 툴체인 검증 기능 필요

![Simulator/Emulator 기반 단계별 검증 Process](https://image.semiconductor.samsung.com/image/samsung/p6/semiconductor/newsroom/techblog/ondeviceai-251212/pc-contents-03.png?$ORIGIN_PNG$)
  + Exynos AI Studio의 EHT 모듈 출력값은 시뮬레이션 기능을 통해 원본 모델과 연산자 단위로 비교할 수 있다. 이때 SNR(Signal-to-Noise Ratio) 지표를 활용한다. 시뮬레이터는 양자화 정보를 처리하기 위해 특정 연산자를 de-quantize/quantize 연산으로 감싸고, fake quantization 방식으로 연산을 수행하여 정확도를 검증한다. ELT모듈 결과는 에뮬레이터 기능을 통해 정확도를 검증하는데, 이는 EHT 검증 방식과 유사하다. 에뮬레이터는 NPU 하드웨어를 모사한 에뮬레이션 코드를 통해 연산하기 때문에 정밀 검증 가능.






## 핵심 기술  
- NPU, sensor (data gathering), 통신 모듈, os & ui
- 모델 경량화 (Deep Learning framework), AI framework & SDK (Deep Learning framework), algorithms, data processing & inferencing engine 
- 개인정보 보호

## 고려 사항
- Cloud + On-Device 아키텍쳐 필요
  + 어느 시점에, 어떤 AI 연산을 On-Device에서 수행하고 어떤 연산을 Cloud에서 수행할지 정의 필요

---
ㅁ Intermediate Representation (IR) : 여러 딥러닝 프레임워크의 모델들을 하나의 형태로 통합한 뒤 최적화·양자화·컴파일 등의 후처리를 수행하는 하드웨어 비종속적 포맷  
ㅁ   
ㅁ   
ㅁ   









