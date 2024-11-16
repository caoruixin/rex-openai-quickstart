import tkinter as tk
from tkinter import messagebox

class BasicCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("基本功能计算器")
        self.master.geometry("600x800")
        
        self.result_var = tk.StringVar()
        self.create_widgets()
        
        self.history = []  # 用于存储计算历史

    def create_widgets(self):
        # 显示区域
        display_frame = tk.Frame(self.master)
        display_frame.pack(pady=20)

        self.result_display = tk.Entry(display_frame, textvariable=self.result_var, font=('Arial', 24), justify='right')
        self.result_display.grid(row=0, column=0, ipadx=8, columnspan=4)

        # 按键区域
        button_frame = tk.Frame(self.master)
        button_frame.pack()

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            if button == '=':
                btn = tk.Button(button_frame, text=button, command=self.calculate_result, width=10)
            elif button == 'C':
                btn = tk.Button(button_frame, text=button, command=self.clear_display, width=10)
            else:
                btn = tk.Button(button_frame, text=button, command=lambda b=button: self.add_to_display(b), width=10)
            btn.grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def add_to_display(self, value):
        current_text = self.result_var.get()
        self.result_var.set(current_text + value)

    def clear_display(self):
        self.result_var.set("")

    def calculate_result(self):
        try:
            expression = self.result_var.get().replace('/', '/')
            result = eval(expression)
            self.result_var.set(result)
            self.history.append(expression + " = " + str(result))  # 保存历史记录
        except ZeroDivisionError:
            messagebox.showerror("错误", "除以零的运算无效！")
        except Exception as e:
            messagebox.showerror("错误", "无效输入！请检查您的输入。")

if __name__ == "__main__":
    root = tk.Tk()
    calculator = BasicCalculator(root)
    root.mainloop()
