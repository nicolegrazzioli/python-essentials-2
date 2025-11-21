# experimentos
import os, sys

dir_atual = os.path.dirname(os.path.abspath(__file__)) #acha main2.py
dir_pai = os.path.dirname(dir_atual) #acha pai de progs = python
caminho_zip = os.path.join(dir_pai, 'packages', 'extrapack.zip') #monta caminho

if os.path.exists(caminho_zip):
    sys.path.append(caminho_zip) #adiciona ao sys.path (python procura modulos aqui)
    print(f"caminho adicionado: {caminho_zip}")
else:
    print(f"caminho nao existe: {caminho_zip}")
    
# path.append('..\\packages\\extrapack.zip')


import extra.good.best.sigma as sig #alias
import extra.good.alpha as alp 
from extra.iota import funI
from extra.good.beta import funB

print(sig.funS())
print(alp.funA())
