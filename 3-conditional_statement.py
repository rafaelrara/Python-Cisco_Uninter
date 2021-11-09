# Condicionais
sheep_conter = 15
start = 0

good_weather = True
good_restaurant = True
bad_weather = False
bad_restaurant = False

if start == 0:                      # Se start for igual a zero, vá para cama
    print("Go to the bed")
#------------------------------------
if start >= sheep_conter:           # Se 0 for maior ou igual a 15 ZzzzZzz (dormindo)
    print("ZzzzzzzZZzz")
else:
    print("Run away!")              # Se não corra!
# -----------------------------------
if good_weather:                    # se o tempo estiver bom,
    if good_restaurant:                 # Se o restaurante for bom,
        print("huuum great food!")          # Comer
    else:
        print(":x")                         # Se não, comida ruim
else:                               # se o tempo não estiver bom
    if bad_restaurant:                  # se o restaurante não for bom
        print("Watch TV! ")                  # Asista TV
    else:                           # Se o restaurante for bom
        print("Huuum great food")       # Comer 
# -----------------------------------
if good_weather:                    # Se o tempo estiver bom,   
    print("To Walk")                    # Caminhar
elif bad_restaurant:                # Ou se o restaurante for ruim,
    print ("Go to the home")            # Vá para casa    
elif start == sheep_conter:         # Ou se start for igual a sheep_conter
    print("Wake up")                    # Levante
else:                               # Se não
    print("Search a good food")     # Procure uma boa comida