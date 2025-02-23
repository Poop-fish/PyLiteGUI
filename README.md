NOTE: Everthing is a work in progress and i will be adding more docs as i go along in this project. 
with thta being said. Making Projects like this helps me get better as a coder.
Windows 10/11 is required to support title bar color changes. If the feature is unavailable, the title bar will revert to the default white. (it should at lease)

---

# PyLiteGUI

A lightweight, object-oriented GUI framework built on Tkinter with modern styling and simplified widget management.

## Features

- 🖼️ **Tkinter-based** - Familiar foundation with enhanced features
- 🧩 **Pre-built Widgets** - Button, Label, Input, Dropdown, Canvas, etc.
- 🎨 **Customizable Styles** - Colors, fonts, hover effects, and border styles
- 📐 **Flexible Layouts** - Grid, Pack, and Place layout managers
- 🖱️ **Cursor Support** - 25+ cursor types for interactive elements
- 🪟 **Window Management** - Position control, resizing, and theming

---

## Example files  
- Example_1.py
- Example_2.py

--- 

# Quick Examples 

## Window and Application Manager

### Window Initialization
```
from PyLiteViewGUI import App, Window
app = App()
window = Window(
    title="Layout Examples", 
    size=(800, 600), 
    bg_color="gray", 
    resizable=True
)
app.run(window)
```


---
## Grid Layout Example

### Grid Frame
```
grid_frame = Frame(
    key="grid_frame",
    bg="lightgray",             
    border_width=50,               
    layout=LAYOUT_GRID,
    row=0,                        
    column=0,                     
    padx=10,                      
    pady=10                        
)
window.add_element(grid_frame)
```

### Label in Grid
```
label_grid1 = Label(
    text="Grid Label 1", 
    key="lbl_grid1", 
    layout=LAYOUT_GRID, 
    row=0, column=0, 
    padx=5, pady=5
)
window.add_element(label_grid1, parent=grid_frame.Widget)  
```

## Pack Layout Example

### Pack Frame
```
pack_frame = Frame(
    key="pack_frame",
    bg="lightgray",              
    border_width=5,                
    layout=LAYOUT_GRID,            
    row=0,                         
    column=1,                      
    padx=10,                       
    pady=10                        
)
window.add_element(pack_frame)
```

### Labels in Pack
```
label_pack1 = Label(
    text="Pack Label 1", 
    key="lbl_pack1", 
    layout=LAYOUT_PACK, 
    side="top", 
    padx=5, 
    pady=5
)
window.add_element(label_pack1, parent=pack_frame.Widget)  
```

```
label_pack2 = Label(
    text="Pack Label 2", 
    key="lbl_pack2", 
    layout=LAYOUT_PACK, 
    side="top", 
    padx=5, pady=5
)
window.add_element(label_pack2, parent=pack_frame.Widget) 
```

### Button in Pack
```
button_pack = Button(
    text="Pack Button", 
    key="btn_pack",
    font=("Arial", 12, "underline"),
    layout=LAYOUT_PACK, 
    side="bottom",
    padx=5, pady=5
)
window.add_element(button_pack, parent=pack_frame.Widget)  
```

## Place Layout Example

### Place Frame
```
place_frame = Frame(
    key="place_frame",
    bg="lightgray",  
    relief="groove",               
    border_width=5,                
    layout=LAYOUT_GRID,            
    row=1,                         
    column=0,                      
    columnspan=2,                  
    padx=10,                       
    pady=10                        
)
window.add_element(place_frame)
```

### Labels in Place
```
label_place1 = Label(
    text="Place Label 1", 
    key="lbl_place1", 
    layout=LAYOUT_PLACE, 
    x=20, y=20
)
window.add_element(label_place1, parent=place_frame.Widget)  
```

```
label_place2 = Label(
    text="Place Label 2", 
    key="lbl_place2", 
    layout=LAYOUT_PLACE, 
    x=120, y=50
)
window.add_element(label_place2, parent=place_frame.Widget)  
```

### Button in Place
```
button_place = Button(
    text="Place Button", 
    key="btn_place", 
    layout=LAYOUT_PLACE, 
    x=300, y=300
)
window.add_element(button_place)  
```

### Other Widgets
```
Checkbox1 = Checkbox (
    text="test", 
    key="chk1", 
    layout=LAYOUT_PLACE, 
    x=600, y=300
)
window.add_element(Checkbox1)
```

```
entry1 = Entry(
    default_text="Type Here...", 
    layout=LAYOUT_PLACE, 
    key="ent1", 
    x=600, y=500
)
window.add_element(entry1)
```

```
dropdown1 = Dropdown(
    key="drop1",
    options=[1,2,3,4], 
    default=4, 
    layout=LAYOUT_PLACE, 
    x=300, y=400
)
window.add_element(dropdown1)
```

```
RadioButton1 = RadioButton(
    key="rad1", 
    options=["Test"]
)
window.add_element(RadioButton1)
```

```
slider1 = Slider(
    key="sld1", 
    min_value=1, max_value=100, 
    default=1, 
    layout=LAYOUT_PLACE, 
    x=100, y=400
)
window.add_element(slider1)
```

## Label Frame Example
```
label_frame = LabelFrame(
    text="Group of Widgets", 
    key="group_frame", 
    layout=LAYOUT_PLACE, 
    x=550, y=400
)
window.add_element(label_frame)
```

```
button_inside_frame = Button(
    text="Click Me", 
    key="button1"
)
window.add_element(button_inside_frame, parent=label_frame.Widget)
```




