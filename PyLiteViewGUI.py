#==============================================================================#
#       ___                                                           ___      #
#      /  /\        ___                     ___           ___        /  /\     #
#     /  /::\      /__/|                   /  /\         /  /\      /  /:/_    #
#    /  /:/\:\    |  |:|    ___     ___   /  /:/        /  /:/     /  /:/ /\   #
#   /  /:/~/:/    |  |:|   /__/\   /  /\ /__/::\       /  /:/     /  /:/ /:/_  #
#  /__/:/ /:/   __|__|:|   \  \:\ /  /:/ \__\/\:\__   /  /::\    /__/:/ /:/ /\ #
#  \  \:\/:/   /__/::::\    \  \:\  /:/     \  \:\/\ /__/:/\:\   \  \:\/:/ /:/ #
#   \  \::/       ~\~~\:\    \  \:\/:/       \__\::/ \__\/  \:\   \  \::/ /:/  #
#    \  \:\         \  \:\    \  \::/        /__/:/       \  \:\   \  \:\/:/   #
#     \  \:\         \__\/     \__\/         \__\/         \__\/    \  \::/    #
#      \__\/                                                         \__\/     #
#                                ___           ___                             #
#       ___        ___          /  /\         /__/\                            #
#      /__/\      /  /\        /  /:/_       _\_ \:\                           #
#      \  \:\    /  /:/       /  /:/ /\     /__/\ \:\                          #
#       \  \:\  /__/::\      /  /:/ /:/_   _\_ \:\ \:\                         #
#   ___  \__\:\ \__\/\:\__  /__/:/ /:/ /\ /__/\ \:\ \:\                        #
#  /__/\ |  |:|    \  \:\/\ \  \:\/:/ /:/ \  \:\ \:\/:/                        #
#  \  \:\|  |:|     \__\::/  \  \::/ /:/   \  \:\ \::/                         #
#   \  \:\__|:|     /__/:/    \  \:\/:/     \  \:\/:/                          #
#    \__\__:::/      \__\/      \  \::/       \  \::/                          #
#                                \__\/         \__\/                           #
#==============================================================================#


 ###### ##   ##  ######   ##### ###### ########  #####
   ##   #######  ##  ## ### ### ##  ## ## ## ## ##   ##  
   ##   ## # ##  ##  ## ##   ## ##  ##    ##    ##       
   ##   ##   ##  #####  ##   ## #####     ##     #####   
   ##   ##   ##  ##     ##   ## ##  ##    ##         ##  
   ##   ##   ##  ##     ### ### ##  ##    ##    ##   ##  
 ###### ##   ## ####     ##### #### ###  ####    #####

#=====================#
#    Base imports     #
#=====================#
import tkinter as tk
from tkinter import ttk
from typing import Optional, Callable, Tuple, Dict, Any, List
from ctypes import windll, byref, sizeof, c_int

#---------------------------------------------------------------------------------------------------------------------------------------------

 #####   ##### ###  ## ########  #####  ######  ###### ########  #####
##   ## ### ### ### ## ## ## ## ##   ## ## ###  ### ## ## ## ## ##   ##  
##   ## ##   ## ######    ##    ##      ##  ##  ######    ##    ##       
##      ##   ## ## ###    ##     #####  ######  ## ###    ##     #####   
##   ## ##   ## ##  ##    ##         ## ##  ##  ##  ##    ##         ##  
##   ## ### ### ##  ##    ##    ##   ## ##  ##  ##  ##    ##    ##   ##  
 #####   ##### ###  ##   ####    ##### ###  ## ###  ##   ####    #####

#=====================#
# Widget Element Type #
#=====================#
ELEM_TYPE_BUTTON = 0
ELEM_TYPE_TEXT = 1
ELEM_TYPE_INPUT = 2
ELEM_TYPE_CHECKBOX = 3
ELEM_TYPE_DROPDOWN = 4
ELEM_TYPE_RADIO = 5
ELEM_TYPE_SLIDER = 6
ELEM_TYPE_FRAME = 7  
ELEM_TYPE_CANVAS = 8
ELEM_TYPE_LIST = 9
ELEM_TYPE_MENU = 10
ELEM_TYPE_SPINBOX = 11

