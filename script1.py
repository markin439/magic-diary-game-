import random
import tkinter as tk
from tkinter import messagebox


class MagicDiaryGame:

  def __init__(self, root):
    self.root = root
    self.root.title("Гра-клікер «Бомба» / Щоденник мага")
    self.root.geometry("400x300")
    self.root.config(bg="#2c3e50")

    self.score = 0

    self.title_label = tk.Label(
        root,
        text="Збирай магічну енергію!",
        font=("Arial", 14, "bold"),
        bg="#2c3e50",
        fg="#ecf0f1",
    )
    self.title_label.pack(pady=20)

    self.score_label = tk.Label(
        root,
        text=f"Енергія: {self.score}",
        font=("Arial", 16),
        bg="#2c3e50",
        fg="#f39c12",
    )
    self.score_label.pack(pady=10)

    self.click_btn = tk.Button(
        root,
        text="✨ Зібрати енергію ✨",
        font=("Arial", 12, "bold"),
        bg="#e74c3c",
        fg="white",
        padx=10,
        pady=10,
        command=self.increase_score,
    )
    self.click_btn.pack(pady=20)

  def increase_score(self):
    self.score += 1
    self.score_label.config(text=f"Енергія: {self.score}")


if __name__ == "__main__":
  root = tk.Tk()
  app = MagicDiaryGame(root)
  root.mainloop()