# SmartPharma: Pill Counter

Counts the pills placed under a webcam and sorts them into **round tablets, rectangular tablets and capsules**, using classical computer vision (no training data needed).

Computer Vision course, KMITL, 2026. Team of 2.

![Results on 10 arrangements](media/test_results.png)

## How it works (`pill_counter.py`)
1. Live webcam view. Press SPACE to capture, Q to quit.
2. Convert to grayscale, Gaussian blur, then **Otsu threshold** to separate the pills from the black background.
3. **Morphological opening** removes noise. A **distance transform** helps split pills that touch.
4. For each contour: area, aspect ratio and circularity. Round pills are found by circularity. Long shapes are checked with **HSV colour** to tell capsules from rectangular tablets.
5. Draw labelled boxes and show the total and the count per type.

## The rig (my CAD and print)
I modelled and 3D-printed the whole rig in Fusion 360: a 20 x 20 cm black base and an arm that holds the camera 30 cm above the centre. The base is flat on purpose, so it prints without supports.

| Rig | Setup |
|---|---|
| ![](media/01_stand_with_pills_closeup.jpg) | ![](media/02_setup_laptop_angle.jpg) |

## Results and limits
It was tested on 10 different arrangements and classified most pills correctly. Errors happen when pills touch or overlap.
Classical rules can't separate look-alike or stacked pills. A trained detector (for example YOLO) plus a vibrating tray to spread the pills out would fix that.
