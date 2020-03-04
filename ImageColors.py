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

		self.__loadFile()
		self.__loadPix()
		self.__setImageColorsOccurrences()


	def getColorsList(self) -> list:
		return [c[0] for c in self.colors]

	
	def getMainColor(self) -> str:
		return self.colors[0][0]


	def count(self) -> int:
		return len(self.colors)

	
	def __loadFile(self) -> None:
		if (path.exists(self.file_path) == False):
			raise FileExistsError(f"File '{self.file_path}' does not exists")
		
		try:
			self.file = Image.open(self.file_path)
		except Exception:
			raise Exception(f"Cannot load file '{self.file_path}'")


	def __setImageColorsOccurrences(self) -> None:
		for x in range(self.file.size[0]):
			for y in range(self.file.size[1]):
				key = self.__getKey(x, y)
				if key not in self.colors:
					self.colors[key] = 1
				else:
					self.colors[key] += 1

		self.colors = sorted(self.colors.items(), key=lambda kv: kv[1], reverse=True)


	def __loadPix(self) -> None:
		self.__pix = self.file.load()


	def __getKey(self, x, y) -> str:
		return ','.join(map(str, self.__pix[x,y]))
