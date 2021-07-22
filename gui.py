import tkinter as tk
import tkinter.font as tkf

def startup():
	"""Creates the tkinter window
	Param: 
	Returns: tk window
	Raises: 
	"""
	window = tk.Tk()
	return window

def create_frames(window):
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

def setup_suggested_page_frames(frm_main_right, number_of_articles):
	suggested_page_frm_lst = []
	suggested_page_frm_lst_borders = []
	for i in range(number_of_articles):
		# create border for article and then 
		suggested_page_frm_lst_borders.append(tk.Frame(master=frm_main_right, height=30, bd=5))
		suggested_page_frm_lst.append(tk.Frame(master=suggested_page_frm_lst_borders[i], bg="Light gray"))
		suggested_page_frm_lst_borders[i].pack(fill=tk.BOTH, side=tk.TOP, expand=True)
		suggested_page_frm_lst[i].pack(fill=tk.BOTH, side=tk.TOP, expand=True)

	return suggested_page_frm_lst

def setup_url_frm(frm_url):
	ent_url = tk.Entry(master=frm_url, font=("MS Sans Serif",30))
	ent_url.pack(fill=tk.BOTH, expand=True)
	return ent_url

def main():
	window = startup()
	frm_url, frm_web, frm_main_right = create_frames(window)
	ent_url = setup_url_frm(frm_url)
	frm_suggest_lst = setup_suggested_page_frames(frm_main_right, 5)
	window.mainloop()


if __name__ == "__main__":
	main()