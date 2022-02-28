from MarkovNetwork import *
img_noisy=mpimg.imread('img/05_25_noisy.png')
plt.imshow(img_noisy, cmap='gray')
(size_x, size_y) = img_noisy.shape
print("Image size:")
print(size_x, "x", size_y)

stochastic_search(img_noisy, max_iter=30)