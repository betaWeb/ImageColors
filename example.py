from ImageColors import ImageColors

imColor = ImageColors('./image.jpg')
print(
	f'Color list : {imColor.getColorsList()}\n\n',
	f'Main color : {imColor.getMainColor()}\n\n',
	f'Colors count : {imColor.count()}\n')
