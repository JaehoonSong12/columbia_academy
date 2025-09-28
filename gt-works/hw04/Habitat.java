// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

public class Habitat {
    private String name;
    private Animal[] animals;
    private int animalCount;

    public Habitat(String name, int capacity) {
        this.name = name;
        this.animals = new Animal[capacity];
        this.animalCount = 0;
    }

    public boolean isFull() {
        return animalCount == animals.length;
    }

    public int getCapacity() {
        return animals.length;
    }

    public boolean addAnimal(Animal a) {
        if (a == null || isFull()) {
            return false;
        }
        for (int i = 0; i < animalCount; i++) {
            if (animals[i] == a) {
                return false;
            }
        }
        animals[animalCount++] = a;
        return true;
    }

    public boolean removeAnimal(Animal a) {
        if (a == null) {
            return false;
        }
        for (int i = 0; i < animalCount; i++) {
            if (animals[i] == a) {
                for (int j = i; j < animalCount - 1; j++) {
                    animals[j] = animals[j + 1];
                }
                animals[--animalCount] = null;
                return true;
            }
        }
        return false;
    }

    public void feedAnimals(int food) {
        for (int i = 0; i < animalCount; i++) {
            animals[i].eat(food);
        }
    }

    public Animal[] getAllAnimals() {
        Animal[] copy = new Animal[animalCount];
        for (int i = 0; i < animalCount; i++) {
            copy[i] = animals[i];
        }
        return copy;
    }

    public Animal[] getHungryAnimals() {
        int count = 0;
        for (int i = 0; i < animalCount; i++) {
            if (animals[i].isHungry()) {
                count++;
            }
        }
        Animal[] hungry = new Animal[count];
        int idx = 0;
        for (int i = 0; i < animalCount; i++) {
            if (animals[i].isHungry()) {
                hungry[idx++] = animals[i];
            }
        }
        return hungry;
    }

    public String getName() {
        return name;
    }

    public int getAnimalCount() {
        return animalCount;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        String plural = (animalCount == 1) ? "animal" : "animals";
        return name + " has " + animalCount + " " + plural
                + " and has a capacity of " + getCapacity();
    }
}
