// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents an archer hero with optional armor.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Archer extends Hero {

    private boolean hasArmorEquipped;

    /**
     * Constructs an archer with all fields.
     *
     * @param name archer name
     * @param health archer health
     * @param damage archer damage
     * @param hasArmorEquipped whether armor is equipped
     */
    public Archer(String name, int health, int damage, boolean hasArmorEquipped) {
        super(name, health, damage);
        this.hasArmorEquipped = hasArmorEquipped;
    }

    /**
     * Constructs an archer with 4 damage and no armor.
     *
     * @param name archer name
     * @param health archer health
     */
    public Archer(String name, int health) {
        this(name, health, 4, false);
    }

    /**
     * Constructs an archer with 20 health, 4 damage, no armor.
     *
     * @param name archer name
     */
    public Archer(String name) {
        this(name, 20);
    }

    /**
     * Equips armor if alive.
     */
    public void equipArmor() {
        if (isAlive()) {
            this.hasArmorEquipped = true;
        }
    }

    /**
     * Unequips armor if alive.
     */
    public void unequipArmor() {
        if (isAlive()) {
            this.hasArmorEquipped = false;
        }
    }

    @Override
    public void train(TrainingGround tg) {
        if (tg == null) {
            return;
        }
        if (!tg.isOutdoors()) {
            return;
        }
        int increase = (int) (3 * tg.getTrainingMultiplier());
        increaseDamage(increase);
    }

    @Override
    public boolean hasArmor() {
        return hasArmorEquipped;
    }

    @Override
    public String toString() {
        String heroPrefix = super.toString();
        if (isAlive()) {
            if (hasArmorEquipped) {
                return heroPrefix + ". I am an archer with my armor equipped";
            }
            return heroPrefix + ". I am an archer with my armor unequipped";
        }
        return heroPrefix + ". I was an archer";
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
        Archer other = (Archer) obj;
        return this.hasArmorEquipped == other.hasArmorEquipped;
    }
}
