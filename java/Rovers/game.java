
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
    }
    public void create(String setup){
        //Later on, will create some stuff
        master.draw(map);
    }
    public void processCommand(String command){
        //Later on, will actually make stuff
    }
}
