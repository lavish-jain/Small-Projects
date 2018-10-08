import tkinter as tk 
from backend import RockPaperScissors

LARGE_FONT = ('Verdana', 12)
# MEDIUM_FONT = ('Georgia', 10)
SMALL_FONT = ('Helvetica', 9)
ROCK = "ROCK"
PAPER = "PAPER"
SCISSOR = "SCISSOR"

class gui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Magic 8 Ball')

        self.container = tk.Frame(self)
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage,):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        StartPage.choice = tk.StringVar()

        label1 = tk.Label(self, text="Rock Paper Scissors!", font=LARGE_FONT)
        label1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        label2 = tk.Label(self, text="Choose your move: ", font=SMALL_FONT)
        label2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        rock = tk.Radiobutton(self, text=ROCK, value=ROCK, font=SMALL_FONT, variable=StartPage.choice)
        rock.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        paper = tk.Radiobutton(self, text=PAPER, value=PAPER, font=SMALL_FONT, variable=StartPage.choice)
        paper.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        scissor = tk.Radiobutton(self, text=SCISSOR, value=SCISSOR, font=SMALL_FONT, variable=StartPage.choice)
        scissor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        button2 = tk.Button(self, text="PLAY!", command=lambda: self.show_result(choice, controller))
        button2.pack(side=tk.TOP, padx=10, pady=10)

        button1 = tk.Button(self, text="Quit", command=controller.destroy)
        button1.pack(side=tk.TOP, padx=10, pady=10)

    def show_result(choice, controller):
        pass        