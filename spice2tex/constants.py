
FULL_EXAMPLE_HEADER = '''\\documentclass[a4paper,12pt]{article}
\\pagestyle{empty}
\\usepackage{amsmath}
\\usepackage{tikz}
\\usepackage[siunitx,american]{circuitikz}
\\usetikzlibrary{bending}
\\usetikzlibrary{arrows}

\\begin{document}
'''

CIRCUIT_BEGINNING_TEX = '''\\ctikzset{tripoles/mos style/arrows}
\\begin{circuitikz}[transform shape,scale=1]
'''

CIRCUIT_BEGINNING_PGF = '''\\documentclass[margin=10pt]{standalone}
\\usepackage[siunitx]{circuitikz}
\begin{document}
\\ctikzset{tripoles/mos style/arrows}
\\begin{circuitikz}[transform shape,scale=1]
'''

CIRCUIT_END = '''
\\end{circuitikz}
'''

END_DOCUMENT = '''\n\\end{document}'''

special_components_names = {
    'mesfet': ['D', 'G', 'S'],
    'njf': ['D', 'G', 'S'],
    'nmos': ['D', 'G', 'S'],
    'nmos4': ['D', 'G', 'S', 'bulk'],
    'npn': ['C', 'B', 'E'],
    'npn2': ['C', 'B', 'E'],
    'npn3': ['C', 'B', 'E'],
    'pjf': ['C', 'B', 'E'],
    'pmos': ['D', 'G', 'S'],
    'pmos4': ['D', 'G', 'S', 'bulk'],
    'pnp': ['C', 'B', 'E'],
    'pnp2': ['C', 'B', 'E'],
}

special_components = {
    'mesfet': 'njfet,anchor=D',
    'njf': 'njfet,anchor=D',
    'nmos': 'nigfete,anchor=D',
    'nmos4': 'nfet,anchor=D',
    'npn': 'npn,anchor=D',
    'npn2': 'npn,anchor=D',
    'npn3': 'npn,anchor=D',
    'pmos': 'pigfete,anchor=D,yscale=-1',
    'pmos4': 'pfet,anchor=D,yscale=-1',
    'pnp': 'pnp,anchor=D,yscale=-1',
    'pnp2': 'pnp,anchor=D,yscale=-1',
}

possible_components = {
    'bi': 'controlled current source,i=\ ',
    'bi2': 'controlled current source,i_=\ ',
    'bv': 'controlled voltage source,v_=\ ',
    'cap': 'C',
    'csw': 'switch',
    'current': 'current source,i=\ ',
    'diode': 'D',
    'f': 'controlled current source,i=\ ',
    'h': 'voltage source,v_=\ ',
    'ind': 'L',
    'LED': 'led',
    'load': 'vR',
    'load2': 'controlled current source,i=\ ',
    'polcap': 'eC',
    'res': 'R',
    'res2': 'R',
    'schottky': 'sDo',
    'TVSdiode': 'zDo',
    'varactor': 'VCo',
    'voltage': 'voltage source,v_=\ ',
    'zener': 'zDo', }

rotations = {
    'R0': [[1, 0], [0, 1]],
    'R90': [[0, -1], [1, 0]],
    'R180': [[-1, 0], [0, -1]],
    'R270': [[0, 1], [-1, 0]],
    'M0': [[-1, 0], [0, 1]],
    'M90': [[0, -1], [-1, 0]],
    'M180': [[1, 0], [0, -1]],
    'M270': [[0, 1], [1, 0]], }