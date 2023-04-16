import os
from glob import glob

from gabora_filter import create_gabor_filter, create_gabora_img


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
    SAVE_PATH = os.path.normpath("./img_gabora/")
    FILE_PATH = os.path.normpath("./img/expls/")

    main(save_path=SAVE_PATH, file_path=FILE_PATH)
