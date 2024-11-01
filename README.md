# Mandelbrot et Julia Set Visualization

Ce projet contient un package Python pour visualiser et générer les ensembles de Mandelbrot et de Julia, deux ensembles fractals complexes. Ces ensembles sont représentés sous forme d'images et sont calculés en fonction de points complexes, permettant de créer de magnifiques fractales.

## Table des matières
- [Aperçu](#aperçu)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Exemples](#exemples)

## Aperçu

L'ensemble de Mandelbrot et les ensembles de Julia sont des fractales obtenues par itérations de suites complexes. Ce projet inclut des fonctions Python permettant de calculer et de visualiser ces ensembles. Les fonctionnalités principales incluent :

- Génération d'une suite complexe pour un nombre d'itérations donné
- Détermination de l'appartenance d'un point à l'ensemble de Mandelbrot
- Génération d'un ensemble de Julia pour un point donné
- Affichage des ensembles de Mandelbrot et Julia en utilisant Matplotlib

## Installation

Assurez-vous que les modules `numpy` et `matplotlib` sont installés. Pour les installer, utilisez la commande suivante :

```bash
pip install numpy matplotlib
```
Pour installer le package, clonez ce dépôt et installez les dépendances nécessaires avec les commandes suivantes :

```bash
# Clonez le dépôt
git clone <https://github.com/Jleduc23/TP_Leduc_Jun_Mandelbrot>


# Naviguez vers le répertoire du projet
cd Mandelbrot_Julia_TP

# Installez les dépendances
pip install numpy matplotlib
```

## Utilisation

Ce projet permet de visualiser les ensembles de Mandelbrot et de Julia. Vous pouvez exécuter les scripts pour générer les images correspondantes en ligne de commande.

Pour utiliser mandelbrot

```bash
python -m mandelbrot_julia.main_mandelbrot
```

Pour utiliser julia avec un paramètre 

```bash
python -m mandelbrot_julia.main_julia --param 0.355+0.355j
```

## Exemples 

Le dossier images contient deux rendus du code, un pour l'ensemble de Mandelbrot, un pour Julia.

## 


