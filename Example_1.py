from PyLiteViewGUI import *

def Example_1():
    app = App()
    window = Window("Layout Examples", size=(800, 600) , bg_color="gray", resizable=True)

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

    label_grid1 = Label(
        text="Grid Label 1", 
        key="lbl_grid1", 
        layout=LAYOUT_GRID, 
        row=0, column=0, 
        padx=5, pady=5
    )
    window.add_element(label_grid1, parent=grid_frame.Widget)  

    label_grid2 = Label(
        text="Grid Label 2", 
        key="lbl_grid2", 
        layout=LAYOUT_GRID, 
        row=0, column=1, 
        padx=5, pady=5 
    )
    window.add_element(label_grid2, parent=grid_frame.Widget)  

    button_grid = Button(
        text="Grid Button", 
        key="btn_grid", 
        layout=LAYOUT_GRID, 
        row=1, column=0, columnspan=2, 
        padx=5, pady=5, 
        frame="raised", 
        hover_color="blue",
        border_width=5
    )
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

    label_pack1 = Label(
        text="Pack Label 1", 
        key="lbl_pack1", 
        layout=LAYOUT_PACK, 
        side="top", 
        padx=5, 
        pady=5
    )
    window.add_element(label_pack1, parent=pack_frame.Widget)  

    label_pack2 = Label(
        text="Pack Label 2", 
        key="lbl_pack2", 
        layout=LAYOUT_PACK, 
        side="top", 
        padx=5, pady=5
    )
    window.add_element(label_pack2, parent=pack_frame.Widget) 

    button_pack = Button(
        text="Pack Button", 
        key="btn_pack",
        font=("Arial", 12, "underline"),
        layout=LAYOUT_PACK, 
        side="bottom",
        padx=5, pady=5
    )
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

    label_place1 = Label(
        text="Place Label 1", 
        key="lbl_place1", 
        layout=LAYOUT_PLACE, 
        x=20, y=20
    )
    window.add_element(label_place1, parent=place_frame.Widget)  

    label_place2 = Label(
        text="Place Label 2", 
        key="lbl_place2", 
        layout=LAYOUT_PLACE, 
        x=120, y=50
    )
    window.add_element(label_place2, parent=place_frame.Widget)  

    button_place = Button(
        text="Place Button", 
        key="btn_place", 
        layout=LAYOUT_PLACE, 
        x=300, y=300
    )
    window.add_element(button_place)  

    Checkbox1 = Checkbox (
        text="test", 
        key="chk1", 
        layout=LAYOUT_PLACE, 
        x=600, y=300
    )
    window.add_element(Checkbox1)

    entry1 = Entry(
        default_text="Type Here...", 
        layout=LAYOUT_PLACE, 
        key="ent1", 
        x=600, y=500
    )
    window.add_element(entry1)

    dropdown1 = Dropdown(
        key="drop1",
        options=[1,2,3,4], 
        default=4, 
        layout=LAYOUT_PLACE, 
        x=300, y=400
    )
    window.add_element(dropdown1)

    RadioButton1 = RadioButton(
        key="rad1", 
        options=["Test"]
    )
    window.add_element(RadioButton1)

    slider1 = Slider(
        key="sld1", 
        min_value=1, max_value=100, 
        default=1, 
        layout=LAYOUT_PLACE, 
        x=100, y=400
    )
    window.add_element(slider1)

    label_frame = LabelFrame(
        text="Group of Widgets", 
        key="group_frame", 
        layout=LAYOUT_PLACE, 
        x=550, y=400
    )
    window.add_element(label_frame)

    button_inside_frame = Button(
        text="Click Me", 
        key="button1"
    )
    window.add_element(button_inside_frame, parent=label_frame.Widget)
    
    spinbox = Spinbox(from_=0, to=100, increment=1,layout=LAYOUT_PLACE, x=550, y=200)
    window.add_element(spinbox)

    def on_button_click():
        print("Button clicked!")

    button = RoundButton(
        text="Click Me",
        key="btn1",
        on_click=on_button_click,
        bg="blue",
        fg="black",
        hover_color="red",
        width=10,
        height=2,
        layout=LAYOUT_GRID,
        row=2,
        column=0,
        padx=10,
        pady=10
    )
    window.add_element(button)
    app.run(window) 


if __name__ == "__main__":
    Example_1() 


#---------------------------------------------------------------------------------------------------------------------------------------------

def Example_2():
    # \\ Create window
    window = Window("Demo App", size=(800, 600))

    # \\ Add list widget
    my_list = ListWidget(
        key="main_list",
        items=["First Item", "Second Item"],
        width=30,
        height=15,
        layout=LAYOUT_GRID,
        row=0,
        column=0,
        padx=100,
        pady=10
    )
    window.add_element(my_list)

    # \\ Create and attach main menu
    menu_bar = Menu(key="main_menu")
    menu_bar.create_widget(window.TKroot)

    # \\ File menu
    file_menu = Menu(key="file_menu")
    menu_bar.add_cascade("File", file_menu)
    file_menu.add_command("Open", lambda: print("Opening..."))
    file_menu.add_separator()
    file_menu.add_command("Exit", window.TKroot.quit)

    # \\  Edit menu
    edit_menu = Menu(key="edit_menu")
    menu_bar.add_cascade("Edit", edit_menu)
    edit_menu.add_command("Copy", lambda: my_list.add_item("Copied Item"))

    window.read() 

# if __name__ == "__main__":
#     Example_2() 
