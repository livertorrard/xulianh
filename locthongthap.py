import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('logo.png',0)
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
rows, cols = img.shape
crow,ccol=round(rows/2),round(cols/2)
# Tao mot mat la, hinh vuong trung tam =1, con lai =0
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-10:crow+10, ccol-10:ccol+10] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Anh goc'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('bien do quang pho'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Anh ket qua '), plt.xticks([]), plt.yticks([])
plt.show()