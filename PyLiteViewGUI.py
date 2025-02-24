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

#=======================================================#
#  ___ __  __ ____   ___  ____ _____ ____               #
# |_ _|  \/  |  _ \ / _ \|  _ \_   _/ ___|              #
#  | || |\/| | |_) | | | | |_) || | \___ \              #
#  | || |  | |  __/| |_| |  _ < | |  ___) |             #
# |___|_|  |_|_|    \___/|_| \_\|_| |____/              #
#                                                       #
# ----------------------------------------------------- #                                                       
#   ____ ___  _   _ ____ _____  _    _   _ _____ ____   #
#  / ___/ _ \| \ | / ___|_   _|/ \  | \ | |_   _/ ___|  #
# | |  | | | |  \| \___ \ | | / _ \ |  \| | | | \___ \  #
# | |__| |_| | |\  |___) || |/ ___ \| |\  | | |  ___) | #
#  \____\___/|_| \_|____/ |_/_/   \_\_| \_| |_| |____/  #
#                                                       #
#=======================================================#                  

#=====================#
#    Base imports     #
#=====================#

import tkinter as tk
from tkinter import ttk

from typing import Optional, Callable, Tuple, Dict, Any, List

import ctypes
from ctypes import windll, byref, sizeof, c_int, c_void_p

#=====================#
# Widget Element Type #
#=====================#
ELEM_TYPE_BUTTON = 0
ELEM_TYPE_LABEL = 1
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
ELEM_TYPE_BUTTON2 = 12 
ELEM_TYPE_TEXT = 13
ELEM_TYPE_TOPLEVEL = 14

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

#============================#
#  Default Style For PyStyle #
#============================#
DEFAULT_THEME = "classic"
DEFAULT_FONT = ("Helvetica", 10)
DEFAULT_BACKGROUND = "#868686"
DEFAULT_FOREGROUND = "#000000"
DEFAULT_ACCENT = "#555555"
DEFAULT_ACTIVE = "#666666"
DEFAULT_DISABLED = "#444444"

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

#=========================#
# Themes Tkinter Provides #
#=========================#
TK_THEME_DEFAULT = 'default'  
TK_THEME_WINNATIVE = 'winnative'
TK_THEME_CLAM = 'clam'
TK_THEME_ALT = 'alt'
TK_THEME_CLASSIC = 'classic'
TK_THEME_VISTA = 'vista'
TK_THEME_XPNATIVE = 'xpnative'

#--------------------------------------------END OF CONSTANTS \ IMPORTS-------------------------------------------------------------------------------------------------

#==================#
# Variable Classes #
#==================#

class Variable:
    """A custom value holder for GUI elements like buttons, labels, and entries.
    This class allows me to store and manage values that can be dynamically updated
    and tracked. It supports basic operations like setting, getting, and tracing
    changes to the value.
    """
    _default = None  # Default value for the variable

    def __init__(self, value=None):
        """Initialize the variable with an optional initial value.
        Args:
            value: The initial value of the variable. Defaults to None.
        """
        self._value = value if value is not None else self._default
        self._callbacks = []  # List of callback functions to call on value changes

    def set(self, value):
        """Set the value of the variable.
        Args:
            value: The new value to set.
        """
        if self._value != value:
            self._value = value
            self._notify_callbacks()  # Notify all registered callbacks

    def get(self):
        """Get the current value of the variable.
        Returns:
            The current value.
        """
        return self._value

    def trace_add(self, callback):
        """Add a callback to be called when the value changes.
        Args:
            callback: A function to call when the value is updated.
        """
        if callback not in self._callbacks:
            self._callbacks.append(callback)

    def trace_remove(self, callback):
        """Remove a previously added callback.
        Args:
            callback: The callback function to remove.
        """
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def _notify_callbacks(self):
        """Notify all registered callbacks of a value change."""
        for callback in self._callbacks:
            callback(self._value)

    def __str__(self):
        """Return a string representation of the variable's value."""
        return str(self._value)

    def __eq__(self, other):
        """Compare the variable's value with another value."""
        return self._value == other


