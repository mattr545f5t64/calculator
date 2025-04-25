import tkinter as tk
import math
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("آلة حاسبة متقدمة")
        self.root.geometry("400x600")
        self.root.configure(bg="#1e1e2e")  # خلفية داكنة عصرية
        self.root.resizable(False, False)

        # حقل الإدخال
        self.entry = tk.Entry(root, width=20, font=('Arial', 18, 'bold'), bd=0, 
                             insertwidth=2, justify='right', bg="#2e2e3e", fg="#ffffff",
                             borderwidth=0, relief="flat")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=15)
        self.entry.focus_set()

        # ربط الكتابة عبر لوحة المفاتيح باستخدام KeyPress بدلاً من KeyRelease
        self.root.bind('<Key>', self.on_key_press)

        # إنشاء الأزرار
        self.create_buttons()

    def create_buttons(self):
        button_list = [
            ('C', 1, 0, "#ff5555"), ('(', 1, 1, "#55ff55"), (')', 1, 2, "#55ff55"), ('÷', 1, 3, "#ffaa00"),
            ('7', 2, 0, "#ffffff"), ('8', 2, 1, "#ffffff"), ('9', 2, 2, "#ffffff"), ('×', 2, 3, "#ffaa00"),
            ('4', 3, 0, "#ffffff"), ('5', 3, 1, "#ffffff"), ('6', 3, 2, "#ffffff"), ('−', 3, 3, "#ffaa00"),
            ('1', 4, 0, "#ffffff"), ('2', 4, 1, "#ffffff"), ('3', 4, 2, "#ffffff"), ('+', 4, 3, "#ffaa00"),
            ('0', 5, 0, "#ffffff"), ('.', 5, 1, "#ffffff"), ('=', 5, 2, "#55ff55"), ('√', 5, 3, "#ffaa00"),
            ('sin', 6, 0, "#ffaa00"), ('cos', 6, 1, "#ffaa00"), ('tan', 6, 2, "#ffaa00"), ('^', 6, 3, "#ffaa00")
        ]

        for (text, row, col, fg_color) in button_list:
            button = tk.Button(self.root, text=text, font=('Arial', 14, 'bold'), 
                             bg="#3e3e4e", fg=fg_color, borderwidth=0, relief="flat",
                             activebackground="#4e4e5e", activeforeground=fg_color,
                             command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
            # تأثير الضغط
            button.bind("<Enter>", lambda e, b=button: b.configure(bg="#4e4e5e"))
            button.bind("<Leave>", lambda e, b=button: b.configure(bg="#3e3e4e"))

        # ضبط حجم الصفوف والأعمدة
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                expression = expression.replace('×', '*').replace('÷', '/').replace('^', '**')
                if 'sin' in expression:
                    expression = expression.replace('sin', 'math.sin(math.radians')
                    expression += ')'
                if 'cos' in expression:
                    expression = expression.replace('cos', 'math.cos(math.radians')
                    expression += ')'
                if 'tan' in expression:
                    expression = expression.replace('tan', 'math.tan(math.radians')
                    expression += ')'
                if '√' in expression:
                    expression = expression.replace('√', 'math.sqrt')
                result = eval(expression, {"math": math})
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(round(result, 8)))
            except Exception as e:
                messagebox.showerror("خطأ", "يرجى إدخال تعبير صحيح")
                self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, char)

    def on_key_press(self, event):
        # منع تكرار الإدخال من الكيبورد
        if event.keysym == 'Return':
            self.on_button_click('=')
            return "break"
        elif event.keysym == 'Escape':
            self.on_button_click('C')
            return "break"
        elif event.keysym == 'BackSpace':
            self.entry.delete(len(self.entry.get())-1, tk.END)
            return "break"
        elif event.char in '0123456789.+-*/()':
            # لا تفعل شيئاً، سيتم إدخال الحرف تلقائياً
            pass
        elif event.char == '^':
            self.entry.insert(tk.END, '^')
            return "break"
        elif event.char == 's':
            self.entry.insert(tk.END, 'sin')
            return "break"
        elif event.char == 'c':
            self.entry.insert(tk.END, 'cos')
            return "break"
        elif event.char == 't':
            self.entry.insert(tk.END, 'tan')
            return "break"
        elif event.char == 'r':
            self.entry.insert(tk.END, '√')
            return "break"
        else:
            # تجاهل أي ضغطة مفتاح أخرى
            return "break"

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()