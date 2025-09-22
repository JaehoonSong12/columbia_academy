/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw04/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw04/Animal.java    # compile (.java to .class)
     java           -cp "./out"     Animal              # execute (.class to run)
     rm -rf out/                                        # clean up .class files

DEPENDENCIES:
 */






// Animal
// It represents animals in the zoo. The class will have:
// - The following instance variables: species (String), name (String), energy (int), health (int).
// - energy and health should always be between 1 and 100. If they fall below 1, they should be set to 1 , and if they go above 100 , they should be set to 100 .
// - The following static variable: numberOfAnimals (int). It should start at 0 and increase every time an Animal instance is created.
// - 4-arg constructor that takes the variables in the order above and sets them.
// - Note that energy and health might be out of the desired range, in that case, you need to set them to an appropriate value as described above
// - 2-arg constructor that takes species and name (in that order) and creates an instance with 50 energy and 100 health.
// - 1-arg constructor that takes a name and creates an instance with species "Unknown", 50 energy, and 100 health.
// - Getters for all instance variables.
// - Setters for name, energy, and health. For energy and health setters, make sure that the stored value is appropriate.
// Getter for numberOfAnimals.
// • void eat(int) method that receives an amount of food and increases the energy of the
// animal by 2 times the food amount.
// • void doActivity(int, boolean) method that receives the duration of the activity and
// whether it’s dangerous. It will decrease the energy of the animal by 5 times the duration.
// Additionally, if the activity is dangerous, it will decrease the health of the animal by 3 times the
// duration.
// • void goToZooHospital() method that sets the health of the animal to 100. Additionally, if
// the energy is below 60, it will set it to 60.
// • boolean isHungry() method that returns whether the animal is hungry or not. An animal is
// hungry if their energy is below 50.
// • toString() method to provide a String representation of instances of the class, with the
// format "I am [species] [name]. I have [energy] energy and [health] health" (without the
// brackets)







public class Animal { // extends Object (by JVM)
    private String species;
    private String name;
    // public void setName(String name) { this.name = name; } // Mutators (setters)
    private int energy;
    public void setEnergy(int energy) { // Mutators (setters)
        if (energy < 1) { 
            this.energy = 1;
        } else if (energy > 100) {
            this.energy = 100;
        } else {
            this.energy = energy;
        }
    }
    private int health;
    public static int numberOfAnimals = 0;

    // Chain Constructors
    public Animal() { // no-arg constructor (default constructor)
        this("Unknown", "Unknown", 50, 100);
    }
    public Animal(String species, String name, int energy, int health) { // 4-arg constructor
        this.species = species;
        this.name = name;
        setEnergy(energy);
        setHealth(health);
        numberOfAnimals++;
    }
    






    // Method overloading <- horizontal (having different method signatures)
    public static int hi() {
        return 1;
    }
    public static int hi(int x) {
        return 2;
    }
    public static int hi(double x) {
        return 3;
    }

    @Override
    public String toString() {
        return super.toString();
        // return String.format("Species: %s, Name: %s, Energy: %d, Health: %d", species, name, energy, health);
    }
    
    public static void main(String[] args) {
        System.out.println(hi(5));
        System.out.println(hi());
        System.out.println(hi(5.0));
        // Animal a1 = new Animal();
        // System.out.println(a1);
        // Animal a2 = new Animal("Lion", "Simba", 120, -10);
        // System.out.println(a2);
        // Animal a3 = new Animal("Tiger", "Shere Khan");
        // System.out.println(a3);
        // Animal a4 = new Animal("Baloo");
        // System.out.println(a4);
        // System.out.println("Number of animals: " + Animal.numberOfAnimals);
    }
}
