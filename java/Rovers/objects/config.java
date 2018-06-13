package objects;


/**
 * Handles config stuff
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.io.*;//Import stuff needed to read files
import java.util.regex.Matcher;
import java.util.regex.Pattern;//Stuff to make regexes work nicely
public class config{
    private int scale=10;
    public config(){
        String filename="config.txt";
        try{
            FileReader fileReader = new FileReader(filename);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line=null;
            while((line=bufferedReader.readLine())!=null){
                processLine(line);//This still needs to be coded
            }
            bufferedReader.close();
        }
        catch(FileNotFoundException ex){
            System.out.println("config.txt could not be opened. Switching to default values.");
            //useDefault();//Also needs to be coded
        }
        catch(IOException ex){
            System.out.println("config.txt could not be read. Switching to default values.");
            //useDefault();//Code this later on
        }
    }

    private void processLine(String line){
        if(line.matches("\\s*#.*")){
            //Ignore this line, #'s are comments
        }
        else{
            Pattern pattern=Pattern.compile("\\s*(\\w+)\\s*=\\s*(\\d+).*");
            Matcher matcher = pattern.matcher(line);
            if(!matcher.matches()){
                System.out.println("Invalid line found (use #'s to comment out lines in config).");
                System.out.println(line);
            }
            else{
                if(matcher.group(1).equals("scale")){
                    scale=Integer.parseInt(matcher.group(2));
                }//Other config stuff would go here
                else{
                    System.out.println("Invalid config setting found: "+matcher.group(1));
                }
            }
        }
    }
    public int get_scale(){
        return scale;
    }
}