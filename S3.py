print ("Situacion 3 / Calcular la Masa")

pres = float(input("Ingrese la presion:"))
vol = float(input("Ingrese el volumen:"))
temp = float(input("ingrese la Temperatura:"))

masa = (pres * vol) / (0.37 * (temp + 460))
print ("La Masa es:", masa)
