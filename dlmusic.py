import youtube_dl
import os
import subprocess
import shutil
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
print("Debut du programme \nRecuperation des liens youtube")
with open("liens.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

print("Telechargement des musiques :")
for url in content:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print("Deplacement des Musiques pour modifier leurs noms")
subprocess.call("mv ./*.mp3 ./Musique", shell=True)
directory = "./Musique"

print("Suppression de l id present dans le nom du fichier")
for filename in os.listdir('./Musique'):
    print(filename)
    path = os.path.join(directory, filename)
    rep = filename.replace(filename[-16:], ".mp3")
    target = os.path.join(directory, rep)
    os.rename(path, target)
    shutil.move(target,"../../Musique")

print("Remise au propre du fichier liens.txt")
subprocess.call("echo "">liens.txt", shell=True)

print("Complete")