class StringVar(Variable):
    """A specialized Variable for holding string values."""
    _default = ""  

    def __init__(self, value=None):
        """Initialize the StringVar with an optional initial value.
        Args:
            value: The initial string value. Defaults to an empty string.
        """
        super().__init__(value if value is not None else self._default)


class IntVar(Variable):
    """A specialized Variable for holding integer values."""
    _default = 0  

    def __init__(self, value=None):
        """Initialize the IntVar with an optional initial value.
        Args:
            value: The initial integer value. Defaults to 0.
        """
        super().__init__(value if value is not None else self._default)


class DoubleVar(Variable):
    """A specialized Variable for holding floating-point values."""
    _default = 0.0  

    def __init__(self, value=None):
        """Initialize the DoubleVar with an optional initial value.
        Args:
            value: The initial floating-point value. Defaults to 0.0.
        """
        super().__init__(value if value is not None else self._default)


class BooleanVar(Variable):
    """A specialized Variable for holding boolean values."""
    _default = False 

    def __init__(self, value=None):
        """Initialize the BooleanVar with an optional initial value.
        Args:
            value: The initial boolean value. Defaults to False.
        """
        super().__init__(value if value is not None else self._default)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#===============#
# Style Manager #
#===============#
class PyStyle:
    """Class-based style manager for ttk widgets."""
    def __init__(self, theme: str = DEFAULT_THEME, 
                 font: Tuple[str, int] = DEFAULT_FONT, 
                 background: str = DEFAULT_BACKGROUND,
                 foreground: str = DEFAULT_ELEMENT_TEXT_COLOR,
                 accent: str = DEFAULT_ACCENT,
                 active: str = DEFAULT_ACTIVE,
                 disabled: str = DEFAULT_DISABLED):
        self.style = ttk.Style()
        self.theme = theme
        self.font = font
        self.bg = background
        self.fg = foreground
        self.accent = accent
        self.active = active
        self.disabled = disabled
        self.apply_style()

    def apply_style(self):
        """Applies the defined style to ttk widgets."""
        self.style.theme_use(self.theme)
        # \\ Set global styles
        self.style.configure('.', 
                             font=self.font,
                             background=self.bg,
                             foreground=self.fg)

        self.style.configure('TFrame', background=self.bg)

        self.style.configure('TLabel',
                             font=(self.font[0], 12),
                             background=self.bg,
                             foreground=self.fg)

        self.style.configure('TButton',
                             background=self.accent,
                             borderwidth=1,
                             focusthickness=0,
                             relief='flat')

        self.style.map('TButton',
                       background=[('active', self.active), 
                                   ('disabled', self.disabled)],
                       foreground=[('disabled', '#888888')])

        self.style.configure('TCombobox',
                             fieldbackground=self.accent,
                             arrowsize=15)

        self.style.map('TCombobox',
                       fieldbackground=[('readonly', self.accent)],
                       selectbackground=[('readonly', self.active)],
                       selectforeground=[('readonly', self.fg)])

        self.style.configure('TEntry',
                             fieldbackground=self.accent)

        self.style.map('TEntry',
                       fieldbackground=[('readonly', self.accent)])

        self.style.configure('TLabelframe',
                             background=self.bg,
                             foreground=self.fg)

        self.style.configure('TLabelframe.Label',
                             background=self.bg,
                             foreground=self.fg)

    def update_style(self, **kwargs):
        """Update style attributes dynamically."""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        self.apply_style()

    def apply_to_widget(self, widget: ttk.Widget):
        """Apply the style to a specific ttk widget."""
        widget.configure(style=f"{widget.winfo_class()}")
