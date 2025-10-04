// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents an abstract hero with damage capability.
 *
 * @author Tai Park
 * @version 1.0
 */
public abstract class Hero extends Entity {

    private int damage;

    /**
     * Constructs a hero with name, health, and damage.
     * If damage < 0, sets to 0.
     *
     * @param name hero name
     * @param health hero health
     * @param damage hero damage
     */
    public Hero(String name, int health, int damage) {
        super(name, health);
        this.damage = Math.max(0, damage);
    }

    /**
     * Constructs a hero with default damage of 1.
     *
     * @param name hero name
     * @param health hero health
     */
    public Hero(String name, int health) {
        this(name, health, 1);
    }

    /**
     * Returns damage dealt by hero.
     *
     * @return damage value
     */
    public int getDamage() {
        return damage;
    }

    /**
     * Increases damage if hero is alive.
     *
     * @param amount amount to increase
     */
    protected void increaseDamage(int amount) {
        if (amount > 0 && isAlive()) {
            this.damage += amount;
        }
    }

    /**
     * Abstract method to train hero.
     *
     * @param tg training ground
     */
    public abstract void train(TrainingGround tg);

    /**
     * Abstract method to check armor.
     *
     * @return true if hero has armor
     */
    public abstract boolean hasArmor();

    /**
     * Hero attacks an enemy, if alive.
     *
     * @param enemy target enemy
     */
    public void attack(Enemy enemy) {
        if (isAlive() && enemy != null) {
            enemy.takeDamage(this.damage);
        }
    }

    @Override
    public String toString() {
        String prefix = super.toString();
        if (isAlive()) {
            return prefix + ". I deal " + damage + " damage";
        }
        return prefix;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || this.getClass() != obj.getClass()) {
            return false;
        }
        if (!super.equals(obj)) {
            return false;
        }
        Hero other = (Hero) obj;
        return this.damage == other.damage;
    }
}
