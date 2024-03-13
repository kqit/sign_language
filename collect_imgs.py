import os

import cv2


DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 26
start_collect=0
end_collect=0
dataset_size = 150

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Start collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Press "SPACE" to start collecting!', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 155, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('camera', frame)
        if cv2.waitKey(25) == ord(' '):
            break

    count = 0
    while count < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('camera', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(count)), frame)

        count += 1

cap.release()
cv2.destroyAllWindows()
