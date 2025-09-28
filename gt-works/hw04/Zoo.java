// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

import java.util.Scanner;

public class Zoo {
    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java Zoo <numHabitats> <numAnimals>");
            return;
        }
        int numHabitats = Integer.parseInt(args[0]);
        int numAnimals = Integer.parseInt(args[1]);

        Scanner sc = new Scanner(System.in);

        Habitat[] habitats = new Habitat[numHabitats];
        for (int i = 0; i < numHabitats; i++) {
            String hName = sc.next();
            int capacity = sc.nextInt();
            habitats[i] = new Habitat(hName, capacity);
        }

        Animal[] animals = new Animal[numAnimals];
        for (int i = 0; i < numAnimals; i++) {
            String species = sc.next();
            String name = sc.next();
            int energy = sc.nextInt();
            int health = sc.nextInt();
            animals[i] = new Animal(species, name, energy, health);
        }

        int hIndex = 0;
        for (Animal a : animals) {
            int attempts = 0;
            while (attempts < numHabitats) {
                if (habitats[hIndex].addAnimal(a)) {
                    break;
                }
                hIndex = (hIndex + 1) % numHabitats;
                attempts++;
            }
            hIndex = (hIndex + 1) % numHabitats;
        }

        System.out.println();

        printZoo("Habitats and their animals at the beginning of the day:", habitats);

        if (numHabitats >= 2) {
            Habitat first = habitats[0];
            Habitat last = habitats[numHabitats - 1];
            if (!last.isFull()) {
                Animal[] hungry = first.getHungryAnimals();
                if (hungry.length > 0) {
                    Animal toMove = hungry[0];
                    if (first.removeAnimal(toMove)) {
                        last.addAnimal(toMove);
                    }
                }
            }
        }
        Habitat lastHab = habitats[numHabitats - 1];
        lastHab.feedAnimals(10);

        System.out.println();

        printZoo("Habitats and their animals at the end of the day:", habitats);
    }

    private static void printZoo(String header, Habitat[] habitats) {
        System.out.println(header);
        for (Habitat h : habitats) {
            System.out.println(h.toString());
            for (Animal a : h.getAllAnimals()) {
                System.out.println(a.toString());
            }
        }
    }
}
