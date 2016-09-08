package dataProcess;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

import com.opencsv.CSVWriter;

public class location_week {

	public static void main(String[] args) throws IOException{
		File input = new File("Week_Location.csv");
		File output=new File("all.csv");
		
		BufferedReader bufRead = new BufferedReader(new FileReader(input));
		CSVWriter writer = new CSVWriter(new FileWriter(output),',',CSVWriter.NO_QUOTE_CHARACTER);
		
		List<String[]> title = new ArrayList<String[]>();
		title.add(new String[]{"Week","Year","Keyword match","Location","Count"});
		writer.writeAll(title);
		
		String ids = null;
		while((ids = bufRead.readLine())!=null){
			String[] str = ids.split(",");
			if(str[3].equals("Cumbria")||str[3].equals("Gateshead")||str[3].equals("Leicestershire")||str[3].equals("Lincolnshire")||str[3].equals("South Tyneside")||str[3].equals("Sunderland")){
				System.out.println("aa");
				List<String[]> data = new ArrayList<String[]>();
				data.add(str);
				writer.writeAll(data);
			}
			
		}
		writer.flush();
		bufRead.close();
		writer.close();
	}	
}
