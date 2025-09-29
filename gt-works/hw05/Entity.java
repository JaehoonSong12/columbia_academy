/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw05/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw05/Entity.java     # compile (.java to .class)
     java           -cp "./out"     Entity               # execute (.class to run)
     rm -rf out/                                        # clean up .class files

DEPENDENCIES:
 */

/**
 * This class is something.
 *
 * @author CS 1331 TAs
 * @version 1.0
 */
public abstract class Entity {
    private String name;

    /**
     * Getter for name.
     *
     * @return name of entity
     */
    public String getName() {
        return this.name;
    }

    /**
     * Setter for name.
     *
     * @param name name of entity
     */
    public void setName(String name) {
        this.name = name;
    }

    private int health;

    /**
     * Getter for health.
     *
     * @return health of entity
     */
    public int getHealth() {
        return this.health;
    }

    /**
     * Setter for health.
     *
     * @param health health of entity
     */
    private void setHealth(int health) {
        if (health < 0) {
            this.health = 0;
        } else {
            this.health = health;
        }
    }

    /**
     * Method to check if entity is alive.
     *
     * @return true if entity is alive, false otherwise
     */
    public boolean isAlive() {
        return this.getHealth() > 0;
    }

    /**
     * Reduces the entity's health by a given amount of damage.
     * Health will not drop below 0.
     *
     * @param damage The amount of damage to take.
     */
    public void takeDamage(int damage) {
        this.setHealth(this.health - damage);
    }

    /**
     * Method to heal entity.
     *
     * @param amount amount The amount of health to restore.
     */
    public void heal(int amount) {
        // The entity may only gain health if it’s alive and the parameter is positive.
        if (this.isAlive() && amount > 0) {
            this.setHealth(this.getHealth() + amount);
        }
    }

    /**
     * Constructor for Entity.
     *
     * @param name   name of entity
     * @param health health of entity
     */
    public Entity(String name, int health) { // 2arg constructor
        this.name = name;
        this.setHealth(health);
    }

    @Override public String toString() {
        if (this.isAlive()) {
            return String.format("I am %s, and I have %s health.", this.getName(), this.getHealth());
        } else {
            return String.format("I was %s", this.getName());
        }
    }

    @Override public boolean equals(Object obj) {
        Entity other;
        if (this == obj) {
            return true;
        }
        if (obj instanceof Entity) {
            other = (Entity) obj;
        } else {
            return false;
        }
        return this.getHealth() == other.getHealth() && this.getName().equals(other.getName());
    }
}
