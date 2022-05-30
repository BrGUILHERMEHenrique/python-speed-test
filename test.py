import speedtest
import requests
import shutil
from tkinter import *

s = speedtest.Speedtest()

servers = s.get_servers()
for key, value in servers.items():
    val = value
    for se in value:
        print(se["sponsor"], ":" , se["url"])

best_server = s.get_best_server()

print("Servidor escolhido: ", best_server["sponsor"])

print("Download speed(MB/s): ", s.download())
print("Upload speed(MB/s): ", s.upload())
img_url = s.results.share()

res = requests.get(img_url, stream = True)
file_name = "speed_test.png"

if (res.status_code == 200):
    with open(file_name, "wb") as a:
        shutil.copyfileobj(res.raw, a)
        print("Deu bom imagem baixada: ", file_name)
        win = Tk()
        img = PhotoImage(file = file_name)
        img_source = Label(master = win, image = img)
        img_source.pack()
        win.mainloop()
else:
    print("Deu bom não vey")
