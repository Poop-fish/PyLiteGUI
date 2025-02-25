# PyLiteGUI

A lightweight, object-oriented GUI framework built on Tkinter, offering modern styling and simplified widget management.

> **Note:** This project is a work in progress. Making projects like these helps me improve as a coder. Additional documentation will be added as development continues.

---

## System Requirements

- **Windows 10/11** is required for title bar color customization. If unavailable, the title bar will default to white.

---

## Features

- 🖼️ **Tkinter-Based** – Built on a familiar foundation with enhanced functionality.
- 🧩 **Pre-Built Widgets** – Includes Button, Label, Input, Dropdown, Canvas, and more.
- 🎨 **Customizable Styles** – Supports colors, fonts, hover effects, and border styles.
- 📐 **Flexible Layouts** – Supports Grid, Pack, and Place layout managers.
- 🖱️ **Cursor Support** – Over 25 cursor types for interactive elements.
- 🪟 **Window Management** – Provides control over positioning, resizing, and theming.

---

## Limitations

- **Platform-Specific Features** – Some elements (e.g., rounded buttons, title bar customization) rely on Windows APIs.
- **Performance Considerations** – May face limitations with highly complex UIs.
- **Modern Aesthetic Constraints** – While improved, still retains some native Tkinter appearance on certain platforms.

---

## Why Choose PyLiteGUI?

PyLiteGUI simplifies Tkinter development by offering a structured, feature-rich toolkit. It is particularly suitable for:

- Rapid prototyping
- Educational tools
- Lightweight desktop applications with minimal dependencies

---

## Widget Overview

<details>
<summary>📜 Click to view available widgets</summary>

| Widget          | Description                                      |
|----------------|--------------------------------------------------|
| **Button**     | Clickable button with hover effects              |
| **Label**      | Text display element                             |
| **Entry**      | Text input field                                 |
| **Checkbox**   | Boolean input toggle                             |
| **Dropdown**   | Selectable options menu                          |
| **Slider**     | Value selection within a range                   |
| **Frame**      | Container for grouping widgets                   |
| **Canvas**     | Drawing area for shapes and images               |
| **Notebook**   | Tabbed interface for organizing content          |
| **ListWidget** | Scrollable list of items                         |
| **Menu**       | Menu bar or submenu                              |
| **Spinbox**    | Numeric input with increment/decrement buttons   |
| **RoundButton**| Button with rounded corners                      |

</details>

---

## Example Files

- `Example_1.py`

---

## Code Examples

<details>
<summary>📝 Click to expand code examples</summary>

### Window and Application Initialization

```python
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

### Grid Layout Example

```python
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

```python
label_grid1 = Label(
    text="Grid Label 1",
    key="lbl_grid1",
    layout=LAYOUT_GRID,
    row=0, column=0,
    padx=5, pady=5
)
window.add_element(label_grid1, parent=grid_frame.Widget)  
```

### Pack Layout Example

```python
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

```python
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

```python
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

### Place Layout Example

```python
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

```python
label_place1 = Label(
    text="Place Label 1",
    key="lbl_place1",
    layout=LAYOUT_PLACE,
    x=20, y=20
)
window.add_element(label_place1, parent=place_frame.Widget)  
```

```python
button_place = Button(
    text="Place Button",
    key="btn_place",
    layout=LAYOUT_PLACE,
    x=300, y=300
)
window.add_element(button_place)  
```

### Other Widgets

```python
checkbox1 = Checkbox (
    text="Test",
    key="chk1",
    layout=LAYOUT_PLACE,
    x=600, y=300
)
window.add_element(checkbox1)
```

```python
entry1 = Entry(
    default_text="Type Here...",
    layout=LAYOUT_PLACE,
    key="ent1",
    x=600, y=500
)
window.add_element(entry1)
```

</details>

---

### 🏗️ Layouts

- PyLiteGUI supports multiple layout management options to help you organize widgets effectively:

### 🔳 Grid Layout

- A flexible table-like structure for precise placement.

### 📦 Pack Layout

- Stacks widgets vertically or horizontally in the available space.

### 📍 Place Layout

- Explicit positioning of widgets using x and y coordinates.

