import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

print("Press SPACE to capture image")
print("Press Q to quit")

while True:

    ret, frame = cap.read()
    if not ret:
        break

    display = frame.copy()

    cv2.putText(display,"Press SPACE to capture",(20,30),
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),2)

    cv2.imshow("Camera", display)

    key = cv2.waitKey(1) & 0xFF
    # Capture image
    if key == 32:

        img = frame.copy()

        h, w = img.shape[:2]
        img = img[int(h*0.2):int(h*0.8), int(w*0.2):int(w*0.8)]

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(5,5),0)
        _, bw = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

        kernel = np.ones((3,3),np.uint8)
        bw = cv2.morphologyEx(bw,cv2.MORPH_OPEN,kernel)
        contours, _ = cv2.findContours(bw,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        draw = img.copy()

        total = 0
        round_count = 0
        rect_count = 0
        capsule_count = 0

        for cnt in contours:

            area = cv2.contourArea(cnt)

            if area < 400:
                continue

            x,y,w_box,h_box = cv2.boundingRect(cnt)

            aspect_ratio = w_box/float(h_box)

            perimeter = cv2.arcLength(cnt,True)

            if perimeter == 0:
                continue

            circularity = 4*np.pi*area/(perimeter*perimeter)

            label = "Rect"
            color = (0,255,255)

            # ROUND
            if circularity > 0.8 and 0.8 < aspect_ratio < 1.2:

                label = "Round"
                color = (0,255,0)
                round_count += 1

            # ELONGATED PILLS
            elif aspect_ratio > 1.4 or aspect_ratio < 0.7:

                roi = img[y:y+h_box, x:x+w_box]
                mask = bw[y:y+h_box, x:x+w_box]

                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

                hue = hsv[:,:,0]

                pill_pixels = hue[mask==255]

                if len(pill_pixels) > 50:

                    hue_range = np.max(pill_pixels) - np.min(pill_pixels)

                    if hue_range > 15:

                        label = "Capsule"
                        color = (255,0,0)
                        capsule_count += 1

                    else:

                        label = "Rect"
                        color = (0,255,255)
                        rect_count += 1

                else:
                    rect_count += 1

            else:

                rect_count += 1

            total += 1

            cv2.rectangle(draw,(x,y),(x+w_box,y+h_box),color,2)

            cv2.putText(draw,label,(x,y-5),
                        cv2.FONT_HERSHEY_SIMPLEX,0.6,color,2)

        cv2.putText(draw,"Total: "+str(total),(20,30),
                    cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)

        cv2.putText(draw,"Round: "+str(round_count),(20,60),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

        cv2.putText(draw,"Rect: "+str(rect_count),(20,85),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2)

        cv2.putText(draw,"Capsule: "+str(capsule_count),(20,110),
                    cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

        cv2.imshow("SMARTPHARMA - Result", draw)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()