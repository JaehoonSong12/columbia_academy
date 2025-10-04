// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents a training ground where heroes can train.
 *
 * @author Tai Park
 * @version 1.0
 */
public class TrainingGround {

    private String name;
    private double trainingMultiplier;

    private boolean isOutdoors;

    /**
     * Constructs a training ground with the given parameters.
     *
     * @param name the name
     * @param trainingMultiplier multiplier value (if < 0, set to 0)
     * @param isOutdoors true if outdoors
     */
    public TrainingGround(String name, double trainingMultiplier, boolean isOutdoors) {
        this.name = name;
        setTrainingMultiplier(trainingMultiplier);
        this.isOutdoors = isOutdoors;
    }

    /**
     * Constructs an indoors training ground with multiplier 1.
     *
     * @param name the name
     */
    public TrainingGround(String name) {
        this(name, 1.0, false);
    }

    /**
     * Returns the name of the training ground.
     *
     * @return the name
     */
    public String getName() {
        return name;
    }

    /**
     * Returns the multiplier.
     *
     * @return training multiplier
     */
    public double getTrainingMultiplier() {
        return trainingMultiplier;
    }

    /**
     * Returns whether outdoors.
     *
     * @return true if outdoors
     */
    public boolean isOutdoors() {
        return isOutdoors;
    }

    /**
     * Sets the multiplier (if < 0, set to 0).
     *
     * @param trainingMultiplier new multiplier
     */
    public void setTrainingMultiplier(double trainingMultiplier) {
        if (trainingMultiplier < 0) {
            this.trainingMultiplier = 0.0;
        } else {
            this.trainingMultiplier = trainingMultiplier;
        }
    }

    @Override
    public String toString() {
        String outdoorsPrefix = isOutdoors ? "Outdoors" : "Indoors";
        return String.format("%s Training Ground: %s. "
                + "It has training multiplier %.2f",
                outdoorsPrefix, name, trainingMultiplier);
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || this.getClass() != obj.getClass()) {
            return false;
        }
        TrainingGround other = (TrainingGround) obj;
        if (this.isOutdoors != other.isOutdoors) {
            return false;
        }
        if (Double.compare(this.trainingMultiplier, other.trainingMultiplier) != 0) {
            return false;
        }
        if (this.name == null) {
            return other.name == null;
        }
        return this.name.equals(other.name);
    }
}
