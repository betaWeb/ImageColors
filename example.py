from ImageColors import ImageColors

imColor = ImageColors('./image.jpg')
print(
	f'Color list : {imColor.get_colors_list()}\n\n',
	f'Main color : {imColor.get_main_color()}\n\n',
	f'Colors count : {imColor.count()}\n')
