
/**
 * Main file of the game, the controller
 *
 * @Eli
 * @0.1
 */
import java.util.ArrayList;
import objects.*;
/*import java.util.regex.Matcher;
import java.util.regex.Pattern;//Stuff to make regexes work nicely*/
import java.util.Arrays;
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
        //Pattern comm_finder=Pattern.compile("\\s*(\\w+)\\s*(.*)");
        //Matcher finder=comm_finder.matcher(command);
        
        /*if(!finder.matches()){
            master.notify("Invalid command format");
            return;
        }
        String op=finder.group(1);
        String mods=finder.group(2);*/
        String [] parts=command.split(" ");
        String op=parts[0];
        String mods=String.join(" ", Arrays.copyOfRange(parts, 1, parts.length));
        System.out.println(op);
        switch (op){
            case "q": master.end();
                break;
            case "t":tick();
                master.draw(map);
                break;
            case "list":list(mods);
                break;
            case "veiw":veiw(mods);
                break;
            default: master.notify("Unrecognized command '"+op+"'.");
                break;
        }//*/
        if(command.equals("kill")){
            master.end();
        }
    }
    private void list(String mods){
        String info="";
        for(obj thing: map){
            info+=thing.name()+"\tID: "+thing.get_id();
            info+="\n";
        }
        //System.out.print(info);//Later on, put this somewhere in veiwer
        master.update_info(info);
    }
    private void veiw(String mods){
        String [] ids=mods.split(" ");
        String info="";
        for(int i=0; i<ids.length; i++){
            String temp=ids[i];
            //later on: put in some checks that it is acually a number
            if(temp.equals("")){
                continue;
            }
            int id=Integer.parseInt(temp);
            obj thing;
            boolean looking=true;
            for(int j=0; looking&&j<map.size(); j++){
                obj curr=map.get(j);
                if(curr.get_id()==id){
                    looking=false;
                    thing=curr;
                    info+=thing.info();
                }
            }
            if(looking){
                info+="Object with ID "+id+" could not be found.";
            }
        }
        master.update_info(info);
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
