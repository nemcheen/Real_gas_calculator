import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from calc import get_Z


def make_plot(P_min=0.2e6,
              P_max=6e6, 
              dP=0.1e6, 
              T_min=213, 
              T_max=300, 
              dT=2, 
              Z_min=0.5, 
              Z_max=1.02,
              gas='metan'
            ):
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    P = np.arange(P_min, P_max, dP)
    T = np.arange(T_min, T_max, dT)
    P_grid, T_grid = np.meshgrid(P, T)
    get_Z_vec = np.vectorize(get_Z)
    Z = get_Z_vec(P_grid, T_grid, gas=gas)

    surf = ax.plot_surface(P_grid, T_grid, Z, cmap='viridis', alpha=0.8)
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=20)
        
    ax.set_xlabel('Давление $P$, МПа', fontsize=12, labelpad=10)
    ax.set_ylabel('Температура $T$, K', fontsize=12, labelpad=10)
    ax.set_zlabel('Коэф-т сжимаемости $Z(P,T)$', fontsize=12, labelpad=10)
    
    ax.set_xlim(P_min, P_max)
    ax.set_ylim(T_min, T_max)
    ax.set_zlim(Z_min, Z_max)
    
    plt.title(f'Коэффициент сжимаемости Z(P,T) \nдля газа {gas}\n', 
              fontsize=14, pad=20)
    
    plt.tight_layout()
    plt.show()