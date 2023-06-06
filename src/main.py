import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog


def backup_files(source_dir, destination_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print("Source directory does not exist.")
        return

    # Check if the destination directory exists, if not, create it
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get a list of files in the source directory
    files = os.listdir(source_dir)

    # Backup each file in the source directory
    for file_name in files:
        source_file = os.path.join(source_dir, file_name)
        destination_file = os.path.join(destination_dir, file_name)

        # Check if the file is a regular file (not a directory)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)
            print(f"File '{file_name}' backed up successfully.")

    print("Backup complete.")


def main():
    main_win = tk.Tk()
    main_win.title("Backupper!")
    main_win.geometry("1000x500")
    main_win.source_folder = ''
    main_win.destination_folder = ''

    def choose_dir():
        main_win.source_folder = filedialog.askdirectory(
            parent=main_win, initialdir="/", title='Por favor, elija un directorio...')
        folder_text = tk.Label(main_win, text=main_win.source_folder)
        folder_text.place(x=50, y=150)

    button_choose_dir = tk.Button(
        main_win, text="Directorio a respaldar", width=20, height=3, command=choose_dir)
    button_choose_dir.place(x=50, y=50)
    button_choose_dir.width = 100

    def choose_destination_dir():
        main_win.destination_folder = filedialog.askdirectory(
            parent=main_win, initialdir="/", title='Por favor, elija un directorio...')
        destination_folder_text = tk.Label(
            main_win, text=main_win.destination_folder)
        destination_folder_text.place(x=250, y=150)

    def finish_backup():
        choose_destination_dir()
        backup_files(main_win.source_folder, main_win.destination_folder)
        messagebox.showinfo(
            message="Respaldo finalizado con exito!", title="Backupper!")

    button_destination_dir = tk.Button(
        main_win, text="Guardar respaldo en", width=20, height=3, command=finish_backup)
    button_destination_dir.place(x=250, y=50)
    button_destination_dir.width = 100

    main_win.mainloop()

    print(main_win.source_folder)
    print(main_win.destination_folder)


if __name__ == "__main__":
    main()
