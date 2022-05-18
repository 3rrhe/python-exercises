import csv


# Function to read the file and return its values in a list.
def openAndReadFile(path, debug):
    if debug: print("---- Leyendo el archivo ----")
    list = []

    try:
        file = open(path, mode='x')  # Mode X, create the file if it does not exist and open it.
        file.close()
        if debug: print('archivo creado!')
    except:
        if debug: print('Archivo existente, será actualizado!')

    with open(path, mode='r') as file_data:  # Mode R, we read the contents of the file
        reader = csv.DictReader(file_data)
        lines = 0

        for rowL in reader:
            list.append(dict(rowL))
            lines += 1

        if debug: print(f'Se leyeron {lines} datos del archivo.\n')
        file_data.close()

    return list


# Function to open the file and save the data
def saveDataInFile(list, path, debug):
    if debug: print("---- Guardando la información ----")

    with open(path, mode='w') as file_data:  # Mode w, we open the file in edition mode
        writer = csv.writer(file_data)
        lines = 0

        writer.writerow([
            'carnet',
            'nombre',
            'fechavisita',
            'telefono',
            'correo',
            'enfermedad',
            'medicina',
            'temperatura',
            'presion',
            'recomendacion',
            'seguimiento'
        ])

        for row in list:
            writer.writerow([
                row['carnet'],
                row['nombre'],
                row['fechavisita'],
                row['telefono'],
                row['correo'],
                row['enfermedad'],
                row['medicina'],
                str(row['temperatura']),
                row['presion'],
                row['recomendacion'],
                str(row['seguimiento'])
            ])
            lines += 1

        if debug: print(f'Se guardaron {lines} datos en el archivo.\n')
        file_data.close()


# Function to generate fever report
def generateFeverReport(list, path, debug):
    if debug: print("---- Generando reporte de fiebre alta ----")

    try:
        file = open(path, mode='x')  # Mode X, create the file if it does not exist and open it.
        file.close()
        if debug: print('archivo de reporte de fiebre alta creado!')
    except:
        if debug: print('Archivo de reporte de fiebre alta existente, será actualizado!')

    with open(path, mode='w') as file_data:  # Mode w, we open the file in edition mode
        writer = csv.writer(file_data)
        lines = 0

        writer.writerow([
            'carnet',
            'nombre',
            'fechavisita',
            'telefono',
            'correo',
            'enfermedad',
            'medicina',
            'temperatura',
            'presion',
            'recomendacion',
            'seguimiento'
        ])

        for row in list:
            if float(row['temperatura']) > 37:
                writer.writerow([
                    row['carnet'],
                    row['nombre'],
                    row['fechavisita'],
                    row['telefono'],
                    row['correo'],
                    row['enfermedad'],
                    row['medicina'],
                    str(row['temperatura']),
                    row['presion'],
                    row['recomendacion'],
                    str(row['seguimiento'])
                ])
                lines += 1

        if debug: print(f'Se guardaron {lines} datos en el reporte de fiebre.\n')
        file_data.close()
        print("Reporte de estudiantes con fiebre alta generado, file=" + path)


# Function to generate tracking report
def generateTrackingReport(list, path, debug):
    if debug: print("---- Generando reporte de seguimiento 2 ----")

    try:
        file = open(path, mode='x')  # Mode X, create the file if it does not exist and open it.
        file.close()
        if debug: print('archivo de reporte de seguimiento 2 creado!')
    except:
        if debug: print('Archivo de reporte de seguimiento 2 existente, será actualizado!')

    with open(path, mode='w') as file_data:  # Mode w, we open the file in edition mode
        writer = csv.writer(file_data)
        lines = 0

        writer.writerow([
            'carnet',
            'nombre',
            'fechavisita',
            'telefono',
            'correo',
            'enfermedad',
            'medicina',
            'temperatura',
            'presion',
            'recomendacion',
            'seguimiento'
        ])

        for row in list:
            if int(row['seguimiento']) == 2:
                writer.writerow([
                    row['carnet'],
                    row['nombre'],
                    row['fechavisita'],
                    row['telefono'],
                    row['correo'],
                    row['enfermedad'],
                    row['medicina'],
                    str(row['temperatura']),
                    row['presion'],
                    row['recomendacion'],
                    str(row['seguimiento'])
                ])
                lines += 1

        if debug: print(f'Se guardaron {lines} datos en el reporte de seguimiento 2.\n')
        file_data.close()
        print("Reporte de estudiantes con seguimiento 2 generado, file=" + path)


