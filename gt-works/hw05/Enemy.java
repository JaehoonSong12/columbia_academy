// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents an enemy entity.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Enemy extends Entity {
    /** Whether this enemy can pierce armor. */
    private boolean canPierceArmor;

    /**
     * Constructs an enemy with all fields.
     *
     * @param name enemy name
     * @param health enemy health
     * @param canPierceArmor whether enemy pierces armor
     */
    public Enemy(String name, int health, boolean canPierceArmor) {
        super(name, health);
        this.canPierceArmor = canPierceArmor;
    }

    /**
     * Constructs an enemy that cannot pierce armor.
     *
     * @param name enemy name
     * @param health enemy health
     */
    public Enemy(String name, int health) {
        this(name, health, false);
    }

    /**
     * Returns whether this enemy can pierce armor.
     *
     * @return true if can pierce
     */
    public boolean canPierceArmor() {
        return canPierceArmor;
    }

    /**
     * Attacks a hero.
     * Deals 3 damage if hero has no armor or enemy can pierce,
     * otherwise deals 1 damage.
     *
     * @param h hero to attack
     */
    public void attack(Hero h) {
        if (!isAlive() || h == null) {
            return;
        }
        if (!h.hasArmor() || this.canPierceArmor) {
            h.takeDamage(3);
        } else {
            h.takeDamage(1);
        }
    }

    @Override
    public String toString() {
        String prefix = super.toString();
        if (isAlive()) {
            if (canPierceArmor) {
                return prefix + ". I am an enemy that can pierce armor";
            }
            return prefix + ". I am an enemy that cannot pierce armor";
        }
        return prefix + ". I was an enemy";
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
        Enemy other = (Enemy) obj;
        return this.canPierceArmor == other.canPierceArmor;
    }
}
