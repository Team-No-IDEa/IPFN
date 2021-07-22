import tkinter as tk
import tkinter.font as tkf
from web import *

class Gui():
	def startup(self):
		"""Creates the tkinter window
		Param: 
		Returns: tk window
		Raises: 
		"""
		window = tk.Tk()
		return window

	def create_frames(self, window):
		"""Creates all the main frames for the UI
		Param: window - the main TK window
		Returns: Tuple of the URL frame (which will take the URL of the news article), web frame (which will hold the web page preview)
			and right frame (which will hold the suggested web pages)
		Raises: 
		"""

		# create title box

		frm_title_border = tk.Frame(master=window,bd=10, height=160, bg="black")
		frm_title = tk.Frame(master=frm_title_border, bd=30, height=100, bg="#99d8ea")
		frm_title_border.pack(fill=tk.X)
		frm_title.pack(fill=tk.X)

		if True:
			_ = tk.Label(master=frm_title, text="Information Provenance for Fake News", font=("MS Sans Serif", 30, "bold"), bg="#99d8ea")
			_.pack(side=tk.LEFT)
	
		# create frame for the rest of the window that will be under title
	
		frm_main = tk.Frame(master=window, height=300, width=600)
		frm_main.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=True)

		# create frames for left and right hand sides

		frm_main_left = tk.Frame(master=frm_main, bg="white")
		frm_main_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
		if True:
			frm_main_right_border = tk.Frame(master=frm_main, bg="Black", bd=10)
			frm_main_right_border.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True) # hides some code (makes things look nicer <3)
		frm_main_right=tk.Frame(master=frm_main_right_border, bg="white")
		frm_main_right.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)
	
		# create URL input box frame

		frm_url_border = tk.Frame(master=frm_main_left, bd=10, height=130, bg="black")
		frm_url = tk.Frame(master=frm_url_border, height=110, bg="Light gray")
		frm_url_border.pack(fill=tk.X)
		frm_url.pack(fill=tk.X)
	
		# create webpage frame 

		frm_web_border = tk.Frame(master=frm_main_left, bd=10, height=520, bg="black")
		frm_web = tk.Frame(master=frm_web_border, height=500)
		frm_web_border.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
		frm_web.pack(fill=tk.BOTH, side=tk.TOP, expand=True)
	
		# return

		return frm_url, frm_web, frm_main_right


	def clear_suggested_frames(self):
		for index,frm in enumerate(self.frm_suggest_lst):
			frm.pack_forget()
			self.frm_suggest_lst_border[index].pack_forget()
			frm.destroy()
			self.frm_suggest_lst_border[index].destroy()


	def setup_suggested_page_frames(self, frm_main_right, number_of_articles):
		for i in range(number_of_articles):
			# create border for article and then articles
			self.frm_suggest_lst_border.append(tk.Frame(master=frm_main_right, height=30, bd=5))
			self.frm_suggest_lst.append(tk.Frame(master=self.frm_suggest_lst_border[i], bg="Light gray"))
			self.frm_suggest_lst_border[i].pack(fill=tk.BOTH, side=tk.TOP, expand=True)
			self.frm_suggest_lst[i].pack(fill=tk.BOTH, side=tk.TOP, expand=True)


	def setup_url_frm(self, frm_url, right_frm):
		self.ent_url = tk.Entry(master=frm_url, font=("MS Sans Serif",30))
		self.ent_url.pack(fill=tk.BOTH, expand=True)


	def get_pages(self, frm_main_right):
		print("test3")
		self.clear_suggested_frames()
		# check url is valid 
		if (self.ent_url is not None) and Web.validate_url(self.ent_url.get()):
			print("Test")
		else:
			"Test2"
			# pass it into the main code

		#self.setup_suggested_page_frames(frm_main_right, 5)

	# todo: html/css reader for mini-webpage in the application


	def __init__(self):

		self.frm_suggest_lst = [] 
		self.frm_suggest_lst_border = []
		self.ent_url = None
		inp_buffer = ""

		window = self.startup()
		frm_url, frm_web, frm_main_right = self.create_frames(window)
		self.setup_url_frm(frm_url,frm_main_right)
		while True:
			if self.ent_url.get() != inp_buffer:
				inp_buffer = self.ent_url.get()
				self.get_pages(frm_main_right)


if __name__ == "__main__":
	b = Gui()
