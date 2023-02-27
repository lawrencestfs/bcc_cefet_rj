# File-Organization-and-Processing
Collection of algorithms related to file organization and processing.

## Bank

A simple banking program, developed with C and SQLite3.

## Converter

Converters written in C and Java between multiple numeral systems (binary, decimal and hexadecimal).

### Converter.c

The program reads an "input.txt" file containing two columns. The first column of the input file specifies the numeral system, while the second specifies the number that must be converted. After reading the file, the program converts the numbers to other numeral systems (binary, decimal and hexadecimal) and writes the result in an "output.txt" file. The program and the input file must be on the same folder/directory.

### FileIO.java and Converter.java 

These Java classes does the same thing of the C program forementioned. The FileIO class reads the "input.txt" file and writes to the "output.txt" file. It calls the Converter class to process the conversions, which in turn returns a List with the converted numbers. To run the program, execute FileIO.java through the terminal or your prefered IDE. The classes and the input file must be on the same folder/directory or package.

### input.txt

This is an example to be used with the Converter programs (works with both C and Java versions).

### diagram-conversor.png

This is a graphical representation of the behavior of the Converter.c program. The object oriented aproach from the Java version differs a little bit.
