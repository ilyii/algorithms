"""
Canny operator for edge detection.
"""

import numpy as np
import cv2
import requests
import matplotlib.pyplot as plt

def canny(image: np.array):
    """
    Canny operator for edge detection.

    Args:
    image (np.array): Grayscale image.

    Returns:
    np.array: Edge image.
    
    """

    # 1. Gaussian blur
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # 2. Gradient calculation
    gx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    gradient = np.sqrt(gx ** 2 + gy ** 2)
    gradient = gradient / gradient.max() * 255
    theta = np.arctan2(gy, gx)

    # 3. Non-maximum suppression
    rows, cols = image.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            angle = theta[i, j] * 180 / np.pi # $$\theta \in [-\pi, \pi] \to [0, 180]$$
            if (0 <= angle < 22.5) or (157.5 <= angle <= 180):
                before = gradient[i, j - 1]
                after = gradient[i, j + 1]
            elif 22.5 <= angle < 67.5:
                before = gradient[i - 1, j - 1]
                after = gradient[i + 1, j + 1]
            elif 67.5 <= angle < 112.5:
                before = gradient[i - 1, j]
                after = gradient[i + 1, j]
            else: 
                before = gradient[i - 1, j + 1]
                after = gradient[i + 1, j - 1]
            if gradient[i, j] < before or gradient[i, j] < after:
                gradient[i, j] = 0

    # 4. Hysteresis thresholding 
    low_threshold = 0.05 * gradient.max() # 5% of the maximum gradient value
    high_threshold = 0.09 * gradient.max() # 9% of the maximum gradient value
    strong = np.where(gradient > high_threshold, 255, 0)
    weak = np.where((gradient >= low_threshold) & (gradient <= high_threshold), 75, 0)
    return strong + weak

if __name__ == "__main__":

    url = r"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Chessboard480.svg/416px-Chessboard480.svg.png"

    response = requests.get(url)
    image = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_GRAYSCALE)
    print(image.shape)
    edges = canny(image)
    
    plt.figure(figsize=(12, 6))
    plt.subplot(121)
    plt.imshow(image, cmap="gray")
    plt.title("Original Image")
    plt.subplot(122)
    plt.imshow(edges, cmap="gray")
    plt.title("Edges")
    plt.show()
    

