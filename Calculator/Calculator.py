import tkinter
import math

LARGE_FONT_STYLE = ("Quicksand", 34)
SMALL_FONT_STYLE = ("Quicksand", 18)
DIGIT_FONT_STYLE = ("Quicksand", 22)
DEFAULT_FONT_STYLE = ("Dosis", 20)
LABEL_COLOR = "#154360"


class Calculator:
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.geometry("375x600")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()
        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3),
                       4: (2, 1), 5: (2, 2), 6: (2, 3),
                       1: (3, 1), 2: (3, 2), 3: (3, 3),
                       0: (4, 2), '.': (4, 1)}
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    # Binding Keys to Keyboard:
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_label(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_inverse_button()
        self.create_square_root_button()
        self.create_log_button()
        self.create_sin_button()
        self.create_cos_button()
        self.create_tan_button()

    def create_display_labels(self):
        total_label = tkinter.Label(self.display_frame, text=self.total_expression, anchor=tkinter.E, bg="#1B4F72",
                                    fg="#AED6F1", padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tkinter.Label(self.display_frame, text=self.current_expression, anchor=tkinter.E, bg="#1B4F72",
                              fg="#AED6F1", padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tkinter.Frame(self.window, height=221, bg="#4A235A")
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_label(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tkinter.Button(self.buttons_frame, text=str(digit), bg="#D6EAF8", fg=LABEL_COLOR,
                                    font=DIGIT_FONT_STYLE,
                                    borderwidth=0, command=lambda x=digit: self.add_to_label(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tkinter.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tkinter.Button(self.buttons_frame, text=symbol, bg="#AED6F1", fg=LABEL_COLOR,
                                    font=("Dosis", 24),
                                    borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tkinter.NSEW)
            i += 1

    # Clear Button:
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tkinter.Button(self.buttons_frame, text="C", bg="#AED6F1", fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.clear)
        button.grid(row=0, column=0, sticky=tkinter.NSEW)

    # Square Button:
    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tkinter.Button(self.buttons_frame, text="x\u00b2", bg="#AED6F1", fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tkinter.NSEW)

    # Inverse Button:
    def inverse(self):
        self.current_expression = str(eval(f"{self.current_expression}**-1"))
        self.update_label()

    def create_inverse_button(self):
        button = tkinter.Button(self.buttons_frame, text="1/x", bg="#AED6F1", fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.inverse)
        button.grid(row=0, column=1, sticky=tkinter.NSEW)

    # Log Button:
    def log(self):
        self.current_expression = str(eval(f"math.log({self.current_expression}, 10)"))
        self.update_label()

    def create_log_button(self):
        button = tkinter.Button(self.buttons_frame, text="log(x)", bg="#AED6F1", fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.log)
        button.grid(row=1, column=0, sticky=tkinter.NSEW)

    # Sin Button:
    def sin(self):
        self.current_expression = str(eval(f"math.sin({self.current_expression})"))
        self.update_label()

    def create_sin_button(self):
        button = tkinter.Button(self.buttons_frame, text="sin x", bg="#AED6F1", fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.sin)
        button.grid(row=2, column=0, sticky=tkinter.NSEW)

    # Cos Button:
    def cos(self):
        self.current_expression = str(eval(f"math.cos({self.current_expression})"))
        self.update_label()

    def create_cos_button(self):
        button = tkinter.Button(self.buttons_frame, text="cos x", bg="#AED6F1", fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.sin)
        button.grid(row=3, column=0, sticky=tkinter.NSEW)

    # Tan Button:
    def tan(self):
        self.current_expression = str(eval(f"math.tan({self.current_expression})"))
        self.update_label()

    def create_tan_button(self):
        button = tkinter.Button(self.buttons_frame, text="tan x", bg="#AED6F1", fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.sin)
        button.grid(row=4, column=0, sticky=tkinter.NSEW)

    # Square Root Button:
    def square_root(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_square_root_button(self):
        button = tkinter.Button(self.buttons_frame, text="\u221ax", bg="#AED6F1", fg=LABEL_COLOR,
                                font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.square_root)
        button.grid(row=0, column=3, sticky=tkinter.NSEW)

    # Evaluate Function:
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()

        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ""

        except Exception as exc:
            self.current_expression = "Error"

        finally:
            self.update_label()

    # Equals-To Button:
    def create_equals_button(self):
        button = tkinter.Button(self.buttons_frame, text="=", bg="#2E86C1", fg="#fff", font=DEFAULT_FONT_STYLE,
                                borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=3, sticky=tkinter.NSEW)

    def create_buttons_frame(self):
        frame = tkinter.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # Adding Functionality:
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')

        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


# Driver Code:
calc = Calculator()
calc.run()
