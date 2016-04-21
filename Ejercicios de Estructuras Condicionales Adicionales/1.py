print ("\n#################################################")
print ("             Bienvenidos a FLIGHT")
print ("  #################################################")
respuesta="si"

while Respuesta=="si":
      nombre = str(raw_input("\nIngrese nombre del cliente :"))
      numeroDoc = int(raw_input("\nIngrese numero de Documento :"))
      print ("\nElija con los numeros los tipos de pasajes")
      print (" 1 - Primera Clase")
      print (" 2 - Segunda Clase")
      print (" 3 - Tercera Clase")
      tipoPasaje=int(raw_input("Elija :"))
      print ("Elija con los numeros los tipos de Destinos")
      print (" 1 - Europa")
      print (" 2 - America del Norte")
      print (" 3 - America del Sur")
      print (" 4 - Islas del Caribe")
      destino= int(raw_input("Elija :"))
      print ("\nElija con True(FUMADOR) o False(NO FUMADOR) a la zona que corresponda ")
      zona = raw_input("Elija : ")
      print (" ")
      print nombre
      # DESTINO EUROPA
      if(destino==1):
            #PRIMERA CLASE FUMADOR
      	if(tipoPasaje==1 and zona==True):
      	      valorTotal=2500.000
                  valorRecargo=valorTotal*1.10
                  print ("\nEl valor total del boleto es : $ %s  y con el recargo serian :$ %s" &(valorTotal,valorRecargo))
      	#PRIMERA CLASE NO FUMADOR
            elif(tipoPasaje==1 and zona==False):
      		valorTotal=2500.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.08
                  print("Con el descuento quedaria: $ %s"%(valorDescuento))
            #SEGUNDA CLASE FUMADOR
            elif(tipoPasaje==2 and zona==True):
                  valorTotal=2100.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s"  %(valorDescuento))
            #SEGUNDA CLASE NO FUMADOR
            elif(tipoPasaje==2 and zona==False):
                  valorTotal=2100.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s"  %(valorRecargo))

            #TERCERA CLASE FUMADOR
            elif(tipoPasaje==3 and zona==True):
                  valorTotal=1900.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s"  %(valorDescuento))

            #TERCERA CLASE NO FUMADOR
            elif(tipoPasaje==3 and zona==False):
                  valorTotal=1900.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s"  %(valorRecargo))
      #DESTINO AMERICA DEL NORTE
      elif(destino==2):

            #PRIMERA CLASE FUMADOR
            if(tipoPasaje==1 and zona==True):
                  valorTotal=2000.000
                  print ("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.10
                  print("Con el recargo serian: $ %s"(valorRecargo))

            #PRIMERA CLASE NO FUMADOR
            elif(tipoPasaje==1 and zona==False):
                  valorTotal=2000.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.08
                  print("Con el descuento quedaria: $ %s" %(valorDescuento))

            #SEGUNDA CLASE FUMADOR
            elif(tipoPasaje==2 and zona==True):
                  valorTotal=1700.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s"  %(valorDescuento))

            #SEGUNDA CLASE NO FUMADOR
            elif(tipoPasaje==2 and zona==False):
                  valorTotal=1700.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s" %(valorRecargo))

            #TERCERA CLASE FUMADOR
            elif(tipoPasaje==3 and zona==True):
                  valorTotal=1400.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s"  %(valorDescuento))

            #TERCERA CLASE NO FUMADOR
            elif(tipoPasaje==3 and zona==False):
                  valorTotal=1400.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s" %(valorRecargo))
      # DESTINO AMERICA DEL SUR
      elif(destino==3):
            #PRIMERA CLASE FUMADOR
            if(tipoPasaje==1 and zona==True):
                  valorTotal=1000.000
                  print ("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.10
                  print("Con el recargo serian: $ %s"(valorRecargo))

            #PRIMERA CLASE NO FUMADOR
            elif(tipoPasaje==1 and zona==False):
                  valorTotal=1000.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.08
                  print("Con el descuento quedaria: $ %s" %(valorDescuento))

            #SEGUNDA CLASE FUMADOR
            elif(tipoPasaje==2 and zona==True):
                  valorTotal=900.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s" %(valorDescuento))

            #SEGUNDA CLASE NO FUMADOR
            elif(tipoPasaje==2 and zona==False):
                  valorTotal=900.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s" %(valorRecargo))

            #TERCERA CLASE FUMADOR
            elif(tipoPasaje==3 and zona==True):
                  valorTotal=750.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s" %(valorDescuento))

            #TERCERA CLASE NO FUMADOR
            elif(tipoPasaje==3 and zona==False):
                  valorTotal=750.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s" %(valorRecargo))
      #DESTINO ISLAS CARIBE
      elif(destino==4):

            #PRIMERA CLASE FUMADOR
            if(tipoPasaje==1 and zona==True):
                  valorTotal=800.000
                  print ("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.10
                  print("Con el recargo serian: $ %s"(valorRecargo))

            #PRIMERA CLASE NO FUMADOR
            elif(tipoPasaje==1 and zona==False):
                  valorTotal=800.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.08
                  print("Con el descuento quedaria: $ %s" %(valorDescuento))

            #SEGUNDA CLASE FUMADOR
            elif(tipoPasaje==2 and zona==True):
                  valorTotal=700.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s"  %(valorDescuento))

            #SEGUNDA CLASE NO FUMADOR
            elif(tipoPasaje==2 and zona==False):
                  valorTotal=700.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s"  %(valorRecargo))

            #TERCERA CLASE FUMADOR
            elif(tipoPasaje==3 and zona==True):
                  valorTotal=500.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorDescuento=valorTotal-valorTotal*0.05
                  print("Con el descuento quedaria: $ %s"  %(valorDescuento))

            #TERCERA CLASE NO FUMADOR
            elif(tipoPasaje==3 and zona==False):
                  valorTotal=500.000
                  print("\nEl valor total del boleto es : $ %s" %(valorTotal))
                  valorRecargo=valorTotal*1.08
                  print("Con el recargo serian: $ %s"  %(valorRecargo))

            #SENTENCIA PARA SEGUIR O NO INGRESANDO CLIENTES
      Respuesta= input("\nIngresa otro cliente si o no : ")