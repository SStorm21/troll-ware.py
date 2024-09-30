import threading
global word,num
num=10
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
ammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammarammar
	"""

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