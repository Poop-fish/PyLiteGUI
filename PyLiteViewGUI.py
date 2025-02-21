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


import tkinter as tk
from tkinter import ttk
from typing import Optional, Callable, Tuple, Dict, Any
from ctypes import windll, byref, sizeof, c_int

#---------------------------------------------------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------------------------------------------
class PyWidget:
    """Base class for all UI Widgets."""
    def __init__(self, elem_type: int, key: Optional[str] = None, 
                 bg: str = DEFAULT_ELEMENT_BACKGROUND_COLOR, 
                 fg: str = DEFAULT_ELEMENT_TEXT_COLOR, 
                 hover_color: str = DEFAULT_HOVER_COLOR, 
                 frame: str = DEFAULT_FLAT, 
                 border_width: int = DEFAULT_BORDER_WIDTH, 
                 visible: bool = True, 
                 layout: str = LAYOUT_GRID, **layout_options):
        self.elem_type = elem_type
        self.key = key
        self.bg = bg
        self.fg = fg
        self.HoverColor = hover_color
        self.Frame = frame  
        self.BorderWidth = border_width  
        self.visible = visible
        self.layout = layout
        self.layout_options = layout_options  
        self.Widget = None  
        self.ParentForm = None

    def create_widget(self, parent: tk.Widget):
        """This method should be overridden by subclasses to create the actual Tkinter widget."""
        pass

    def apply_layout(self):
        """Applies the chosen layout, filtering out styling options."""
        if self.Widget:
            # Filter out styling options (relief, border_width, etc.) 
            #? this might need to be cleaned up and re done 
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

    def get_value(self):
        """Returns the current value of the element."""
        return None

#---------------------------------------------------------------------------------------------------------------------------------------------

class Window:
    """Manages the main Tkinter window and elements."""
    def __init__(self, title: str, size: Optional[tuple[int,int]]= None , bg_color: Optional[str]= None):    #  ADD PARMS FIRST 
        self.TKroot = tk.Tk()
        self.TKroot.title(title)
        self.elements = []  
        self.key_dict = {}  
        self.TKroot.after(100, self._set_title_bar_gray)  

        if size is not None:
            self.TKroot.geometry(f"{size[0]}x{size[1]}")
        if bg_color is not None:
            self.TKroot.configure(bg=bg_color)

    def _set_title_bar_gray(self):
        """This Uses Windows API to set the title bar color to gray."""
        try:
            hwnd = windll.user32.GetParent(self.TKroot.winfo_id())  # \\ Get window handle
            DWMWA_CAPTION_COLOR = 35  # \\ Windows 11+
            GRAY_COLOR = 0x808080  # \\ RGB(128, 128, 128) → Dark Gray
            # \\ Apply title bar color
            windll.dwmapi.DwmSetWindowAttribute(
                hwnd, DWMWA_CAPTION_COLOR, byref(c_int(GRAY_COLOR)), sizeof(c_int)
            )
            windll.user32.RedrawWindow(hwnd, None, None, 0x85)
        except Exception as e:
            print("Failed to change title bar color:", e)

    def add_element(self, element: 'PyWidget', parent: Optional[tk.Widget] = None):
        """Adds an element to the window, optionally specifying a parent widget."""
        self.elements.append(element)
        if element.key:
            self.key_dict[element.key] = element
        element.ParentForm = self
        if parent is None:
            parent = self.TKroot  # \\ Default to main window if no parent is specified
        element.create_widget(parent)  # \\ Use specified parent or main window
        element.apply_layout()

    def read(self):
        """Starts the event loop and handles user interactions."""
        self.TKroot.mainloop()

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
            relief=self.Frame,  
            borderwidth=self.BorderWidth,  
            activebackground=self.HoverColor,
            command=self._generic_callback_handler
        )

    def _generic_callback_handler(self):
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
            bg=self.bg, 
            fg=self.fg,
            relief=self.Frame,  
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
                variable=self.var, 
                value=option, 
                bg=self.bg, 
                fg=self.fg,
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
            fg=self.fg,
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
            bg=self.bg,  
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
            bg=self.bg,
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



class LabelFrame(PyWidget):
    def __init__(self, text: str, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_FRAME, key=key, **kwargs)
        self.text = text  # The label text for the frame

    def create_widget(self, parent: tk.Widget):
        self.Widget = ttk.LabelFrame(
            parent,
            text=self.text,
            relief=self.Frame,
            borderwidth=self.BorderWidth
        ) 


class Notebook(PyWidget):
    """A Notebook widget for creating tabbed interfaces."""
    def __init__(self, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_FRAME, key=key, **kwargs)
        self.tabs = {}  # Dictionary to store tabs and their associated frames

    def create_widget(self, parent: tk.Widget):
        self.Widget = ttk.Notebook(parent)

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


