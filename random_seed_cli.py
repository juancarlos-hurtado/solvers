import numpy as np
from numpy import random
import sympy
from sympy import *

def max_solver():

    vector_booleano = []
    seeds = []
    var_max_lst = []
    ev_max_lst = []

    if num_variables == 1:
        for item in range(num_pob):
            local_max_f = 0
            local_max_x = 0
            print("")
            print(f'--- POBLACIÓN {item + 1} ---')
            for item in range(tam_pob):
                print(f'--- ID {item + 1} ---')
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    print('VARIABLE ', variable, ' LIMS', lims)
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    print('semilla = ', seed)
                    seeds.append(seed)               
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0])])
                            print(f'r{index + 1}: {evl}')
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        #print(vector_booleano)
                        if sum(vector_booleano) == len(vector_restricciones):
                            print('RESTRICCIONES SATISFECHAS')
                            if (fun_obj.subs([(vector_variables[0], seeds[0])]) > local_max_f):
                                local_max_f = fun_obj.subs([(vector_variables[0], seeds[0])])
                                print(f'NUEVO MAX LOCAL: {local_max_f}')
                                local_max_x = seeds[0]
                                print(f'{vector_variables[0]} =  {local_max_x}')
                                var_max_lst.append(local_max_x)
                                ev_max_lst.append(local_max_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0])])
                                print(f'z = {res} NO ES MAX LOCAL')
                                print(f'MAX LOCAL: {local_max_f}')
                                seeds.clear()
                        else:
                            print('RESTRICCIONES NO CUMPLIDAS')
                            seeds.clear()
            var_max_lst.append(local_max_x)
            ev_max_lst.append(local_max_f)
            print('===========  MÁXIMO LOCAL  ============')
            print(f'{vector_variables[0]} = ',local_max_x)
            print('MAX z = ', local_max_f)
            print("")
        global_max = max(ev_max_lst)
        dct = {ev_max_lst[i] : var_max_lst[i] for i in range(len(ev_max_lst))}
        for key, value in dct.items():
            if key == global_max:
                print("")
                print('=== VALORES MÁXIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value}')
                print(f'MAX z = {key}')

    elif num_variables == 2:
        for item in range(num_pob):
            local_max_f = 0
            local_max_x = 0
            local_max_y = 0
            print("")
            print(f'--- POBLACIÓN {item + 1} ---')
            for item in range(tam_pob):
                print(f'--- ID {item + 1} ---')
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    print('VARIABLE ', variable, ' LIMS', lims) 
                    if tipo_semilla == '0':
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    print('semilla = ', seed)
                    seeds.append(seed)               
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                            print(f'r{index + 1}: {evl}')
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        #print(vector_booleano)
                        if sum(vector_booleano) == len(vector_restricciones):
                            print('RESTRICCIONES SATISFECHAS')
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])]) > local_max_f):
                                local_max_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                print(f'NUEVO MAX LOCAL: {local_max_f}')
                                local_max_x = seeds[0]
                                local_max_y = seeds[1]
                                print(f'{vector_variables[0]} = {local_max_x}')
                                print(f'{vector_variables[1]} = {local_max_y}')
                                #var_max_lst.append(local_max_x)
                                #ev_max_lst.append(local_max_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                print(f'z = {res} NO ES MAX LOCAL')
                                print(f'MAX LOCAL: {local_max_f}')
                                seeds.clear()
                        else:
                            print('RESTRICCIONES NO CUMPLIDAS')
                            seeds.clear()
            tpl = (local_max_x, local_max_y)
            var_max_lst.append(tpl)
            ev_max_lst.append(local_max_f)
            print('===========  MÁXIMO LOCAL  ============')
            print(f'{vector_variables[0]} = ',local_max_x)
            print(f'{vector_variables[1]} = ', local_max_y)
            print('MAX z = ', local_max_f)
            print("")
        global_max = max(ev_max_lst)
        dct = {ev_max_lst[i] : var_max_lst[i] for i in range(len(ev_max_lst))}
        for key, value in dct.items():
            if key == global_max:
                print("")
                print('=== VALORES MÁXIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'MAX z = {key}')
    
    elif num_variables == 3:
        for item in range(num_pob):
            local_max_f = 0
            local_max_x = 0
            local_max_y = 0
            local_max_z = 0
            print("")
            print(f'--- POBLACIÓN {item + 1} ---')
            for item in range(tam_pob):
                print(f'--- ID {item + 1} ---')
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    print('VARIABLE ', variable, ' LIMS', lims)
                    if tipo_semilla == '0':
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    print('semilla = ', seed)
                    seeds.append(seed)               
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                            print(f'r{index + 1}: {evl}')
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        #print(vector_booleano)
                        if sum(vector_booleano) == len(vector_restricciones):
                            print('RESTRICCIONES SATISFECHAS')
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])]) > local_max_f):
                                local_max_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                print(f'NUEVO MAX LOCAL: {local_max_f}')
                                local_max_x = seeds[0]
                                local_max_y = seeds[1]
                                local_max_z = seeds[2]
                                print(f'{vector_variables[0]} = {local_max_x}')
                                print(f'{vector_variables[1]} = {local_max_y}')
                                print(f'{vector_variables[2]} = {local_max_z}')
                                var_max_lst.append(local_max_x)
                                ev_max_lst.append(local_max_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                print(f'z = {res} NO ES MAX LOCAL')
                                print(f'MAX LOCAL: {local_max_f}')
                                seeds.clear()
                        else:
                            print('RESTRICCIONES NO CUMPLIDAS')
                            seeds.clear()
            tpl = (local_max_x, local_max_y, local_max_z)
            var_max_lst.append(tpl)
            ev_max_lst.append(local_max_f)
            print('===========  MÁXIMO LOCAL  ============')
            print(f'{vector_variables[0]} = ',local_max_x)
            print(f'{vector_variables[1]} = ', local_max_y)
            print(f'{vector_variables[2]} = ', local_max_z)
            print('MAX z = ', local_max_f)
            print("")
        global_max = max(ev_max_lst)
        dct = {ev_max_lst[i] : var_max_lst[i] for i in range(len(ev_max_lst))}
        for key, value in dct.items():
            if key == global_max:
                print("")
                print('=== VALORES MÁXIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'{vector_variables[2]} = {value[2]}')
                print(f'MAX z = {key}')
    print("")
    while (nxt := input('¿CALCULAR MÍNIMO?: [y|n]')) not in yes_no:
        print('ERROR. INGRESA OTRO VALOR.')
    if nxt == 'y':
        min_solver()
    
#################################################################

def max_solver_simple():

    vector_booleano = []
    seeds = []
    var_max_lst = []
    ev_max_lst = []

    if num_variables == 1:
        for item in range(num_pob):
            local_max_f = 0
            local_max_x = 0
            for item in range(tam_pob):
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    seeds.append(seed)               
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0])])
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        if sum(vector_booleano) == len(vector_restricciones):
                            if (fun_obj.subs([(vector_variables[0], seeds[0])]) > local_max_f):
                                local_max_f = fun_obj.subs([(vector_variables[0], seeds[0])])
                                local_max_x = seeds[0]
                                var_max_lst.append(local_max_x)
                                ev_max_lst.append(local_max_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0])])
                                seeds.clear()
                        else:
                            seeds.clear()
            var_max_lst.append(local_max_x)
            ev_max_lst.append(local_max_f)
        global_max = max(ev_max_lst)
        dct = {ev_max_lst[i] : var_max_lst[i] for i in range(len(ev_max_lst))}
        for key, value in dct.items():
            if key == global_max:
                print("")
                print('=== VALORES MÁXIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value}')
                print(f'MAX z = {key}')

    elif num_variables == 2:
        for item in range(num_pob):
            local_max_f = 0
            local_max_x = 0
            local_max_y = 0
            for item in range(tam_pob):
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    if tipo_semilla == '0':
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    seeds.append(seed)               
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        if sum(vector_booleano) == len(vector_restricciones):
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])]) > local_max_f):
                                local_max_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                local_max_x = seeds[0]
                                local_max_y = seeds[1]
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                seeds.clear()
                        else:
                            seeds.clear()
            tpl = (local_max_x, local_max_y)
            var_max_lst.append(tpl)
            ev_max_lst.append(local_max_f)
        global_max = max(ev_max_lst)
        dct = {ev_max_lst[i] : var_max_lst[i] for i in range(len(ev_max_lst))}
        for key, value in dct.items():
            if key == global_max:
                print("")
                print('=== VALORES MÁXIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'MAX z = {key}')
    
    elif num_variables == 3:
        for item in range(num_pob):
            local_max_f = 0
            local_max_x = 0
            local_max_y = 0
            local_max_z = 0
            for item in range(tam_pob):
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    if tipo_semilla == '0':
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    seeds.append(seed)               
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        if sum(vector_booleano) == len(vector_restricciones):
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])]) > local_max_f):
                                local_max_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                local_max_x = seeds[0]
                                local_max_y = seeds[1]
                                local_max_z = seeds[2]
                                var_max_lst.append(local_max_x)
                                ev_max_lst.append(local_max_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                seeds.clear()
                        else:
                            seeds.clear()
            tpl = (local_max_x, local_max_y, local_max_z)
            var_max_lst.append(tpl)
            ev_max_lst.append(local_max_f)
        global_max = max(ev_max_lst)
        dct = {ev_max_lst[i] : var_max_lst[i] for i in range(len(ev_max_lst))}
        for key, value in dct.items():
            if key == global_max:
                print("")
                print('=== VALORES MÁXIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'{vector_variables[2]} = {value[2]}')
                print(f'MAX z = {key}')
    print("")
    while (nxt := input('¿CALCULAR MÍNIMO? [y|n]: ')) not in yes_no:
        print('ERROR. INGRESA OTRO VALOR.')
    if nxt == 'y':
        min_solver_simple()

#################################################################

def min_solver():

    vector_booleano = []
    seeds = []
    var_min_lst = []
    ev_min_lst = []

    if num_variables == 1:
        for item in range(num_pob):
            local_min_f = 10000000
            local_min_x = 0
            print("")
            print(f'--- POBLACIÓN {item + 1} ---')
            for item in range(tam_pob):
                print(f'--- ID {item + 1} ---')
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    print('VARIABLE', variable, 'LIMS', lims)
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    print('semilla = ', seed)
                    seeds.append(seed)             
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0])])
                            print(f'r{index + 1}: {evl}')
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        #print(vector_booleano)
                        if sum(vector_booleano) == len(vector_restricciones):
                            print('RESTRICCIONES SATISFECHAS')
                            if (fun_obj.subs([(vector_variables[0], seeds[0])]) < local_min_f):
                                local_min_f = fun_obj.subs([(vector_variables[0], seeds[0])])
                                print(f'NUEVO MIN LOCAL: {local_min_f}')
                                local_min_x = seeds[0]
                                print(f'{vector_variables[0]} =  {local_min_x}')
                                var_min_lst.append(local_min_x)
                                ev_min_lst.append(local_min_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0])])
                                print(f'z = {res} NO ES MIN LOCAL')
                                print(f'MIN LOCAL: {local_min_f}')
                                seeds.clear()
                        else:
                            print('RESTRICCIONES NO CUMPLIDAS')
                            seeds.clear()
            var_min_lst.append(local_min_x)
            ev_min_lst.append(local_min_f)
            print('===========  MÍNIMO LOCAL  ============')
            print(f'{vector_variables[0]} = ', local_min_x)
            print('MIN z = ', local_min_f)
            print("")
        global_min = min(ev_min_lst)
        dct = {ev_min_lst[i] : var_min_lst[i] for i in range(len(ev_min_lst))}
        for key, value in dct.items():
            if key == global_min:
                print("")
                print('=== VALORES MÍNIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value}')
                print(f'MIN z = {key}')

    elif num_variables == 2:
        for item in range(num_pob):
            local_min_f = 100000
            local_min_x = 0
            local_min_y = 0
            print("")
            print(f'--- POBLACIÓN {item + 1} ---')
            for item in range(tam_pob):
                print(f'--- ID {item + 1} ---')
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    print('VARIABLE', variable, 'LIMS', lims)
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    print('semilla = ', seed)
                    seeds.append(seed)             
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                            print(f'r{index + 1}: {evl}')
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        #print(vector_booleano)
                        if sum(vector_booleano) == len(vector_restricciones):
                            print('RESTRICCIONES SATISFECHAS')
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])]) < local_min_f):
                                local_min_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                print(f'NUEVO MIN LOCAL: {local_min_f}')
                                local_min_x = seeds[0]
                                local_min_y = seeds[1]
                                print(f'{vector_variables[0]} = {local_min_x}')
                                print(f'{vector_variables[1]} = {local_min_y}')
                                #var_max_lst.append(local_max_x)
                                #ev_max_lst.append(local_max_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                print(f'z = {res} NO ES MIN LOCAL')
                                print(f'MIN LOCAL: {local_min_f}')
                                seeds.clear()
                        else:
                            print('RESTRICCIONES NO CUMPLIDAS')
                            seeds.clear()
            tpl = (local_min_x, local_min_y)
            var_min_lst.append(tpl)
            ev_min_lst.append(local_min_f)
            print('===========  MÍNIMO LOCAL  ============')
            print(f'{vector_variables[0]} = ',local_min_x)
            print(f'{vector_variables[1]} = ', local_min_y)
            print('MIN z = ', local_min_f)
            print("")
        global_min = min(ev_min_lst)
        dct = {ev_min_lst[i] : var_min_lst[i] for i in range(len(ev_min_lst))}
        for key, value in dct.items():
            if key == global_min:
                print("")
                print('=== VALORES MÍNIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'MIN z = {key}')
    
    elif num_variables == 3:
        for item in range(num_pob):
            local_min_f = 100000
            local_min_x = 0
            local_min_y = 0
            local_min_z = 0
            print("")
            print(f'--- POBLACIÓN {item + 1} ---')
            for item in range(tam_pob):
                print(f'--- ID {item + 1} ---')
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    print('VARIABLE', variable, 'LIMS', lims)
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    print('semilla = ', seed)
                    seeds.append(seed)             
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]),(vector_variables[2], seeds[2])])
                            print(f'r{index + 1}: {evl}')
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        #print(vector_booleano)
                        if sum(vector_booleano) == len(vector_restricciones):
                            print('RESTRICCIONES SATISFECHAS')
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]),(vector_variables[2], seeds[2])]) < local_min_f):
                                local_min_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                print(f'NUEVO MIN LOCAL: {local_min_f}')
                                local_min_x = seeds[0]
                                local_min_y = seeds[1]
                                local_min_z = seeds[2]
                                print(f'{vector_variables[0]} = {local_min_x}')
                                print(f'{vector_variables[1]} = {local_min_y}')
                                print(f'{vector_variables[2]} = {local_min_z}')
                                #var_max_lst.append(local_max_x)
                                #ev_max_lst.append(local_max_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                print(f'z = {res} NO ES MIN LOCAL')
                                print(f'MIN LOCAL: {local_min_f}')
                                seeds.clear()
                        else:
                            print('RESTRICCIONES NO CUMPLIDAS')
                            seeds.clear()
            tpl = (local_min_x, local_min_y, local_min_z)
            var_min_lst.append(tpl)
            ev_min_lst.append(local_min_f)
            print('===========  MÍNIMO LOCAL  ============')
            print(f'{vector_variables[0]} = ',local_min_x)
            print(f'{vector_variables[1]} = ', local_min_y)
            print(f'{vector_variables[2]} = ', local_min_z)
            print('MIN z = ', local_min_f)
            print("")
        global_min = min(ev_min_lst)
        dct = {ev_min_lst[i] : var_min_lst[i] for i in range(len(ev_min_lst))}
        for key, value in dct.items():
            if key == global_min:
                print("")
                print('=== VALORES MÍNIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'{vector_variables[2]} = {value[2]}')
                print(f'MIN z = {key}')
    print("")  
    while (nxt := input('¿CALCULAR MÁXIMO?: [y|n]: ')) not in yes_no:
        print('ERROR. INGRESA OTRO VALOR.')
    if nxt == 'y':
        max_solver()

########################################################################

def min_solver_simple():

    vector_booleano = []
    seeds = []
    var_min_lst = []
    ev_min_lst = []

    if num_variables == 1:
        for item in range(num_pob):
            local_min_f = 10000000
            local_min_x = 0
            for item in range(tam_pob):
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    seeds.append(seed)             
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0])])
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        if sum(vector_booleano) == len(vector_restricciones):
                            if (fun_obj.subs([(vector_variables[0], seeds[0])]) < local_min_f):
                                local_min_f = fun_obj.subs([(vector_variables[0], seeds[0])])
                                local_min_x = seeds[0]
                                var_min_lst.append(local_min_x)
                                ev_min_lst.append(local_min_f)
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0])])
                                seeds.clear()
                        else:
                            seeds.clear()
            var_min_lst.append(local_min_x)
            ev_min_lst.append(local_min_f)
        global_min = min(ev_min_lst)
        dct = {ev_min_lst[i] : var_min_lst[i] for i in range(len(ev_min_lst))}
        for key, value in dct.items():
            if key == global_min:
                print("")
                print('=== VALORES MÍNIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value}')
                print(f'MIN z = {key}')

    elif num_variables == 2:
        for item in range(num_pob):
            local_min_f = 100000
            local_min_x = 0
            local_min_y = 0
            for item in range(tam_pob):
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    seeds.append(seed)             
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        if sum(vector_booleano) == len(vector_restricciones):
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])]) < local_min_f):
                                local_min_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                local_min_x = seeds[0]
                                local_min_y = seeds[1]
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1])])
                                seeds.clear()
                        else:
                            seeds.clear()
            tpl = (local_min_x, local_min_y)
            var_min_lst.append(tpl)
            ev_min_lst.append(local_min_f)
        global_min = min(ev_min_lst)
        dct = {ev_min_lst[i] : var_min_lst[i] for i in range(len(ev_min_lst))}
        for key, value in dct.items():
            if key == global_min:
                print("")
                print('=== VALORES MÍNIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'MIN z = {key}')
    
    elif num_variables == 3:
        for item in range(num_pob):
            local_min_f = 100000
            local_min_x = 0
            local_min_y = 0
            local_min_z = 0
            for item in range(tam_pob):
                index = 0
                vector_booleano.clear()
                for variable, lims in zip(vector_variables, vector_lims):
                    if tipo_semilla == '0': 
                        seed = (random.randint(low = lims[0], high = lims[1]))
                    else:
                        seed = (random.rand() * lims[1]) - abs(lims[0])
                    seeds.append(seed)             
                    if len(seeds) == num_variables:
                        for item in vector_restricciones:
                            rst = item[0]
                            rst = sympify(rst)
                            evl = rst.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]),(vector_variables[2], seeds[2])])
                            index = index + 1
                            if evl:
                                vector_booleano.append(1)
                            else:
                                vector_booleano.append(0)
                        if sum(vector_booleano) == len(vector_restricciones):
                            if (fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]),(vector_variables[2], seeds[2])]) < local_min_f):
                                local_min_f = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                local_min_x = seeds[0]
                                local_min_y = seeds[1]
                                local_min_z = seeds[2]
                                seeds.clear()
                            else:
                                res = fun_obj.subs([(vector_variables[0], seeds[0]), (vector_variables[1], seeds[1]), (vector_variables[2], seeds[2])])
                                seeds.clear()
                        else:
                            seeds.clear()
            tpl = (local_min_x, local_min_y, local_min_z)
            var_min_lst.append(tpl)
            ev_min_lst.append(local_min_f)
        global_min = min(ev_min_lst)
        dct = {ev_min_lst[i] : var_min_lst[i] for i in range(len(ev_min_lst))}
        for key, value in dct.items():
            if key == global_min:
                print("")
                print('=== VALORES MÍNIMOS FINALES ===')
                print(f'{vector_variables[0]} = {value[0]}')
                print(f'{vector_variables[1]} = {value[1]}')
                print(f'{vector_variables[2]} = {value[2]}')
                print(f'MIN z = {key}')
    print("")  
    while (nxt := input('¿CALCULAR MÁXIMO?: [y|n]: ')) not in yes_no:
        print('ERROR. INGRESA OTRO VALOR.')
    if nxt == 'y':
        max_solver_simple()


