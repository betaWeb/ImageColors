from os import path
from PIL import Image

class ImageColors:
	file_path = ''
	file = None
	colors = {}

	def __init__(self, file_path):
		self.file_path = file_path

		self.__loadFile()
		self.__loadPix()
		self.__setImageColorsOccurrences()


	def getColorsList(self):
		return [c[0] for c in self.colors]

	
	def getMainColor(self):
		return self.colors[0]


	def count(self):
		return len(self.colors)

	
	def __loadFile(self):
		if (path.exists(self.file_path) == False):
			raise FileExistsError("File '%s' does not exists" % (self.file_path))

		print("Loading file '%s'..." % (path.basename(self.file_path)))
		
		try:
			self.file = Image.open(self.file_path)
		except Exception:
			raise Exception("Cannot load file '%s'" % (self.file_path))


	def __setImageColorsOccurrences(self):
		for x in range(self.file.size[0]):
			for y in range(self.file.size[1]):
				key = self.__getKey(x, y)
				if key not in self.colors:
					self.colors[key] = 1
				else:
					self.colors[key] += 1

		self.colors = sorted(self.colors.items(), key=lambda kv: kv[1], reverse=True)

		
	def __loadPix(self):
		self.__pix = self.file.load()


	def __getKey(self, x, y):
		return ','.join(map(str, self.__pix[x,y]))
