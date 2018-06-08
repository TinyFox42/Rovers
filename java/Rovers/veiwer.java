
/**
 * Interface class for the UI, which will be what the user actually selects to start up
 * So that I don't have to redo a lot of flow to remake this with fancy GUI
 *
 * @Eli
 * @0.1
 */
import java.util.ArrayList;
public interface veiwer
{
    void draw(ArrayList<obj> obs);//Remakes the map view
    String ask(String question);//For the game to be able to ask for a response to a question
    void end();//Tells the UI that it is safe to end the game
    void notify(String message);//For some other popup
}
