import csv
import functions

# Variables definition.
debug = False  # Set variable for debugging
filePath = 'files/clinica.csv'
feverReportPath = 'files/estudiantes_con_fiebre_alta.csv'
trackingReportPath = 'files/estudiantes_con_seguimiento_2.csv'
clinicData = functions.openAndReadFile(filePath, debug)  # Read the file and save its contents.

print("--- Bienvenido al sistema de control medico ---")

if debug: print(clinicData)

# Iterate until the user types SI or S
exit = 'no'
option = 0

# No data is going to be saved if operation fails
while exit.upper() != 'SI' and exit.upper() != 'S':
    option = functions.showMenu()

    if option == 1:  # Add medical card
        clinicData.append(functions.addMedicalCard())
    elif option == 2:  # Show tracking of specific user
        functions.showSpecificMedicalCard(clinicData)
    elif option == 3:  # Show all medical cards
        functions.showListData(clinicData)
    elif option == 4:  # generate reports
        functions.generateFeverReport(clinicData, feverReportPath, debug)
        functions.generateTrackingReport(clinicData, trackingReportPath, debug)
    else:
        print("Operación invalida, intente nuevamente")

    if option > 0:
        try:
            if debug: print(clinicData)

            if option == 1:
                functions.saveDataInFile(clinicData, filePath, debug)
        except:
            print("Hubo un error al guardar la información.\n")

    exit = input("\n Desea salir (SI o NO)? ")
