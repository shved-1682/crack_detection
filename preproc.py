from PIL import Image, ImageEnhance


class PreprocessingImg:
    def __init__(self):
        print("init PreprocessingImg")

    def stay_gray(
        self,
        save_path: str,
        tail: str,
        name: str
    ) -> None:
        img = Image.open(f"{tail}/{name}")
        gray_img = img.convert("L")
        gray_img.save(save_path)
        print("Gray DONE")


    def contrast(
        self,
        save_path: str,
        contrast_factor: float=1.0
    ) -> None:
        # open(save_path) because gray_img saved on this path
        img = Image.open(save_path)
        enhancer_contrast = ImageEnhance.Contrast(img)
        contrast_img = enhancer_contrast.enhance(contrast_factor)
        contrast_img.save(save_path)
        print("Contrast DONE")


    def brightness(
        self,
        save_path: str,
        light_factor: float=1.0
    ) -> None:
        # open(save_path) because gray_img saved on this path
        img = Image.open(save_path)
        enhancer_light = ImageEnhance.Brightness(img)
        br_img = enhancer_light.enhance(light_factor)
        br_img.save(save_path)
        print("Brightness DONE")


    def sharpness(
        self,
        save_path: str,
        sharpness_factor: float=1.0
    ) -> None:
        # open(save_path) because gray_img saved on this path
        img = Image.open(save_path)
        enhancer_sharpness = ImageEnhance.Sharpness(img)
        sh_img = enhancer_sharpness.enhance(sharpness_factor)
        sh_img.save(save_path)
        print("Sharpness DONE")