#====================#
#    Layout Types    #
#====================#
LAYOUT_GRID = "grid"
LAYOUT_PACK = "pack"
LAYOUT_PLACE = "place"

#====================#
#   Default Colors   #
#====================#
DEFAULT_ELEMENT_BACKGROUND_COLOR = 'white'
DEFAULT_ELEMENT_TEXT_COLOR = 'black'
DEFAULT_HOVER_COLOR = 'lightgray'

#===========================#
#   Default Relief Styles   #
#===========================#
DEFAULT_RAISED = "raised"
DEFAULT_FLAT = "flat"
DEFAULT_GROOVE = "groove"
DEFAULT_SUNKEN = "sunken"
DEFAULT_RIDGE = "ridge"
DEFAULT_BORDER_WIDTH = 2

#====================#
#   Default Fonts    #
#====================#
DEFAULT_FONT = ("Arial", 12, "normal")

#=====================#
#   Cursor Types      #
#=====================#
CURSOR_ARROW = "arrow"
CURSOR_CIRCLE = "circle"
CURSOR_CLOCK = "clock"
CURSOR_CROSS = "cross"
CURSOR_DOTBOX = "dotbox"
CURSOR_EXCHANGE = "exchange"
CURSOR_FLEUR = "fleur"
CURSOR_HEART = "heart"
CURSOR_MAN = "man"
CURSOR_MOUSE = "mouse"
CURSOR_PIRATE = "pirate"
CURSOR_PLUS = "plus"
CURSOR_SIZING = "sizing"
CURSOR_SPIDER = "spider"
CURSOR_SPRAYCAN = "spraycan"
CURSOR_STAR = "star"
CURSOR_TARGET = "target"
CURSOR_TREK = "trek"
CURSOR_WATCH = "watch"
CURSOR_XTERM = "xterm"
CURSOR_HAND2 = "hand2"
CURSOR_QUESTION_ARROW = "question_arrow"
CURSOR_IBEAM = "ibeam"
CURSOR_SIZING_WE = "size_we"
CURSOR_SIZING_NS = "size_ns"
CURSOR_SIZING_NWSE = "size_nwse"
CURSOR_SIZING_NESW = "size_nesw"
CURSOR_SIZING_ALL = "size_all"

#--------------------------------------------END OF CONSTANTS-------------------------------------------------------------------------------------------------

#==========================================================================#
#                                                                          #
#   #####   #######     #     ######   #######             ###    #######  #
#  #     #     #        #     #     #     #               #   #   #        #
#  #           #       ###    #     #     #              #     #  #        #
#   #####      #       # #    ######      #              #     #  #####    #
#        #     #      #####   #   #       #              #     #  #        #
#  #     #     #      #   #   #    #      #               #   #   #        #
#   #####      #     ##   ##  #     #     #                ###    #        #
#                                                                          #
#  #     #   #####   #####      ####   #######  #######   #####            #
#  #     #     #     #    #    #    #  #           #     #     #           #
#  #     #     #     #     #  #        #           #     #                 #
#  #  #  #     #     #     #  #   ###  #####       #      #####            #
#  # # # #     #     #     #  #     #  #           #           #           #
#  ##   ##     #     #    #    #    #  #           #     #     #           #
#  #     #   #####   #####      #####  #######     #      #####            #
#                                                                          #
#==========================================================================#


