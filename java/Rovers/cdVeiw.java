
/**
 * Write a description of class cdVeiw here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
import java.util.Scanner;
import java.util.ArrayList;
import objects.obj;
import objects.config;
public class cdVeiw implements veiwer
{
    private String help="To veiw the help tab, enter \"/help\"\nTo veiw the info tab, enter \"/info\"\nTo use the backup quit, enter \"/kill\"";
    private Scanner s;
    private String map;
    private game g;
    private boolean running=true;
    private String info="";
    public static void main(){
        cdVeiw main=new cdVeiw();
        main.start();
    }
    public cdVeiw(){
        s=new Scanner(System.in);
        g=new game(this);
    }
    public void start(){
        g.create();
        while(running){
            System.out.print(map);
            System.out.print(">");
            String comm=s.next();
            comm=comm.trim();
            if(comm.startsWith("/")){//A few special commands
                if(comm.equals("/kill")){
                    return;
                }
                else if(comm.equals("/info")){
                    System.out.println(info);
                }
                else if(comm.equals("/help")){
                    System.out.println(help);
                }
            }
            else{
                g.processCommand(comm);
            }
        }
    }
    public void notify(String note){
        System.out.println(note);
    }
    public void end(){
        running=false;
    }
    public String ask(String question){
        System.out.print(question);
        return s.next();
    }
    public void draw(ArrayList<obj> obs){
        map="";
        String [][] temp=new String[10][10];//Yeah, for now max map is 10X10
        ////Should probably set them all to .s here
        config cfg=objects.obj.get_config();
        for(int i=0; i<10; i++){
            for(int j=0; j<10; j++){
                temp[i][j]=".";//I think "....." is more clear than "     "
            }
        }
        //For the record, for the GUI I should look into AWT
        //Seems to be like tkinter, but in this case I will be working with java
        
        for(int i=0; i<obs.size(); i++){
            obj t=obs.get(i);
            int x=t.get_x()/cfg.get_scale();
            int y=t.get_y()/cfg.get_scale();
            if(0<=x&&x<=9&&0<=y&&y<=9){
                temp[x][y]=t.draw();
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
    public void update_info(String info){
        this.info=info;
        System.out.println("Info tab has been updated. Enter /info to veiw the info tab.");
    }
}
