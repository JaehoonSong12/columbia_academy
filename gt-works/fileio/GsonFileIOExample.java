/**
INSTRUCTIONS: 
    Available in Javadoc...



COMPILE & EXECUTE & CLEANUP (Java):

     javac  -cp "./gson-2.13.1/lib/gson-2.13.1.jar"         -d out  fileio/GsonFileIOExample.java   # compile (.java to .class)
     java   -cp "./out;./gson-2.13.1/lib/gson-2.13.1.jar"           GsonFileIOExample               # execute (.class to run)
     rm -rf out/                                                                                    # clean up .class files

    Note*: For Linux/macOS (using ':' as classpath separator) 

DEPENDENCIES: 
 */
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.reflect.TypeToken;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

/**
 * This class provides a practical example of serializing and deserializing a list of
 * Java objects to and from a JSON file using Google's Gson library.
 *
 * <p>Key Concepts Demonstrated:
 * <ul>
 * <li><b>Serialization:</b> Converting a Java object (or a list of objects) into a JSON string.
 * <li><b>Deserialization:</b> Parsing a JSON string back into its corresponding Java object(s).
 * <li><b>File I/O:</b> Writing the JSON string to a file and reading it back.
 * <li><b>Wrapper Classes:</b> Using {@code Integer} and {@code Boolean} to handle potentially
 * missing data in the JSON, which will correctly map to {@code null} fields in the objects.
 * <li><b>Gson TypeTokens:</b> Using {@code TypeToken} to correctly handle deserialization of
 * generic types like {@code List<User>}.
 * </ul>
 *
 * <h3>Dependency Information</h3>
 * To run this code, you need to include the Gson library in your project.
 * 
 * <p><b>Maven:</b>
 * <pre>{@code
 * <dependency>
 * <groupId>com.google.code.gson</groupId>
 * <artifactId>gson</artifactId>
 * <version>2.11.0</version>
 * </dependency>
 * }</pre>
 * 
 * <p><b>Gradle:</b>
 * <pre>{@code
 * implementation("com.google.code.gson:gson:2.11.0")
 * }</pre>
 * 
 * <p><b>JAR Download:</b> You can download the JAR from Maven Central or 
 * the official Gson GitHub repository in the following hyperlink.
 * https://repo1.maven.org/maven2/com/google/code/gson/gson/2.13.1/
 */
public class GsonFileIOExample {

    /**
     * A simple POJO (Plain Old Java Object) to represent user data.
     * Note the use of wrapper classes for fields that might be optional.
     */
    static class User {
        // Primitive types are fine for required data
        private long id;
        private String username;

        // Wrapper types MUST be used for optional/nullable data.
        // If 'age' is missing in the JSON, this will become 'null', not 0.
        private Integer age;

        // If 'isPremium' is missing in the JSON, this will be 'null', not 'false'.
        private Boolean isPremium;

        // A no-argument constructor is good practice for libraries like Gson.
        public User() {}

        public User(long id, String username, Integer age, Boolean isPremium) {
            this.id = id;
            this.username = username;
            this.age = age;
            this.isPremium = isPremium;
        }

        public void report() {
            System.out.println(
                "\tUser{id=" + this.id +
                ", username=" + this.username + 
                ", age=" + this.age +
                ", isPremium=" + this.isPremium +
                "}"
            );
        }

        /**
         * Provides a natural, human-readable string representation of the object.
         * This is great for logging and debugging.
         *
         * <p><b>Important Clarification:</b> This {@code toString()} method is NOT used by Gson for
         * creating the JSON file. Gson inspects the object's fields directly. The prompt mentioned
         * "serialize using toString naturally", which typically means having a readable output;
         * however, for file serialization into a structured format like JSON, a dedicated
         * library is the correct approach.
         *
         * @return A string representation of the user.
         */
        @Override
        public String toString() {
            return String.format(
                "User{id=%d, username='%s', age=%s, isPremium=%s}", // Dict or Map string representation (Serializing)
                id,
                username,
                (age == null ? "null" : age.toString()), // Handle null for clean printing
                (isPremium == null ? "null" : isPremium.toString())
            );
        }
    }

