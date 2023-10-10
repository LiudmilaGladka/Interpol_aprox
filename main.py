import numpy as np
from tkinter import Tk, filedialog, Label, Button
import matplotlib.pyplot as plt

def least_squares(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x*y)

    m = (n*sum_xy - sum_x*sum_y) / (n*sum_x_squared - sum_x**2)
    b = (sum_y - m*sum_x) / n

    return m, b

def choose_file():
    Tk().withdraw()  # Запуск Tkinter, але без головного вікна
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])  # Відкрити діалог вибору файлу
    return filename

def process_data():
    # Вибір файлу та зчитування даних
    file_path = choose_file()
    data = np.loadtxt(file_path, delimiter=',')

    # Розділення даних на стовпці x та y
    x = data[:, 0]
    y = data[:, 1]

    # Виклик функції та отримання коефіцієнтів
    m, b = least_squares(x, y)

    # Виведення результатів
    result_label.config(text=f"Отримана лінійна функція: y = {m:.2f}x + {b:.2f}")

    # Графічне представлення
    plt.scatter(x, y, color='blue', label='Дані')
    plt.plot(x, m*x + b, color='red', label='Лінійна регресія')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

def exit_program():
    root.quit()

# Створення головного вікна
root = Tk()
root.title("Лінійна Регресія")

# Додавання елементів на форму
choose_file_button = Button(root, text="Вибрати файл", command=process_data)
choose_file_button.pack(pady=20)

exit_button = Button(root, text="Вихід", command=exit_program)
exit_button.pack(pady=10)

result_label = Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=10)

# Запуск головного циклу
root.mainloop()
