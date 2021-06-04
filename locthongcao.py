import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('logo.png',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift)) #tính ra biên độ của các giá trị tầng số
rows, cols = img.shape
crow,ccol=round(rows/2),round(cols/2)
###--------------xoa cac gia tri vung trung tam (vung tan so thap) ---------
## -----------------pham vi ban kich 30 -------------------
fshift[crow-5:crow+5, ccol-5:ccol+5] = 0
#fshift[crow-10:crow+10, ccol-10:ccol+10] = 0
f_ishift = np.fft.ifftshift(fshift)  #biến đổi fourier từ miền fourier sang miền tần số
img_back = np.fft.ifft2(f_ishift) #biến đổi fourier từ miền tần số sang giá trị ban đầu
img_back = np.abs(img_back) # vì có giá trị âm nên sử dụng giá trị tuyệt đối
# hien thi cac anh ket qua
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Anh goc'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Mien Fourier'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
plt.title('Anh ket qua sau loc'), plt.xticks([]), plt.yticks([])
plt.show()