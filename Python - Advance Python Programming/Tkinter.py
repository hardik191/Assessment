import os
import tkinter as tk
from tkinter import messagebox


class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def filename(self):
        return f"playlist_{self.name}.txt"

    def save_to_file(self):
        folder = "playlists"
        if not os.path.exists(folder):
            os.mkdir(folder)

        filepath = os.path.join(folder, self.filename())

        if os.path.exists(filepath):
            raise FileExistsError("Playlist already exists!")

        with open(filepath, "w", encoding="utf-8") as f:
            for song in self.songs:
                f.write(song + "\n")

    @staticmethod
    def load_from_file(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            songs = f.read().splitlines()
        return songs
 
 
class MusicBoxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 MusicBox - Playlist Manager")
        self.root.geometry("600x400")

        # Labels
        tk.Label(root, text="Playlist Name:").pack(anchor="w", padx=10, pady=5)

        # Entry for Playlist Name
        self.playlist_entry = tk.Entry(root, width=40)
        self.playlist_entry.pack(padx=10)

        tk.Label(root, text="Enter Songs (one per line):").pack(anchor="w", padx=10, pady=5)

        # Text widget for songs
        self.song_text = tk.Text(root, height=8, width=50)
        self.song_text.pack(padx=10)

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Save Playlist", command=self.save_playlist).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Refresh Playlists", command=self.load_playlists).pack(side="left", padx=5)

        # Listbox for playlists
        tk.Label(root, text="Saved Playlists:").pack(anchor="w", padx=10)
        self.playlist_listbox = tk.Listbox(root, width=40, height=8)
        self.playlist_listbox.pack(padx=10, pady=5)
        self.playlist_listbox.bind("<<ListboxSelect>>", self.show_playlist)

        # Load playlists on start
        self.load_playlists()

    def load_playlists(self):
        self.playlist_listbox.delete(0, tk.END)
        folder = "playlists"

        if not os.path.exists(folder):
            os.mkdir(folder)

        for file in os.listdir(folder):
            if file.startswith("playlist_") and file.endswith(".txt"):
                self.playlist_listbox.insert(tk.END, file)


    def save_playlist(self):
        name = self.playlist_entry.get().strip()
        songs_text = self.song_text.get("1.0", tk.END).strip()

        try:
            if not name:
                raise ValueError("Playlist name cannot be empty!")
            if not songs_text:
                raise ValueError("Song list cannot be empty!")

            songs = [song.strip() for song in songs_text.split("\n") if song.strip()]

            playlist = Playlist(name, songs)
            playlist.save_to_file()

            messagebox.showinfo("Success", "Playlist saved successfully!")
            self.load_playlists()

        except FileExistsError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f" {e}")


    def show_playlist(self, event):
        try:
            selected = self.playlist_listbox.get(self.playlist_listbox.curselection())
            filepath = os.path.join("playlists", selected)

            songs = Playlist.load_from_file(filepath)

            self.song_text.delete("1.0", tk.END)
            self.song_text.insert(tk.END, "\n".join(songs))

        except Exception:
            pass



if __name__ == "__main__":
    root = tk.Tk()
    app = MusicBoxApp(root)
    root.mainloop()
