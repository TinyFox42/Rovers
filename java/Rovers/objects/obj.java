
/**
 * Abstract class for everything on the map
 *
 * @Eli
 * @0.1
 */
package objects;
public abstract class obj
{
   private int x;
   private int y;
   static int nextId=0;
   private int id;
   public obj(int x, int y){
       this.x=x;
       this.y=y;
       id=nextId;
       nextId++;
    }
   public int get_x(){
       return x;
    }
   public int get_y(){
       return y;
    }
   public abstract void tick();
   public abstract String draw();//returns the sprite to show
   public abstract String name();//gives the name of the object
   public abstract String desc();//returns the full description of the object
   public void change_x(int delta){
       x+=delta;
    }
   public void change_y(int delta){
       y+=delta;
    }
}