class PyWidget:
    """Base class for all UI Widgets."""
    def __init__(self, elem_type: int, key: Optional[str] = None, 
                 bg: str = DEFAULT_ELEMENT_BACKGROUND_COLOR, 
                 fg: str = DEFAULT_ELEMENT_TEXT_COLOR, 
                 hover_color: str = DEFAULT_HOVER_COLOR, 
                 frame: str = DEFAULT_FLAT, 
                 border_width: int = DEFAULT_BORDER_WIDTH,
                 width: int = None, 
                 height: int = None, 
                 visible: bool = True, 
                 layout: str = LAYOUT_GRID, 
                 border_color: str = None,
                 cursor: str = CURSOR_ARROW,
                 font: Tuple[str, int, str] = DEFAULT_FONT, 
                 **layout_options):
        self.elem_type = elem_type
        self.key = key
        self.bg = bg
        self.fg = fg
        self.width = width 
        self.height = height 
        self.HoverColor = hover_color
        self.Frame = frame  
        self.BorderWidth = border_width  
        self.visible = visible
        self.layout = layout
        self.layout_options = layout_options  
        self.Widget = None  
        self.ParentForm = None
        self.font = font 
        self.cursor = cursor   
        
        if len(font) == 2: # \\ Ensure the font tuple has 3 elements (family, size, style)
            font = (font[0], font[1], DEFAULT_FONT[2])  # \\ Fallback to default style
        self.font = font
    
    def create_widget(self, parent: tk.Widget):
        """This method should be overridden by subclasses to create the actual Tkinter widget."""
        pass

    def apply_layout(self):
        """Applies the chosen layout, filtering out styling options."""
        if self.Widget:
            layout_options = {
                key: value for key, value in self.layout_options.items()
                if key not in ["relief", "border_width"]
            }
            if self.layout == LAYOUT_GRID:
                self.Widget.grid(**layout_options)
            elif self.layout == LAYOUT_PACK:
                self.Widget.pack(**layout_options)
            elif self.layout == LAYOUT_PLACE:
                self.Widget.place(**layout_options)

    def update_font(self, font_family: Optional[str] = None, font_size: Optional[int] = None, font_style: Optional[list] = None):
        if font_family:
            self.font_family = font_family
        if font_size:
            self.font_size = font_size
        if font_style:
            self.font_style = font_style

        self.font = (self.font_family, self.font_size)
        
        if "bold" in self.font_style:
            self.font += ("bold",)
        if "italic" in self.font_style:
            self.font += ("italic",)
        if "underline" in self.font_style:
            self.font += ("underline",)
        if self.Widget:
            self.Widget.config(font=self.font)
    
    def get_value(self):
        """Returns the current value of the element."""
        return None

#---------------------------------------------------------------------------------------------------------------------------------------------

class Button(PyWidget):
    def __init__(self, text: str, key: str, on_click: Optional[Callable] = None, **kwargs):
        super().__init__(ELEM_TYPE_BUTTON, key=key, **kwargs)
        self.text = text
        self.on_click = on_click  

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Button(
            parent,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            cursor=self.cursor,
            font=self.font,
            width=self.width,
            height=self.height,
            relief=self.Frame,  
            borderwidth=self.BorderWidth,  
            activebackground=self.HoverColor,
            command=self.callback_handler
        )
        self.Widget.bind("<Enter>", self.on_hover)
        self.Widget.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        self.Widget.config(bg=self.HoverColor)

    def on_leave(self, event):
        self.Widget.config(bg=self.bg)
    
    def callback_handler(self):
        """Handles button click event."""
        print(f"Button '{self.text}' clicked!")
        if self.on_click:
            self.on_click()

#---------------------------------------------------------------------------------------------------------------------------------------------

class Label(PyWidget):
    """A label element."""
    def __init__(self, text: str, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_TEXT, key=key, **kwargs)
        self.text = text

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Label(
            parent,
            text=self.text,
            bg=self.bg,
            fg=self.fg,
            width=self.width,
            height=self.height,            
            cursor=self.cursor,
            font=self.font,
            relief=self.Frame, 
            borderwidth=self.BorderWidth 
        )

#---------------------------------------------------------------------------------------------------------------------------------------------

class Entry(PyWidget):
    """A text input element."""
    def __init__(self, key: str, default_text: str = "", **kwargs):
        super().__init__(ELEM_TYPE_INPUT, key=key, **kwargs)
        self.var = tk.StringVar(value=default_text)

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Entry(
            parent, 
            textvariable=self.var, 
            bg=self.bg, 
            fg=self.fg,
            width=self.width,
            height=self.height,
            font=self.font,
            cursor=self.cursor,
            relief=self.Frame,  
            borderwidth=self.BorderWidth  
        )

    def get_value(self):
        return self.var.get()

#---------------------------------------------------------------------------------------------------------------------------------------------

