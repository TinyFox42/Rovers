
/**
 * Write a description of class ball here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class ball extends obj
{
    private String name;
    private String desc;
    private int dx;
    private int dy;
    public ball(int x, int y){
        this(x, y, "Ball", "It rolls very easily.");
    }
    public ball(int x, int y, String name, String desc){
        this(x, y, name, desc, 0, 0);
    }
    public ball(int x, int y, String name, String desc, int dx, int dy){
        super(x, y);
        this.name=name;
        this.desc=desc;
        this.dx=dx;
        this.dy=dy;
    }
    public String desc(){
        return desc;
    }
    public String name(){
        return name;
    }
    public String draw(){
        return "o";
    }
    public void tick(){
        change_x(dx);
        change_y(dy);
    }
}
