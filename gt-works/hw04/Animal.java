// Collaboration Statement: I worked on the homework assignment alone, using only course materials.
// java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw04/*.java

public class Animal {
    private String species;
    private String name;
    private int energy;
    private int health;
    private static int numberOfAnimals = 0;

    public Animal(String species, String name, int energy, int health) {
        this.species = species;
        this.name = name;
        setEnergy(energy);
        setHealth(health);
        numberOfAnimals++;
    }

    public Animal(String species, String name) {
        this(species, name, 50, 100);
    }

    public Animal(String name) {
        this("Unknown", name, 50, 100);
    }

    public String getSpecies() {
        return species;
    }

    public String getName() {
        return name;
    }

    public int getEnergy() {
        return energy;
    }

    public int getHealth() {
        return health;
    }

    public static int getNumberOfAnimals() {
        return numberOfAnimals;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setEnergy(int energy) {
        int e = energy;
        if (e < 1) {
            e = 1;
        } else if (e > 100) {
            e = 100;
        }
        this.energy = e;
    }

    public void setHealth(int health) {
        int h = health;
        if (h < 1) {
            h = 1;
        } else if (h > 100) {
            h = 100;
        }
        this.health = h;
    }

    public void eat(int food) {
        setEnergy(this.energy + 2 * food);
    }

    public void doActivity(int duration, boolean dangerous) {
        setEnergy(this.energy - 5 * duration);
        if (dangerous) {
            setHealth(this.health - 3 * duration);
        }
    }

    public void goToZooHospital() {
        setHealth(100);
        if (energy < 60) {
            setEnergy(60);
        }
    }

    /**
     * Returns a boolean value of whether the animal is hungry depending on the energy level.
     *
     * @return boolean value of (energy < 50)
     *
     */
    public boolean isHungry() {
        return energy < 50;
    }

    @Override
    public String toString() {
        return "I am " + species + " " + name + ". I have " + energy
                + " energy and " + health + " health";
    }
}
