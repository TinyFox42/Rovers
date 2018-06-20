
/**
 * Write a description of class ball here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
package objects;
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
        //System.out.println(get_x());
        change_x(dx);
        //System.out.println(get_x());
        //System.out.println(dx);
        change_y(dy);
        System.out.println("The ball moves a bit.");
    }
    public String info(){
        String info=name+"\tID: "+get_id();
        info+="\n\t"+desc;
        info+="\n\tx:  "+get_x()+"\n\ty:  "+get_y();
        info+="\n\tdx: "+dx+"\n\tdy: "+dy;
        return info;
    }
}
