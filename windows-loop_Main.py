
from customtkinter import *
from PIL import Image
global times
times=300
def l00p():
	while True:
		main_window= CTk()
		main_window.state('withdraw')
		main_window.title("close me!")
		imag_path="image.jpg"
		ig=Image.open(imag_path)
		ctk_img=CTkImage(light_image=ig,size=(392,359))
		for i in range(times):
			window=CTkToplevel(main_window)
			window.title("ammar ammar ammar ammar ammar ammar ammar ammar")
			window.geometry("392x359")
			label =CTkLabel(window,text=' ',image=ctk_img)
			label.pack(pady=20)
		main_window.mainloop()
def main():
	l00p()
main()
			