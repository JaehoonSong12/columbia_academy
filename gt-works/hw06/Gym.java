// COLLABORATION STATEMENT: I worked on the homework assignment alone, using only course materials.

import java.util.Arrays;

/**
 * Represents a gym that manages its equipment.
 * Stores arrays of FreeWeight and WeightMachine objects.
 *
 * @author Taiyun
 * @version 1.2
 */
public class Gym {
    private FreeWeight[] freeWeights;
    private WeightMachine[] weightMachines;

    /**
     * Constructs a Gym with the given arrays of equipment.
     *
     * @param freeWeights the free weights array
     * @param weightMachines the weight machines array
     */
    public Gym(FreeWeight[] freeWeights, WeightMachine[] weightMachines) {
        if (freeWeights == null) {
            this.freeWeights = new FreeWeight[0];
        } else {
            Arrays.sort(freeWeights);
            this.freeWeights = freeWeights;
        }

        if (weightMachines == null) {
            this.weightMachines = new WeightMachine[0];
        } else {
            Arrays.sort(weightMachines);
            this.weightMachines = weightMachines;
        }
    }

    /**
     * Constructs an empty Gym with no equipment.
     */
    public Gym() {
        this.freeWeights = new FreeWeight[0];
        this.weightMachines = new WeightMachine[0];
    }

    /**
     * Prints all gym equipment, free weights first, then weight machines.
     */
    public void browseGymEquipment() {
        for (FreeWeight fw : this.freeWeights) {
            System.out.println(fw.toString());
        }
        for (WeightMachine wm : this.weightMachines) {
            System.out.println(wm.toString());
        }
    }

    /**
     * Adds a FreeWeight to the gym.
     * The new array remains sorted.
     *
     * @param newWeight the free weight to add
     */
    public void addEquipment(FreeWeight newWeight) {
        if (newWeight == null) {
            return;
        }
        FreeWeight[] newArr = Arrays.copyOf(this.freeWeights, this.freeWeights.length + 1);
        newArr[newArr.length - 1] = newWeight;
        Arrays.sort(newArr);
        this.freeWeights = newArr;
    }

    /**
     * Adds a WeightMachine to the gym.
     * The new array remains sorted.
     *
     * @param newMachine the weight machine to add
     */
    public void addEquipment(WeightMachine newMachine) {
        if (newMachine == null) {
            return;
        }
        WeightMachine[] newArr =
                Arrays.copyOf(this.weightMachines, this.weightMachines.length + 1);
        newArr[newArr.length - 1] = newMachine;
        Arrays.sort(newArr);
        this.weightMachines = newArr;
    }

    /**
     * Finds a FreeWeight in the gym by its ID.
     *
     * @param id the ID to search for
     * @return the FreeWeight with that ID, or null if not found
     */
    public FreeWeight getFreeWeight(String id) {
        if (id == null) {
            return null;
        }
        for (FreeWeight fw : this.freeWeights) {
            if (id.equals(fw.getFreeWeightID())) {
                return fw;
            }
        }
        return null;
    }

    /**
     * Finds a WeightMachine in the gym by its ID.
     *
     * @param id the ID to search for
     * @return the WeightMachine with that ID, or null if not found
     */
    public WeightMachine getWeightMachine(String id) {
        if (id == null) {
            return null;
        }
        for (WeightMachine wm : this.weightMachines) {
            if (id.equals(wm.getWeightMachineID())) {
                return wm;
            }
        }
        return null;
    }

    /**
     * Returns the total number of equipment in the gym.
     *
     * @return total count of free weights and weight machines
     */
    public int getEquipmentCount() {
        return this.freeWeights.length + this.weightMachines.length;
    }
}
