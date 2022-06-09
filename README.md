# USB-KeyLogger
<sub> Un keylogger pour clé usb  </sub>


**FEATURES:**
- Deconnexion de toutes sessions sur le navigateur
- Détection du navigateur par défaut
- Envoie des touches par mail/drive/docs,...
- Ouvre des pages sur le navigateur

PS: certaines fonctionnalités sont en cours de développement et d'autres peuvent voir le jour

--------------------------------------------------------

**FONCTIONNEMENT:**
1) Ouvre une fenetre de navigateur avec le site de votre choix (l'utilisateur est déconnecté de toute session sur ce site afin qu'il doive se reconnecter)
2) Toutes les touches sont enregistrées dans un fichier texte dans le répertoire fourni.

--------------------------------------------------------

**Le faire fonctionner sur une clé USB**
1) Obfusquer et/ou chiffrer le code pour le rendre indétectable. Vous pouvez utiliser des tools comme [celui là](https://github.com/spicesouls/onelinepy)
2) Compiler en .exe avec [pyinstaller](https://pyinstaller.org/en/stable/) ou sinon trouver un autre format afin de pouvoir l'exécuter sur la victime.
3) Mettre le keylogger sur la clé et le mettre en autorun à l'aide de [cet outil](https://usb-autorun-creator.fr.softonic.com/)

--------------------------------------------------------

**Bibliotèques Python à installer:**

_Pour installer une bibliotèque:_

1) Ouvrir le CMD
2) pip install nom_de_la_bibliotèque

Pynput

os
  
webbrowser
  
winreg
  
shlex

--------------------------------------------------------

**Projet en cours de developpement, vous trouverez dans le code source des parties qui serviront à des futures fonctionnalitées**
