from display import *
from draw import *
from parser import *
from matrix import *
import sys

filename = sys.argv[1]

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( filename, edges, transform, screen, color )
