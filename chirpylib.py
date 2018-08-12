import chirplib

#Init Chirp Lib
chirpy = chirplib.Chirp(4,5)

print("Feuchtigkeit: ",+ chirpy.moisture())
print("LichtLevel: ",+ chirpy.light_level())
print("Temperatur: ",+ chirpy.temperature())
print("Adresse: ",+ chirpy.getaddress())
print("Besetzt? ",+ chirpy.busy())
print("Version: ",+ chirpy.version())
