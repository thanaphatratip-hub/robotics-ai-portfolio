from ultralytics import YOLO
import cv2
import pygame

model = YOLO("best.pt")

print("Model classes:", model.names)

cap = cv2.VideoCapture(0)

pygame.mixer.init()
alarm = pygame.mixer.Sound("alarm.wav")

required_items = ["Helmet", "Vest", "Goggles"]

alarm_on = False

print("Safety Detection Started...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    detected_items = []

    results = model.predict(source=frame, conf=0.3, verbose=False)

    for r in results:
        if r.boxes is not None:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]
                confidence = float(box.conf[0])

                detected_items.append(class_name)

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, f"{class_name} {confidence:.2f}",
                            (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.6, (0,255,0), 2)

    detected_items = list(set(detected_items))

    print("Detected:", detected_items)

    missing_items = [item for item in required_items if item not in detected_items]

    if len(missing_items) == 0:
        status = "PASS"
        color = (0,255,0)

        if alarm_on:
            pygame.mixer.stop()
            alarm_on = False
    else:
        status = "WARNING"
        color = (0,0,255)

        if not alarm_on:
            alarm.play(-1)
            alarm_on = True

    cv2.putText(frame, f"Detected: {detected_items}",
                (10,30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255,255,255), 2)

    if len(missing_items) == 0:
        cv2.putText(frame, status,
                    (10,70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.2, color, 3)
    else:
        cv2.putText(frame, f"{status} - Missing: {', '.join(missing_items)}",
                    (10,70),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, color, 3)

    cv2.imshow("Safety Monitor", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()