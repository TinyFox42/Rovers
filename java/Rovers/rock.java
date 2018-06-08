
/**
 * A test object
 *
 * @Eli
 * @0.1
 */
public class rock extends obj
{
    private String name;
    private String desc;
    public rock(int x, int y){
        this(x, y, "Rock", "It is a rock");
    }
    public rock(int x, int y, String name, String desc){
        super(x, y);
        this.name=name;
        this.desc=desc;
    }
    public String desc(){
        return name;
    }
    public String name(){
        return desc;
    }
    public String draw(){
        return "*";
    }
    public void tick(){}
}