class Checkbox(PyWidget):
    """A checkbox element."""
    def __init__(self, text: str, key: str, default: bool = False, **kwargs):
        super().__init__(ELEM_TYPE_CHECKBOX, key=key, **kwargs)
        self.text = text 
        self.var = tk.BooleanVar(value=default)

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Checkbutton(
            parent, 
            text=self.text,  
            variable=self.var,
            width=self.width,
            height=self.height, 
            bg=self.bg, 
            fg=self.fg,
            cursor=self.cursor,
            relief=self.Frame, 
            font=self.font,
            borderwidth=self.BorderWidth,  
            activebackground=self.HoverColor
        )

    def get_value(self):
        return self.var.get()

#---------------------------------------------------------------------------------------------------------------------------------------------

class Dropdown(PyWidget):
    """A dropdown (combobox) element."""  
    def __init__(self, key: str, options: list, default: str = None, **kwargs):
        super().__init__(ELEM_TYPE_DROPDOWN, key=key, **kwargs)
        self.var = tk.StringVar(value=default if default else options[0])
        self.options = options

    def create_widget(self, parent: tk.Widget):
        self.Widget = ttk.Combobox(
            parent, textvariable=self.var, 
            values=self.options,
            cursor=self.cursor,
            font=self.font, 
            state="readonly"
        )

    def get_value(self):
        return self.var.get()

#---------------------------------------------------------------------------------------------------------------------------------------------

class RadioButton(PyWidget):
    """A radio button group element."""
    def __init__(self, key: str, options: list, default: str = None, **kwargs):
        super().__init__(ELEM_TYPE_RADIO, key=key, **kwargs)
        self.var = tk.StringVar(value=default if default else options[0])
        self.options = options

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Frame(parent)
        for option in self.options:
            rb = tk.Radiobutton(
                self.Widget, 
                text=option,
                cursor=self.cursor, 
                variable=self.var, 
                value=option,
                width=self.width,
                height=self.height, 
                bg=self.bg, 
                fg=self.fg,
                font=self.font,
                relief=self.Frame,  
                borderwidth=self.BorderWidth,  
                activebackground=self.HoverColor
            )
            rb.pack(anchor="w")

    def get_value(self):
        return self.var.get()

#---------------------------------------------------------------------------------------------------------------------------------------------

class Slider(PyWidget):
    """A slider (scale) element."""  
    def __init__(self, key: str, min_value: int, max_value: int, default: int = 0, **kwargs):
        super().__init__(ELEM_TYPE_SLIDER, key=key, **kwargs)
        self.var = tk.IntVar(value=default)
        self.min_value = min_value
        self.max_value = max_value

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Scale(
            parent, 
            from_=self.min_value, 
            to=self.max_value, 
            variable=self.var, 
            orient="horizontal", 
            bg=self.bg,
            width=self.width,
            height=self.height,
            cursor=self.cursor, 
            fg=self.fg,
            font=self.font,
            relief=self.Frame,  
            borderwidth=self.BorderWidth  
        )

    def get_value(self):
        return self.var.get() 
    
#---------------------------------------------------------------------------------------------------------------------------------------------

class Frame(PyWidget):
    """A Frame container element."""
    def __init__(self, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_FRAME, key=key, **kwargs)

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Frame(
            parent,
            width=self.width,
            height=self.height,
            bg=self.bg,
            cursor=self.cursor,  
            relief=self.Frame,       
            borderwidth=self.BorderWidth  
        )

#---------------------------------------------------------------------------------------------------------------------------------------------

class Canvas(PyWidget):
    def __init__(self, key: Optional[str] = None, width: int = 200, height: int = 200, **kwargs):
        super().__init__(ELEM_TYPE_CANVAS, key=key, **kwargs)
        self.width = width
        self.height = height

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Canvas(
            parent,
            width=self.width,
            height=self.height,
            cursor=self.cursor,
            bg=self.bg,
            # font=self.font,
            relief=self.Frame,
            borderwidth=self.BorderWidth
        )

    def draw_line(self, x1: int, y1: int, x2: int, y2: int, **kwargs):
        """Draws a line on the canvas."""
        if self.Widget:
            self.Widget.create_line(x1, y1, x2, y2, **kwargs)

    def draw_rectangle(self, x1: int, y1: int, x2: int, y2: int, **kwargs):
        """Draws a rectangle on the canvas."""
        if self.Widget:
            self.Widget.create_rectangle(x1, y1, x2, y2, **kwargs)

    def draw_oval(self, x1: int, y1: int, x2: int, y2: int, **kwargs):
        """Draws an oval on the canvas."""
        if self.Widget:
            self.Widget.create_oval(x1, y1, x2, y2, **kwargs)

    def draw_text(self, x: int, y: int, text: str, **kwargs):
        """Draws text on the canvas."""
        if self.Widget:
            self.Widget.create_text(x, y, text=text, **kwargs)

    def clear(self):
        """Clears all drawings from the canvas."""
        if self.Widget:
            self.Widget.delete("all") 

