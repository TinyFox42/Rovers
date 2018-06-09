
/**
 * Main file of the game, the controller
 *
 * @Eli
 * @0.1
 */
import java.util.ArrayList;
public class game
{
    private ArrayList<obj> map;
    private veiwer master;
    public game(veiwer master){
        this.master=master;
        map=new ArrayList();
    }
    public void create(){
        this.create(master.ask("Enter setup code:"));
    }
    public void create(String setup){
        //Later on, will create some stuff
        master.notify("Yeah... setup codes don't actually do anything yet...");
        master.draw(map);
    }
    public void processCommand(String command){
        //Later on, will actually make stuff
        if(command.equals("q")){
            master.end();
        }
    }
}
