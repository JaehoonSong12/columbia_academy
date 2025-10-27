// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

/**
 * Class representing a Barbarian troop.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Barbarian extends Troop implements Treatable {
    private final boolean isElite;

    /**
     * Constructs a Barbarian with given parameters.
     *
     * @param name name
     * @param experienceLevel experience level
     * @param health health
     * @param isElite elite status
     */
    public Barbarian(String name, int experienceLevel, int health, boolean isElite) {
        super(name, experienceLevel, health);
        this.isElite = isElite;
    }

    /**
     * Constructs a Barbarian with only elite status.
     *
     * @param isElite elite status
     */
    public Barbarian(boolean isElite) {
        this("Buzz", 1, 25, isElite);
    }

    /**
     * Returns elite status.
     *
     * @return true if elite
     */
    public boolean isElite() {
        return isElite;
    }

    @Override
    public void trainWith(Troop p) {
        if (getHealth() < 10 || getHealth() == 100
                || getExperienceLevel() == 50
                || !(p instanceof Barbarian || p instanceof Archer)) {
            return;
        }

        if (p instanceof Barbarian) {
            Barbarian other = (Barbarian) p;
            int damage = (int) (0.1 * other.getExperienceLevel());
            int oldHealth = getHealth();
            setHealth(getHealth() - damage);
            System.out.println("AAAARGH! I just trained with a level "
                + other.getExperienceLevel() + " barbarian, and my health went from "
                + oldHealth + " to " + getHealth());
            int expIncrease = (isElite || other.isElite()) ? 8 : 5;
            setExperienceLevel(getExperienceLevel() + expIncrease);
            other.setExperienceLevel(other.getExperienceLevel() + expIncrease);
            other.setHealth(other.getHealth() - damage);
        } else if (p instanceof Archer) {
            Archer archer = (Archer) p;
            if ("purple".equalsIgnoreCase(archer.getHairColor())) {
                int oldHealth = getHealth();
                setHealth(getHealth() + 10);
                System.out.println("YAAARG. My health increased from "
                    + oldHealth + " to " + getHealth());
                setExperienceLevel(getExperienceLevel() + 1);
                archer.setExperienceLevel(archer.getExperienceLevel() + 1);
            } else {
                setHealth(getHealth() - 15);
                System.out.println("AAAARGH! I hate that color!");
            }
        }
    }

    @Override
    public void treat() {
        setHealth(getHealth() + 5);
    }

    @Override
    public boolean needsTreatment() {
        return getHealth() < 100;
    }

    /**
     * Barbarian screams.
     */
    public void scream() {
        System.out.println("AAAARGH!");
    }

    @Override
    public String toString() {
        String base = super.toString();
        if (isElite) {
            return base + ". I am an elite barbarian";
        }
        return base + ". I am a regular barbarian";
    }

    @Override
    public boolean equals(Object obj) {
        if (!super.equals(obj)) {
            return false;
        }
        if (!(obj instanceof Barbarian)) {
            return false;
        }
        Barbarian other = (Barbarian) obj;
        return isElite == other.isElite;
    }
}
