import youtube_dl
import os
import subprocess

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
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

print("Telechargement des musiques :")
for url in content:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print("Deplacement des Musiques pour modifier leurs noms")
subprocess.call("mv ./*.mp3 ./Musique", shell=True)
directory = "./Musique"
for filename in os.listdir('./Musique'):
    print(filename)
    path = os.path.join(directory, filename)
    rep = filename.replace(filename[-16:], ".mp3")
    target = os.path.join(directory, rep)
    os.rename(path, target)

print("Placement des musiques dans le Dossier Musique du Desktop")
subprocess.call("mv ./Musique/*.mp3 ../Musique", shell=True)

print("Remise au propre du fichier liens.txt")
subprocess.call("echo "">liens.txt", shell=True)

print("Complete")


"""/Library/Frameworks/Python.framework/Versions/3.6/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin   CHEMIN VERS PYTHON"""