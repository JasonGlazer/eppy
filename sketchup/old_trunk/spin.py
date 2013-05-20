# Copyright (c) 2012 Santosh Phillip

# This file is part of eplusinterface_diagrams.

# Eplusinterface_diagrams is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Eplusinterface_diagrams is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with eplusinterface_diagrams.  If not, see <http://www.gnu.org/licenses/>.

"""testing to see in what order the points in sketchup are given
Results: Right hand corkscrew in the direction of the normal"""

from Scientific.Geometry import Vector
import readsketchup
import geometry

txt = open('e.txt', 'r').read()
dct = readsketchup.readsketchup(txt)
for key in dct.keys():
    plane = dct[key]['points']
    normal = Vector(dct[key]['normal'])
    calcnormal = geometry.facenormal(plane)
    # print normal
    # print calcnormal
    print normal.angle(calcnormal)
    print
    