/*
INSTRUCTIONS:
    A PDF file is attached in the same folder.

COLLABORATION STATEMENT:
    I worked on the homework assignment alone, using only course materials.

CHECKSTYLE:
     java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw05/*.java

COMPILE & EXECUTE & CLEANUP (Java):
     javac  -d out                  hw05/TrainingGround.java     # compile (.java to .class)
     java           -cp "./out"     TrainingGround               # execute (.class to run)
     rm -rf out/                                        # clean up .class files

DEPENDENCIES:
 */





public abstract class A {}
public class B extends A {
    public B() {
        super();
    }
}
public class C extends B {
    public C() {
        super();
    }
}








/**
 * This class is homework 5.
 *
 * @author CS 1331 TAs
 * @version 1.0.0
 */
public class TrainingGround {

    // All instance variables must be private.
    private String name;
    private double trainingMultiplier;
    private boolean isOutdoors;

    /**
     * 3-arg constructor that takes all instance variables.
     * If the trainingMultiplier is less than 0, it should be set to 0.
     *
     * @param name The name of the training ground.
     * @param trainingMultiplier The effectiveness multiplier of the ground.
     * @param isOutdoors true if the ground is outdoors, false otherwise.
     */
    public TrainingGround(String name, double trainingMultiplier, boolean isOutdoors) {
        this.name = name;
        this.setTrainingMultiplier(trainingMultiplier); // Use setter for validation.
        this.isOutdoors = isOutdoors;
    }

    /**
     * 1-arg constructor that takes a name and constructs an indoors training ground
     * with a trainingMultiplier of 1.0.
     * This constructor uses "this" to chain to the 3-arg constructor.
     *
     * @param name The name of the training ground.
     */
    public TrainingGround(String name) {
        this(name, 1.0, false);
    }

    /**
     * Gets the name of the training ground.
     *
     * @return The name.
     */
    public String getName() {
        return this.name;
    }

    /**
     * Gets the training multiplier.
     *
     * @return The training multiplier.
     */
    public double getTrainingMultiplier() {
        return this.trainingMultiplier;
    }

    /**
     * Checks if the training ground is outdoors.
     * This method is named differently from a standard getter for better readability.
     *
     * @return true if the training ground is outdoors, false otherwise.
     */
    public boolean isOutdoors() {
        return this.isOutdoors;
    }

    /**
     * Sets the training multiplier. If the parameter is less than 0,
     * the trainingMultiplier is set to 0.
     *
     * @param trainingMultiplier The new multiplier value.
     */
    public void setTrainingMultiplier(double trainingMultiplier) {
        if (trainingMultiplier < 0) {
            this.trainingMultiplier = 0;
        } else {
            this.trainingMultiplier = trainingMultiplier;
        }
    }

    /**
     * Returns a string representation of the TrainingGround.
     * Uses String.format to ensure the training multiplier is displayed with two decimal digits.
     *
     * @return The formatted string.
     */
    @Override
    public String toString() {
        String locationType = isOutdoors ? "Outdoors" : "Indoors";
        String formattedMultiplier = String.format("%.2f", this.trainingMultiplier);
        return locationType + " Training Ground: " + this.name + ". It has training multiplier " + formattedMultiplier;
    }

    /**
     * Checks for equality with another object.
     * Two TrainingGrounds are equal if they have the same name, training multiplier,
     * and outdoor status.
     *
     * @param o The object to compare with.
     * @return true if the objects are equal, false otherwise.
     */
    @Override
    public boolean equals(Object o) {
        // 1. Check if o is the exact same object as this.
        if (this == o) {
            return true;
        }
        // 2. Check if o is null or if the classes don't match.
        if (o == null || this.getClass() != o.getClass()) {
            return false;
        }
        // 3. Cast the object and compare instance variables.
        TrainingGround other = (TrainingGround) o;
        return this.trainingMultiplier == other.trainingMultiplier
               && this.isOutdoors == other.isOutdoors
               && this.name.equals(other.name);
    }
}
