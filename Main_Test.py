from PyLiteView import *

#---------------------------------------------------------------------------------------------------------------------------------------------

# window = Window("Customizable UI")

# button = Button(
#     text="Click Me", 
#     key="btn1", 
#     background_color="blue", 
#     text_color="white", 
#     hover_color="lightblue", 
#     frame="raised", 
#     border_width=3
# )
# window.add_element(button)

# label = Label(
#     text="Hello, World!", 
#     key="lbl1", 
#     background_color="lightyellow", 
#     text_color="darkblue", 
#     frame="sunken", 
#     border_width=2
# )
# window.add_element(label)


# window.read() 


#! ----------- Place/Grid/Pack Layout Example -----------

# window = Window("Layout Examples")

# # Grid Layout Example
# grid_frame = tk.Frame(window.TKroot, bd=2, relief="sunken")
# grid_frame.grid(row=0, column=0, padx=10, pady=10)

# label_grid1 = Label(text="Grid Label 1", key="lbl_grid1", layout=LAYOUT_GRID, row=0, column=0, padx=5, pady=5)
# label_grid1.create_widget(grid_frame)
# label_grid1.apply_layout()

# label_grid2 = Label(text="Grid Label 2", key="lbl_grid2", layout=LAYOUT_GRID, row=0, column=1, padx=5, pady=5)
# label_grid2.create_widget(grid_frame)
# label_grid2.apply_layout()

# button_grid = Button(text="Grid Button", key="btn_grid", layout=LAYOUT_GRID, row=1, column=0, columnspan=2, padx=5, pady=5)
# button_grid.create_widget(grid_frame)
# button_grid.apply_layout()

# # Pack Layout Example
# pack_frame = tk.Frame(window.TKroot, bd=2, relief="sunken")
# pack_frame.grid(row=0, column=1, padx=10, pady=10)

# label_pack1 = Label(text="Pack Label 1", key="lbl_pack1", layout=LAYOUT_PACK, side="top", padx=5, pady=5)
# label_pack1.create_widget(pack_frame)
# label_pack1.apply_layout()

# label_pack2 = Label(text="Pack Label 2", key="lbl_pack2", layout=LAYOUT_PACK, side="top", padx=5, pady=5)
# label_pack2.create_widget(pack_frame)
# label_pack2.apply_layout()

# button_pack = Button(text="Pack Button", key="btn_pack", layout=LAYOUT_PACK, side="bottom", padx=5, pady=5)
# button_pack.create_widget(pack_frame)
# button_pack.apply_layout()

# # Place Layout Example
# place_frame = tk.Frame(window.TKroot, bd=2, relief="sunken")
# place_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# label_place1 = Label(text="Place Label 1", key="lbl_place1", layout=LAYOUT_PLACE, x=20, y=20)
# label_place1.create_widget(place_frame)
# label_place1.apply_layout()

# label_place2 = Label(text="Place Label 2", key="lbl_place2", layout=LAYOUT_PLACE, x=120, y=50)
# label_place2.create_widget(place_frame)
# label_place2.apply_layout()

# button_place = Button(text="Place Button", key="btn_place", layout=LAYOUT_PLACE, x=80, y=100)
# button_place.create_widget(place_frame)
# button_place.apply_layout()

# window.read() 

#! ----------- Place Layout Example -----------

# window = Window("Place Layout Example")

# # Add elements using place layout
# label1 = Label(text="Label 1", key="lbl1", layout=LAYOUT_PLACE, x=50, y=50)
# window.add_element(label1)

# label2 = Label(text="Label 2", key="lbl2", layout=LAYOUT_PLACE, x=150, y=100)
# window.add_element(label2)

# button = Button(text="Click Me", key="btn1", layout=LAYOUT_PLACE, x=100, y=200)
# window.add_element(button)

# window.read() 


#! ----------- Pack Layout Example -----------

# window = Window("Pack Layout Example")

# # Add elements using pack layout
# label1 = Label(text="Label 1", key="lbl1", layout=LAYOUT_PACK, side="top", padx=10, pady=10)
# window.add_element(label1)

# label2 = Label(text="Label 2", key="lbl2", layout=LAYOUT_PACK, side="top", padx=10, pady=10)
# window.add_element(label2)

# button = Button(text="Click Me", key="btn1", layout=LAYOUT_PACK, side="bottom", padx=10, pady=10)
# window.add_element(button)

# window.read() 


#! ----------- Grid Layout Example -----------

# window = Window("Grid Layout Example")

# # Add elements using grid layout
# label1 = Label(text="Label 1", key="lbl1", layout=LAYOUT_GRID, row=0, column=0, padx=10, pady=10)
# window.add_element(label1)

