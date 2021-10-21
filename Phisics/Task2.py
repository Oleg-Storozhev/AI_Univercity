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

Va = OmegaOA * OA  # Нахожу ввекторскорости Va по стандартной формуле
AP = AB/cos_al  # Нахожу длину AP по ыормуле a = c x cos(b)

OmegaAB = Va/AP
BP = math.sqrt(AP**2 - AB**2)
Vb = OmegaAB * BP
CP = math.sqrt(BP**2 + (AB - AC)**2)
Vc = CP * OmegaAB

print("wAB =", round(OmegaAB, 5))
print("Vb =", round(Vb, 5))
print("Vc =", round(Vc, 5))

# Этап 2

wA = EpsilOA * OA + OmegaOA**2 * OA
wB = (wA * cos_al + OmegaAB**2 * AB) / sin_al
eAB = (wB * cos_al + wA * sin_al) / AB
wCx = AC * OmegaAB**2 + wA * cos_al
wCy = eAB * AC - wA * sin_al
wC = math.sqrt(wCx**2 + wCy**2)
wACc = AC * OmegaAB**2
wACr = eAB * AC

print("wA =", round(wA, 5))
print("wB =", round(wB, 5))
print("wC =", round(wC, 5))
print("eAB =", round(eAB, 5))
