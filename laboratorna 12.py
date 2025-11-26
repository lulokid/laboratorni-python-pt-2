import cv2
import numpy as np

img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")

if img1 is None or img2 is None:
    print("Одне або обидва зображення не знайдено.")
    exit()

# перетворення у відтінки сірого
g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create(nfeatures=2000)

# ключові точки та дескриптори
kp1, des1 = orb.detectAndCompute(g1, None)
kp2, des2 = orb.detectAndCompute(g2, None)

# пошук схожрстей
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# відмінності
diff_mask = np.zeros_like(g1)
GOOD_DISTANCE = 35 #якщо відстань між ознаками > 35, то це уже відмінність

for m in matches:
    x1, y1 = kp1[m.queryIdx].pt
    if m.distance > GOOD_DISTANCE:
        cv2.circle(diff_mask, (int(x1), int(y1)), 10, 255, -1)

# збільшення білої області
kernel = np.ones((7, 7), np.uint8)
diff_mask = cv2.dilate(diff_mask, kernel, iterations=2)

# кольорова карта
diff_color = cv2.applyColorMap(diff_mask, cv2.COLORMAP_JET)

# накладання карт
diff_on_img1 = cv2.addWeighted(img1, 0.7, diff_color, 0.7, 0)
diff_color_resized = cv2.resize(diff_color, (img2.shape[1], img2.shape[0]))
diff_on_img2 = cv2.addWeighted(img2, 0.7, diff_color_resized, 0.7, 0)


cv2.imshow("differance on image 1", diff_on_img1)
cv2.imshow("differance on image 2", diff_on_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
