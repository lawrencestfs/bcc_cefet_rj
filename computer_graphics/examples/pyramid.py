from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys


def pyramid():
    glColor3fv((0,0,1))
    glutSolidCone(2,3,sidesInBase,1);
    glColor3fv((1,1,1))
    glutWireCone(2,3,sidesInBase,1);    

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,1,2)
    pyramid()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def mouse(button,state,x,y):
    global sidesInBase	
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
    	sidesInBase += 1
    if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
	sidesInBase -= 1	

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Cubo")
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()
sidesInBase=4
main()