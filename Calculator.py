import tkinter as tk  # Импортируем библиотеку tkinter для создания графического интерфейса
from tkinter import messagebox  # Импортируем messagebox для отображения сообщений об ошибках
import math  # Импортируем библиотеку math для выполнения математических операций

class ScientificCalculator:
    def __init__(self, master):
        self.master = master  # Сохраняем ссылку на главный объект окна
        self.master.title("Физический научный калькулятор")  # Устанавливаем заголовок окна
        
        self.expression = ""  # Переменная для хранения текущего выражения
        self.memory = [0, 0, 0]  # Массив для хранения значений памяти (3 ячейки)
        
        # Создание текстового поля для отображения выражения
        self.display = tk.Entry(master, width=40, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=5)  # Размещаем текстовое поле в сетке

        # Создание кнопок калькулятора
        self.create_buttons()

    def create_buttons(self):
        # Определяем кнопки и их расположение в сетке
        buttons = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('-', 3, 3),
            ('.', 4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2),
            ('ln', 5, 3), ('log10', 6, 0),
            ('M1', 6, 1), ('M2', 6, 2), ('M3', 6, 3),
            ('C', 7, 0)
        ]

        for (text, row, col) in buttons:  
            # Создаем кнопку в зависимости от ее текста
            if text == '=':
                btn = tk.Button(self.master, text=text, command=self.calculate)  
                # Кнопка "равно" вызывает метод calculate
            elif text == 'C':
                btn = tk.Button(self.master, text=text, command=self.clear)  
                # Кнопка "C" очищает текущее выражение
            elif text in ['M1', 'M2', 'M3']:
                btn = tk.Button(self.master, text=text,
                                command=lambda t=text: self.memory_function(t))  
                # Кнопки памяти вызывают метод memory_function с соответствующим номером ячейки
            else:
                btn = tk.Button(self.master, text=text,
                                command=lambda t=text: self.append_to_expression(t))  
                # Остальные кнопки добавляют символы к текущему выражению
            
            btn.grid(row=row, column=col)  
            # Размещаем кнопку в сетке по заданным координатам

    def append_to_expression(self, value):
        """Добавляет значение к текущему выражению и обновляет дисплей."""
        self.expression += str(value)  
        self.display.delete(0, tk.END)  
        self.display.insert(0, self.expression)  

    def calculate(self):
        """Вычисляет результат текущего выражения и обновляет дисплей."""
        try:
            result = eval(self.expression.replace('sin', 'math.sin')
                                   .replace('cos', 'math.cos')
                                   .replace('tan', 'math.tan')
                                   .replace('ln', 'math.log')
                                   .replace('log10', 'math.log10'))  
            # Используем eval для вычисления выражения с заменой функций на соответствующие из модуля math
            
            self.display.delete(0, tk.END)  
            self.display.insert(0, result)  
            self.expression = str(result)  
        except Exception as e:
            messagebox.showerror("Ошибка", "Неверное выражение!")  
            # Обработка ошибок и вывод сообщения об ошибке

    def clear(self):
        """Очищает текущее выражение и дисплей."""
        self.expression = ""  
        self.display.delete(0, tk.END)  

    def memory_function(self, mem_slot):
        """Сохраняет текущее значение в указанную ячейку памяти."""
        if mem_slot == 'M1':
            self.memory[0] = float(self.display.get())  
        elif mem_slot == 'M2':
            self.memory[1] = float(self.display.get())  
        elif mem_slot == 'M3':
            self.memory[2] = float(self.display.get())  
        
        messagebox.showinfo("Память", f"Значение сохранено в {mem_slot}: {self.memory[int(mem_slot[1])-1]}")  
        # Вывод сообщения о сохранении значения в память

if __name__ == "__main__":
    root = tk.Tk()  
    calculator = ScientificCalculator(root)  
    root.mainloop()  
    # Запуск главного цикла приложения
