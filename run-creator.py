#!/usr/bin/env python3
from ast import literal_eval

import sys

from functions import *

template = sys.argv[1]  # Template file path
elements = sys.argv[2]  # Elements
fraction = sys.argv[3]  # Fraction of second element
potential = sys.argv[4]  # The potential used
potential_type = sys.argv[5]  # The type of potential
side = sys.argv[6]  # The length of the cubic simulation box
unit_cell_type = sys.argv[7]  # fcc, hcp, or bcc
lattice_param = sys.argv[8]  # The lattice paramter
timestep = sys.argv[9]  # The timestep
dump_rate = sys.argv[10]  # The rate to dump data
ensemble = sys.argv[11]  # The ensemble for the holds
vols = sys.argv[12]  # The volume for nvt holds (write None for npt)
holds = sys.argv[13:]  # temperature and holds as tuples

# Open and read template
template = open(template)
template_contents = template.read()
template.close()

# Format the holds
holds = list(map(literal_eval, holds))

# Format the volumes
try:
    vols = literal_eval(vols)

except Exception:
    pass

contents = run_creator(
                       template_contents,
                       elements,
                       fraction,
                       potential,
                       potential_type,
                       side,
                       unit_cell_type,
                       lattice_param,
                       timestep,
                       dump_rate,
                       ensemble,
                       vols,
                       holds
                       )

# Write the input file
file_out = open('steps.in', 'w')
file_out.write(contents)
file_out.close()

print(contents)