# Function to show the application menu
def showMenu():
    print("Seleccione la actividad que desea realizar:")
    print("\n1. Agregar nueva ficha medica")
    print("\n2. Ver ficha medica de un estudiante")
    print("\n3. Ver todas las fichas medicas")
    print("\n4. Reportes (Fiebre, Seguimiento malo)")
    return int(input("\nInserte la opción deseada: "))


# Function to show all list items
def showListData(list):
    print('\n\n--Fichas guardadas --\n')
    print(
        'carnet | nombre | fechavisita | telefono | correo | enfermedad | medicina | temperatura | presion | recomendacion | seguimiento'
    )

    for item in list:
        print(
            item['carnet'] + ' | ' +
            item['nombre'] + ' | ' +
            item['fechavisita'] + ' | ' +
            item['telefono'] + ' | ' +
            item['correo'] + ' | ' +
            item['enfermedad'] + ' | ' +
            item['medicina'] + ' | ' +
            str(item['temperatura']) + ' | ' +
            item['presion'] + ' | ' +
            item['recomendacion'] + ' | ' +
            str(item['seguimiento'])
        )


# Function to show all list items
def showSpecificMedicalCard(list):
    print('\n\n-- Ficha especifica --\n')
    carnet = input('Ingrese el carnet del estudiante: ')
    foundUser = 0

    for item in list:
        if item['carnet'] == carnet:
            if int(item['seguimiento']) == 1:
                tracking = 'Presenta mejora'
            elif int(item['seguimiento']) == 2:
                tracking = 'Sin mejora'
            elif int(item['seguimiento']) == 3:
                tracking = 'Visito al doctor'
            else:
                tracking = 'Sin seguimiento'

            print('\n\n| Carnet | ' + item['carnet'])
            print('|  ___       Nombre: ' + item['nombre'])
            print('| [(_)]      Telefono: ' + item['telefono'])
            print('|  \'_\'       Correo: ' + item['correo'])
            print('| ')
            print('| Visita: ' + item['fechavisita'] + ' | Seguimiento: ' + tracking)
            print('| ')
            print('| Condición de la visita: ' + item['enfermedad'])
            print('| Medicina que toma actualmente: ' + item['medicina'])
            print('| Temperatura: ' + str(item['temperatura']) + '°C | Presión: ' + item['presion'])
            print('| ')
            print('| Recomendación: ' + item['recomendacion'] + '\n\n')
            foundUser += 1

    if foundUser <= 0: print("El estudiante no fue encontrado!")


# Function to add new medical card to the list
def addMedicalCard():
    print('\n\n-- Nueva ficha medica --\nIngrese los datos del paciente.\n')
    cardId = input("Carnet: ")
    name = input("Nombre: ")
    date = input("Fecha: ")
    phone = input("Telefono: ")
    email = input("Correo: ")
    disease = input("Enfermedad o condición: ")
    medicine = input("Medicina que toma actualmente: ")
    temperature = float(input("Temperatura en grados centígrados: "))
    pressure = input("Presión arterial: ")
    recommendation = input("Recomendación dada: ")
    tracking = int(
        input("Seguimiento (0. No se ha dado seguimiento 1. Esta mejor 2. Se siente mal 3. Fue al doctor): ")
    )

    return {
        "carnet": cardId,
        "nombre": name,
        "fechavisita": date,
        "telefono": phone,
        "correo": email,
        "enfermedad": disease,
        "medicina": medicine,
        "temperatura": temperature,
        "presion": pressure,
        "recomendacion": recommendation,
        "seguimiento": tracking,
    }
