import time
import tkinter as tk
from tkinter import messagebox
from CubeSolver import Cube, A_star_algorithm

def solve_cube():
    cube_string = cube_entry.get()

    if len(cube_string) != 8:
        messagebox.showerror("Invalid Cube", "Invalid cube string. Please enter a valid Rubik's Cube state.")
        return

    test_cube = Cube(cube_string)
    start_time = time.time()
    moves = A_star_algorithm(test_cube, test_cube.SOLVED_STATE)
    end_time = time.time()
    
    if moves == -1:
        messagebox.showinfo("Rubik's Cube Solver", "Unable to solve the cube.")
    else:
        messagebox.showinfo("Rubik's Cube Solver", f"Solved the cube in {moves}  in {end_time - start_time} seconds.")

# Create the main window
window = tk.Tk()
window.title("Rubik's Cube Solver")

# Create a label and entry for cube input
cube_label = tk.Label(window, text="Enter the cube state (8 characters):")
cube_label.pack()
cube_entry = tk.Entry(window)
cube_entry.pack()

# Create a solve button
solve_button = tk.Button(window, text="Solve", command=solve_cube)
solve_button.pack()

# Start the GUI event loop
window.mainloop()



