import os
from glob import glob

import cv2
import numpy as np

from preproc import PreprocessingImg


def create_gabor_filter(
) -> list:
    """
    Эта функция предназначена для создания набора GaborFilters
    с равномерным распределением тета-значений, равномерно 
    распределенных между Пи рад / 180 градусов.
    """
    filters = []
    num_filters = 16
    ksizes = (31, 31)
    sigma = 1.0     # 3.0
    lambd = 12.0    # 12.0
    gamma = .3      # .2
    psi = 0.0
    for theta in np.arange(0, np.pi / 12, np.pi / 12 / num_filters):
        kern = cv2.getGaborKernel(
            # Первый параметр: размер Размер ядра, как правило, нечетное число
            ksize=ksizes,
            # σ представляет стандартное отклонение функции Гаусса,
            # чем больше стандартное отклонение, тем больше пульсаций
            sigma=sigma,
            # θ представляет угол гофра
            theta=theta,
            # λ представляет длину волны, чем длиннее длина волны, тем плотнее
            lambd=lambd,
            # γ представляет отношение длинной и короткой оси эллипса, когда оно равно 1,
            # оно является круглым
            gamma=gamma,
            # Шестой параметр: пси означает сдвиг фазы, -180 ~ +180, обычно 0
            psi=psi,
            ktype=cv2.CV_64F
        )
        kern /= 1.0 * kern.sum()  # Нормализация яркости
        filters.append(kern)

    return filters


def apply_g_filter(
    img,
    filters
):
    """
    First create a numpy array the same size as our input image
    Начиная с пустого изображения, мы перебираем изображения и 
    применяем наш фильтр Габора.
    На каждой итерации мы берем наибольшее значение (суперналожение),
    пока не получим максимальное значение по всем фильтрам.
    Окончательное изображение возвращается
    """
    DEPTH = -1 # глубина остается такой же, как у исходного изображения
    new_image = np.zeros_like(img)
     
    for kern in filters:  # Loop through the kernels in our GaborFilter
        image_filter = cv2.filter2D(img, DEPTH, kern)  #A pply filter to image
        # Using Numpy.maximum to compare our filter and cumulative image,
        # taking the higher value (max)
        np.maximum(new_image, image_filter, new_image)

    return new_image


def create_gabora_img(
    save_path: str,
    tail: str,
    name: str,
    filters: list,
) -> None:
    MIN_INTERVAL = 0
    MAX_INTERVAL = 255

    # Photo preprocessing
    preprocessing_img.stay_gray(
        save_path=save_path,
        tail=tail,
        name=name
    )
    preprocessing_img.contrast(
        save_path=save_path,
        contrast_factor=2.0
    )
    preprocessing_img.brightness(
        save_path=save_path,
        light_factor=1.5
    )
    preprocessing_img.sharpness(
        save_path=save_path,
        sharpness_factor=2.0
    )

    img_path = save_path if os.path.exists(save_path) else f"{tail}/{name}"
    image = cv2.imread(img_path)
    # Apply Gabora filter to our image
    image2gabora = apply_g_filter(image, filters)
    image_edge_g = cv2.Canny(
        image2gabora,
        MIN_INTERVAL,
        MAX_INTERVAL,
        L2gradient=False
    )
    # Save img with filter Gabora
    cv2.imwrite(save_path, image_edge_g)
    print("finish one file")


def main(
    save_path: str,
    file_path: str
) -> None:
    gabora_filters = create_gabor_filter()  # We create our gabor filters

    if os.path.isfile(FILE_PATH):
        tail, name = os.path.split(FILE_PATH)
        save_path = os.path.normpath(SAVE_PATH + name)
        create_gabora_img(
            save_path=save_path,
            tail=tail,
            name=name,
            filters=gabora_filters
        )
    else:
        img_folder = FILE_PATH.split("\\")[-1]  # Folder name where is img
        # Create folder if image path is not exist
        if os.path.exists(f"{SAVE_PATH}{img_folder}") == False:
            os.mkdir(f"{SAVE_PATH}{img_folder}")
        # Iterates over all files in a folder
        for folders in glob(f"{FILE_PATH}/*"):
            tail, name = os.path.split(folders)
            save_path = os.path.normpath(f"{SAVE_PATH}{img_folder}/{name}")
            create_gabora_img(
                save_path=save_path,
                tail=tail,
                name=name,
                filters=gabora_filters
            )
        else:
            print("FINISH one folder")


if __name__ == "__main__":
    SAVE_PATH = "./img_gabora/"
    FILE_PATH = os.path.normpath("./img/expls/")

    preprocessing_img = PreprocessingImg()

    main(save_path=SAVE_PATH, file_path=FILE_PATH)
