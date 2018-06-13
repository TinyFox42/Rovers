
/**
 * Main file of the game, the controller
 *
 * @Eli
 * @0.1
 */
import java.util.ArrayList;
import objects.*;
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
        //master.notify("Yeah... setup codes don't actually do anything yet...");
        if(setup.equals("1")){
            obj rocky=new rock(5,5);
            add(rocky);
            obj ball=new ball(3,3,"Ball","It rolls *very* easily.",1,-1);
            add(ball);
        }
        master.draw(map);
    }
    public void processCommand(String command){
        //Later on, will actually make stuff
        /*
        if(command.equals("q")){
            master.end();
        }
        else if(command.equals("t")){
            tick();
            master.draw(map);//Tells the UI to update the display
        }*/
        ///*
        switch (command){
            case "q": master.end();
                break;
            case "t":tick();
                master.draw(map);
                break;
        }//*/
        if(command.equals("kill")){
            master.end();
        }
    }
    private void add(obj thing){
        map.add(thing);
    }
    private void tick(){
        for(obj thing: map){
            thing.tick();
        }
    }
}
