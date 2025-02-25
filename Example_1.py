from PyLiteViewGUI import *

def Example_1():
    app = App()
    window = Window("Layout Examples", size=(800, 600) , bg_color="darkgray", resizable=True)
    # window = Window("Layout Examples")
    # window.wm.geometry("800x600")
    # window.wm.configure(bg="darkgray")  
     
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
        bg="gray",
        compound=RIGHT, 
        layout=LAYOUT_PLACE,
        icon="Assets/Pat2.png", 
        icon_size=(32, 32),
        x=300, y=300
    )
    window.add_element(button_place)  
    button_place.set_tooltip("test tool tip text :)") 
    
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
        focus_bg="lightgray", 
        focus_fg="black",  
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
    
    RadioButton1.set_tooltip("This is a Radio Button") 
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
        bg="white",
        frame="raised",
        border_width =10,
        fg="black",
        hover_color="red",
        width=10,
        height=2,
        enable_hover= False
        
    )
    window.add_element(button)
    button.set_margins(20,20)
    button.enable_drag()    
    
    optionMenu1 = OptionMenu(       
        key="drop2",
        options=[1,2,3,4], 
        default=4, 
        layout=LAYOUT_PLACE,
        x=300, y=500,
        hover_color = "#545454"
        
    )
    window.add_element(optionMenu1)

    app.run(window) 

if __name__ == "__main__":
    Example_1() 