#---------------------------------------------------------------------------------------------------------------------------------------------

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
                 focus_bg=None, focus_fg=None,
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
        self.focus_bg = focus_bg  
        self.focus_fg = focus_fg        
        self.tooltip = None  #
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

    def update_font(
        self,
        font_family: Optional[str] = None,
        font_size: Optional[int] = None,
        font_style: Optional[list] = None,
        strikethrough: bool = False,
        overstrike: bool = False,
        slant: Optional[str] = None,
        weight: Optional[str] = None,
    ):
        """
        Update the font properties of the widget.
        :param font_family: The font family (e.g., "Arial", "Helvetica").
        :param font_size: The font size (e.g., 12, 14).
        :param font_style: A list of font styles (e.g., ["bold", "italic", "underline"]).
        :param strikethrough: Whether to apply strikethrough to the text.
        :param overstrike: Whether to apply overstrike to the text.
        :param slant: The slant of the font (e.g., "italic", "roman").
        :param weight: The weight of the font (e.g., "bold", "normal").
        """
        if font_family:
            self.font_family = font_family
        if font_size:
            self.font_size = font_size
        if font_style:
            self.font_style = font_style
        # \\ Initialize font tuple with family and size
        self.font = (self.font_family, self.font_size)
        # \\ Apply font styles
        if "bold" in self.font_style:
            self.font += ("bold",)
        if "italic" in self.font_style:
            self.font += ("italic",)
        if "underline" in self.font_style:
            self.font += ("underline",)
        if overstrike:
            self.font += ("overstrike",)

    def get_value(self):
        """Returns the current value of the element."""
        return None
    def bind_hover_events(self):
        """Binds hover events to change background color."""
        if self.HoverColor and self.Widget:
            self.Widget.bind("<Enter>", self.on_hover)
            self.Widget.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        self._original_bg = self.Widget.cget("bg")  # \\ Save original color
        self.Widget.config(bg=self.HoverColor)

    def on_leave(self, event):
        self.Widget.config(bg=self._original_bg)

    def bind_focus_events(self):
        """Bind focus events to change styling."""
        if self.Widget and (self.focus_bg or self.focus_fg):
            self.Widget.bind("<FocusIn>", self.on_focus_in)
            self.Widget.bind("<FocusOut>", self.on_focus_out)

    def on_focus_in(self, event):
        if self.focus_bg:
            self._original_bg = self.Widget.cget("bg")
            self.Widget.config(bg=self.focus_bg)
        if self.focus_fg:
            self._original_fg = self.Widget.cget("fg")
            self.Widget.config(fg=self.focus_fg)

    def on_focus_out(self, event):
        if hasattr(self, "_original_bg"):
            self.Widget.config(bg=self._original_bg)
        if hasattr(self, "_original_fg"):
            self.Widget.config(fg=self._original_fg)
    
    def set_highlight_colors(self, bg: str, fg: str):
        """
        Set the highlight colors for selected text.
        :param bg: Background color of the selected text.
        :param fg: Foreground (text) color of the selected text.
        """
        self.highlight_bg = bg
        self.highlight_fg = fg
        if self.Widget:
            try: # \\ Update the highlight colors for the widget
                self.Widget.config(selectbackground=self.highlight_bg, selectforeground=self.highlight_fg)
            except tk.TclError: # \\ Widget does not support text selection (e.g., Button)
                pass
    
    def set_tooltip(self, text: str):
        """
        Set a tooltip for the widget.
        :param text: The text to display in the tooltip.
        """
        if self.Widget:
            self.tooltip = Tooltip(self.Widget, text)
    
    def bind_event(self, event: str, callback: Callable, add: Optional[str] = None):
        """
        Bind an event to a callback function.
        :param event: The event to bind (e.g., "<Button-1>", "<KeyPress>", "<Enter>").
        :param callback: The function to call when the event occurs.
        :param add: Optional argument to add a new binding instead of replacing existing ones.
        """
        if self.Widget:
            self.Widget.bind(event, callback, add)

    def unbind_event(self, event: str):
        """
        Unbind an event from the widget.
        :param event: The event to unbind.
        """
        if self.Widget:
            self.Widget.unbind(event) 

    def set_padding(self, padx: int, pady: int):
        """
        Set padding inside the widget.
        :param padx: Horizontal padding (left and right).
        :param pady: Vertical padding (top and bottom).
        """
        if self.Widget:
            self.Widget.config(padx=padx, pady=pady) 

    def set_margins(self, marginx: int, marginy: int):
        """
        Set margins outside the widget.
        :param marginx: Horizontal margin (left and right).
        :param marginy: Vertical margin (top and bottom).
        """
        if self.Widget:
            if self.layout == LAYOUT_GRID:
                self.layout_options.update({"padx": marginx, "pady": marginy})
            elif self.layout == LAYOUT_PACK:
                self.layout_options.update({"padx": marginx, "pady": marginy})
            elif self.layout == LAYOUT_PLACE:
                self.layout_options.update({"relx": marginx / 100, "rely": marginy / 100})
            self.apply_layout()

    def enable_drag(self):
        """Enable smooth dragging of the widget without screen tearing."""
        if self.Widget:
            self.Widget.bind("<ButtonPress-1>", self.on_drag_start)
            self.Widget.bind("<B1-Motion>", self.on_drag_motion)
            self.Widget.bind("<ButtonRelease-1>", self.on_drag_end)

    def on_drag_start(self, event):
        """Capture the initial mouse position and widget position when dragging starts."""
        self._drag_data = {
            "x": event.x_root, 
            "y": event.y_root,  
            "widget_x": self.Widget.winfo_x(),  
            "widget_y": self.Widget.winfo_y()   
        }
        self.Widget.config(cursor="fleur")

    def on_drag_motion(self, event):
        """Update the widget's position smoothly as the user drags the mouse."""
        if hasattr(self, "_drag_data"):
            dx = event.x_root - self._drag_data["x"]
            dy = event.y_root - self._drag_data["y"]
            new_x = self._drag_data["widget_x"] + dx
            new_y = self._drag_data["widget_y"] + dy
            self.Widget.place(x=new_x, y=new_y)
            self._drag_data["x"] = event.x_root
            self._drag_data["y"] = event.y_root
            self._drag_data["widget_x"] = new_x
            self._drag_data["widget_y"] = new_y

    def on_drag_end(self, event):
        """Clean up after dragging ends."""
        if hasattr(self, "_drag_data"):
            del self._drag_data
        self.Widget.config(cursor="arrow")

