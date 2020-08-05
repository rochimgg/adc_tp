import numpy as np
import os
from constants import *


def write_full_example_header(file):
    file.write(FULL_EXAMPLE_HEADER)


def first_item(ls):
    if ls:
        return ls[0]


def find_pins_in_lib(some_path):
    with open(some_path + ".asy", "r") as a_file:
        sym = a_file.readlines()
    pin = []
    for a_line in sym:
        some_words = a_line.split()
        if some_words[0] == 'PIN':
            pin.append((int(some_words[1]), -int(some_words[2])))
    return pin


def node_search(coordinate, node_list):
    a_node = [idx for idx, x1 in enumerate(node_list) if x1[0] == coordinate]
    if not a_node:
        a_node = [len(node_list)]
        node_list.append([coordinate, [], [], []])
    return a_node[0]


def coordinate_node_scale(scale, node_list):
    for idx_i, data_i in enumerate(node_list):
        node_list[idx_i][0] = np.array(node_list[idx_i][0]) * scale


def print_xy(coordinates, offset=None):
    if offset is None:
        offset = [0, 0]
    return '(' + str(coordinates[0] - offset[0]) + ',' + str(coordinates[1] - offset[1]) + ')'


def get_node_name(a_node, node_list):
    if node_list[a_node][3]:
        return '(' + str(node_list[a_node][3]) + ')'
    else:
        return print_xy(node_list[a_node][0])


def convert_new_name(a_name):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    result = ''.join(ones[int(i)] if i.isdigit() else str(i) for i in a_name)
    result = result.replace("-", "")
    return result.replace("/", "")


def create_dev_from_lib(ltspice_directory, component, scale=1 / 64):
    with open(ltspice_directory+component + ".asy", "r") as fi:
        sym = fi.readlines()

    pin = []
    pin_name = []
    line = []
    rect = []
    circ = []
    arc = []
    text = []
    window = []
    for l in sym:
        line_words = l.split()
        if line_words[0] == 'PIN':  # that is not drawn
            pin.append([int(line_words[1]) * scale, -int(line_words[2]) * scale])
        if line_words[0] == 'LINE':  # \draw (-1.5,0) -- (1.5,0);
            line.append(
                [int(line_words[2]) * scale, -int(line_words[3]) * scale, int(line_words[4]) * scale,
                 -int(line_words[5]) * scale])
        if line_words[0] == 'RECTANGLE':  # \draw (0,0) rectangle (1,1)
            rect.append(
                [int(line_words[2]) * scale, -int(line_words[3]) * scale, int(line_words[4]) * scale,
                 -int(line_words[5]) * scale])
        if line_words[0] == 'CIRCLE':  # \draw[x radius=2, y radius=1] (0,0) ellipse [];
            circ.append(
                [int(line_words[2]) * scale, -int(line_words[3]) * scale, int(line_words[4]) * scale,
                 -int(line_words[5]) * scale])
        if line_words[0] == 'ARC':  # \draw (3mm,0mm) arc (0:30:3mm);
            arc.append(
                [int(line_words[2]) * scale, -int(line_words[3]) * scale, int(line_words[4]) * scale,
                 -int(line_words[5]) * scale,
                 int(line_words[6]) * scale, -int(line_words[7]) * scale, int(line_words[8]) * scale,
                 -int(line_words[9]) * scale])
        if line_words[0] == 'TEXT':  # \node[right] at (0,1) {bla} ;
            text.append(
                [int(line_words[1]) * scale, -int(line_words[2]) * scale, line_words[3], ' '.join(line_words[5:])])
        if line_words[0] == 'WINDOW':  # that is not drawn
            window.append([int(line_words[2]) * scale, -int(line_words[3]) * scale])

    offset = pin[0] if pin else [0, 0]

    new_lib = '\\def\\' + convert_new_name(component) + r'(#1)#2#3{%' + '\n' + r'  \begin{scope}[#1,transform canvas={scale=1}]' + '\n'

    for t in line:
        new_lib = new_lib + r'  \draw ' + print_xy(t[0:], offset) + ' -- ' + print_xy(t[2:], offset) + ';' + '\n'
    if window:  # \draw  (2,0.5) node[left] {$x$};
        t = window[0]
        new_lib = new_lib + r'  \draw ' + print_xy(t[0:], offset) + ' coordinate (#2 text);' + '\n'
    for t in circ:
        new_lib = new_lib + r'  \draw[x radius=' + str((t[2] - t[0]) / 2) + ', y radius=' + str(
            (t[3] - t[1]) / 2) + ']'
        new_lib = new_lib + print_xy([(t[0] + t[2]) / 2, (t[1] + t[3]) / 2], offset) + ' ellipse [];' + '\n'
    for t in arc:  # \draw (0,4)++(49: 1 and 2)  arc (49:360: 1 and 2);
        center = [(t[0] + t[2]) / 2, (t[1] + t[3]) / 2]
        rx = (t[2] - t[0]) / 2
        ry = (t[3] - t[1]) / 2
        start_angle = np.angle((t[4] - center[0]) + 1j * (t[5] - center[1])) * 180 / np.pi
        end_angle = np.angle((t[6] - center[0]) + 1j * (t[7] - center[1])) * 180 / np.pi
        str_r = str(abs(rx)) + ' and ' + str(abs(ry))
        new_lib = new_lib + r'  \draw ' + print_xy(center, offset) + '++( ' + str(start_angle) + ': ' + str_r
        new_lib = new_lib + ')  arc (' + str(start_angle) + ':' + str(end_angle) + ': ' + str_r + ');' + '\n'
    for t in rect:
        new_lib = new_lib + r'  \draw ' + print_xy(t[0:], offset) + ' rectangle ' + print_xy(t[2:],
                                                                                             offset) + ';' + '\n'
    for t in text:
        new_lib = new_lib + r'  \node[right] at ' + print_xy(t[0:], offset) + r'{' + str(t[3]) + r'};' + '\n'
    for ind, t in enumerate(pin):
        new_lib = new_lib + r'  \draw ' + print_xy(t[0:], offset) + ' coordinate (#2 X' + str(ind) + ');' + '\n'
        pin_name.append('  X' + str(ind))

    new_lib = new_lib + r'  \end{scope}' + '\n'

    if window:
        new_lib = new_lib + r'  \draw (#2 text) node[right] {#3};' + '\n'

    new_lib = new_lib + r'}' + '\n'
    return new_lib


