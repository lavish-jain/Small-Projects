import tkinter as tk
import random
import time

RESPONSES = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.',
            'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
            'Reply hazy, try again', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
            'Don\'t count on it.', 'My reply is no', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
LARGE_FONT = ('Verdana', 12)
MEDIUM_FONT = ('Georgia', 10)


class gui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Magic 8 Ball')

        self.container = tk.Frame(self)
        self.container.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, ResultPage, ThinkingPage):
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

        label1 = tk.Label(self, text="Magic 8 Ball", font=LARGE_FONT)
        label1.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.question = tk.Entry(self)
        self.question.pack(side=tk.TOP, padx=10, pady=10)

        button1 = tk.Button(self, text="Clear", command=self.clear_text)
        button1.pack(side=tk.TOP, padx=10, pady=10)

        button2 = tk.Button(self, text="ASK!", command=lambda: self.show_result(controller))
        button2.pack(side=tk.TOP, padx=10, pady=10)

    def clear_text(self):
        self.question.delete(0, tk.END)

    def show_result(self, controller):
        if len(self.question.get()) == 0:
            controller.show_frame(StartPage)
        else:
            controller.show_frame(ThinkingPage)
            ResultPage.get_answer()
            controller.after(random.randint(1000,5000), controller.show_frame, ResultPage)

class ResultPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ResultPage.text = tk.StringVar()
        label1= tk.Label(self, text="The Results are Out!", font=LARGE_FONT)
        label1.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)

        label2 = tk.Label(self, textvariable=self.text, font=MEDIUM_FONT, fg='green')
        label2.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)
        

        button1 = tk.Button(self, text="Play Again!", command=lambda: controller.show_frame(StartPage))
        button1.pack(side=tk.TOP, padx=10, pady=10)

        button2 = tk.Button(self, text="Quit", command=controller.destroy)
        button2.pack(side=tk.TOP, padx=10, pady=10)

    def get_answer():
        ResultPage.text.set(random.choice(RESPONSES))

class ThinkingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Thinking...", font=LARGE_FONT)
        label.pack(side=tk.TOP, padx=10, pady=10, fill=tk.BOTH, expand=True)