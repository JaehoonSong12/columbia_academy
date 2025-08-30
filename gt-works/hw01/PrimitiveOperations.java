// I worked on the assignment alone, using only course-provided materials.

public class PrimitiveOperations {
    public static void main(String[] args) {
        int spongebobIQ = 5;
        double patrickIQ = 3.5;

        System.out.println(spongebobIQ);
        System.out.println(patrickIQ);

        double einsteinIQ = spongebobIQ * patrickIQ;
        System.out.println(einsteinIQ);

        double spongebobIQDouble = (double) spongebobIQ;
        System.out.println(spongebobIQDouble);

        int patrickIqInt = (int) patrickIQ;
        System.out.println(patrickIqInt);

        char favoriteLetter = 'E';
        System.out.println(favoriteLetter);

        char lowerChar = (char) (favoriteLetter + 32);
        System.out.println(lowerChar);
    }
}
