# Viết chương trình đọc và chuyển đổi file ảnh

import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(cX, cY) = (image.shape[1] / 2 , image.shape[0]/2)
radius = 120
mask = np.zeros(image.shape[:2], dtype = "uint8")
cv2.circle(mask, (cX, cY), radius, 255, -1)
masked = cv2.bitwise_and(image, image, mask = mask)
avatar = masked[ cY - radius : cY + radius, cX - radius : cX + radius]
cv2.imshow("Mask", mask)
cv2.imshow("Avatar", avatar)
cv2.imwrite("avatar.jpg", avatar)
cv2.waitKey(0)
 