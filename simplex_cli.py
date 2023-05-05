import numpy as np
import scipy as sp
from scipy.optimize import linprog
from datetime import date

def Solver(pre_c, pre_A_ub, pre_b_ub, vector_signos):
    rst_lst = []
    sol_lst = []

    if max_min == '0':
        c = np.negative(pre_c)
    else:
        c = np.array(pre_c)

    for signo, index, sol in zip(vector_signos, pre_A_ub, pre_b_ub):
        if (signo == '>='):
            lst = []
            for num in index:
                item = -abs(num)
                lst.append(item)
            rst_lst.append(lst)
            aux = -abs(sol)
            sol_lst.append(aux)
        else:
            rst_lst.append(index)
            sol_lst.append(sol)

    A_ub = np.array(rst_lst)
    b_ub = np.array(sol_lst)

    res = linprog(c, A_ub, b_ub, bounds = (0, None))

    print(res)
    print('\n=========================')
    if (max_min == '0'):
        print('Valor óptimo: ', (res.fun * -1))
    else:
        print('Valor óptimo: ', res.fun) 
    print('x: ', res.x)
    print('h: ', res.slack)
    print('=========================\n')

    GenerarArchivo(pre_c, pre_A_ub, pre_b_ub, vector_signos)

def GenerarArchivo(pre_c, pre_A_ub, pre_b_ub, vector_signos):
    answers = ['y', 'n']
    while (generar := input('¿Generar archivo? [y/n]: ' )) not in answers:
        print('ERROR. ELIGE OTRA OPCIÓN')
    if (generar == 'y'):
        hoy = str(date.today())
        titulo = input('Nombre del archivo: ')
        nombre_archivo = titulo + '_' + hoy + '.txt'
        if (max_min == '0'):
            op_txt = 'Maximizar z = '
        else:
            op_txt = 'Minimizar z = '
        index = 1
        func_obj = ''
        for item in pre_c:
            func_obj = func_obj + str(item) + f'x{index} + '
            index = index + 1
        print(hoy, '\n', titulo, '\n', op_txt, func_obj, '\ns.a.\n')




if __name__ == '__main__':

    print('======================')
    print('   CLI - PPL SOLVER   ')
    print('======================')

    # INPUT
    matrix_coeficientes_fo = []
    matrix_restricciones = []
    vector_resultados = []
    vector_signos = []
    opt_operaciones = str([x for x in range(2)])
    opt_signos = ['<=', '>=']
    var_lst = str([x for x in range(1, 6, 1)])

    while (max_min := input('\nMax||Min [0|1]: ')) not in opt_operaciones:
        print('ERROR. ELIGE OTRA OPCIÓN')
    while (num_variables := input('Ingresa el número de variables: '))not in var_lst:
        print('ERROR. INGRESA UN VALOR ENTRE 1 Y 5')
    num_variables = int(num_variables)
    while True:
        try:
            num_restricciones = int(input('Ingresa el número de restricciones: '))
            break
        except ValueError:
            print('ERROR. INGRESA UN VALOR ENTERO')
    
    print('\nFUNCIÓN OBJETIVO')
    for var in range(num_variables):
        valor = float(input('Ingresa el coeficiente {}: '.format(var + 1)))
        matrix_coeficientes_fo.append(valor)

    for i in range (num_restricciones):
        matrix_restricciones.append([])
        print ("\nRestricción {}".format (i + 1))
        for j in range (num_variables + 1):
            if (j != num_variables):
                valor = float((input("Ingresa el coeficiente {}: ".format (j + 1))))
                matrix_restricciones[i].append(valor)
            else:
                while (signo := input('Introduce el signo: ')) not in opt_signos:
                    print('ERROR. INGRESA UN SIGNO VÁLIDO')
                vector_signos.append(signo)
                valor = int((input("Introduce el resultado de la desigualdad: ")))
                vector_resultados.append(valor)

    Solver(matrix_coeficientes_fo, matrix_restricciones, vector_resultados, vector_signos)
