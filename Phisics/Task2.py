import math

OA = 1
AB = 2
AC = 1.2
OmegaOA = 1.9
EpsilOA = 0.2
alpha = 35
cos_al = math.cos(math.pi * alpha/180)
sin_al = math.cos(math.pi * alpha/180)

# Этап 1
vA = OmegaOA * OA
AP = AB * cos_al
OmegaAB = vA / AP
BP = AB * sin_al
CP = math.sqrt(AC**2 + AP**2 - 2 * AC * AP * cos_al)
vB = OmegaAB * AB
vC = OmegaAB * CP
print('vA =', vA)
print('wAB =', OmegaAB)
print('vB =', vB)
print('vC =', vC)

# Этап 2
wAO_bp = EpsilOA * OA
wAO_c = OmegaOA**2 * OA
wA = math.sqrt(wAO_bp ** 2 + wAO_c)
print('wA =', wA)

wBA_c = OmegaAB**2 * AB
wB = (wAO_bp * sin_al - wAO_c * cos_al - wBA_c) / cos_al
eAB = (wB * sin_al + wAO_bp * cos_al + wAO_c * sin_al) / AB
print('wB =', wB)
print('eAB =', eAB)

BC = AB - AC
wB = -wB
wCB_c = OmegaAB ** 2 * BC
wCB_bp = eAB * BC
wCx = wCB_bp + wB * sin_al
wCy = wCB_c - wB * cos_al
wC = math.sqrt(wCx ** 2 + wCy ** 2)
print('wC =', wC)
