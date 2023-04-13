import numpy as np
import skimage
from matplotlib import pyplot as plt

image = skimage.io.imread("img_gabora/expls/1_50%_x1(1).jpg", as_gray=True)
height = image.shape[0]
width = image.shape[1]

start = (height / 2, 0)  # Start of the profile line row=100, col=0
end = (height / 2, width - 1)  # End of the profile line row=100, col=last

# profile intensity
profile = skimage.measure.profile_line(image, start, end)

crack_count = np.sum(profile == 255) // 2
print(crack_count)

# Image profile intensity
fig1 = plt.plot(profile)
plt.savefig('img/expls/test1.jpg')

# Image :)
_, ax = plt.subplots()
ax.imshow(image)
plt.savefig('img/expls/test2.jpg')


# fig, ax = plt.subplots(1, 2)
# ax[0].set_title('Image')
# ax[0].imshow(image)
# ax[0].plot([start[1], end[1]], [start[0], end[0]], 'r')
# ax[1].set_title('Profile')
# ax[1].plot(profile)
# fig.savefig('img/expls/test.jpg')


