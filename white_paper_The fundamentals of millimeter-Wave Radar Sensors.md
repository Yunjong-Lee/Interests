---
date: 2024-03-23 16:51:21
layout: post
---

# [The fundamentals of millimeter wave radar sensors](https://www.tij.co.jp/jp/lit/wp/spyy005a/spyy005a.pdf?ts=1711143374972)

# Introduction

# Range measurement
## Range resolution


# Velocity measurement
## Velocity measurement with two chirps

## Velocity measurement with multiple objects at the same range

## Velocity resolution

# Angle Detection

## Angle Estimation

## Maximum Angular Field of View
- The maximum angular field of view of the radar is
defined by the maximum AoA that the radar can
estimate. See Figure 13. 
- Unambiguous measurement of angle requires $\Delta$ < 180$^\circ$ 



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