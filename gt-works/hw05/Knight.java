// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents a knight hero.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Knight extends Hero {

    /**
     * Constructs a knight with name, health, and damage.
     *
     * @param name knight name
     * @param health knight health
     * @param damage knight damage
     */
    public Knight(String name, int health, int damage) {
        super(name, health, damage);
    }

    /**
     * Constructs a knight with damage 2.
     *
     * @param name knight name
     * @param health knight health
     */
    public Knight(String name, int health) {
        this(name, health, 2);
    }

    /**
     * Constructs a knight with default health 40 and damage 2.
     *
     * @param name knight name
     */
    public Knight(String name) {
        this(name, 40);
    }

    @Override
    public void train(TrainingGround tg) {
        if (tg == null) {
            return;
        }
        int increase = (int) (5 * tg.getTrainingMultiplier());
        increaseDamage(increase);
    }

    @Override
    public boolean hasArmor() {
        return true;
    }

    @Override
    public String toString() {
        String heroPrefix = super.toString();
        if (isAlive()) {
            return heroPrefix + ". I am a knight";
        }
        return heroPrefix + ". I was a knight";
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }
}
