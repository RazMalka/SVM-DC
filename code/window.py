# Data Mining and Machine Learning 2020
# Group Number 2    ->  [Raz Malka | Shoham Yamin | Raz Itzhak Afriat]
# Research Subject  ->  One-Class SVMs for Document Classification

# This file is meant to provide implementation of gui windows
# including graphical presentation, controllers and handlers

# GUI
import tkinter as tk; from tkinter import ttk
import webbrowser as browser

# Data Analysis Libraries
import numpy as np
from scipy import stats

# MatplotLib and Embedding with tkinter
import matplotlib; matplotlib.use("TkAgg");
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure; import matplotlib.pyplot as plt;

# -------------------------------------------------------------------
# General Purpose
def destroyAll(root: tk.Toplevel):
    for widget in root.winfo_children():
        if (isinstance(widget, tk.Toplevel)):
            widget.destroy()
    root.destroy()

def createWindow(width: int, height: int, title: str, root: tk.Toplevel):
    # Create Window Instance and compute position and dimensions
    if root == None: window = tk.Tk()
    else: window = tk.Toplevel(root, bg="white")
    geometry_settings = "%dx%d+%d+%d" % (width, height, (window.winfo_screenwidth()-width)/2, (window.winfo_screenheight()-height)/2)

    # Basic Window Settings
    window.geometry(geometry_settings)
    window.wm_resizable(False, False)
    window.wm_title(title)

    # Return Instance
    return window

def testFunc(str: str):
    print(str)

# -------------------------------------------------------------------
# About Window
def aboutWindow(root: tk.Toplevel):
    about = createWindow(400, 180, "About", root)

    # About Window Content
    title = tk.Label(master=about, text="\nOne-Class SVM Document Classification\nVersion 0.03", bg="white").pack()
    repository_link = tk.Label(master=about, text = "Open Source Repository", fg="Blue", cursor="hand2", bg="white")
    repository_link.bind("<Button-1>", lambda e: browser.open_new("https://github.com/RazMalka/SVM-DC"))
    footer = tk.Label(master=about, text="MIT License © 2020\n\nRaz Malka\tShoham Yamin\tRaz Itzhak Afriat", bg="white")

    # Pack Content into About Window
    repository_link.pack()
    footer.pack()

    # Display About Window
    about.mainloop()

# -------------------------------------------------------------------
# Root Window

# -------------------------------------------------------------------
# Content
representations = ["-", "Binary", "Frequency", "TF-IDF", "Hadamard"]
training_sets = ["-", "Harry Potter", "Game of Thrones"]

leftFrame = rightFrame = item_xpos = item_ypos = figure = canvas = toolbar = None

def exampleFigure():
    global figure, canvas, toolbar

    # Figure
    figure = Figure(figsize=(5,5), dpi=100)
    a = figure.add_subplot(111)

    a.plot([5,6,7,8],[8,9,3,5], 'ro', label="point A")
    a.plot([1,2,3,4],[5,6,1,3], 'go', label="point B")
    a.plot([5,6],[8,9], 'bx', label="point C")
    a.legend(loc="upper left")

    canvas = FigureCanvasTkAgg(figure, rightFrame)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, rightFrame)
    toolbar.config(bg="white")
    toolbar.update()
    toolbar._message_label.config(bg="white")

    canvas.get_tk_widget().pack(side="bottom", fill="both", expand=True, padx=item_xpos, pady=item_ypos)
    canvas._tkcanvas.pack(side="top", fill="both", expand=True, padx=item_xpos, pady=item_ypos)

# EDIT ME
def createFigure():
    global figure, canvas, toolbar

    # Destroy Previous Canvas
    canvas.get_tk_widget().destroy()
    canvas._tkcanvas.destroy()

    # Figure
    figure = Figure(figsize=(5,5), dpi=100)
    a = figure.add_subplot(111)

    a.plot([11,8], [8,9], 'ro', label="BBB")
    a.plot([1,4], [5,3], 'go', label="AAA")
    a.plot([11,4], [8,3], 'bx', label="CCC")
    a.legend(loc="upper left")

    canvas = FigureCanvasTkAgg(figure, rightFrame)
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, rightFrame)
    toolbar.config(bg="white")
    toolbar.update()
    toolbar._message_label.config(bg="white")
    
    canvas.get_tk_widget().pack(side="bottom", fill="both", expand=True, padx=item_xpos, pady=item_ypos)
    canvas._tkcanvas.pack(side="top", fill="both", expand=True, padx=item_xpos, pady=item_ypos)

def initRootFrames(root: tk.Toplevel, width: int, height: int):
    global leftFrame, rightFrame, item_xpos, item_ypos

    item_xpos = width/108
    item_ypos = height/22
    leftFrame = tk.Frame(master=root, bg="white")
    rightFrame = tk.Frame(master=root, bg="white")

def initControlPort(root: tk.Toplevel, width: int, height: int):
    label_controlport = tk.Label(text="Control Port", bg="white").place(x=6.75 * item_xpos, y=0, in_=leftFrame)

    label_rep = tk.Label(text="Representation:", bg="white").place(x=item_xpos,y=height/18, in_=leftFrame)
    label_ts = tk.Label(text="Training Set:", bg="white").place(x=item_xpos,y=height/6, in_=leftFrame)

    combobox_rep = ttk.Combobox(width=int(2 * item_xpos), values=representations)
    combobox_ts = ttk.Combobox(width=int(2 * item_xpos), values=training_sets)

    combobox_rep.current(0)
    combobox_ts.current(0)

    combobox_rep.place(x=item_xpos, y=height/10, in_=leftFrame)
    combobox_ts.place(x=item_xpos, y=height/4.8, in_=leftFrame)

def initViewPort(root: tk.Toplevel, width: int, height: int):
    label_viewport = tk.Label(text="View Port", bg="white").place(x=33 * item_xpos, y=0, in_=rightFrame)
    exampleFigure()

def contentEventHandlers(root: tk.Toplevel, width: int, height: int):
    print("Event Handlers")

def contentPacking(root: tk.Toplevel, width: int, height: int):
    leftFrame.place(x=0, y=0, in_=root)
    rightFrame.place(x=27 * item_xpos, y=0, in_=root)
    tk.Frame(master=root, height=height, bg="black").place(x=27 * item_xpos, y=0, in_=root)

def configureRootContent(root: tk.Toplevel, width: int, height: int):
    initRootFrames(root, width, height)
    initControlPort(root, width, height)
    initViewPort(root, width, height)

    contentEventHandlers(root, width, height)
    contentPacking(root, width, height)

# -------------------------------------------------------------------
# Menu
def initMenuItems(root: tk.Toplevel, menu: tk.Menu, options_menu: tk.Menu, help_menu: tk.Menu):
    # Init Main Items
    menu.add_cascade(label="Options", menu=options_menu)
    menu.add_cascade(label="Help", menu=help_menu)

    # Init Sub Items
    options_menu.add_command(label="Test", command=lambda: createFigure())
    options_menu.add_command(label="Quit", command=lambda: destroyAll(root))

    help_menu.add_command(label="v0.02", command=lambda: testFunc("test"))
    help_menu.entryconfig("v0.02", state="disabled")
    help_menu.add_separator()
    help_menu.add_command(label="About", command=lambda: aboutWindow(root))
    
    root.config(menu=menu, bg="white")

def configureRootMenu(root: tk.Toplevel):
    menu = tk.Menu(root, tearoff=False)
    options_menu = tk.Menu(menu, tearoff=False)
    help_menu = tk.Menu(menu, tearoff=False)
    initMenuItems(root, menu, options_menu, help_menu)