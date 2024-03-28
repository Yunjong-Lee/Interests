---
date: 2024-02-17 10:11:38
layout: post
---







rangeAzimuthHeatMap array로부터 




### Inter Frame Processing

|  |  |
|--|--|
| VitalSigns_DaaPathObj *obj_VS_zone_1; | VitalSigns_DaaPathObj을 가리키는 포인터 obj_VS_zone_1 |
| obj_VS_zone_1 = &vitalsigns_dataPathObj_zone_1; | 포인터 obj_VS_zone_1에 vitalsigns_dataPathObj_zone_1의 address를 대입 |

- oddemo_rangeAzimuthHeatMap의 0번째 배열의 address(&oddemo_rangeAzimuthHeatMap[0])를 oddemo_dataPathObj 구조체 변수 rangeAzimuthHeatMap(oddemo_dataPathObj.rangeAzimuthHeatMap)에 대입
- oddemo_rangeAzimuthHeatMap data로 arc removal 수행(arc removal 수행 결과는 oddemo_rangeAzimuthHeatMap에 update)

※ "/=" (할당연산자) : 저신을 오른쪽 값으로 나누어 몫을 대입




