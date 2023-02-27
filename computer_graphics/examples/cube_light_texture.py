#!/usr/bin/python
# -*- coding: utf-8 -*-
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *
import sys
import random

ESCAPE = '\033'

window = 0

xrot = yrot = zrot = 0.0
 
texture = []
 
def load_texture():
    """Load an image file as a 2D texture"""
    global texture
    texture = sys.argv[1]
    image = open(texture).read()
    ix = 256
    iy = 256
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, ix, iy, 0, GL_RGB, GL_UNSIGNED_BYTE, image)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)#GL_DECAL


def init(Width, Height):
    """An OpenGL initialization function."""""
    glClearColor(0.6,0.8,1.0,1.0)

    #mat_ambient = (0.0, 0.0, 0.5, 1.0)
    #mat_diffuse = (1.0, 1.0, 1.0, 1.0)
    #mat_specular = (0.0, 0.0, 0.5, 1.0)
    mat_ambient = (1.0, 1.0, 1.5, 1.0)
    mat_diffuse = (1.0, 1.0, 1.0, 1.0)
    mat_specular = (1.0, 1.0, 1.0, 1.0)
    mat_shininess = (50,)
    light_position = (0, 10, 10, 0.0)
 
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

    #Texturing the cube
    load_texture()
    glEnable(GL_TEXTURE_2D)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

def cube(): 
    """Draw a cube with texture coordinates"""
    global xrot, yrot, zrot
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()        
    glTranslatef(0.0,0.0,-5.0)  
    glRotatef(xrot,1.0,0.0,0.0)
    glRotatef(yrot,0.0,1.0,0.0)
    glRotatef(zrot,0.0,0.0,1.0) 
    glBegin(GL_QUADS);
    # Front Face
    glNormal3f(0.0, 0.0, 1.0)                               # Normal Pointing Front
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)    # Top Left Of The Texture and Quad     
    # Back Face
    glNormal3f(0.0, 0.0, -1.0)                              # Normal Pointing Back
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)    # Bottom Left Of The Texture and Quad   
    # Top Face
    glNormal3f(0.0, 1.0, 0.0)                               # Normal Pointing Top
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0,  1.0,  1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad    
    # Bottom Face
    glNormal3f(0.0, -1.0, 0.0)                              # Normal Pointing Bottom
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, -1.0, -1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0, -1.0, -1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad
    # Right face
    glNormal3f(1.0, 0.0, 0.0)                               # Normal Pointing Right
    glTexCoord2f(1.0, 0.0); glVertex3f( 1.0, -1.0, -1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f( 1.0,  1.0, -1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f( 1.0,  1.0,  1.0)    # Top Left Of The Texture and Quad
    glTexCoord2f(0.0, 0.0); glVertex3f( 1.0, -1.0,  1.0)    # Bottom Left Of The Texture and Quad   
    # Left Face
    glNormal3f(-1.0, 0.0, 0.0)                              # Normal Pointing Left
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)    # Bottom Left Of The Texture and Quad
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    # Bottom Right Of The Texture and Quad
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)    # Top Right Of The Texture and Quad
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0,  1.0, -1.0)    # Top Left Of The Texture and Quad   
    glEnd()
    
    xrot = xrot + 0.1
    yrot = yrot + 0.2
    zrot = zrot + 0.3
    
    glutSwapBuffers()
 
def reshape(Width,Height):
    """OpenGL function that enables to resize/reshape the scene whe the screen size changes"""
    if Height == 0:       # Prevent A Divide By Zero If The Window Is Too Small 
        Height = 1
    glViewport(0,0,Width,Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Calculate The Aspect Ratio Of The Window
    gluPerspective(60.0,float(Width)/float(Height),0.1,50.0)
    glMatrixMode(GL_MODELVIEW)

def key_pressed(*args):
    # If escape is pressed, kill everything.
    if args[0] == ESCAPE:
        sys.exit()
 
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Cubo")
    glutDisplayFunc(cube)
    glutIdleFunc(cube)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(key_pressed)
    init(800,600)
    glutMainLoop()
 
# Print message to console, and kick off the main to get it rolling.
if __name__ == "__main__":
    print "Hit ESC key to quit."
    main()
