import numpy as np
import cv2  


img = cv2.imread("mozgus.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Mozgus", img)

k = cv2.waitKey(0)

if k == 27: 
    cv2.destroyAllWindows()
 


