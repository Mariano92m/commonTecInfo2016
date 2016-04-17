mecs = (int(input("Ingrese la nota del exámen de matemática")))
promTarM= (int(input("Ingrese la primer nota de tareas de matemática")) + int(input("Ingrese la segunda nota de tareas de matemática")) + int(input("Ingrese la tercer nota de tareas de matemática")))/3  
promTotMat=((mex * 0.9)+(promTarM*0.1))
print ("Su promedio de nota de matemática es:", promTotMat)
print ("                ")
FisEx = int(input ("Ingrese la nota del exámen de Física"))
promTarFis= (int(input("Ingrese la primer nota de tareas de Física")) + int(input("Ingrese la segunda nota de tareas de Física")))/2
PromTotFis=((FisEx*0.8)+(promTarFis*0.2))
print ("Su promedio de nota de Física es:", PromTotFis)
print("                             ")
QuimEx= int(input("Ingrese la nota del exámen de Química"))
promTarQ= (int(input("Ingrese la primer nota de tareas de Química")) + int(input("Ingrese la segunda nota de tareas de Química")) + int(input("Ingrese la tercer nota de tareas de Química")))/3  
PromTotQuim= (QuimEx*0.85) + (promTarQ*0.15)
print ("Su promediode nota de Química es:", PromTotQuim )
print("                                   ")
print("                                ")
print(" Su promedio general es", ((promTotMat + PromTotQuim + PromTotFis)/3))