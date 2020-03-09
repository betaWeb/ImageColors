from os import path
from PIL import Image


class ImageColors:
    file_path = ''
    file = None
    colors = {}

    def __init__(self, file_path) -> None:
        """
        :param str file_path the image file path
        """

        self.file_path = file_path

        self.__load_file()
        self.__load_pix()
        self.__set_image_colors_occ()

    def get_colors_list(self) -> list:
        return [c[0] for c in self.colors]

    def get_main_color(self) -> str:
        return self.colors[0][0]

    def count(self) -> int:
        return len(self.colors)

    def __load_file(self) -> None:
        if (path.exists(self.file_path) == False):
            raise FileExistsError(f"File '{self.file_path}' does not exists")

        try:
            self.file = Image.open(self.file_path)
        except Exception:
            raise Exception(f"Cannot load file '{self.file_path}'")

    def __set_image_colors_occ(self) -> None:
        for x in range(self.file.size[0]):
            for y in range(self.file.size[1]):
                key = self.__get_key(x, y)
                if key not in self.colors:
                    self.colors[key] = 1
                else:
                    self.colors[key] += 1

        self.colors = sorted(self.colors.items(),
                             key=lambda kv: kv[1], reverse=True)

    def __load_pix(self) -> None:
        self.__pix = self.file.load()

    def __get_key(self, x, y) -> str:
        pix = list(map(str, self.__pix[x, y]))
        return ','.join(pix[:3])
