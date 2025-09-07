/**
INSTRUCTIONS: 
    Homework1 is going on...
    
COLLABORATION: 
    I worked on the assignment alone, using only course-provided materials.

COMPILE & EXECUTE & CLEANUP (Java):

     javac  -d out                  fileio/WrapperClassUseCases.java        # compile (.java to .class)
     java           -cp "./out"     WrapperClassUseCases                    # execute (.class to run)
     rm -rf out/                                                            # clean up .class files
    
 */










/**
 * This class provides practical examples of why wrapper classes (like Integer, Double, Boolean)
 * are essential in Java, especially when dealing with data that can be missing or null.
 *
 * <p>Primitive types (int, double, boolean) cannot hold a 'null' value. They always have a
 * default value (0, 0.0, false). This becomes a significant problem when a default value
 * has a different meaning than "not present" or "unknown". Wrapper classes solve this by
 * being objects, which can be 'null'.
 *
 * <p>We will explore three common scenarios:
 * 1. ORM Frameworks (like JPA/Hibernate) mapping to nullable database columns.
 * 2. API Data Transfer Objects (DTOs) deserializing JSON with optional fields.
 * 3. Data Processing from sources like CSV files where cells can be empty.
 */
public class WrapperClassUseCases {

    public static void main(String[] args) {
        System.out.println("--- 1. ORM Framework (JPA/Hibernate) Example ---");
        demonstrateOrmMapping();

        System.out.println("\n--- 2. API Data Transfer Object (DTO) Example ---");
        demonstrateApiDtoMapping();

        System.out.println("\n--- 3. Data Processing (CSV) Example ---");
        demonstrateCsvProcessing();
    }

    // =================================================================================
    // Scenario 1: ORM Frameworks (like JPA/Hibernate)
    // =================================================================================

    /**
     * Represents a Product entity that would be mapped to a database table.
     * In a real application, this would have annotations like @Entity, @Table, @Column, etc.
     */
    static class Product {
        private Long id;
        private String name;

        /**
         * The problem with primitives: A 'stock_count' column in a database might be NOT NULL,
         * so a primitive 'int' is fine. It can't be null, and 0 is a valid stock count.
         */
        private int stockCount;

        /**
         * The necessity of wrappers: A 'discount_percentage' column is likely nullable.
         * A product might not have a discount. If we use 'int', a null from the DB would
         * become 0, implying a 0% discount, which is different from *no discount applied*.
         * Using 'Integer' allows us to represent this missing value as 'null'.
         */
        private Integer discountPercentage;

        public Product(Long id, String name, int stockCount, Integer discountPercentage) {
            this.id = id;
            this.name = name;
            this.stockCount = stockCount;
            this.discountPercentage = discountPercentage;
        }

        @Override
        public String toString() {
            // We can check for null to provide meaningful output.
            String discountInfo = (discountPercentage == null)
                    ? "No discount"
                    : discountPercentage + "% discount";
            return String.format("Product [id=%d, name='%s', stock=%d, info=%s]",
                    id, name, stockCount, discountInfo);
        }
    }

    /**
     * Simulates fetching product data from a database and mapping it to Product objects.
     */
    public static void demonstrateOrmMapping() {
        /*
         * Informative Note:
         * Imagine a 'products' table in your database.
         *
         * | id | name         | stock_count | discount_percentage |
         * |----|--------------|-------------|---------------------|
         * | 1  | "Laptop"     | 50          | 15                  |
         * | 2  | "Mouse"      | 200         | NULL                |
         *
         * When an ORM (Object-Relational Mapper) like Hibernate reads these rows, it needs
         * to create Java objects.
         */

        // Simulating the ORM fetching a product that has a discount.
        Product laptop = new Product(1L, "Laptop", 50, 15);

        // Simulating the ORM fetching a product with a NULL discount.
        // The 'null' value from the database is correctly mapped to the 'Integer' field.
        Product mouse = new Product(2L, "Mouse", 200, null);

        System.out.println(laptop); // Output shows "15% discount"
        System.out.println(mouse);  // Output correctly shows "No discount"

        // If 'discountPercentage' were an 'int', the 'null' for the mouse would cause an
        // error or be incorrectly defaulted to 0 by the framework, corrupting your data's meaning.
    }


    // =================================================================================
    // Scenario 2: API Data Transfer Objects (DTOs)
    // =================================================================================

    /**
     * Represents user data received from a JSON API. This is a Data Transfer Object (DTO).
     */
    static class UserDTO {
        private String username; // Required field
        private String email; // Required field