if __name__ == '__main__':
    print('================================')
    print('       SEMILLA ALEATORIA  ')
    print('================================')

    x, y, z = symbols('x y z')
    yes_no = ['y', 'n']
    bin_option = ['0', '1']
    var_lst = str([x for x in range(1, 4, 1)])
    vector_variables = []
    vector_restricciones = []
    vector_lims = []

#    # LEVANTAMIENTO DE VARIABLES
    while (max_min := input('\nMax||Min [0|1]: ')) not in bin_option:
        print('ERROR. ELIGE OTRA OPCIÓN')
    while (num_variables := input('Ingresa el número de variables: '))not in var_lst:
        print('ERROR. INGRESA UN ENTERO ENTRE 1 Y 3')
    num_variables = int(num_variables)
    for item in range(num_variables):
        new_variable = symbols(f'x{item + 1}')
        vector_variables.append(new_variable)
    print(vector_variables)

    # LEVANTAMIENTO DE RESTRICCIONES
    while True:
        try:
            num_restricciones = int(input('Ingresa el número de restricciones: '))
            break
        except ValueError:
            print('ERROR. INGRESA UN VALOR ENTERO')
    for item in range(num_restricciones):
        vector_restricciones.append([])
        new_restriccion = input(f'Ingresa la restricción {item + 1}: ')
        vector_restricciones[item].append(new_restriccion)
    pprint(vector_restricciones)

    # LÍMITES DE VARIABLES
    for item in range(num_variables):
        lim_inf = float(input(f'Límite inferior de {vector_variables[item]}: '))
        lim_sup = float(input(f'Límite superior de {vector_variables[item]}: '))
        vector_lims.append([lim_inf, lim_sup])
    print(vector_lims)

   # LEVANTAMIENTO DE FUNCIÓN OBJETIVO, POBLACIONES E ITERACIONES
    exp_mat = input('Ingresa la función objetivo: ')
    fun_obj = sympify(exp_mat)
    while True:
        try:
            num_pob = int(input('Ingresa el número de poblaciones: '))
            break
        except ValueError:
            print('ERROR. INGRESA UN VALOR ENTERO')
    while True:
        try:
            tam_pob = int(input('Ingresa el tamaño de la población: '))
            break
        except ValueError:
            print('ERROR. INGRESA UN NÚMERO ENTERO')
    
    while (tipo_semilla := input('Entero|Decimal [0|1]: ')) not in bin_option:
        print('ERROR. INGRESA UN VALOR VÁLIDO')

    while(informe := input('IMPRIMIR INFORME COMPLETO [y|n]: ')) not in yes_no:
        print('ERROR. INGRESA UNA OPCIÓN VÁLIDA')

    if max_min == '0' and informe == 'y':
        max_solver()
    elif max_min == '0' and informe == 'n':
        max_solver_simple()
    elif max_min == '1' and informe == 'y':
        min_solver()
    elif max_min == '1' and informe == 'n':
        min_solver_simple()