#---------------------------------------------------------------------------------------------------------------------------------------------

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_window = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip_window, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

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
        self.bind_hover_events()     
      
    def callback_handler(self):
        """Handles button click event."""
        print(f"Button '{self.text}' clicked!")
        if self.on_click:
            self.on_click()

    def set_tooltip(self, text: str):
        """
        Set a tooltip for the button.
        :param text: The text to display in the tooltip.
        """
        super().set_tooltip(text) 

#---------------------------------------------------------------------------------------------------------------------------------------------

class Label(PyWidget):
    """label element."""
    def __init__(self, text: str, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_LABEL, key=key, **kwargs)
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
    """text input element."""
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
        # Set highlight colors
        self.set_highlight_colors(bg="yellow", fg="black")  
        self.bind_focus_events()
    def get_value(self):
        return self.var.get()

#---------------------------------------------------------------------------------------------------------------------------------------------

class Checkbox(PyWidget):
    """checkbox element."""
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
    """dropdown (combobox) element."""  
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
    """radio button group element."""
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
    """slider (scale) element."""  
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
    """Frame container element."""
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
# TODO: Need to fix tab frame size
class Notebook(PyWidget):
    """Notebook widget for creating tabbed interfaces."""
    def __init__(self, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_FRAME, key=key, **kwargs)
        self.tabs = {}  # \\ Dictionary to store tabs and their associated frames
    
    def create_widget(self, parent: tk.Widget):
        self.Widget = ttk.Notebook(parent)
        PyStyle(theme="clam", background="lightgray", accent="gray")
    
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
    """scrollable list widget."""
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
    """menu bar or submenu."""
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
    """numeric entry widget with increment/decrement buttons."""
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
    
