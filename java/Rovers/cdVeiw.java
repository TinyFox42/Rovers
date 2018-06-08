
/**
 * Write a description of class cdVeiw here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
import java.util.ArrayList;
public class cdVeiw implements veiwer
{
    private Scanner s;
    private String map;
    private game g;
    private boolean running=true;
    public cdVeiw(String [] args){
        s=new Scanner(System.in);
        g=new game(this);
    }
    public void notify(String note){
        System.out.println(note);
    }
    public void end(){
        running=false;
    }
    public String ask(String question){
        System.out.println(question);
        return s.next();
    }
    public void draw(ArrayList<obj> obs){
        map="";
        ArrayList<ArrayList<String>> temp=new ArrayList();
        temp.add(new ArrayList());
        for(int i=0; i<obs.size(); i++){
            obj t=obs.get(i);
            int x=t.get_x();
            
        }
    }
}
