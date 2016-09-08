
import java.io.IOException;
import java.util.HashMap;
import java.util.StringTokenizer;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Mapper.Context;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class CountMR {
	public static class TokenizerMapper extends Mapper<Object, Text, Text, Text>{
		private Text word = new Text();
		private Text pair = new Text();

		public void map(Object key, Text value, Context context
	             ) throws IOException, InterruptedException {
			//分隔text
			String[] list = value.toString().split(",");
			if(!list[0].equals("Week")){
				word.set(list[0]+","+list[1]);
				if(!list[2].equals("0")){
					pair.set(list[2]+";"+list[4]);
					context.write(word, pair);
				}
		    	pair.set(list[4]);
		    	context.write(word, pair);
			}
		}
	  }

	  public static class IntSumReducer
	       extends Reducer<Text,Text,Text,Text> {
		  private Text result = new Text();
			
		  public void reduce(Text key, Iterable<Text> values,Context context) throws IOException, InterruptedException {
			  //整合word count and twittes num
			  int total = 0;
			  HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
			  for (Text val : values) {
				  String str= val.toString();
				  if(!str.contains(";")){
					  total += Integer.parseInt(str);
				  }else{
					  String[] st = str.split(";");
					  int keys = Integer.parseInt(st[0]);
					  int value = Integer.parseInt(st[1]);
					  if(map.containsKey(keys))
						  map.put(keys, map.get(keys)+value);
					  else
						  map.put(keys, value);
				  }
			  }
			  String res = "";
			for(int keys: map.keySet()){
				res += keys+":"+map.get(keys)+";";
			}
			result.set(total+";"+res);
			context.write(key, result);	
	    }
	  }

	  public static void main(String[] args) throws Exception {
			Configuration conf = new Configuration();
			Job job = Job.getInstance(conf, "word count");
			job.setJarByClass(LocationMapReduce.class);
			job.setMapperClass(TokenizerMapper.class);
			
			job.setReducerClass(IntSumReducer.class);
			
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(Text.class);
			
			job.setMapOutputKeyClass(Text.class);
			job.setMapOutputValueClass(Text.class);
			
			FileInputFormat.addInputPath(job, new Path("all.csv"));
			FileOutputFormat.setOutputPath(job, new Path("all"));
			
			System.exit(job.waitForCompletion(true) ? 0 : 1);
		}
	
}
