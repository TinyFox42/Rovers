
/**
 * Main file of the game, the controller
 *
 * @Eli
 * @0.1
 */
import java.util.ArrayList;
import java.util.Hashtable;
public class game
{
    private ArrayList<obj> obs;
    private Hashtable<Integer, Hashtable<Integer, obj>> map;
    private veiwer master;
    public game(veiwer master){
        this.master=master;
        obs=new ArrayList();
    }
    public void create(){
        this.create(master.ask("Enter setup code:"));
    }
    public void create(String setup){
        //Later on, will create some stuff
        //master.notify("Yeah... setup codes don't actually do anything yet...");
        if(setup.equals("1")){
            obj rocky=new rock(5,5);
            add(rocky);
        }
        master.draw(obs);
    }
    public void processCommand(String command){
        //Later on, will actually make stuff
        if(command.equals("q")){
            master.end();
        }
        else if(command.equals("t")){
            tick();
        }
    }
    private void add(obj thing){
        obs.add(thing);
    }
    private void tick(){
        for(obj thing: obs){
            thing.tick();
        }
    }
}
