# experimentos
# acessar funI() from iota
from sys import path
path.append('..\\packages')

import extra.iota
print(extra.iota.funI())

from extra.good.best.tau import funT
print(extra.good.best.sigma.funS())
print(funT())

import extra.good.best.sigma as sig #alias
import extra.good.alpha as alp 
print(sig.funS())
print(sig.funA())
