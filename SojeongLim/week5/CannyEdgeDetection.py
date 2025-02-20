import cv2
import numpy as np

# 1. 이미지 불러오기
img = cv2.imread(r'python_study/week5/sample.jpg')

# 2. 그레이스케일 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 가우시안 블러 적용
blur = cv2.GaussianBlur(gray, (5,5), 1.5)

# 4. Canny Edge Detection 실행 (이중 임계값 적용)
edges = cv2.Canny(blur, 100, 200)

# 5. 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


