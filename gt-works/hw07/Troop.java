// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

/**
 * Abstract class representing a troop.
 *
 * @author Tai Park
 * @version 1.0
 */
public abstract class Troop {
    private String name;
    private int experienceLevel;
    private int health;

    /**
     * Constructs a Troop with the given parameters.
     *
     * @param name name of the troop
     * @param experienceLevel experience level (bounded 1–50)
     * @param health health value (bounded 1–100)
     */
    public Troop(String name, int experienceLevel, int health) {
        setName(name);
        setExperienceLevel(experienceLevel);
        setHealth(health);
    }

    /**
     * Gets the name of this troop.
     *
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * Sets the name of this troop.
     *
     * @param name new name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Gets the experience level.
     *
     * @return the experience level
     */
    public int getExperienceLevel() {
        return experienceLevel;
    }

    /**
     * Sets the experience level (bounded 1–50).
     *
     * @param experienceLevel new experience level
     */
    public void setExperienceLevel(int experienceLevel) {
        if (experienceLevel < 1) {
            this.experienceLevel = 1;
        } else if (experienceLevel > 50) {
            this.experienceLevel = 50;
        } else {
            this.experienceLevel = experienceLevel;
        }
    }

    /**
     * Gets the health.
     *
     * @return the health
     */
    public int getHealth() {
        return health;
    }

    /**
     * Sets the health (bounded 1–100).
     *
     * @param health new health
     */
    public void setHealth(int health) {
        if (health < 1) {
            this.health = 1;
        } else if (health > 100) {
            this.health = 100;
        } else {
            this.health = health;
        }
    }

    /**
     * Abstract method for training with another troop.
     *
     * @param p the other troop
     */
    public abstract void trainWith(Troop p);

    @Override
    public String toString() {
        return "My name is " + name + ", my experience level is "
            + experienceLevel + ", and my health is " + health;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj == this) {
            return true;
        }
        if (!(obj instanceof Troop)) {
            return false;
        }
        Troop other = (Troop) obj;
        return name.equals(other.name)
            && experienceLevel == other.experienceLevel
            && health == other.health;
    }
}
