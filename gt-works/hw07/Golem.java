// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

/**
 * Class representing a Golem troop.
 *
 * @author Tai Park
 * @version 1.0
 */
public class Golem extends Troop {
    private int weight;

    /**
     * Constructs a Golem with given parameters.
     *
     * @param name name
     * @param experienceLevel experience level
     * @param health health
     * @param weight weight in tons
     */
    public Golem(String name, int experienceLevel, int health, int weight) {
        super(name, experienceLevel, health);
        this.weight = weight;
    }

    /**
     * Default constructor for Golem.
     */
    public Golem() {
        this("Nelly", 19, 80, 10);
    }

    /**
     * Gets weight.
     *
     * @return weight
     */
    public int getWeight() {
        return weight;
    }

    /**
     * Sets weight.
     *
     * @param weight weight
     */
    public void setWeight(int weight) {
        this.weight = weight;
    }

    @Override
    public void trainWith(Troop p) {
        if (getHealth() < 15 || getHealth() == 100
                || getExperienceLevel() == 50
                || !(p instanceof Golem)) {
            return;
        }
        Golem other = (Golem) p;
        setExperienceLevel(getExperienceLevel() + 3);
        other.setExperienceLevel(other.getExperienceLevel() + 3);
        setHealth(getHealth() - 12);
        other.setHealth(other.getHealth() - 12);
    }

    @Override
    public String toString() {
        return super.toString() + ". I am a golem that weighs " + weight + " tons";
    }

    @Override
    public boolean equals(Object obj) {
        if (!super.equals(obj)) {
            return false;
        }
        if (!(obj instanceof Golem)) {
            return false;
        }
        Golem other = (Golem) obj;
        return weight == other.weight;
    }
}
