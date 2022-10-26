import math;
icg = [];
opcion = 1;

while (opcion == 1 or opcion == 2):
    opcion = input("Las opciones disponibles son: \n1.Ingresar país \n2.Ver paises   \n\nopcion: ");
    opcion = int(opcion);

    if (opcion == 1 or opcion == 2):
        if opcion == 1:
            icg.append({"nombre" : "prueba"});
            icg[len(icg) - 1]["nombre"] = input("Ingrese el nombre del pais: ");
            icg[len(icg) - 1]["region"] = input("Ingrese la region: ");
            icg[len(icg) - 1]["inst"] = int(input("Ingrese las instituciones: "));
            icg[len(icg) - 1]["infr"] = int(input("Ingrese la infraestructura: "));
            icg[len(icg) - 1]["adopTec"] = int(input("Ingrese la adopcion de tecnologia: "));
            icg[len(icg) - 1]["estaMacro"] = int(input("Ingrese la estabilidad macroeconomica: "));
            icg[len(icg) - 1]["salud"] = int(input("Ingrese la salud: "));
            icg[len(icg) - 1]["habil"] = int(input("Ingrese las habilidades: "));
            icg[len(icg) - 1]["mercProd"] = int(input("Ingrese el mercado de productos: "));
            icg[len(icg) - 1]["mercLab"] = int(input("Ingrese el mercado laboral: "));
            icg[len(icg) - 1]["sisFin"] = int(input("Ingrese el sistema financiero: "));
            icg[len(icg) - 1]["tamMerc"] = int(input("Ingrese el tamaño de mercado: "));
            icg[len(icg) - 1]["dinNeg"] = int(input("Ingrese el dinamismo de negocios: "));
            icg[len(icg) - 1]["capIno"] = int(input("Ingrese la capacidad de inovacion: "));
            
            promedio = icg[len(icg) - 1]["inst"] + icg[len(icg) - 1]["infr"] + icg[len(icg) - 1]["adopTec"] + icg[len(icg) - 1]["estaMacro"] + icg[len(icg) - 1]["salud"] + icg[len(icg) - 1]["habil"] + icg[len(icg) - 1]["mercProd"];
            promedio = promedio + icg[len(icg) - 1]["mercLab"] + icg[len(icg) - 1]["sisFin"] + icg[len(icg) - 1]["tamMerc"] + icg[len(icg) - 1]["dinNeg"] + icg[len(icg) - 1]["capIno"];
            promedio = math.ceil(promedio / 12);
            
            icg[len(icg) - 1]["promedio"] = promedio;

        if opcion == 2:
            print("Indice de competitividad global\n\n");
            print("pais | region | Instituciones | infraestructura | adopcion tecnologia | estabilidad macroeconomica | Salud | Habilidades | mercado de productos |" +
                  " Mercado laboral | sistema financiero | tamaño mercado | dinamismo de negocios | capacidad de inovacion | punteo promedio");
            
            # printing the list using loop
            for x in range(len(icg)):
                print (icg[x]["nombre"], " | ", icg[x]["region"], " | ", icg[x]["inst"], " | ", icg[x]["infr"], " | ", icg[x]["adopTec"], " | ", icg[x]["estaMacro"], " | ", icg[x]["salud"], " | ", icg[x]["habil"], " | ", icg[x]["mercProd"], " | ", icg[x]["mercLab"], " | ", icg[x]["sisFin"], " | ", icg[x]["tamMerc"], " | ", icg[x]["dinNeg"], " | ", icg[x]["capIno"], " | ", icg[x]["promedio"]);
            
            print("\n\n");
    else:
        opcion = 0;
        break;