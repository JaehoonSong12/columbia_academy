/**
INSTRUCTIONS: 
    Available in Javadoc...



COMPILE & EXECUTE & CLEANUP: 

     javac  -cp "./gson-2.13.1/lib/gson-2.13.1.jar"         -d out  fileio/GsonFileIOExample.java   # compile (.java to .class)
     java   -cp "./out;./gson-2.13.1/lib/gson-2.13.1.jar"           GsonFileIOExample               # execute (.class to run)
     rm -rf out/                                                                                    # clean up .class files

    Note*: For Linux/macOS (using ':' as classpath separator) 
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
                    "User{id=%d, username='%s', age=%s, isPremium=%s}",
                    id,
                    username,
                    (age == null ? "N/A" : age), // Handle null for clean printing
                    (isPremium == null ? "Unknown" : isPremium)
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

            List<User> restoredUsers = gson.fromJson(reader, userListType);

            System.out.println("Successfully read and parsed users from " + fileName + ":\n");
            for (User user : restoredUsers) {
                // We are now working with the restored Java objects.
                // The .toString() method is used here for a clean console display.
                System.out.println(user);
            }

        } catch (IOException e) {
            System.err.println("An error occurred while reading the JSON file.");
            e.printStackTrace();
        }
    }
}
