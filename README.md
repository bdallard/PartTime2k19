# JEDHA 2019 part time session

## Set up : intaller ses outils de travail 

### Anaconda

Pour télecharger anaconda gratuitement sur MacOS ou bien Windows [cliquer ici](https://www.anaconda.com/distribution/).

**Si vous avez installé Anaconda, la partie set up ci-dessous ne vous concerne pas!** 

### Pour ceux qui ne veulent pas installer Anaconda  : Set up à la mano
Pour ceux qui ne veulent pas utiliser anaconda vous pouvez bien sur installer python, pip, jupyter et les autres librairies manuellement. Ci-dessous un petit résumé des commandes.
#### Installer Python 3.x (3.4, 3.5 ou 3.6) et son gestionnaire de paquets pip (pip3 pour python3)
**Pour Windows** : <https://www.python.org/downloads/windows/>

**Pour Mac** : <https://www.python.org/downloads/mac-osx/>

ou avec le terminal de Mac Os : 
```
brew install python3
brew install python3-pip
```

<a href ="https://brew.sh/index_fr"> <img src="https://upload.wikimedia.org/wikipedia/commons/3/34/Homebrew_logo.png">

#### Installer Homebrew sur votre Mac 
Si les commandes ci-dessus ne fonctionnent pas c'est que **vous n'avez pas Homebrew sur votre Mac** ! 
Cliquer sur le logo ci-dessus et suivre le tutoriel d'installation. 

#### Installer Jupyter 
Jupyter est une application web permettant de créer des notebooks, des fichiers mélangeant à la fois du texte (en syntaxe markdown), des images, des équations mathématiques et bien sur du code.

Lancer la commande suivante : 
```
 pip3 install jupyter
``` 

#### Installer les dépendances usuelles 
Lancer la commande suivante : 
```
pip3 install numpy matplotlib scipy requests pandas scikit-learn
```


## Configurer un bon environnement de travail

### Rappel des commandes de bases 
- pwd : ou je suis (dans quel dossier je suis) 
- cd *MonRepo* : changer de dossier (direcrtory)
- ls : lister les objets présents (fichier et dossier) dans le répertoire sélectionné
- mkdir *NewRepo* : créer un nouveau dossier de nom *NewRepo*  
- rm *UnFichier* : supprimer un fichier (attention avec cette commande!) 
- man *UneCommande* : afficher le manuel de la commande sélectionnée

## Organisation du repo 
Ce repo suit l'organisation de votre Drive. 

### Les séances et exercices
Les séances sont donc numérotées semaines par semaines, *S-i* fait donc référence à *la semaine numéro i*. Chaque dossier S-i contient donc deux sous dossier S-iA et S-iB, où A correspond à la séance du lundi et B celle du samedi.

### Les projets 
Comme vous le savez, chaque semaine vous devez faire des projets. **Les projets seront déposés sur la branche DEV dans le repo Projets à la racine de ce git.** 
