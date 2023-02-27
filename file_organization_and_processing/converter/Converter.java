/**
  * File Name: 	Converter.java
  * Author: Lawrence Fernandes
  * This class reads an input.txt file containing numbers,
  * and calls the Converter.java class to convert them to different numerical bases.
  * The results are written in an output.txt file.
 */

//package converter;

import java.util.LinkedList;
import java.util.List;

public class Converter {
	public static List<String> converte(List<String> list) {
		List<String> listConverted = new LinkedList<>();
		String s = "", binary = "", hexadecimal = "", out = "";
		int decimal = 0;

		System.out.println();
		for (int i=0; i<list.size(); i++) {
			s = list.get(i);
			if(s!=null) {
				String[] field = s.trim().split("\\s+");
				if (field[0].equals("2")) {
					binary = field[1];
					decimal = Integer.parseInt(field[1], 2); // binary-decimal
					hexadecimal = Integer.toHexString(decimal);
				} else if (field[0].equals("10")) {
					decimal = Integer.parseInt(field[1], 10);
					binary = Integer.toBinaryString(decimal);
					hexadecimal = Integer.toHexString(decimal);
				} else if (field[0].equals("16")) {
					hexadecimal = field[1];
					decimal = Integer.parseInt(field[1], 16); // hexadecimal-decimal
					binary = Integer.toBinaryString(decimal);
				}
				out = hexadecimal + "\t" + decimal + "\t" + binary;
				listConverted.add(out);
				System.out.println(out);
			}
			else break;
		}
		return listConverted;
	}
}
