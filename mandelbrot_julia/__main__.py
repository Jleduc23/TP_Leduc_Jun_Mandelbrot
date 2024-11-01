#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 02:14:15 2024

@author: leduc-beppujun
"""

from TP_Fin_Leduc_Jun import plot_mandelbrot, plot_julia
import argparse

def main_mandelbrot():
    parser = argparse.ArgumentParser(description="Génère et affiche l'ensemble de Mandelbrot.")
    parser.add_argument("--zmin", type=complex, default=-2 - 2j, help="Coin inférieur gauche de la région d'affichage (par défaut -2-2j).")
    parser.add_argument("--zmax", type=complex, default=2 + 2j, help="Coin supérieur droit de la région d'affichage (par défaut 2+2j).")
    parser.add_argument("--pixel_size", type=float, default=0.0001, help="Taille du pixel pour la résolution de l'image (par défaut 0.0001).")
    parser.add_argument("--max_iter", type=int, default=100, help="Nombre maximal d'itérations pour le test de convergence (par défaut 100).")
    parser.add_argument("--figname", type=str, default="mandelbrot.png", help="Nom du fichier pour sauvegarder l'image (par défaut mandelbrot.png).")

    args = parser.parse_args()
    plot_mandelbrot(zmin=args.zmin, zmax=args.zmax, pixel_size=args.pixel_size, max_iter=args.max_iter, figname=args.figname)

if __name__ == "__main__":
    main_mandelbrot()
    
def main_julia():
    parser = argparse.ArgumentParser(description="Génère et affiche l'ensemble de Julia.")
    parser.add_argument("--c", type=complex, default=0.1 + 0.1j, help="Paramètre complexe pour l'ensemble de Julia (par défaut 0.1+0.1j).")
    parser.add_argument("--zmin", type=complex, default=-2 - 2j, help="Coin inférieur gauche de la région d'affichage (par défaut -2-2j).")
    parser.add_argument("--zmax", type=complex, default=2 + 2j, help="Coin supérieur droit de la région d'affichage (par défaut 2+2j).")
    parser.add_argument("--pixel_size", type=float, default=0.0001, help="Taille du pixel pour la résolution de l'image (par défaut 0.0001).")
    parser.add_argument("--max_iter", type=int, default=50, help="Nombre maximal d'itérations pour le test de convergence (par défaut 50).")
    parser.add_argument("--figname", type=str, default="julia.png", help="Nom du fichier pour sauvegarder l'image (par défaut julia.png).")

    args = parser.parse_args()
    plot_julia(c=args.c, zmin=args.zmin, zmax=args.zmax, pixel_size=args.pixel_size, max_iter=args.max_iter, figname=args.figname)

if __name__ == "__main__":
    main_julia()