#---------------------------------------------------------------------------------------------------------------------------------------------

# TODO: Clean up edges 
class RoundButton(PyWidget):
    def __init__(self, text: str, key: str, on_click: Optional[Callable] = None, **kwargs):
        super().__init__(ELEM_TYPE_BUTTON2, key=key, **kwargs)
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
        self.Widget.bind("<Configure>", self.rounded_corners)  
        self.apply_layout() 

    def rounded_corners(self, event=None):
        """Apply rounded corners to the button using Windows API."""
        hwnd = self.Widget.winfo_id()
        width = self.Widget.winfo_width()
        height = self.Widget.winfo_height()
        radius = 20  # \\ Adjust the radius to control the roundness

        # \\ Create a rounded rectangle region
        region = windll.gdi32.CreateRoundRectRgn(0, 0, width, height, radius, radius)
        windll.user32.SetWindowRgn(hwnd, region, True)

    def on_hover(self, event):
        """Change background color on hover."""
        self.Widget.config(bg=self.HoverColor)

    def on_leave(self, event):
        """Restore background color on leave."""
        self.Widget.config(bg=self.bg)
    
    def callback_handler(self):
        """Handles button click event."""
        print(f"Button '{self.text}' clicked!")
        if self.on_click:
            self.on_click()



class Text(PyWidget):
    """Multi-line text input element."""
    def __init__(self, key: str, default_text: str = "", **kwargs):
        super().__init__(ELEM_TYPE_TEXT, key=key, **kwargs)
        self.default_text = default_text

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Text(
            parent,
            bg=self.bg,
            fg=self.fg,
            width=self.width,
            height=self.height,
            font=self.font,
            cursor=self.cursor,
            relief=self.Frame,
            borderwidth=self.BorderWidth
        )
        self.Widget.insert(tk.END, self.default_text)
        self.set_highlight_colors(bg="yellow", fg="black")  # Set highlight colors
        self.bind_focus_events()

    def get_value(self):
        return self.Widget.get("1.0", tk.END).strip() 
    

class TopLevel(PyWidget):
    """A new window that can contain other widgets."""
    def __init__(self, title: str, key: Optional[str] = None, **kwargs):
        super().__init__(ELEM_TYPE_TOPLEVEL, key=key, **kwargs)
        self.title = title

    def create_widget(self, parent: tk.Widget):
        self.Widget = tk.Toplevel(parent)
        self.Widget.title(self.title)
        self.Widget.geometry(f"{self.width}x{self.height}") if self.width and self.height else None
        self.Widget.configure(bg=self.bg)

    def add_widget(self, widget: PyWidget):
        """Add a widget to the TopLevel window."""
        widget.create_widget(self.Widget)
        widget.apply_layout()

#=================================================================#
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
#=================================================================#


#======================================================================#
# ██      ██ ████ ██    ██ ████████   ███████  ██      ██              #
# ██  ██  ██  ██  ███   ██ ██     ██ ██     ██ ██  ██  ██              #
# ██  ██  ██  ██  ████  ██ ██     ██ ██     ██ ██  ██  ██              #
# ██  ██  ██  ██  ██ ██ ██ ██     ██ ██     ██ ██  ██  ██              #
# ██  ██  ██  ██  ██  ████ ██     ██ ██     ██ ██  ██  ██              #
# ██  ██  ██  ██  ██   ███ ██     ██ ██     ██ ██  ██  ██              #
#  ███  ███  ████ ██    ██ ████████   ███████   ███  ███               #

