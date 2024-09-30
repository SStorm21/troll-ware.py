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
