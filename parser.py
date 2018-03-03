from display import *
from matrix import *
from draw import *


"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         `line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 `ident: set the transform matrix to the identity matrix - 
	 `scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 `move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 `rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 `apply: apply the current transformation matrix to the 
	    edge matrix
	 `display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    lines = []
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip("\n")
            lines.append(line)

    print len(lines)
    for i in range(len(lines)):
        cmd = lines[i]
        
        if cmd == 'line':
            arg = lines[i+1].split()
            for i in range(len(arg)):
                arg[i] = int(arg[i])
                
            add_edge(points, arg[0], arg[1], arg[2],arg[3], arg[4], arg[5])
            i += 1
            
        if cmd == 'ident':
            ident(transform)

        if cmd == 'scale':
            arg = lines[i+1].split()
            for i in range(len(arg)):
                 arg[i] = int(arg[i])
            mult_matrix( make_scale(arg[0], arg[1], arg[2]), transform )
            i += 1

        if cmd == 'move':
            arg = lines[i+1].split()
            for i in range(len(arg)):
                arg[i] = int(arg[i])
            mult_matrix( make_translate(arg[0], arg[1], arg[2]), transform )
            i += 1
        
        if cmd == 'rotate':
            arg = lines[i+1].split()
            axis = arg[0]
            if axis == 'x':
                mult_matrix( make_rotX( int(arg[1]) ), transform )
            if axis == 'y':
                mult_matrix( make_rotY( int(arg[1]) ), transform )
            if axis == 'z':
                mult_matrix( make_rotZ( int(arg[1]) ), transform )
            i += 1

        if cmd == 'apply':
            mult_matrix( transform, points )
            print_matrix(points)
            for i in range(len(points)):
                for j in range(len(points[i])):
                     points[i][j] = int(points[i][j])

        if cmd == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)

        if cmd == 'save':
            arg = lines[i+1].split()
            save_ppm(screen, arg[0])

        if cmd == 'quit':
            break
