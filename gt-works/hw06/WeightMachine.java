// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

/**
 * Represents a weight machine that can adjust weight in increments.
 * Implements both Adjustable and Comparable.
 *
 * <p>Weight machines can only be compared to other weight machines.</p>
 *
 * @author Tai Park
 * @version 1.0.0
 */
public class WeightMachine implements Adjustable, Comparable<WeightMachine> {
    private final String weightMachineID;
    private final int weightIncrement;
    private final int maxWeight;
    private int currentWeight;

    /**
     * Constructs a WeightMachine object with the specified parameters.
     *
     * @param weightMachineID the ID of this weight machine
     * @param weightIncrement the increment between weight levels
     * @param maxWeight the maximum weight allowed
     */
    public WeightMachine(String weightMachineID, int weightIncrement, int maxWeight) {
        this.weightMachineID = weightMachineID;
        this.weightIncrement = weightIncrement;
        this.maxWeight = maxWeight;
        this.currentWeight = 0;
    }

    /**
     * Compares this weight machine to another.
     *
     * @param other the other weight machine
     * @return comparison integer
     */
    @Override
    public int compareTo(WeightMachine other) {
        if (other == null) {
            throw new NullPointerException("Cannot compare to null");
        }

        int result = Integer.compare(this.maxWeight, other.maxWeight);
        if (result != 0) {
            return result;
        }

        result = Integer.compare(other.currentWeight, this.currentWeight);
        if (result != 0) {
            return result;
        }

        return this.weightMachineID.compareTo(other.weightMachineID);
    }

    /**
     * Adjusts the current weight by the specified adjustment.
     *
     * @param adjustment the change in weight
     * @return true if the adjustment was valid, false otherwise
     */
    @Override
    public boolean adjustWeight(int adjustment) {
        if (this.weightIncrement == 0 && adjustment != 0) {
            return false;
        }

        if (this.weightIncrement != 0 && adjustment % this.weightIncrement != 0) {
            return false;
        }

        int newWeight = this.currentWeight + adjustment;
        if (newWeight < 0 || newWeight > this.maxWeight) {
            return false;
        }

        this.currentWeight = newWeight;
        return true;
    }

    /**
     * Returns a string representation of this weight machine.
     *
     * @return formatted string with current weight
     */
    @Override
    public String toString() {
        return this.weightMachineID + ": " + this.currentWeight + " lb. weight machine";
    }

    /**
     * Returns the weight machine ID.
     *
     * @return the weight machine ID
     */
    public String getWeightMachineID() {
        return this.weightMachineID;
    }

    /**
     * Returns the weight increment.
     *
     * @return the weight increment
     */
    public int getWeightIncrement() {
        return this.weightIncrement;
    }

    /**
     * Returns the maximum weight.
     *
     * @return the maximum weight
     */
    public int getMaxWeight() {
        return this.maxWeight;
    }

    /**
     * Returns the current weight.
     *
     * @return the current weight
     */
    public int getCurrentWeight() {
        return this.currentWeight;
    }
}
