# Cahier des charges 
## Saphie Project :

Saphie est un projet qui a pour but de crée un outil de stéganographie de trois type : Photographie, Audio (Spectre), Vidéo.

### Quel languages ?
* Script : Python
* Web : HTML, CSS, Java Script

### **Objectifs**
*1er Objectif:* Cryptage stéganographique de trois type : Image, Vidéo, Audio (Spectre) 

*2ème Objectif :* Echange de clé de chifferement

*3ème Objectif :* Support Web

### A faire pour le fonctionnement de l'outil :

***Fonction :***
* Stéganographie [Image](./Fonctions/steg_image.py)
* Stéganographie [Spectre](./Fonctions/steg_spectre.py)
* Stéganographie [Video](./Fonctions/steg_video.py) 

***Class :***
* Ajout des fonctions dans une class pour faciliter l'usage

(*Facultatif* :)

* Echange de clé sécurisé 
* Interface Web 

**Difficultées potentielles** :

Pour la première partie la difficulté principale sera de bien comprendre les packages et savoir comment les utiliser afin de concevoir notre outil.

La deuxième est de savoir comment échanger nos clé de chiffrement.

La dernière partie sera de concevoir une app-web pour utiliser notre outil de façon plus claire pour faire ceci nous devrons nous documenté sur comment le réaliser.

La partie la plus complexe en termes de conception sera les programmes a réaliser.