import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

animals = {
    "Elephant": "elephant.png",
    "Giraffe": "giraffe.png",
    "Hippopotamus": "hippo.png",
    "Kangaroo": "kangaroo.png",
    "Lion": "lion.png",
    "Panda": "panda.png",
    "Penguin": "penguin.png",
    "Rhino": "rhino.png",
    "Tiger": "tiger.png",
    "Zebra": "zebra.png"
}

class GuessFrame(tk.Frame):
    def __init__(self, master, animal):
        super().__init__(master)

        self.animal = animal
        self.master = master

        # Set up image
        image_path = "images/" + animals[self.animal]
        image = Image.open(image_path)
        image = image.resize((250, 250), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(image)

        # Set up labels
        self.title_label = tk.Label(self, text="Guess the animal!")
        self.title_label.pack(pady=10)

        self.image_label = tk.Label(self, image=self.photo)
        self.image_label.pack(pady=10)

        self.prompt_label = tk.Label(self, text="What is the name of this animal?")
        self.prompt_label.pack(pady=10)

        # Set up entry box and button
        self.entry_var = tk.StringVar()
        self.entry_box = tk.Entry(self, textvariable=self.entry_var)
        self.entry_box.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=10)

    def check_answer(self):
        answer = self.entry_var.get().lower()
        if answer == self.animal.lower():
            messagebox.showinfo("Correct!", "You guessed it!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the answer was {self.animal}")

        self.master.play_game()

class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Animal Guessing Game")

        # Shuffle animals and pick first one
        self.animals_list = list(animals.keys())
        random.shuffle(self.animals_list)
        self.current_animal = self.animals_list[0]

        # Set up guess frame
        self.guess_frame = GuessFrame(self, self.current_animal)
        self.guess_frame.pack()

    def play_game(self):
        # Remove current frame and set up new one with next animal
        self.guess_frame.destroy()
        self.animals_list.pop(0)
        if len(self.animals_list) > 0:
            self.current_animal = self.animals_list[0]
            self.guess_frame = GuessFrame(self, self.current_animal)
            self.guess_frame.pack()
        else:
            # No more animals left, end the game
            messagebox.showinfo("Game Over", "You have guessed all the animals!")


if __name__ == "__main__":
    game = Game()
    game.mainloop()