def file_name(path_name):
    return os.path.splitext(os.path.basename(path_name))[0]


def wire_addition(order, wire_list, node_list):
    x1 = (int(order[1]), -int(order[2]))
    x2 = (int(order[3]), -int(order[4]))
    wire_quantity = len(wire_list)

    node1 = node_search(x1, node_list)
    node2 = node_search(x2, node_list)
    node_list[node1][1].append(wire_quantity)
    node_list[node2][1].append(wire_quantity)

    wire_list.append([node1, node2])


def ground_text_addition(order, component_list, node_list):
    x1 = (int(order[1]), -int(order[2]))
    component_quantity = len(component_list)
    a_node = node_search(x1, node_list)
    node_list[a_node][2].append(component_quantity)
    if order[0] == 'FLAG':
        component_list.append([a_node, 'FLAG', '', []])
    else:
        text = ' '.join(order[5:]).replace(';', '')
        component_list.append([a_node, 'TEXT', text, []])


def component_addition(an_idx, order, ltspice_directory, component_list, node_list, words, components_count, components_add_memory):
    x = np.array([int(order[2]), -int(order[3])])
    pin = find_pins_in_lib(ltspice_directory+order[1])
    component_quantity = len(component_list)

    pin = np.dot(pin, rotations[order[4]])

    node_memory = []
    for pin_n in pin:
        a_node = node_search(tuple(pin_n + x), node_list)
        node_memory.append(a_node)
        node_list[a_node][2].append(component_quantity)

    for i in range(an_idx + 1, an_idx + 4):
        if words[i][0] == 'SYMATTR':
            component_designation = words[i][2]
            if component_designation.count('_') > 0 and component_designation.count('$') < 2:
                component_designation = r'$' + component_designation + r'$'
            break

    node_related = []

    if not order[1] in possible_components and not order[1] in special_components_names:
        if not order[1] in components_add_memory:
            print('The following component is new: ' + order[1])
            components_add_memory.append(order[1])

        node_related = []
        for ind, y0 in enumerate(pin):
            node_related.append('B' + str(components_count) + ' X' + str(ind))

        components_count = components_count + 1
        order[1] = order[1] + ' ' + (order[4] + '  ')[0:4]
        for x0, a_name in enumerate(node_related):
            node_list[node_memory[x0]][3] = a_name

    if not order[1] in possible_components and order[1] in special_components_names:
        node_related = special_components_names[order[1]]
        node_related = ['B' + str(components_count) + '.' + t for t in node_related]
        components_count = components_count + 1
        if order[4].count('M'):
            if special_components[order[1]].count('yscale=-1'):
                order[1] = order[1] + r',yscale=-1' + ',xscale=-1' + ',rotate=' + '-' + order[4][1:] + r',yscale=-1'
            else:
                order[1] = order[1] + ',xscale=-1' + ',rotate=' + '-' + order[4][1:]
        else:
            if special_components[order[1]].count('yscale=-1'):
                order[1] = order[1] + r',yscale=-1' + ',rotate=' + '-' + order[4][1:] + r',yscale=-1'
            else:
                order[1] = order[1] + ',rotate=' + '-' + order[4][1:]
        for x0, a_name in enumerate(node_related):
            node_list[node_memory[x0]][3] = a_name

    component_list.append([node_memory, order[1], component_designation, node_related])
    return components_count
