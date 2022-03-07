# [A Sensor Fused Rear Cross Traffic Detection System Using Transfer Learning](https://www.mdpi.com/1424-8220/21/18/6055/htm)
- summary
  - proposes a RCT detection system by fusing information from the rear view camera and short range radar  
  - The overall architecture of the proposed RCT detection system  
  ![img](https://www.mdpi.com/sensors/sensors-21-06055/article_deploy/html/images/sensors-21-06055-g001-550.jpg)
  
  deep learning methods:
    - CNN () / SSD(model) 
- 
* 참고: CNN 주요 모델
  . AlexNoet : 의미있는 성능을 낸 첫번째 CNN 아키텍처로, 드롭아웃 기법 적용 등 선도적 역할  
    - conv layer, max-pooling layer, dropout layer 5개  
    - fully connected layer 3개  
    - nonlinearity function: Relu  
    - batch stochatic gradient descent  
  ![img](https://i.imgur.com/CwIvlUW.png)
  
  . GoogleNet : 하나의 layer에 다양한 종류의 filter나 pooling을 도입 (inception module, 1x1 conv filter)
    - 현재 층 입력데이터 이미지의 차원수가 100×100×60이고, 1×1 conv filter를 20개 사용한다면 데이터의 차원 수는 100×100×20으로 감소(차원 축소)  
  ![img](https://i.imgur.com/VY3BkBR.png)
  
  . ResNet : 층이 깊어질 수록 역전파되는 그래디언트가 중간에 죽어서 학습이 잘 되지 않는 문제(gradient vanishing)를 residual block으로 해결  
  ![img](https://i.imgur.com/fse3Ntq.png)
  
  . DenseNet : 전체 네트워크의 모든 층과 통하는 지름길 구축  
  ![img](https://i.imgur.com/EITg2BX.png)
  
  . Region Based CNNs : object detection 문제를 풀기 위해 제안된 모델  
  ![img](https://i.imgur.com/JN72JHW.png)
  
  . CNNs for NLP
  ![img](https://i.imgur.com/WDVOZIH.png)
  
  
  
  
