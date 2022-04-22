def arithmetic_arranger(list, opcion=False):
    """Realiza suma y resta
    
    Recibe una lista de string como primer parametro, un valor opcional y
    retorna una una operacion de suma o resta entre los valores de la lista,
    pero el resultado que se muestra por pantalla depende del parametro opcional.

    list: [string]
    opcion:False(por defecto), True
    """
    for i in range(len(list)):
        parte = list[i].split("+")
        print(
            f"{parte[0]}\n"
            f" +          \n"
            f"  {parte[1]}\n "
            f"------------"
            )
        print(list[i])