        /**
         * The necessity of wrappers: In a JSON payload, some fields might be optional.
         * For example, a user may not have provided their age.
         *
         * If the 'age' field is missing from the JSON:
         * - A primitive 'int age' would default to 0. Is the user 0 years old or did they just not provide their age? We can't tell.
         * - A wrapper 'Integer age' will be 'null'. This clearly tells us the data was not provided.
         */
        private Integer age;

        /**
         * Another example: a user might not be a premium member.
         *
         * If 'isPremium' is missing from the JSON:
         * - A primitive 'boolean isPremium' would default to 'false'. Is the user a non-premium member, or is their status unknown?
         * - A wrapper 'Boolean isPremium' will be 'null', indicating the information is missing.
         */
        private Boolean isPremium;


        public UserDTO(String username, String email, Integer age, Boolean isPremium) {
            this.username = username;
            this.email = email;
            this.age = age;
            this.isPremium = isPremium;
        }

        public void displayProfile() {
            System.out.printf("User: %s (%s)\n", username, email);

            // Using the wrapper, we can differentiate between provided and non-provided data.
            if (age == null) {
                System.out.println(" - Age: Not provided");
            } else {
                System.out.printf(" - Age: %d\n", age);
            }

            if (isPremium == null) {
                System.out.println(" - Premium Status: Unknown");
            } else {
                System.out.printf(" - Premium Status: %s\n", isPremium);
            }
        }
    }

    /**
     * Simulates receiving JSON data and deserializing it into UserDTO objects.
     */
    public static void demonstrateApiDtoMapping() {
        /*
         * Informative Note:
         * Imagine you are consuming a REST API. You might get two different JSON responses.
         *
         * JSON 1 (Full data):
         * { "username": "jane_doe", "email": "jane@example.com", "age": 28, "isPremium": true }
         *
         * JSON 2 (Optional fields missing):
         * { "username": "john_smith", "email": "john@example.com" }
         *
         * A JSON parsing library (like Jackson or Gson) would create UserDTO objects from this.
         */

        // Simulating deserialization of JSON 1
        UserDTO jane = new UserDTO("jane_doe", "jane@example.com", 28, true);

        // Simulating deserialization of JSON 2. The missing fields correctly map to 'null'.
        UserDTO john = new UserDTO("john_smith", "john@example.com", null, null);

        jane.displayProfile();
        System.out.println();
        john.displayProfile();
    }


    // =================================================================================
    // Scenario 3: Data Processing from Files (e.g., CSV)
    // =================================================================================

    /**
     * Represents a single row from a survey results CSV file.
     */
    static class SurveyResponse {
        private String participantId;

        /**
         * The necessity of wrappers: A 'rating' column might have empty cells if a
         * participant skipped a question.
         * - A primitive 'int' would default to 0. This is disastrous if 0 is a valid rating (e.g., on a 0-5 scale).
         * - An 'Integer' can be 'null', correctly representing a skipped question.
         */
        private Integer rating; // Rating on a scale of 1-5. Can be null if skipped.

        public SurveyResponse(String participantId, Integer rating) {
            this.participantId = participantId;
            this.rating = rating;
        }

        @Override
        public String toString() {
            String ratingText = (rating == null) ? "SKIPPED" : String.valueOf(rating);
            return String.format("Participant '%s' gave a rating of: %s", participantId, ratingText);
        }
    }

    /**
     * Simulates reading a CSV file and parsing its rows into objects.
     */
    public static void demonstrateCsvProcessing() {
        /*
         * Informative Note:
         * Consider a simple survey.csv file:
         *
         * participant_id,rating
         * P001,5
         * P002,
         * P003,2
         *
         * The second row for participant P002 has an empty value for the rating.
         * Our parsing logic needs to handle this gracefully.
         */

        // Simulating parsing the first row: "P001,5"
        String row1 = "P001,5";
        String[] parts1 = row1.split(",");
        SurveyResponse response1 = new SurveyResponse(parts1[0], Integer.parseInt(parts1[1])); // Parsing '5' works.

        // Simulating parsing the second row: "P002,"
        String row2 = "P002,";
        String[] parts2 = row2.split(",", -1); // Use -1 limit to keep trailing empty strings
        Integer rating2 = parts2[1].isEmpty() ? null : Integer.parseInt(parts2[1]); // Smart parsing
        SurveyResponse response2 = new SurveyResponse(parts2[0], rating2); // Correctly assigns null

        System.out.println(response1); // Shows a rating of 5
        System.out.println(response2); // Correctly shows SKIPPED

        // If we used a primitive `int rating`, we would have no clean way to represent the
        // skipped answer from P002. We'd either have to throw an exception or assign a
        // "magic number" like -1, which complicates the code and is poor practice.
        // `null` is the clear, idiomatic way to represent absence of a value.
    }
}