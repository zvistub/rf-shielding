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
def shield_AB(t, sd):
    """Calculates dB loss with thickness t and skindepth sd"""
    AdB = 8.7 * (t / sd)
    return AdB
def wave(f):
    """calculates wavelenght in meters"""
    wl = 299792458 / f
    return wl
def shield_AP_holes(w, l, n = 1, k = 40):
    """claculates SE of apatures with a given wavelehtn, size of apature, number of apatures within half wavelngth and
    k=20 for slots k=40 for holes (by defult)"""
    se = k * math.log10( w / (2 * l)) - 20 * math.log10(n)
    return se
def shield_AP(w, l, k = 40):
    """claculates SE of apatures with a given wavelehtn, size of apature, number of apatures within half wavelngth and
    k=20 for slots k=40 for holes (by defult)"""
    se = k * math.log10( w / (2 * l))
    return se

frequency_mhz = float(input("input frequency in Mhz: ")) * 10 ** 6
wl = wave(frequency_mhz)
ql = wl / 4
hl = wl / 2
Material_σ = float(input("input Conductivity in S/m: 10^-7 ")) * 10 ** 7
Shield_thickness_meters = float(input("input shield thickness in um: ")) * 10 ** -6
Hole_Diameter_meters = float(input("input hole diameter in mm: ")) * 10 ** -3
Number_of_holes = float(input("number of holes within mm: "))


# sd = skin(ssn, f1)
sd = skin(Material_σ, frequency_mhz)
# db = shieldAB(sT)
db = shield_AB(Shield_thickness_meters, sd)
# se = shieldAP(wl, hd)
se = shield_AP(wl, Hole_Diameter_meters)
se_holes = shield_AP_holes(wl, Hole_Diameter_meters, Number_of_holes)

# print(f1, "Hz")
# print(scu, "S/m")
# print(sd * 10 ** 6, "um")
print(round(db, 4), "dB Absorption loss")
# print(wl, "wavelength")
# print(ql, "quarter wave")
# print(hl, "half wave")
print(round(se, 4), "dB Aperture attenuation")
print(round(se_holes, 4), "dB Aperture array attenuation")