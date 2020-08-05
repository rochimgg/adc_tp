#!/usr/local/bin/python3
import os
import sys
from functions import *
from constants import *


def dir_spice2tex(path='.', final_path = "" ,ltspice_directory=r'C:\Program Files\LTC\LTspiceXVII\lib\sym',
                  full_example=0):
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)) and filename.endswith('.asc'):
            print('Convert: ' + filename)
            spice2tex(path+os.sep+filename, final_path,ltspice_directory=ltspice_directory, full_example=full_example)


components_count = 0
components_add_memory = []


def spice2tex(file_name_ltspice='Draft.asc', final_path = "" ,ltspice_directory=r'C:\Program Files\LTC\LTspiceXVII\lib\sym',
              full_example=0):

    global components_count
    global components_add_memory

    if final_path:
        if not final_path[-1] == os.path.sep:
            final_path = final_path + os.path.sep
        save_file = final_path + file_name_ltspice.split(os.sep)[-1].split('.')[0] + r'.tex'
    else:
        save_file = file_name_ltspice[0:-len(file_name_ltspice.split('.')[-1])] + r'tex'

    if not ltspice_directory[-1] == os.path.sep:
        ltspice_directory = ltspice_directory + os.path.sep

    with open(file_name_ltspice, "r") as fi:
        data = fi.readlines()

    words = []
    for line in data:
        words.append(line.split())

    components_add_memory = []
    node_list = []
    component_list = []
    wire_list = []
    components_count = 0

    for idx in enumerate(words):
        if idx[1][0] == 'WIRE':
            wire_addition(idx[1], wire_list, node_list)

        if idx[1][0] == 'FLAG' or idx[1][0] == 'TEXT':
            ground_text_addition(idx[1], component_list, node_list)

        if idx[1][0] == 'SYMBOL':
            components_count = component_addition(idx[0], idx[1], ltspice_directory, component_list, node_list, words, components_count, components_add_memory)

    coordinate_node_scale(1 / 64, node_list)

    for c1, c2 in wire_list:  # Wire that directly connects two components is divided into two parts
        if (len(node_list[c1][2]) == 1 and len(node_list[c2][2]) == 1
                and len(node_list[c1][1]) == 1 and len(node_list[c2][1]) == 1):
            old_wire = node_list[c1][1][0]
            new_wire = len(wire_list)  # New wire index
            node_list[c2][1] = [new_wire]  # Connect new wire to K2

            c3 = len(node_list)  # Add nodes between the two old nodes
            xy_c3 = (node_list[c1][0] + node_list[c2][0]) / 2
            node_list.append([xy_c3, [new_wire, old_wire], [], []])

            wire_list.append([c3, c2])  # add new wire
            wire_list[old_wire][1] = c3  # Connect the old wire to the new knot

    current_node_index = 0
    node_coordinates = ''
    for ind, t in enumerate(node_list):
        if not node_list[ind][3] and (len(node_list[ind][1]) + len(node_list[ind][2])) > 2:
            node_list[ind][3] = 'X' + str(current_node_index)
            xy = print_xy(node_list[ind][0])
            node_coordinates = node_coordinates + '\draw ' + xy + ' to[short,-*] '
            node_coordinates += xy + ' coordinate (' + str(node_list[ind][3]) + ');\n'
            current_node_index = current_node_index + 1

    f = open(save_file, "w")

    if full_example:
        write_full_example_header(f)

    f.write(CIRCUIT_BEGINNING)
    f.write(node_coordinates)

    for component in components_add_memory:
        f.write(create_dev_from_lib(ltspice_directory,  component, scale=1 / 64))

    for node, component, name, node_name in component_list:
        if component in possible_components:
            xy = [[], []]
            for idx, c1 in enumerate(node):
                wire_number = first_item(node_list[c1][1])
                if not isinstance(wire_number, int) or node_list[c1][3]:  # No cable is connected to the component
                    xy[idx] = c1
                else:
                    if wire_list[wire_number][0] == c1:  # Component between IndexK1-IndexK2 or IndexK2-IndexK1
                        c2 = wire_list[wire_number][1]
                    else:
                        c2 = wire_list[wire_number][0]

                    xy[idx] = c2
                    wire_list[wire_number] = []
            f.write('\\draw %s to[%s,l=%s] %s ;\n' % (
                get_node_name(xy[0], node_list), possible_components[component], name, get_node_name(xy[1], node_list)))

        if component == 'FLAG':
            f.write('\\draw %s node[ground] {} ;\n' % (get_node_name(node, node_list),))

        if component == 'TEXT':
            f.write('\\node[right] at %s {%s} ;\n' % (get_node_name(node, node_list), name))

        temp = component.split(',')[0]
        if temp in special_components_names:
            rot = component[len(temp):]
            rotation = rot.split('rotate=')[1].split(',')[0]
            component = component.split(',')[0]
            t_node_name = node_name[0].partition(".")[0]
            if not rot.count('xscale=-1'):
                if special_components[component].count('yscale=-1'):
                    f.write('\\draw %s node[%s](%s){\\rotatebox{%s}{\\reflectbox{%s}}} ;\n' % (
                        print_xy(node_list[node[0]][0]), special_components[component] + rot, t_node_name,
                        str(180 + int(rotation)), name))
                else:
                    f.write('\\draw %s node[%s](%s){\\rotatebox{%s}{%s}} ;\n' % (
                        print_xy(node_list[node[0]][0]), special_components[component] + rot, t_node_name,
                        str(-int(rotation)),
                        name))
            else:
                if special_components[component].count('yscale=-1'):
                    f.write('\\draw %s node[%s](%s){\\rotatebox{%s}{%s}} ;\n' % (
                        print_xy(node_list[node[0]][0]), special_components[component] + rot, t_node_name,
                        str(180 + int(rotation)), name))
                else:
                    f.write('\\draw %s node[%s](%s){\\rotatebox{%s}{\\reflectbox{%s}}} ;\n' % (
                        print_xy(node_list[node[0]][0]), special_components[component] + rot, t_node_name,
                        str(-int(rotation)),
                        name))

        if component[:-5] in components_add_memory:
            rot = component[-4:]
            if rot[0] == 'M':
                rot = 'rotate=' + rot[1:] + ',xscale=-1'
            else:
                rot = 'rotate=' + rot[1:]

            component = component[:-5]
            t_node_name = node_name[0].partition(" ")[0]
            f.write('\\%s (shift={%s},%s) {%s} {%s};\n' % (
                convert_new_name(component), print_xy(node_list[node[0]][0]), rot, t_node_name, name))

    for x in wire_list:
        if len(x) != 0:
            f.write('\\draw %s to[short,-] %s ;\n' % (get_node_name(x[0], node_list), get_node_name(x[1], node_list)))

    f.write(CIRCUIT_END)
    if full_example:
        f.write(END_DOCUMENT)

    f.close()

    print('Congratulations. The run was successful.')


def main():
    dir_spice2tex(r'/Users/rgallo/Repositorios/adc_tp/ltspice', r'/Users/rgallo/Repositorios/adc_tp/latex/', r'/Users/rgallo/sym', 0)


if __name__ == '__main__':
    main()