    public static void main(String[] args) {
        // --- 1. SETUP: Create some sample data ---
        List<User> userList = new ArrayList<>();
        // User with complete data
        userList.add(new User(1L, "jane_doe", 28, true));
        // User with missing optional data (age and premium status are null)
        userList.add(new User(2L, "john_smith", null, null));
        // Another user with some data
        userList.add(new User(3L, "alex_ray", 35, false));

        // --- 2. GSON CONFIGURATION ---
        // We use GsonBuilder to create a Gson instance with pretty printing.
        // This makes the output JSON file human-readable.
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        String fileName = "users.json";

        // --- 3. SERIALIZATION: Write the list of users to a JSON file ---
        // The try-with-resources statement ensures the FileWriter is automatically closed.
        try (FileWriter writer = new FileWriter(fileName)) {
            // gson.toJson() handles the conversion of the List<User> to a JSON string.
            gson.toJson(userList, writer);
            System.out.println("Successfully wrote user list to " + fileName);
            System.out.println("----------------------------------------------");
        } catch (IOException e) {
            System.err.println("An error occurred while writing the JSON file.");
            e.printStackTrace();
        }

        // --- 4. DESERIALIZATION: Read and parse the JSON file back into a List of objects ---
        try (FileReader reader = new FileReader(fileName)) {
            /*
             * Informative Note on TypeToken:
             * When deserializing generic types like List<User>, Java's type erasure prevents us
             * from simply using 'List<User>.class'. At runtime, Java doesn't know what kind of
             * list it is.
             *
             * Gson's TypeToken is a clever workaround. By creating an anonymous subclass of
             * TypeToken<List<User>>, we capture the generic type information, allowing Gson
             * to correctly deserialize the JSON into a fully typed list of User objects.
             */
            Type userListType = new TypeToken<ArrayList<User>>(){}.getType();

            /*
             * ==============================================================================
             * * \/ \/ \/   THIS IS WHERE THE PARSING HAPPENS   \/ \/ \/
             *
             * ==============================================================================
             *
             * The `gson.fromJson()` method is the core of the deserialization process.
             * It takes the raw text content read from the file and parses it into
             * structured Java objects. Here's a step-by-step breakdown:
             *
             * 1.  `reader`: This is the first argument. The `FileReader` object reads the
             * `users.json` file character by character. `gson.fromJson()` is smart
             * enough to consume this entire stream of characters, which represents
             * the JSON string.
             *
             * 2.  `userListType`: This is the second argument and it's crucial. It acts as
             * a "blueprint" that tells Gson what kind of Java structure to create from
             * the JSON string. Because of Java's type erasure, you can't just use
             * `List<User>.class`. The `TypeToken` captures the full generic type
             * (`ArrayList<User>`), so Gson knows to create a list that specifically
             * holds `User` objects.
             *
             * 3.  The Parsing Process:
             * - Gson reads the opening `[` from the file, recognizing it as a JSON array.
             * - It then starts creating a Java `ArrayList`.
             * - For each JSON object `{...}` it finds inside the array, it does the following:
             * a. Creates a new instance of the `User` class (this is why a no-arg
             * constructor is helpful).
             * b. It reads the key-value pairs (e.g., `"id": 1`, `"username": "jane_doe"`).
             * c. It matches the JSON key (e.g., "username") to the field name in your
             * `User` class (e.g., `private String username;`).
             * d. It converts the JSON value to the correct Java type and sets the
             * field on the `User` object instance.
             * e. If a field from the Java class is missing in the JSON object (like
             * 'age' for john_smith), and the field is a wrapper type (like `Integer`),
             * Gson correctly assigns `null` to it.
             * - Once it has processed all the objects in the JSON array, it returns the
             * fully populated `ArrayList<User>`.
             *
             * In short, this single line reads the file content, interprets its structure,
             * creates the necessary Java objects, and populates them with the data.
             */
            List<User> restoredUsers = gson.fromJson(reader, userListType); // Object Restoration from String (Parsing)

            System.out.println("Successfully read and parsed users from " + fileName + ":\n");
            for (User user : restoredUsers) {
                // We are now working with the restored Java objects.
                // The .toString() method is used here for a clean console display.
                // System.out.println(user);
                user.report();
            }

            /*
             * SIDE NOTE: You can also parse a raw string directly.
             * If the JSON content was already in a String variable, you would do this:
             *
             * String jsonString = "[{\"id\":10,\"username\":\"string_user\"}]";
             * List<User> usersFromString = gson.fromJson(jsonString, userListType);
             * System.out.println("\nParsed from a raw string: " + usersFromString.get(0));
             *
             */
        } catch (IOException e) {
            System.err.println("An error occurred while reading the JSON file.");
            e.printStackTrace();
        }
    }
}
