/**
 * This file demonstrates how to make a custom class compatible with
 * Java's for-each loop by implementing the java.lang.Iterable interface.
 * All explanations are included as Javadoc or inline comments
 * as requested.
 */
package doc;

// We need these two interfaces for the demonstration.
import java.util.Iterator;
import java.util.NoSuchElementException;

/**
 * This is the main class that answers the user's question.
 * The primary answer is provided in the Javadoc for this class.
 *
 * <h2>Question: Which interface is needed for a custom for-each loop?</h2>
 *
 * <p>To make your custom class work with Java's for-each loop
 * (e.g., {@code for (MyType item : myCustomObject)}), you must implement the
 * <b>{@code java.lang.Iterable<T>}</b> interface.</p>
 *
 * <h3>How It Works:</h3>
 *
 * <ol>
 * <li><b>Implement {@code Iterable<T>}:</b>
 * <p>This interface has only one method you must implement:
 * {@code public Iterator<T> iterator()}</p>
 * <p>This method's job is to return a new "iterator" object that
 * knows how to loop over your class's data.</p>
 * </li>
 * <li><b>The {@code Iterator<T>} Interface:</b>
 * <p>The object you return from {@code iterator()} must
 * implement the <b>{@code java.util.Iterator<T>}</b> interface.
 * This {@code Iterator} object is the *actual* mechanism that
 * handles the logic of the iteration.</p>
 *
 * <p>The {@code Iterator} interface has two core methods the
 * for-each loop uses:</p>
 * <ul>
 * <li><b>{@code boolean hasNext()}:</b> Returns {@code true}
 * if there is another element, {@code false} otherwise.
 * (The loop calls this *before* getting the next element).</li>
 * <li><b>{@code T next()}:</b> Returns the next element in the
 * sequence. (The loop calls this to get the item for
 * the loop variable).</li>
 * </ul>
 * </li>
 * </ol>
 *
 * <p>When you write {@code for (String s : myIterableObject)},
 * the compiler "de-sugars" it into something like this:</p>
 *
 * <pre>
 * {@code
 * // 1. It gets the Iterator from your object.
 * Iterator<String> it = myIterableObject.iterator();
 *
 * // 2. It loops as long as hasNext() is true.
 * while (it.hasNext()) {
 * // 3. It gets the next item and assigns it to your variable.
 * String s = it.next();
 *
 * // Your loop body here
 * }
 * }
 * </pre>
 *
 * <p>See the example class {@link CustomRoster} below for a
 * concrete implementation.</p>
 */
public class ForEachExample {

    /**
     * Main method to demonstrate the CustomRoster class.
     *
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        // 1. Create an instance of our custom class.
        CustomRoster roster = new CustomRoster(3);
        roster.addName("Alice");
        roster.addName("Bob");
        roster.addName("Charlie");

        /*
         * 2. Because CustomRoster implements Iterable<String>,
         * we can use it directly in a for-each loop.
         * Java will automatically call our iterator() method
         * and then use the hasNext() and next() methods we defined.
         */
        System.out.println("--- Iterating with for-each loop: ---");
        for (String name : roster) {
            // This works!
            System.out.println(name);
        }

        /*
         * 3. This is what the for-each loop does "under the hood."
         * This code is functionally equivalent to the loop above.
         */
        System.out.println("\n--- Iterating manually with iterator: ---");
        // We get the iterator from our object
        Iterator<String> it = roster.iterator();
        
        // We loop while it.hasNext() is true
        while (it.hasNext()) {
            // We get the item using it.next()
            String name = it.next();
            System.out.println(name);
        }
    }
}

/**
 * An example custom class (a simple list of names) that we want
 * to use in a for-each loop.
 *
 * <p>To do this, we must implement <b>{@code Iterable<String>}</b>.</p>
 */
class CustomRoster implements Iterable<String> {

    // --- Class Fields ---
    private String[] names;
    private int currentSize = 0; // Tracks how many names are *actually* in the array

    /**
     * Constructor for our custom roster.
     *
     * @param maxSize The maximum number of names this roster can hold.
     */
    public CustomRoster(int maxSize) {
        this.names = new String[maxSize];
    }

    /**
     * A helper method to add names to our roster.
     *
     * @param name The name to add.
     */
    public void addName(String name) {
        if (currentSize < names.length) {
            names[currentSize] = name;
            currentSize++;
        }
    }

    /**
     * <b>This is the required method from the {@code Iterable} interface.</b>
     *
     * <p>It must return a new instance of an {@code Iterator}.</p>
     * <p>We can do this by creating a separate private class
     * (see {@link RosterIterator}) or an "anonymous inner class."</p>
     *
     * @return A new Iterator object that can iterate over the names.
     */
    @Override
    public Iterator<String> iterator() {
        /*
         * We return a new instance of our custom Iterator logic.
         * This is important! Every time a new loop starts, it
         * gets a *fresh* iterator that starts from the beginning.
         */
        return new RosterIterator();
    }


    /**
     * <b>This is the inner class that implements the {@code Iterator} interface.</b>
     *
     * <p>It holds the *state* of a single iteration (e.g., the current
     * position). It is declared 'private' because no class outside
     * CustomRoster needs to know about it.</p>
     *
     * <p>This could also be an anonymous inner class inside the
     * {@code iterator()} method, but a separate private class is often
     * easier to read.</p>
     */
    private class RosterIterator implements Iterator<String> {

        // This is the "cursor" or "index" for this *specific* iteration.
        // It is separate from the CustomRoster's 'currentSize'.
        private int iteratorIndex = 0;

        /**
         * <b>Required method from {@code Iterator}</b>
         * <p>Checks if we have more names to iterate over.</p>
         *
         * @return true if there is another name, false otherwise.
         */
        @Override
        public boolean hasNext() {
            /*
             * The iteration continues as long as our iterator's index
             * is less than the number of names actually added (currentSize).
             * We do NOT check against names.length, or we would get nulls.
             */
            return iteratorIndex < currentSize;
        }

        /**
         * <b>Required method from {@code Iterator}</b>
         * <p>Returns the *next* name in the sequence and advances
         * the iterator's position.</p>
         *
         * @return The next String (name).
         * @throws NoSuchElementException if next() is called when hasNext() is false.
         */
        @Override
        public String next() {
            // First, check if we even have a next element.
            // If not, it's conventional to throw this exception.
            if (!hasNext()) {
                throw new NoSuchElementException("No more names in roster.");
            }

            // Get the name at the current iterator position
            String nextName = names[iteratorIndex];
            
            // CRITICAL: Advance the iterator's position for the *next* call.
            iteratorIndex++;
            
            // Return the name we found.
            return nextName;
        }
        
        /*
         * The remove() method is optional and part of the Iterator interface.
         * The for-each loop doesn't use it, so you don't need to
         * implement it. The default implementation (from the Interface)
         * throws an UnsupportedOperationException, which is fine.
         */
    }
}