# ██     ██    ███    ██    ██    ███     ██████   ████████ ████████   #
# ███   ███   ██ ██   ███   ██   ██ ██   ██    ██  ██       ██     ██  #
# ████ ████  ██   ██  ████  ██  ██   ██  ██        ██       ██     ██  #
# ██ ███ ██ ██     ██ ██ ██ ██ ██     ██ ██   ████ ██████   ████████   #
# ██     ██ █████████ ██  ████ █████████ ██    ██  ██       ██   ██    #
# ██     ██ ██     ██ ██   ███ ██     ██ ██    ██  ██       ██    ██   #
# ██     ██ ██     ██ ██    ██ ██     ██  ██████   ████████ ██     ██  #
#======================================================================#

class WM:
    """Communication with the Tkinter window manager (Tcl interpreter)."""
    def __init__(self, window):
        self.window = window  # \\ Reference to the parent window (Tk or Toplevel)
        self.tk = window.tk  # \\ Reference to the Tcl interpreter

    def configure(self, **kwargs):
        """
        Configure the window's properties.
        Example: window.wm.configure(bg="gray")
        """
        self.window.configure(**kwargs)
    
    def aspect(self, minNumer=None, minDenom=None, maxNumer=None, maxDenom=None):
        """Set or get the aspect ratio constraints for the window."""
        if minNumer is None and minDenom is None and maxNumer is None and maxDenom is None:
            return self.tk.call("wm", "aspect", self.window)
        self.tk.call("wm", "aspect", self.window, minNumer, minDenom, maxNumer, maxDenom)

    def attributes(self, *args, **kwargs):
        """Set or get platform-specific window attributes."""
        if not args and not kwargs:
            return self.tk.call("wm", "attributes", self.window)
        if len(args) == 1:
            return self.tk.call("wm", "attributes", self.window, args[0])
        self.tk.call("wm", "attributes", self.window, *args, **kwargs)

    def client(self, name=None):
        """Set or get the WM_CLIENT_MACHINE property."""
        if name is None:
            return self.tk.call("wm", "client", self.window)
        self.tk.call("wm", "client", self.window, name)

    def colormapwindows(self, *wlist):
        """Set or get the WM_COLORMAP_WINDOWS property."""
        if not wlist:
            return self.tk.call("wm", "colormapwindows", self.window)
        self.tk.call("wm", "colormapwindows", self.window, *wlist)

    def command(self, value=None):
        """Set or get the WM_COMMAND property."""
        if value is None:
            return self.tk.call("wm", "command", self.window)
        self.tk.call("wm", "command", self.window, value)

    def deiconify(self):
        """Deiconify the window (restore from minimized state)."""
        self.tk.call("wm", "deiconify", self.window)

    def focusmodel(self, model=None):
        """Set or get the focus model."""
        if model is None:
            return self.tk.call("wm", "focusmodel", self.window)
        self.tk.call("wm", "focusmodel", self.window, model)

    def forget(self, window):
        """Unmap the window and stop managing it."""
        self.tk.call("wm", "forget", window)

    def frame(self):
        """Get the identifier for the window's decorative frame."""
        return self.tk.call("wm", "frame", self.window)

    def geometry(self, newGeometry=None):
        """Set or get the window geometry."""
        if newGeometry is None:
            return self.tk.call("wm", "geometry", self.window)
        self.tk.call("wm", "geometry", self.window, newGeometry)

    def grid(self, baseWidth=None, baseHeight=None, widthInc=None, heightInc=None):
        """Set or get the grid size for the window."""
        if baseWidth is None and baseHeight is None and widthInc is None and heightInc is None:
            return self.tk.call("wm", "grid", self.window)
        self.tk.call("wm", "grid", self.window, baseWidth, baseHeight, widthInc, heightInc)

    def group(self, pathName=None):
        """Set or get the group leader for the window."""
        if pathName is None:
            return self.tk.call("wm", "group", self.window)
        self.tk.call("wm", "group", self.window, pathName)

    def iconbitmap(self, bitmap=None, default=None):
        """Set or get the icon bitmap for the window."""
        if bitmap is None and default is None:
            return self.tk.call("wm", "iconbitmap", self.window)
        if default:
            self.tk.call("wm", "iconbitmap", self.window, "-default", default)
        else:
            self.tk.call("wm", "iconbitmap", self.window, bitmap)

    def iconify(self):
        """Iconify the window (minimize it)."""
        self.tk.call("wm", "iconify", self.window)

    def iconmask(self, bitmap=None):
        """Set or get the icon mask for the window."""
        if bitmap is None:
            return self.tk.call("wm", "iconmask", self.window)
        self.tk.call("wm", "iconmask", self.window, bitmap)

    def iconname(self, newName=None):
        """Set or get the icon name for the window."""
        if newName is None:
            return self.tk.call("wm", "iconname", self.window)
        self.tk.call("wm", "iconname", self.window, newName)

    def iconposition(self, x=None, y=None):
        """Set or get the icon position for the window."""
        if x is None and y is None:
            return self.tk.call("wm", "iconposition", self.window)
        self.tk.call("wm", "iconposition", self.window, x, y)

    def iconwindow(self, pathName=None):
        """Set or get the icon window for the window."""
        if pathName is None:
            return self.tk.call("wm", "iconwindow", self.window)
        self.tk.call("wm", "iconwindow", self.window, pathName)

    def manage(self, widget):
        """Manage a widget as a top-level window."""
        self.tk.call("wm", "manage", widget)

    def maxsize(self, width=None, height=None):
        """Set or get the maximum size for the window."""
        if width is None and height is None:
            return self.tk.call("wm", "maxsize", self.window)
        self.tk.call("wm", "maxsize", self.window, width, height)

    def minsize(self, width=None, height=None):
        """Set or get the minimum size for the window."""
        if width is None and height is None:
            return self.tk.call("wm", "minsize", self.window)
        self.tk.call("wm", "minsize", self.window, width, height)

    def overrideredirect(self, boolean=None):
        """Set or get the override-redirect flag for the window."""
        if boolean is None:
            return self.tk.call("wm", "overrideredirect", self.window)
        self.tk.call("wm", "overrideredirect", self.window, boolean)

    def positionfrom(self, who=None):
        """Set or get the position-from flag for the window."""
        if who is None:
            return self.tk.call("wm", "positionfrom", self.window)
        self.tk.call("wm", "positionfrom", self.window, who)

    def protocol(self, name=None, func=None):
        """Bind a function to a window protocol."""
        if name is None:
            return self.tk.call("wm", "protocol", self.window)
        if func is None:
            return self.tk.call("wm", "protocol", self.window, name)
        self.tk.call("wm", "protocol", self.window, name, func)

    def resizable(self, width=None, height=None):
        """Set or get the resizable flag for the window."""
        if width is None and height is None:
            return self.tk.call("wm", "resizable", self.window)
        self.tk.call("wm", "resizable", self.window, width, height)

    def sizefrom(self, who=None):
        """Set or get the size-from flag for the window."""
        if who is None:
            return self.tk.call("wm", "sizefrom", self.window)
        self.tk.call("wm", "sizefrom", self.window, who)

    def state(self, newstate=None):
        """Set or get the window state."""
        if newstate is None:
            return self.tk.call("wm", "state", self.window)
        self.tk.call("wm", "state", self.window, newstate)

    def title(self, string=None):
        """Set or get the window title."""
        if string is None:
            return self.tk.call("wm", "title", self.window)
        self.tk.call("wm", "title", self.window, string)

    def transient(self, master=None):
        """Set or get the transient flag for the window."""
        if master is None:
            return self.tk.call("wm", "transient", self.window)
        self.tk.call("wm", "transient", self.window, master)

    def withdraw(self):
        """Withdraw the window from the screen."""
        self.tk.call("wm", "withdraw", self.window)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

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
        self.wm = WM(self.TKroot)
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
