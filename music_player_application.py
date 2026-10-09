import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame

# Initialize Pygame audio
try:
    pygame.mixer.init()
except pygame.error as error:
    print("Audio could not start:", error)

# Create the application window
window = tk.Tk()
window.title("My Music Player")
window.geometry("460x350")
window.configure(bg="#f4f0ff")

song_path = ""


def choose_song():
    global song_path

    selected_file = filedialog.askopenfilename(
        title="Choose a song",
        filetypes=[
            ("Music files", "*.mp3 *.wav *.ogg"),
            ("All files", "*.*")
        ]
    )

    if selected_file:
        song_path = selected_file
        song_name = os.path.basename(song_path)
        song_label.config(text=song_name)
        status_label.config(text="Song selected. Press Play!")


def play_song():
    if not song_path:
        choose_song()

    if song_path:
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            status_label.config(text="Playing music...")
        except pygame.error as error:
            messagebox.showerror("Playback Error", str(error))


def pause_song():
    if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        status_label.config(text="Music paused.")


def resume_song():
    if pygame.mixer.get_init():
        pygame.mixer.music.unpause()
        status_label.config(text="Music resumed.")


def stop_song():
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()
        status_label.config(text="Music stopped.")


def close_player():
    if pygame.mixer.get_init():
        pygame.mixer.music.stop()
        pygame.mixer.quit()
    window.destroy()


# Heading
heading = tk.Label(
    window,
    text="♫  My Music Player",
    font=("Arial", 20, "bold"),
    bg="#f4f0ff",
    fg="#50358c"
)
heading.pack(pady=(22, 8))

subtitle = tk.Label(
    window,
    text="Choose a song and enjoy!",
    font=("Arial", 10),
    bg="#f4f0ff",
    fg="#5f5a70"
)
subtitle.pack(pady=(0, 18))

# Song information
song_card = tk.Frame(
    window, bg="white", padx=14, pady=14
)
song_card.pack(fill="x", padx=28, pady=4)

song_label = tk.Label(
    song_card,
    text="No song selected",
    font=("Arial", 11, "bold"),
    bg="white",
    fg="#30264b",
    wraplength=360
)
song_label.pack()

status_label = tk.Label(
    window,
    text="Ready to play",
    font=("Arial", 10),
    bg="#f4f0ff",
    fg="#5f5a70"
)
status_label.pack(pady=12)

# Choose Song button
choose_button = tk.Button(
    window,
    text="Choose Song",
    command=choose_song,
    font=("Arial", 10, "bold"),
    bg="#d9ccff",
    fg="#30264b",
    activebackground="#c7b4ff",
    relief="flat",
    padx=16,
    pady=7,
    cursor="hand2"
)
choose_button.pack(pady=4)

# Music control buttons
controls = tk.Frame(window, bg="#f4f0ff")
controls.pack(pady=12)

play_button = tk.Button(
    controls,
    text="▶ Play",
    command=play_song,
    width=9,
    font=("Arial", 10, "bold"),
    bg="#8b6bd6",
    fg="white",
    relief="flat",
    padx=5,
    pady=8,
    cursor="hand2"
)
play_button.pack(side="left", padx=4)

pause_button = tk.Button(
    controls,
    text="Ⅱ Pause",
    command=pause_song,
    width=9,
    font=("Arial", 10, "bold"),
    bg="#ded6f5",
    fg="#30264b",
    relief="flat",
    padx=5,
    pady=8,
    cursor="hand2"
)
pause_button.pack(side="left", padx=4)

resume_button = tk.Button(
    controls,
    text="▶ Resume",
    command=resume_song,
    width=9,
    font=("Arial", 10, "bold"),
    bg="#ded6f5",
    fg="#30264b",
    relief="flat",
    padx=5,
    pady=8,
    cursor="hand2"
)
resume_button.pack(side="left", padx=4)

stop_button = tk.Button(
    controls,
    text="■ Stop",
    command=stop_song,
    width=9,
    font=("Arial", 10, "bold"),
    bg="#ded6f5",
    fg="#30264b",
    relief="flat",
    padx=5,
    pady=8,
    cursor="hand2"
)
stop_button.pack(side="left", padx=4)

# Close the application safely
window.protocol("WM_DELETE_WINDOW", close_player)

# Run the application
window.mainloop()