#---------------------------------------------------------------------------------------------------------------------------------------------

# TODO : Fix font not working 
class LabelFrame(PyWidget):
    def __init__(self, text: str, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_FRAME, key=key, **kwargs)
        self.text = text  # \\ The label text for the frame

    def create_widget(self, parent: tk.Widget):
        self.Widget = ttk.LabelFrame(
            parent,
            width=self.width,
            height=self.height,
            text=self.text,
            cursor=self.cursor,
            # font=self.font,
            relief=self.Frame,
            borderwidth=self.BorderWidth
        ) 

#---------------------------------------------------------------------------------------------------------------------------------------------

class Notebook(PyWidget):
    """A Notebook widget for creating tabbed interfaces."""
    def __init__(self, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_FRAME, key=key, **kwargs)
        self.tabs = {}  # \\ Dictionary to store tabs and their associated frames

    def create_widget(self, parent: tk.Widget):
        self.Widget = ttk.Notebook(parent)
        # cursor=self.cursor,
        # width=self.width,
        # height=self.height

    def add_tab(self, title: str, widget: PyWidget):
        """Adds a new tab to the notebook with the specified title and widget."""
        if self.Widget:
            tab_frame = tk.Frame(self.Widget, bg=self.bg)
            tab_frame.pack(expand=True, fill="both")
            widget.create_widget(tab_frame)
            widget.apply_layout()
            self.Widget.add(tab_frame, text=title)
            self.tabs[title] = widget 

    def get_tab(self, title: str) -> Optional[PyWidget]:
        """Returns the widget associated with the specified tab title."""
        return self.tabs.get(title)

    def remove_tab(self, title: str):
        """Removes the tab with the specified title."""
        if self.Widget and title in self.tabs:
            self.Widget.forget(self.tabs[title].Widget.master)  
            del self.tabs[title]  

#---------------------------------------------------------------------------------------------------------------------------------------------

