import math
f1 = 401.65*10**6 # frequancy is 100mhz
fA = 401.65*10**6 # Argos frequancy is 401.65mhz
fGL1 = 1575.42 * 10 ** 6 # GPS frequancy is 401.65mhz
scu = 5.7 * 10 ** 7 #conductivity of copper in S/m
ssn = 5.5 * 10 ** 7 #conductivity of nickel sliver 770 in S/m
def skin(s, f):
    """Returns skindepth at given s=σ materal conctutivity @ f frequancy in Hz"""
    d = 1 / math.sqrt((math.pi * f) * (4 * math.pi * 10** -7) * s)
    return d
print(f1, "frequancy")
print(skin(scu, f1), "μm")