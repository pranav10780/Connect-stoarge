#this file is to be a better alternative to termux-setup-storage
import subprocess
import os

path = "ls -a /storage/emulated/0/"
dirs = subprocess.run(path, shell=True , stdout=subprocess.PIPE , text=True)
output=dirs.stdout.split()
link_directory="/data/data/com.termux/files/home/"
for file_name in output:
    source_path = f"/storage/emulated/0/{file_name}"
    link_path = os.path.join(link_directory, file_name)

    try:
        os.symlink(source_path, link_path)
        print(f"Symbolic link created for {file_name}")
    except Exception as e:
        print(f"Error creating symbolic link for {file_name}: {e}")
