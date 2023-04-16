import numpy as np
import skimage
from matplotlib import pyplot as plt


def find_crack(path: str):
    SAVE_PATH = "./img_gabora/expls"
    crack_list = []
    image = skimage.io.imread(path, as_gray=True)
    height = image.shape[0]
    width = image.shape[1]

    file_name = path.split("/")[-1]

    for coef in np.arange(0.2, 0.8, 0.05):
        start = (height * coef, 0)  # Start of the profile line row=100, col=0
        end = (height * coef, width - 1)  # End of the profile line row=100, col=last

        # profile intensity
        profile = skimage.measure.profile_line(image, start, end)
        crack_count = np.sum(profile == 255) // 2
        crack_list.append(crack_count)

        # Image profile intensity
        fig, ax = plt.subplots(1, 2)
        ax[0].set_title('Image')
        ax[0].imshow(image)
        ax[0].plot([start[1], end[1]], [start[0], end[0]], 'r')
        ax[1].set_title('Profile')
        ax[1].plot(profile)
        plt.savefig(f"{SAVE_PATH}/{coef}_{file_name}")

    print(crack_list)
    print(sum(crack_list) / len(crack_list))


find_crack(path="./img_gabora/expls/1_0%_crack_1x (2).jpg")
# img\expls\1_0%_crack_1x (2).jpg
# img_gabora\expls\1_0%_crack_1x (2).jpg
