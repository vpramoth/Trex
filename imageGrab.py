import numpy as np
import cv2
from PIL import ImageGrab as ig

img = ig.grab((200,200,500,500))
img_np = np.array(img)
# img_cv = cv2.cvtColor(img_np)
img.show()
# cv2.imshow("alpha", img_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print img_np