import math
f1 = 100 * 10 ** 6 # frequancy is 100mhz in hz
fA = 401.65 * 10 ** 6 # Argos frequancy is 401.65mhz in hz
fGL1 = 1575.42 * 10 ** 6 # GPS frequancy is 1575.42mhz in hz 
scu = 5.7 * 10 ** 7 #conductivity of copper in S/m
ssn = 5.5 * 10 ** 7 #conductivity of nickel sliver 770 in S/m
sT = 203.2 * 10 ** -6 #thickness of Shield in um converted to m
hd = 797.9 * 10 ** -6 # rf can hole diameter in m
hn = 17 * 24 #total number of an array of holes 


def skin(s, f):
    """Returns skindepth at given s=σ materal conctutivity @ f frequancy in Hz"""
    d = 1 / math.sqrt((math.pi * f) * (4 * math.pi * 10 ** -7) * s)
    return d
def shieldAB(t):
    """Calculates dB loss"""
    AdB = 8.7 * (t / sd)
    return AdB
def wave(f):
    """calculates wavelenght in meters"""
    wl = 299792458 / f
    return wl
def shieldAP(w, l, n = 1, k = 40):
    """claculates SE of apatures with a given wavelehtn, size of apature, number of apatures within half wavelngth and
    k=20 for slots k=40 for holes (by defult)"""
    se = k * math.log10( w / (2 * l)) - 20 * math.log10(n)
    return se

sd = skin(ssn, fGL1)
db = shieldAB(sT)
wl = wave(fGL1)
ql = wl / 4
hl = wl / 2
se = shieldAP(wl, hd)

print(f1, "Hz")
print(scu, "S/m")
print(sd * 10 ** 6, "um")
print(db, "dB")
print(wl, "wavelength")
print(ql, "quarter wave")
print(hl, "half wave")
print(se, "DB")
