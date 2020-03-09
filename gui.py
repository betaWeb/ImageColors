from tkinter import *
from tkinter import filedialog, StringVar
from PIL import ImageTk, Image
from ImageColors import ImageColors
import tkinter as tk

img_container = None
main_color_cv = None
filepath_label = None
root_w = 640
root_h = 640


def choose_image() -> None:
    destroy_image()
    destroy_main_color()
    destroy_filepath_label()

    root.update()

    filepath = filedialog.askopenfilename(
        initialdir="/", title="Pick an image",
        filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"), ("gif files", "*.gif"), ("all files", "*.*")))

    image = handle_image(filepath)
    main_color = get_main_color(filepath)

    display_path_label(filepath)
    display_image(image)
    display_main_color(main_color)

    pick_btn_text.set("Pick another image")


def handle_image(filepath: str, width: int = int(root_w/2), height: int = int(root_h/2)) -> ImageTk.PhotoImage:
    im = Image.open(filepath)
    thumb = im.resize((width, height))
    return ImageTk.PhotoImage(thumb)


def display_image(image: ImageTk.PhotoImage) -> None:
    global img_container

    img_container = Label(
        root, image=image, width=image.width(), height=image.height())
    img_container.image = image
    img_container.grid(row=1, column=0)


def destroy_image() -> None:
    global img_container

    if img_container:
        img_container.grid_forget()
        img_container.destroy()
        img_container = None


def get_main_color(filepath: str) -> str:
    try:
        f_color = ImageColors(filepath)
        return _from_rgb(f_color.get_main_color())
    except Exception as e:
        raise e


def display_main_color(main_color: str) -> None:
    global main_color_cv

    main_color_cv = Canvas(root, width=int(root_w/2),
                           height=int(root_h/2), bg=main_color)
    main_color_cv.grid(row=1, column=1)


def destroy_main_color() -> None:
    global main_color_cv

    if main_color_cv:
        main_color_cv.grid_forget()
        main_color_cv.destroy()
        main_color_cv = None


def display_path_label(filepath: str) -> None:
    global filepath_label

    filepath_label = Label(root, text=f"Path: {filepath}")
    filepath_label.grid(row=0, columnspan=2)


def destroy_filepath_label() -> None:
    global filepath_label

    if filepath_label:
        filepath_label.grid_forget()
        filepath_label.destroy()
        filepath_label = None


def _from_rgb(rgb_str: str) -> str:
    rgb = tuple(map(lambda x: int(x), rgb_str.split(',')))
    return "#%02x%02x%02x" % rgb[0:3]


root = Tk()
root.title("Image colors infos")
# root.geometry(f"{root_w}x{root_h}")
root.configure(background='grey')

pick_btn_text = StringVar(root)
pick_btn_text.set("Pick image")

pick_btn = Button(root, textvariable=pick_btn_text, command=choose_image)
pick_btn.grid(columnspan=2, row=2, sticky=S+W+E)

root.mainloop()