# label2 = Label(text="Label 2", key="lbl2", layout=LAYOUT_GRID, row=0, column=1, padx=10, pady=10)
# window.add_element(label2)

# button = Button(text="Click Me", key="btn1", layout=LAYOUT_GRID, row=1, column=0, columnspan=2, padx=10, pady=10)
# window.add_element(button)

# window.read() 


#---------------------------------Layout example------------------------------------------------------------------------------------------------------------


window = Window("Layout Examples", size=(800, 600) , bg_color="gray")

# \\ Grid Layout Example
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

label_grid1 = Label(text="Grid Label 1", key="lbl_grid1", layout=LAYOUT_GRID, row=0, column=0, padx=5, pady=5)
window.add_element(label_grid1, parent=grid_frame.Widget)  

label_grid2 = Label(text="Grid Label 2", key="lbl_grid2", layout=LAYOUT_GRID, row=0, column=1, padx=5, pady=5 , bg="lime")
window.add_element(label_grid2, parent=grid_frame.Widget)  

button_grid = Button(text="Grid Button", key="btn_grid", layout=LAYOUT_GRID, row=1, column=0, columnspan=2, padx=5, pady=5, frame="raised",fg="red" , bg="lime" , hover_color="blue")
window.add_element(button_grid, parent=grid_frame.Widget)  

# \\ Pack Layout Example
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

label_pack1 = Label(text="Pack Label 1", key="lbl_pack1", layout=LAYOUT_PACK, side="top", padx=5, pady=5)
window.add_element(label_pack1, parent=pack_frame.Widget)  

label_pack2 = Label(text="Pack Label 2", key="lbl_pack2", layout=LAYOUT_PACK, side="top", padx=5, pady=5)
window.add_element(label_pack2, parent=pack_frame.Widget) 

button_pack = Button(text="Pack Button", key="btn_pack", layout=LAYOUT_PACK, side="bottom", padx=5, pady=5)
window.add_element(button_pack, parent=pack_frame.Widget)  

# \\ Place Layout Example
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

label_place1 = Label(text="Place Label 1", key="lbl_place1", layout=LAYOUT_PLACE, x=20, y=20)
window.add_element(label_place1, parent=place_frame.Widget)  

label_place2 = Label(text="Place Label 2", key="lbl_place2", layout=LAYOUT_PLACE, x=120, y=50)
window.add_element(label_place2, parent=place_frame.Widget)  

button_place = Button(text="Place Button", key="btn_place", layout=LAYOUT_PLACE, x=300, y=300)
window.add_element(button_place)  

window.read()


#-----------------------------Canvas example----------------------------------------------------------------------------------------------------------------



# if __name__ == "__main__":
#     window = Window("Canvas Example", size=(400, 400))

#     # Create a canvas
#     canvas = Canvas(key="canvas", width=300, height=300, bg="white", layout=LAYOUT_PLACE, x=50, y=50)
#     window.add_element(canvas)

#     # Draw some shapes on the canvas
#     canvas.draw_line(10, 10, 290, 290, fill="blue", width=2)
#     canvas.draw_rectangle(50, 50, 250, 250, fill="yellow", outline="black")
#     canvas.draw_oval(100, 100, 200, 200, fill="red", outline="black")
#     canvas.draw_text(150, 150, text="Hello, Canvas!", fill="black", font=("Arial", 12))

#     window.read() 


# ----------------------------------------------------------------------------------------------------------------

# if __name__ == "__main__":
#     window = Window("LabelFrame and Notebook Example", size=(500, 400))

#     # Create a LabelFrame
#     label_frame = LabelFrame(text="Group of Widgets", key="group_frame", layout=LAYOUT_PACK, padx=10, pady=10)
#     window.add_element(label_frame)

#     # Add widgets inside the LabelFrame
#     button_inside_frame = Button(text="Click Me", key="button1", layout=LAYOUT_PACK, pady=5)
#     window.add_element(button_inside_frame, parent=label_frame.Widget)


#     window.read()


#-----------------------------tabs , label frame----------------------------------------------------------------------------------------------------------------


# if __name__ == "__main__":
#     # Create the main window
#     window = Window(title="Notebook Example", size=(600, 400), bg_color="white")

#     # Create a Notebook widget
#     notebook = Notebook(key="notebook")
#     window.add_element(notebook)

#     # Add tabs to the notebook
#     tab1 = Label(text="This is Tab 1", key="tab1_label", bg="lightblue")
#     notebook.add_tab("Tab 1", tab1)

#     tab2 = Label(text="This is Tab 2", key="tab2_label", bg="lightgreen")
#     notebook.add_tab("Tab 2", tab2)

#     tab3 = Label(text="This is Tab 3", key="tab3_label", bg="lightyellow")
#     notebook.add_tab("Tab 3", tab3)

#     # Start the main event loop
#     window.read()