# TinyML Machine-Speed Classifier

Classification of a machine's motor speed from vibration data, running entirely on a microcontroller.

| | |
|---|---|
| **Course** | Robotics Laboratory 3 (01416516), KMITL |
| **Date** | January 2026 |
| **Team** | 2 members |
| **My role** | Shared development of the model and deployment; design and fabrication of the sensor mount |

## Overview

Monitoring the operating state of a machine from its vibration is the basis of condition monitoring and predictive maintenance. This project classifies a motor into four states (idle, 14,000, 15,000 and 17,000 RPM) using an inertial sensor and a small neural network deployed on the sensor board itself.

## My contribution

- Developed the data pipeline and the classifier together with my teammate.
- Designed the sensor mount in Fusion 360 and 3D-printed it in PLA. The mount holds the board in the same position on the motor for every recording, which keeps the vibration readings repeatable.

## Technical approach

- **Hardware:** Arduino Nano 33 BLE with a 9-axis IMU (accelerometer, gyroscope and magnetometer), sampled at 100 Hz.
- **Features:** Edge Impulse spectral-analysis features computed on 2-second windows.
- **Deployment:** the trained model was quantised to int8 and deployed on the board; predictions were verified live over the serial connection.

| CAD model | Printed mount on the motor |
|---|---|
| ![](media/cad_mount.png) | ![](media/printed_mount_on_motor.png) |

## Results

| Metric | Value |
|---|---|
| Classes | 4 |
| Test accuracy (80/20 split) | 100% |
| Inference time | ~1 ms |
| RAM usage | ~1.5 KB |
| Flash usage | ~17.8 KB |
| Signal processing time | ~51–58 ms |

## Limitations

The dataset is small and was recorded under controlled conditions on a single machine. The 100% accuracy demonstrates feasibility but is not evidence of performance in the field. A larger dataset across different machines, mounting positions and noise conditions would be needed.

**Tech stack:** Arduino Nano 33 BLE, Edge Impulse, C++, Fusion 360, 3D printing
