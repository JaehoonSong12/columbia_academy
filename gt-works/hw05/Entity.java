// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents an abstract entity in the world with a name and health.
 *
 * @author Tai Park
 * @version 1.0
 */
public abstract class Entity {

    private String name;
    private int health;

    /**
     * Constructs an entity with the given name and health.
     * If health is less than 0, it is set to 0.
     *
     * @param name the entity's name
     * @param health the entity's health
     */
    public Entity(String name, int health) {
        this.name = name;
        setHealth(health);
    }

    /**
     * Returns the name of the entity.
     *
     * @return the entity's name
     */
    public String getName() {
        return name;
    }

    /**
     * Returns the health of the entity.
     *
     * @return the entity's health
     */
    public int getHealth() {
        return health;
    }

    /**
     * Sets the entity's name.
     *
     * @param name the new name
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * Sets the entity's health (private).
     * If the value is negative, sets health to 0.
     *
     * @param health the new health value
     */
    private void setHealth(int health) {
        if (health < 0) {
            this.health = 0;
        } else {
            this.health = health;
        }
    }

    /**
     * Returns whether the entity is alive.
     *
     * @return true if alive, false if dead
     */
    public boolean isAlive() {
        return this.health > 0;
    }

    /**
     * Reduces the entity's health by the given damage.
     * Health cannot go below 0.
     *
     * @param damage the amount of damage
     */
    public void takeDamage(int damage) {
        int newHealth = this.health - damage;
        setHealth(newHealth);
    }

    /**
     * Increases the entity's health if alive and amount is positive.
     *
     * @param amount amount to heal
     */
    public void heal(int amount) {
        if (amount > 0 && isAlive()) {
            int newHealth = this.health + amount;
            setHealth(newHealth);
        }
    }

    @Override
    public String toString() {
        if (isAlive()) {
            return "I am " + name + ", and I have " + health + " health";
        } else {
            return "I was " + name;
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || this.getClass() != obj.getClass()) {
            return false;
        }
        Entity other = (Entity) obj;
        if (this.health != other.health) {
            return false;
        }
        if (this.name == null) {
            return other.name == null;
        }
        return this.name.equals(other.name);
    }
}