class ListWidget(PyWidget):
    """A scrollable list widget."""
    def __init__(self, key: str, items: List[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_LIST, key=key, **kwargs)
        self.items = items or []
        self.listbox = None
        self.scrollbar = None

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Frame(parent, bg=self.bg)
        
        self.listbox = tk.Listbox(
            self.Widget,
            bg=self.bg,
            fg=self.fg,
            width=self.width,
            height=self.height,
            relief=self.Frame,
            borderwidth=self.BorderWidth,
            font=self.font,
            selectbackground=self.HoverColor,
            selectmode=tk.SINGLE
        )
        self.scrollbar = tk.Scrollbar(
            self.Widget, 
            orient=tk.VERTICAL,
            command=self.listbox.yview
        )
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        for item in self.items:
            self.listbox.insert(tk.END, item)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def get_selected(self) -> List[str]:
        """Returns selected items."""
        return [self.listbox.get(i) for i in self.listbox.curselection()]

    def add_item(self, item: str):
        """Adds item to end of list."""
        self.listbox.insert(tk.END, item)

    def remove_item(self, index: int):
        """Removes item at specified index."""
        self.listbox.delete(index)

    def clear(self):
        """Clears all items."""
        self.listbox.delete(0, tk.END)

#---------------------------------------------------------------------------------------------------------------------------------------------

class Menu(PyWidget):
    """A menu bar or submenu."""
    def __init__(self, key: str, **kwargs):
        super().__init__(ELEM_TYPE_MENU, key=key, **kwargs)
        self.tk_menu = None
        self.parent_menu = None

    def create_widget(self, parent: tk.Widget):
        if isinstance(parent, (tk.Tk, tk.Toplevel)):
            # Main menu bar
            self.tk_menu = tk.Menu(parent, tearoff=0)
            parent.config(menu=self.tk_menu)  
        elif isinstance(parent, tk.Menu):
            # Submenu
            self.tk_menu = tk.Menu(parent, tearoff=0)
            self.parent_menu = parent
        else:
            raise ValueError("Menu parent must be a window or another menu")

        self.Widget = self.tk_menu

    def apply_layout(self):
        """Override to skip layout management"""
        pass

    def add_cascade(self, label: str, submenu: 'Menu'):
        """Adds a submenu cascade."""
        if not self.tk_menu:
            raise RuntimeError("Menu not initialized. Call create_widget() first.")
        submenu.create_widget(self.tk_menu)  
        self.tk_menu.add_cascade(label=label, menu=submenu.tk_menu)

    def add_command(self, label: str, command: Callable[[], None]):
        if not self.tk_menu:
            raise RuntimeError("Menu not initialized. Call create_widget() first.")
        self.tk_menu.add_command(label=label, command=command)

    def add_separator(self):
        if not self.tk_menu:
            raise RuntimeError("Menu not initialized. Call create_widget() first.")
        self.tk_menu.add_separator() 

#---------------------------------------------------------------------------------------------------------------------------------------------

class Spinbox(PyWidget):
    """A numeric entry widget with increment/decrement buttons."""
    def __init__(self, key: Optional[str] = None,
                 from_: float = 0, to: float = 100, 
                 increment: float = 1, values: list = None,
                 wrap: bool = False, command: Callable = None,
                 **kwargs):
        super().__init__(ELEM_TYPE_SPINBOX, key=key, **kwargs)
        self.from_ = from_
        self.to = to
        self.increment = increment
        self.values = values
        self.wrap = wrap
        self.command = command

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Spinbox(parent,
            bg=self.bg,
            fg=self.fg,
            relief=self.Frame,
            borderwidth=self.BorderWidth,
            font=self.font,
            cursor=self.cursor,
            wrap=self.wrap
        )
        
        if self.values:
            self.Widget.configure(values=self.values)
        else:
            self.Widget.configure(from_=self.from_, to=self.to, increment=self.increment)
        
        if self.command:
            self.Widget.configure(command=self.command)
        
        if self.width:
            self.Widget.configure(width=self.width)
        
        self.apply_layout()
        return self.Widget

    def get_value(self):
        return self.Widget.get() if self.Widget else None

###################################################################
#  #######  #     #  #####               ###    #######           #
#  #        ##    #  #    #             #   #   #                 #
#  #        # #   #  #     #           #     #  #                 #
#  #####    #  #  #  #     #           #     #  #####             #
#  #        #   # #  #     #           #     #  #                 #
#  #        #    ##  #    #             #   #   #                 #
#  #######  #     #  #####               ###    #                 #
#                                                                 #
#  #     #   #####   #####      ####   #######  #######   #####   #
#  #     #     #     #    #    #    #  #           #     #     #  #
#  #     #     #     #     #  #        #           #     #        #
#  #  #  #     #     #     #  #   ###  #####       #      #####   #
#  # # # #     #     #     #  #     #  #           #           #  #
#  ##   ##     #     #    #    #    #  #           #     #     #  #
#  #     #   #####   #####      #####  #######     #      #####   #
###################################################################


##   ## ######  ### ## ######   #####  ##   ##
##   ##   ##    ### ##  ## ### ### ### ##   ##  
##   ##   ##    ######  ##  ## ##   ## ##   ##  
##   ##   ##    ## ###  ##  ## ##   ## ##   ##  
## # ##   ##    ##  ##  ##  ## ##   ## ## # ##  
#######   ##    ##  ##  ## ### ### ### #######  
##   ## ###### ###  ## ######   #####  ##   ##  
                                                
##   ## ######  ###  ## ######   ##### ####### ######   
#######  ## ###  ### ##  ## ### ##   ## ##  ##  ##  ##  
## # ##  ##  ##  ######  ##  ## ##      ##      ##  ##  
##   ##  ######  ## ###  ###### ##  ### ####    #####   
##   ##  ##  ##  ##  ##  ##  ## ##   ## ##      ##  ##  
##   ##  ##  ##  ##  ##  ##  ## ##   ## ##  ##  ##  ##  
##   ## ###  ## ###  ## ###  ##  ##### ####### #### ###

#---------------------------------------------------------------------------------------------------------------------------------------------

class App:
    """
    A custom class to manage the Tkinter application lifecycle.
    """
    def __init__(self):
        self.TKroot = None  # \\ Placeholder for the Tkinter root window
        self.windows = []  

    def run(self, window: 'Window'):
        """
        Run the application with the given main window.
        """
        self.TKroot = window.TKroot  
        self.windows.append(window)  
        self.TKroot.mainloop() 

    def shutdown(self):
        """
        Gracefully shut down the application and close all windows.
        """
        for window in self.windows:
            window.TKroot.destroy()  
        print("Application shutdown complete.")


class Window:
    """Manages the main Tkinter window and elements."""

    def __init__(self, title: str, size: Optional[Tuple[int, int]] = None, bg_color: Optional[str] = None, icon_path: Optional[str] = "Assets/FaceLogo.ico", position: Optional[Tuple[int, int]] = None, resizable: bool = False):
        """
        Initializes the Tkinter window.
        Args:
            title (str): The title of the window.
            size (Optional[Tuple[int, int]]): The size of the window as (width, height).
            bg_color (Optional[str]): The background color of the window.
            icon_path (Optional[str]): The path to the window icon.
            position (Optional[Tuple[int, int]]): The initial position of the window as (x, y).
            resizable (bool): Whether the window is resizable. Defaults to False.
        """
        self.TKroot = tk.Tk()
        self.TKroot.title(title)
        self.elements: List['PyWidget'] = []
        self.key_dict: Dict[str, 'PyWidget'] = {}
        self.TKroot.after(100, self._set_title_bar_gray)

        if size is not None:
            self.TKroot.geometry(f"{size[0]}x{size[1]}")
        if bg_color is not None:
            self.TKroot.configure(bg=bg_color)
        if icon_path is not None:
            self.set_icon(icon_path)
        if position is not None:
            self.set_position(position)

        # Disable resizing if resizable is False
        self.TKroot.resizable(resizable, resizable)

    def _set_title_bar_gray(self):
        """Uses Windows API to set the title bar color to gray."""
        try:
            hwnd = windll.user32.GetParent(self.TKroot.winfo_id())  # Get window handle
            DWMWA_CAPTION_COLOR = 35  # Windows 11+
            GRAY_COLOR = 0x808080  # RGB(128, 128, 128) → Dark Gray
            # Apply title bar color
            windll.dwmapi.DwmSetWindowAttribute(
                hwnd, DWMWA_CAPTION_COLOR, byref(c_int(GRAY_COLOR)), sizeof(c_int)
            )
            windll.user32.RedrawWindow(hwnd, None, None, 0x85)
        except Exception as e:
            print("Failed to change title bar color:", e)

    def set_icon(self, icon_path: str):
        """Sets the window icon.
        Args:
            icon_path (str): The path to the icon file.
        """
        try:
            self.TKroot.iconbitmap(icon_path)
        except Exception as e:
            print("Failed to set window icon:", e)

    def set_position(self, position: Tuple[int, int]):
        """Sets the initial position of the window.
        Args:
            position (Tuple[int, int]): The (x, y) coordinates of the window.
        """
        self.TKroot.geometry(f"+{position[0]}+{position[1]}")

    def add_element(self, element: 'PyWidget', parent: Optional[tk.Widget] = None):
        """Adds an element to the window, optionally specifying a parent widget.
        Args:
            element (PyWidget): The element to add.
            parent (Optional[tk.Widget]): The parent widget. Defaults to the main window.
        """
        self.elements.append(element)
        if element.key:
            self.key_dict[element.key] = element
        element.ParentForm = self
        if parent is None:
            parent = self.TKroot  
        element.create_widget(parent)  
        element.apply_layout()

    def read(self):
        """Starts the event loop and handles user interactions."""
        self.TKroot.mainloop()

#---------------------------------------------------------------------------------------------------------------------------------------------
