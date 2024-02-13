def promedio_notasp():
    
    n1 = float(input("ingresa la nota de las tareas: "))
    n2 = float(input("ingresa la nota de la previa teorica: "))
    n3 = float(input("ingresa la nota de la evaluacion practica: "))
    
    pro1= (n1*0.10)
    pro2= (n2*0.30)
    pro3= (n3*0.60)
    
    final= (pro1+pro2+pro3/3)
    
    print(pro1,pro2,pro3,final)
    return
promedio_notasp()