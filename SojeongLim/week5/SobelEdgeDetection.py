import cv2
import numpy as np

# 1. 이미지 불러오기
img = cv2.imread(r'python_study/week5/sample.jpg', cv2.IMREAD_GRAYSCALE)  # 흑백 이미지로 변환

# 2. Sobel 필터 적용
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # x 방향 미분
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # y 방향 미분

# 3. Gradient 크기 계산
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)  # sqrt(Gx^2 + Gy^2)

# 4. 결과 출력
cv2.imshow('Original', img)
cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('Sobel Magnitude', sobel_magnitude)

cv2.waitKey(0)
cv2.destroyAllWindows()
