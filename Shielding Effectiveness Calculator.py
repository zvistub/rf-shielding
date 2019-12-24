import math
f1 = 100 * 10 ** 6 # frequancy is 100mhz
fA = 401.65 * 10 ** 6 # Argos frequancy is 401.65mhz
fGL1 = 1575.42 * 10 ** 6 # GPS frequancy is 1575.42mhz
scu = 5.7 * 10 ** 7 #conductivity of copper in S/m
ssn = 5.5 * 10 ** 7 #conductivity of nickel sliver 770 in S/m
sT = 203.2 * 10 ** -6 #thickness of Shield in um converted to m


def skin(s, f):
    """Returns skindepth at given s=σ materal conctutivity @ f frequancy in Hz"""
    d = 1 / math.sqrt((math.pi * f) * (4 * math.pi * 10 ** -7) * s)
    return d
def shieldAB(t):
    """Calculates dB loss"""
    AdB = 8.7 * (t / sd)
    return AdB


sd = skin(ssn, fGL1)
db = shieldAB(sT)

print(f1, "Hz")
print(scu, "S/m")
print(sd * 10 ** 6, "um")
print(db, "dB")