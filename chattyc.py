import tkinter as tk
from tkinter import *
import socket               # Import socket module
import select

root = tk.Tk()

T = tk.Text(root, height=20, width = 50, state = NORMAL)
T.pack(side=TOP)


T2 = tk.Text(root, height=1, width=50)
T2.pack(side=LEFT)
T2.insert(tk.END, "")

def buttonclick():
	task()

def buttonclient():
	pass

def buttonserver():
	pass

button1 = Button(root, text = "SEND", fg = "black", bg = "white", command = buttonclick)
button1.pack(side=RIGHT)
buttonc = Button(root, text = "client", fg = "black", bg = "white", command = buttonclient)
buttonc.pack(side=RIGHT)
buttons = Button(root, text = "server", fg = "black", bg = "white", command = buttonserver)
buttons.pack(side=RIGHT)
T.insert(tk.END, "\n I'm client")

s = socket.socket()         # Create a socket object

host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
def task():
	text = T2.get("1.0", "2.0")
	s.send(text.encode())
	#print("HI SERVER")

def listen():
	s.setblocking(0)

	ready = select.select([s], [], [], 0.1)
	if ready[0]:
		T.insert(tk.END, "\nServer: "+str(s.recv(1024)))
	root.after(1000, listen)

root.after(1000, listen)
tk.mainloop()