from ImageColors import ImageColors

imColor = ImageColors('./image.jpg')
print(
	imColor.getColorsList(),
	imColor.getMainColor(),
	imColor.count())
