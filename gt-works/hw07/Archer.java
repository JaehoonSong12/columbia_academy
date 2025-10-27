// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

/**
 * Class representing an Archer troop.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Archer extends Troop implements Treatable {
    private String hairColor;

    /**
     * Constructs an Archer with all parameters.
     *
     * @param name name
     * @param experienceLevel experience level
     * @param health health
     * @param hairColor hair color
     */
    public Archer(String name, int experienceLevel, int health, String hairColor) {
        super(name, experienceLevel, health);
        this.hairColor = hairColor;
    }

    /**
     * Constructs an Archer with hair color only.
     *
     * @param hairColor hair color
     */
    public Archer(String hairColor) {
        this("Sally", 10, 15, hairColor);
    }

    /**
     * Gets hair color.
     *
     * @return hair color
     */
    public String getHairColor() {
        return hairColor;
    }

    /**
     * Sets hair color.
     *
     * @param hairColor hair color
     */
    public void setHairColor(String hairColor) {
        this.hairColor = hairColor;
    }

    @Override
    public void trainWith(Troop p) {
        if (getHealth() < 5 || getHealth() == 100
                || getExperienceLevel() == 50
                || !(p instanceof Barbarian || p instanceof Archer)) {
            return;
        }

        if (p instanceof Archer) {
            Archer other = (Archer) p;
            boolean sameColor = hairColor.equalsIgnoreCase(other.getHairColor());
            if (sameColor) {
                System.out.println("I like training with other archers with the same hair color as me");
                setExperienceLevel(getExperienceLevel() + 4);
                other.setExperienceLevel(other.getExperienceLevel() + 4);
            } else {
                System.out.println("Oof! I prefer training with other archers with the same hair color as me");
                setExperienceLevel(getExperienceLevel() + 2);
                other.setExperienceLevel(other.getExperienceLevel() + 2);
            }
            setHealth(getHealth() - 5);
            other.setHealth(other.getHealth() - 5);
        } else if (p instanceof Barbarian) {
            Barbarian barb = (Barbarian) p;
            setHealth(getHealth() - 10);
            System.out.println("Gross. Go away " + barb.getName() + "! I hate training with Barbarians!");
        }
    }

    @Override
    public void treat() {
        setHealth(getHealth() + 3);
    }

    @Override
    public boolean needsTreatment() {
        return getHealth() < 80;
    }

    @Override
    public String toString() {
        return super.toString() + ". I am an archer with " + hairColor + " hair";
    }

    @Override
    public boolean equals(Object obj) {
        if (!super.equals(obj)) {
            return false;
        }
        if (!(obj instanceof Archer)) {
            return false;
        }
        Archer other = (Archer) obj;
        return hairColor.equals(other.hairColor);
    }
}
