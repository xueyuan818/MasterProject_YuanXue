package finaltest;

import java.io.BufferedReader;
import java.io.BufferedWriter;
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

public class Normalization {
	static Map<String, TreeMap<Integer,Integer>> map = new TreeMap<String,TreeMap<Integer,Integer>>();
	public static void main(String[] args) throws IOException{
		File input = new File("all/part-r-00000");
		File output = new File("all_prim.csv");
		BufferedReader bufRead = new BufferedReader(new FileReader(input));
		CSVWriter bufWrite = new CSVWriter(new FileWriter(output));
		
		HashMap<String,Integer> counts = total_count_per_week.readfile();
		
		String ids = null;
		List<String[]> title = new ArrayList<String[]>();
		title.add(new String[]{"Week","Year","Total_count","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100","101","102","103","104","105","106","107","108","109","110","111","112","113","114","115","116","117","118","119","120","121","122","123","124","125","126","127","128","129","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","148","149","150","151","152","153","154","155","156","157","158","159","160","161","162","163","164","165","166","167","168","169","170","171","172","173","174","175","176","177","178","179","180","181","182","183","184","185","186","187","188","189","190","191","192","193","194","195","196","197","198","199","200","201","202","203","204","205","206","207","208","209","210","211","212","213","214","215","216","217"});
		bufWrite.writeAll(title);
		while((ids = bufRead.readLine())!=null){
			String[] list = ids.split("\t| ");
			String[] week_year = list[0].split(",");
			if(counts.containsKey(list[0])){
				
				int week = Integer.parseInt(week_year[0]);
				int year = Integer.parseInt(week_year[1]);
				
				String[] n_gram = list[1].split(";");
				
//				double total_count = counts.get(list[0])*1.0;
				double total_count = Integer.parseInt(n_gram[0]);
				
				Map<Integer,Double> count_total = new TreeMap<Integer,Double>();
				for(int i=1;i<n_gram.length;i++){
					String[] key_count = n_gram[i].split(":");
					int key = Integer.parseInt(key_count[0]);
					int count = Integer.parseInt(key_count[1]);
					if(count_total.containsKey(key))
						count_total.put(key, count_total.get(key)+count*1.0/total_count);
//						count_total.put(key, count_total.get(key)+count*1.0);
					else
						count_total.put(key, count*1.0/total_count);
//						count_total.put(key, count*1.0);
				}
				for(int i=1;i<218;i++){
					if(!count_total.containsKey(i)){
						count_total.put(i, 0.0);
					}
				}
				String str = week+","+year+","+total_count+",";
				for(int key: count_total.keySet()){
					str += count_total.get(key)+",";
				}
				String[] al= str.split(",");
				List<String[]> data = new ArrayList<String[]>();
				data.add(al);
				bufWrite.writeAll(data);
				bufWrite.flush();
			}
		}
		bufRead.close();
		bufWrite.close();
		//输出格式 date total_number 0count；1coutn;2count......217count
		
		
	}

}
