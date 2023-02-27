#!/usr/bin/python
# -*- coding: utf-8 -*-
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    #glClearColor(0.5, 0.8, 0.3, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    #glColor3ub(red, green, blue)
    # where ub stands for unsigned byte 
    #In this case, the color values range from 0-255
    glPointSize(2.0)
    glLineWidth(3.0)
    #glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    # First triagle
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(1.0, 1.0, 0.0)
    glVertex2f(0.5, -0.5)
    # Second triagle
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(0.5, 0.5)
    #glColor3f(0.0, 0.0, 1.0)
    # End
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Polygons")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
