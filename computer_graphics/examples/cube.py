#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# File Name: cube.py
# Author: Lawrence Fernandes
# Copyright (C) 2016 Lawrence Fernandes
#
""" This module draws a cube with its faces (polygon mesh) or without them.
    The cube is rotated on the screen. It can be done automatically or by the user,
    deppending on the arguments the program takes.
"""
# Import Python modules
import sys
# Import OpenGL modules
try:
    from OpenGL.GLUT import *
    from OpenGL.GLU import *
    from OpenGL.GL import *
except:
    print ("OpenGL wrapper for Python not found.")

#Input arguments
option = ' '.join(sys.argv[1:])

# Global variables
#Define the location (x,y,z) of each vertex
vertices = (
    ( 1,-1,-1),
    ( 1, 1,-1),
    (-1, 1,-1),
    (-1,-1,-1),
    ( 1,-1, 1),
    ( 1, 1, 1),
    (-1,-1, 1),
    (-1, 1, 1),
    )

#Define the edges connecting the vertices
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7),
    )

#Define the faces of the cube
faces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )

#Define the colors used for the faces of the cube
colors = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def cube_faceless():
    """This function creates a faceless cube with colored edges."""
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

def cube_wfaces():
    """This function creates a cube with colored faces."""
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        glColor3fv(colors[i])
        for vertex in face:
            glColor3fv(colors[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()
    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertice in edge:
            glVertex3fv(vertices[vertice])
    glEnd()

def display():
    """This function call the OpenGL functions to actually display something."""
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    # Selecting the function to draw the cube
    if option=="-f" or option=="-f -c":
        cube_faceless()
    elif option=="-m" or option=="-m -c":
        cube_wfaces()
    glutSwapBuffers()

def timer(i):
    """This function creates a timer to automatically rotate the cube."""
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def keyboard(key, x, y):
    """This function creates keyboard controls for the user."""
    rotate_y = 0.0
    rotate_x = 0.0
    scale = 2.0
    # Rotate cube according to keys pressed
    if key == GLUT_KEY_RIGHT:
        rotate_y += 10
    if key == GLUT_KEY_LEFT:
        rotate_y -= 10
    if key == GLUT_KEY_UP:
        rotate_x += 10
    if key == GLUT_KEY_DOWN:
        rotate_x -= 10
    glutPostRedisplay()

def main():
    """This function acts as the main function of the program."""
    # This statement clear the screen.
    glutInit(sys.argv)
    # Create a double-buffer RGBA window.
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    # Uses GLUT to create a graphics window and gives the a size of it.
    glutInitWindowSize(800,600)
    # Set the title of the graphics window.
    glutCreateWindow("Cube")
    # The callback function for the graphics scene.
    glutDisplayFunc(display)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.,0.,0.,1.)
    gluPerspective(45,800.0/600.0,0.1,50.0)
    glTranslatef(0.0,0.0,-10)
    glRotatef(0,0,0,0)
    # Switching the rotation options for the cube.
    if option in {'-f -c','-f-c','-m -c','-m-c','-c -f','-c-f','-c -m','-c-m'}:
        # The callback function for keyboard controls.
        glutSpecialFunc(keyboard)
    else:
        # The callback function for the timer.
        glutTimerFunc(50,timer,1)
    # Run the GLUT main loop until the user closes the graphics window.
    glutMainLoop()

# Standard boilerplate to call the main function to begin the program.
if __name__ == '__main__':
    main()
