[teapot]:images/teapot.png

# Computer Graphics

This repository is dedicated to the works I've developed in the Computer Graphics course from CEFET/RJ.
It contains examples and applications developed using Python, OpenGL, GLUT and PyOpenGL.

## Setup

On a Ubuntu machine, run the following command to install OpenGL:

```
sudo apt-get install freeglut3-dev
```

Then, install PyOpenGL with the following command:

```
pip install PyOpenGL PyOpenGL_accelerate
```

## plotlety
[Plotlety](https://github.com/lawrencestfs/plotlety) is a very simple pure Python math graphics plotter capable of drawing 2D and 3D graphics. It requires PyOpenGL and numpy.

## Examples

### Teapot
Draws a teapot using the built-in `WiredTeapot` function from OpenGL.

![teapot]

### Cube
Draws a cube with its faces (polygon mesh) or without them.
The cube is rotated on the screen. It can be done automatically or by the user, deppending on the arguments the program takes.