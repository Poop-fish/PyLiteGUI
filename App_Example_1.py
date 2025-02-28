from PyLiteViewGUI import *

class Calculator:
    def __init__(self, window: 'Window'):
        self.window = window
        self.first_number = ""
        self.second_number = ""
        self.operation = ""
        self.result = ""
        self.create_widgets()

    def create_widgets(self):
        self.display = Entry(
            key="display",
            default_text="0",
            width=20,
            font=("Arial", 14),
            bg="white",
            fg="black",
            layout=LAYOUT_GRID,
            row=0,
            column=0,
            columnspan=4,
            padx=10,
            pady=10
        )
        self.window.add_element(self.display)

        self.button_frame = Frame(
            key="button_frame",
            bg="lightgray",
            layout=LAYOUT_GRID,
            row=1,
            column=0,
            columnspan=4,
            padx=5,
            pady=5
        )
        self.window.add_element(self.button_frame)

        button_layout = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('C', 4, 0)
        ]

        self.buttons = {}
        for text, row, col in button_layout:
            btn_key = f"btn_{text}"
            btn = Button(
                text=text,
                key=btn_key,
                on_click=lambda x=text: self.button_click(x),
                width=5,
                height=2,
                bg="lightgray",
                fg="black",
                font=("Arial", 12),
                hover_color="gray",
                layout=LAYOUT_GRID,
                row=row,
                column=col,
                padx=2,
                pady=2,
                frame="raised"
            )
            self.buttons[text] = btn
            self.window.add_element(btn, parent=self.button_frame.Widget)

            if text == 'C':
                btn.layout_options.update({"columnspan": 4, "sticky": "ew"})
                btn.apply_layout()

    def button_click(self, value: str):
        if value == 'C':
            self.clear()
        elif value in '0123456789.':
            self.handle_number(value)
        elif value in '+-*/':
            self.handle_operation(value)
        elif value == '=':
            self.calculate()

        self.update_display()

    def clear(self):
        self.first_number = ""
        self.second_number = ""
        self.operation = ""
        self.result = ""
        self.display.var.set("0")

    def handle_number(self, value: str):
        if not self.operation:
            if value == '.' and '.' in self.first_number:
                return
            self.first_number += value
        else:
            if value == '.' and '.' in self.second_number:
                return
            self.second_number += value

    def handle_operation(self, value: str):
        if self.first_number and not self.second_number:
            self.operation = value

    def calculate(self):
        if self.first_number and self.second_number and self.operation:
            try:
                num1 = float(self.first_number)
                num2 = float(self.second_number)

                if self.operation == '+':
                    self.result = num1 + num2
                elif self.operation == '-':
                    self.result = num1 - num2
                elif self.operation == '*':
                    self.result = num1 * num2
                elif self.operation == '/':
                    if num2 == 0:
                        self.result = "Error: Division by zero"
                    else:
                        self.result = num1 / num2
                self.first_number = str(self.result) if isinstance(self.result, (int, float)) else ""
                self.second_number = ""
                self.operation = ""
                
            except ValueError:
                self.result = "Error"

    def update_display(self):
        if self.result != "":
            display_value = str(self.result)
        elif self.second_number:
            display_value = self.second_number
        elif self.operation:
            display_value = f"{self.first_number} {self.operation}"
        elif self.first_number:
            display_value = self.first_number
        else:
            display_value = "0"

        self.display.var.set(display_value)


def main():
    app = App()
    window = Window(
        title="Calculator",
        size=(250, 350),
        bg_color="lightgray",
        resizable=False
    )
    Calculator(window)
    app.run(window)

if __name__ == "__main__":
    main()
 