
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
        String [][] temp=new String[10][10];//Yeah, for now max map is 10X10
        ////Should probably set them all to .s here
        for(int i=0; i<10; i++){
            for(int j=0; j<10; j++){
                temp[i][j]=" ";
            }
        }
        //For the record, for the GUI I should look into AWT
        //Seems to be like tkinter, but in this case I will be working with java
        for(int i=0; i<obs.size(); i++){
            obj t=obs.get(i);
            if(0<=t.get_x()&&t.get_x()<=9&&0<=t.get_y()&&t.get_y()<=9){
                temp[t.get_y()][t.get_x()]=t.draw();
            }
            else{
                System.out.println("Something is out of bounds");
            }
        }
        for(int i=0; i<10; i++){
            for(int j=0; j<10; j++){
                map+=temp[i][j];
            }
            map+="\n";
        }
    }
}
