#https://stackoverflow.com/questions/4098131/how-to-update-a-plot-in-matplotlib
import multiprocessing
import time

manager = multiprocessing.Manager()
final_list = manager.list()


def add():
	import tkinter
	top= tkinter.Tk()
	def cbp():
		print("caught a close click")
		final_list.append(1)
	def obp():
		print("caught an open click")
		final_list.append(2)
	c=tkinter.Button(top,text="Close graph",command=cbp)
	c.pack()
	o=tkinter.Button(top,text="open graph",command=obp)
	o.pack()
	top.mainloop()

def sud():
	import matplotlib.pyplot as plt
	import numpy as np
	plt.ion()
	while(True):
		flag=1
		print("this is in process graph")
		if(len(final_list)>0):
			if(final_list[0]==2):
				final_list.remove(2)
				y= np.random.random([10,1])
				for i in range(50):
					if(len(final_list)>0):
						if(final_list[0]==1):
							final_list.remove(1)
							plt.close()
							flag=2
					if flag==1:
						y=np.random.random([10,1])
						plt.plot(y)
						plt.draw()
						plt.pause(1)
						plt.clf()
					elif flag==2:
						break
if __name__ =='__main__':
	p1 = multiprocessing.Process(name='p1',target=add)
	p2 = multiprocessing.Process(name='p1',target=sud)
	p1.start()
	p2.start()
	p1.join()
	p2.join()
