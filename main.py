import tkinter as tk


def custom_function(a, b):
    output1 = a % 8
    output2 = b % 8
    output3 = (a + b) % 6
    return output1, output2, output3


# 计算
def calculate():
    a = int(entry_a.get())
    b = int(entry_b.get())
    result1, result2, result3 = custom_function(a, b)
    result_var.set(f"上卦：{result1}, 下卦：{result2}, 动爻：{result3}")

# 创建主窗口


root = tk.Tk()
root.title("简易梅花")
root.geometry('500x300')

# 创建输入框和标签
label_a = tk.Label(root, text="上卦数：")
label_a.grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

label_b = tk.Label(root, text="下卦数：")
label_b.grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

# 创建计算按钮
button = tk.Button(root, text="计算", command=calculate)
button.grid(row=2, column=0, columnspan=2)

# 创建结果标签
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=3, column=0, columnspan=2)

# 运行主循环
root.mainloop()
