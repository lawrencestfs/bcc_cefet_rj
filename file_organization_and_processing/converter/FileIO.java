/**
  * File Name: 	FileIO.java
  * Author: Lawrence Fernandes
  * This class reads an input.txt file containing numbers,
  * and calls the Conversor.java class to convert them to different numerical bases.
  * The results are written in an output.txt file.
 */

//package conversor; 

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.nio.charset.Charset;
import java.util.LinkedList;
import java.util.List;

public class FileIO {
	public static void main(String[] args) {
		List<String> lista = new LinkedList<>();
		try {
			BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("input.txt")));
			String s = br.readLine();
			lista.add(s);
			while (s != null) {
				System.out.println(s);
				s = br.readLine();
				lista.add(s);
			}
			br.close();
			
		} catch (FileNotFoundException e) {
			System.out.println(e.getMessage());
			
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
		
		List<String> listaConvertida = Conversor.converte(lista);
		
		try {
			//OutputStream os = new FileOutputStream("output.txt");
			//OutputStreamWriter osw = new OutputStreamWriter(os);
			//BufferedWriter bw = new BufferedWriter(osw);
			FileWriter charectersname = new FileWriter("output.txt");
			BufferedWriter out = new BufferedWriter(charectersname);
			
			for(int i = 0; i<listaConvertida.size(); i++) {
				String str = listaConvertida.get(i); 
				out.write(str);
				out.newLine();
			}
			out.close();
			
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}
	}
}
