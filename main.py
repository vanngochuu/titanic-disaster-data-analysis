import tkinter as tk
from tkinter import messagebox, Toplevel
from data_loader import load_csv
from data_cleaning import clean_data
from visualization import plot_survival, plot_gender


class TitanicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PHÂN TÍCH DỮ LIỆU THẢM HỌA TITANIC")
        self.root.geometry("900x520")

        self.df_raw = load_csv("data/titanic_disaster_data.csv")
        self.df = self.df_raw.copy()

        tk.Label(root, text="PHÂN TÍCH DỮ LIỆU THẢM HỌA TITANIC", font=("Arial", 20, "bold")).pack(pady=10)

        tk.Button(root, text="Làm sạch dữ liệu", width=35, command=self.process).pack(pady=5)
        tk.Button(root, text="Xem 10 dòng đầu", width=35, command=self.show_head).pack(pady=5)
        tk.Button(root, text="Xem toàn bộ dữ liệu", width=35, command=self.show_all).pack(pady=5)
        tk.Button(root, text="Biểu đồ sống sót", width=35, command=self.plot1).pack(pady=5)
        tk.Button(root, text="Biểu đồ theo giới tính", width=35, command=self.plot2).pack(pady=5)

    def process(self):
        self.df = clean_data(self.df_raw.copy())
        messagebox.showinfo("Xong", "Đã làm sạch & chuẩn hóa dữ liệu!")

    def show_head(self):
        self.show_window(self.df.head(10), "10 dòng đầu của dữ liệu")

    def show_all(self):
        self.show_window(self.df, "Toàn bộ dữ liệu Titanic")

    def show_window(self, df_show, title):
        win = Toplevel(self.root)
        win.title(title)
        win.state('zoomed')

        frame = tk.Frame(win)
        frame.pack(expand=True, fill="both")

        y_scroll = tk.Scrollbar(frame)
        y_scroll.pack(side="right", fill="y")

        x_scroll = tk.Scrollbar(frame, orient="horizontal")
        x_scroll.pack(side="bottom", fill="x")

        text = tk.Text(frame, wrap="none",
                       yscrollcommand=y_scroll.set,
                       xscrollcommand=x_scroll.set)
        text.pack(expand=True, fill="both")

        y_scroll.config(command=text.yview)
        x_scroll.config(command=text.xview)

        # Ẩn các cột kỹ thuật bắt đầu bằng _
        df_view = df_show[[c for c in df_show.columns if not c.startswith('_')]]

        text.insert(tk.END, df_view.to_string())

    def plot1(self):
        plot_survival(self.df)

    def plot2(self):
        plot_gender(self.df)


def main():
    root = tk.Tk()
    app = TitanicApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()