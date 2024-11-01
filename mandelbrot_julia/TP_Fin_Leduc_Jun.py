#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 01:38:12 2024

@author: leduc-beppujun
"""

import matplotlib.pyplot as plt
import numpy as np

def suite(z, c, nb_iter):
    """
    Calcule la suite itérative z_{n+1} = z_n^2 + c pour un nombre d'itérations donné.
    
    Paramètres:
    - z (complex): Point initial de la suite.
    - c (complex): Paramètre constant de la suite.
    - nb_iter (int): Nombre d'itérations.

    Retourne:
    - np.ndarray: Liste des valeurs de la suite (type complexe).
    """
    Liste_suite = np.zeros(nb_iter + 1, dtype=complex)
    Liste_suite[0] = complex(z)  # Initialise la suite avec le point de départ z
    for i in range(1, nb_iter + 1):
        z = z * z + c  # Applique l'itération de la suite
        Liste_suite[i] = z  # Stocke la valeur dans la liste
    return Liste_suite

def est_Mandelbrot(c, nb_iter):
    """
    Vérifie si le point `c` appartient à l'ensemble de Mandelbrot.
    
    Paramètres:
    - c (complex): Point à tester pour appartenance à l'ensemble.
    - nb_iter (int): Nombre maximal d'itérations.

    Retourne:
    - bool: True si le point semble appartenir à l'ensemble, False sinon.
    """
    z = 0  # Initialisation de z pour commencer la suite
    for i in range(nb_iter):
        z = z**2 + c  # Applique l'itération de la suite de Mandelbrot
        if abs(z) > 2:  # Si z diverge (dépasse le rayon de 2), c n'appartient pas à l'ensemble
            return False
    return True  # Si z ne diverge pas, c semble appartenir à l'ensemble

def suite_julia(z0, c, nb_iter):
    """Renvoie la suite de Julia pour un candidat `z0` et un paramètre `c`."""
    return suite(z0, c, nb_iter)

def est_julia(z0, c, iteration=100):
    """
    Vérifie la convergence de la suite de Julia pour un point `z0` et un paramètre `c`.
    
    Paramètres:
    - z0 (complex): Point initial pour la suite de Julia.
    - c (complex): Paramètre constant de la suite de Julia.
    - iteration (int): Nombre maximal d'itérations.
    
    Retourne:
    - bool: True si la suite converge, False sinon.
    """
    erreur = 1e-6  # Précision de convergence
    Liste_suite = suite_julia(z0, c, iteration)
    for i in range(len(Liste_suite) - 1):
        zn = Liste_suite[i]
        zn_1 = Liste_suite[i + 1]

        # Vérifie que zn et zn_1 sont des valeurs finies
        if not (np.isfinite(zn) and np.isfinite(zn_1)):
            return False

        # Vérifie si la suite converge (différence entre zn et zn_1 < erreur)
        if abs(zn_1 - zn) < erreur:
            return True
    return False  # Retourne False si la suite ne converge pas

def plot_mandelbrot(zmin=-2 - 2j, zmax=2 + 2j, pixel_size=0.0001, max_iter=100, figname="Mandelbrot.png"):
    """
    Génère et affiche l'ensemble de Mandelbrot dans la région spécifiée.

    Paramètres:
    - zmin (complex): Coin inférieur gauche de la région d'affichage.
    - zmax (complex): Coin supérieur droit de la région d'affichage.
    - pixel_size (float): Taille du pixel pour la résolution de l'image.
    - max_iter (int): Nombre maximal d'itérations pour le test de convergence.
    - figname (str): Nom du fichier pour sauvegarder l'image.
    """
    # Crée une grille de coordonnées pour les parties réelle (X) et imaginaire (Y)
    X, Y = np.meshgrid(np.arange(zmin.real, zmax.real, pixel_size), np.arange(zmin.imag, zmax.imag, pixel_size))
   
    C = X + 1j * Y  # Crée une grille de points complexes à partir de X et Y
    Z = np.zeros(C.shape, dtype=complex)  # Initialise Z pour les itérations
    mandelbrot = np.ones(C.shape, dtype=int)  # Initialisation de la grille pour stocker les résultats

    # Boucle d'itération pour déterminer l'appartenance à l'ensemble
    for i in range(max_iter):
        Z = Z**2 + C  # Applique l'itération de Mandelbrot
        diverge = np.abs(Z) > 2  # Détecte les points qui divergent
        mandelbrot[diverge] = 0  # Marque les points divergents en noir
        Z[diverge] = 0  # Réinitialise les valeurs divergentes pour économiser des calculs

    # Affiche l'image de l'ensemble de Mandelbrot
    plt.imshow(mandelbrot, cmap='Greys', extent=(zmin.real, zmax.real, zmin.imag, zmax.imag))
    plt.title("Ensemble de Mandelbrot")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.savefig(figname, dpi=2000)
    plt.show()

def plot_julia(c=0.1 + 0.1j, zmin=-2 - 2j, zmax=2 + 2j, pixel_size=0.001, max_iter=50, figname="Julia.png"):
    """
    Génère et affiche l'ensemble de Julia pour un paramètre `c` donné.

    Paramètres:
    - c (complex): Paramètre constant de l'ensemble de Julia.
    - zmin (complex): Coin inférieur gauche de la région d'affichage.
    - zmax (complex): Coin supérieur droit de la région d'affichage.
    - pixel_size (float): Taille du pixel pour la résolution de l'image.
    - max_iter (int): Nombre maximal d'itérations pour le test de convergence.
    - figname (str): Nom du fichier pour sauvegarder l'image.
    """
    # Crée une grille de coordonnées pour la région d'affichage
    X, Y = np.meshgrid(np.arange(zmin.real, zmax.real, pixel_size), np.arange(zmin.imag, zmax.imag, pixel_size))
    Z = X + 1j * Y  # Crée une grille de points complexes
    julia = np.ones(Z.shape, dtype=int)  # Initialise la grille pour stocker les résultats

    # Boucle d'itération pour déterminer l'appartenance à l'ensemble de Julia
    for i in range(max_iter):
        Z = Z**2 + c  # Applique l'itération de Julia
        diverge = np.abs(Z) > 2  # Détecte les points qui divergent
        julia[diverge] = 0  # Marque les points divergents en noir
        Z[diverge] = 0  # Réinitialise les valeurs divergentes

    # Affiche l'image de l'ensemble de Julia
    plt.imshow(julia, cmap='Greys', extent=(zmin.real, zmax.real, zmin.imag, zmax.imag))
    plt.title("Ensemble de Julia")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.savefig(figname, dpi=2000)
    plt.show()
    
plot_julia(c=-0.8 + 0.156j,
           zmin=-2-1j,
           zmax=2+1j,
           max_iter=100,
           figname="Julia_-0.8+0.156j.png")
