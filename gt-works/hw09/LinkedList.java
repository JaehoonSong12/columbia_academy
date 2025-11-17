// Collaboration Statement: I worked on the homework assignment alone, using only course materials.

// java -jar checkstyle-10.23.0-all.jar -c cs1331.xml hw09/*.java

/**
 * A generic singly linked list implementation that stores values in nodes connected by
 * references. Supports adding, removing, retrieving, updating, searching, and clearing
 * elements while maintaining the size of the list.
 *
 * @author Tai Park
 * @version 1.0
 * @param <E> the type of elements stored in the linked list
 */
public class LinkedList<E> {

    /**
     * A private inner generic Node class. This Node class has its own type parameter
     * named E so that callers/tests can refer to LinkedList<?>.Node<?> if needed.
     *
     * @author Tai Park
     * @version 1.0
     * @param <E> the type of data stored in the node
     */
    private class Node<E> {

        private E data;
        private Node<E> next;

        /**
         * Constructs a node containing the given data and pointing to the given next node.
         *
         * @param data the data to store
         * @param next the next node reference
         */
        private Node(E data, Node<E> next) {
            this.data = data;
            this.next = next;
        }
    }

    private Node<E> head;
    private int size;

    /**
     * Constructs an empty linked list with head set to null and size set to 0.
     */
    public LinkedList() {
        head = null;
        size = 0;
    }

    /**
     * Returns the number of elements stored in this linked list.
     *
     * @return the size of the linked list
     */
    public int size() {
        return size;
    }

    /**
     * Returns whether the linked list contains no elements.
     *
     * @return true if the list is empty; false otherwise
     */
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Removes all elements from the linked list.
     * This operation sets head to null and size to 0.
     */
    public void clear() {
        head = null;
        size = 0;
    }

    /**
     * Adds an element at a specific index within the linked list.
     *
     * @param index the position at which to insert the element
     * @param value the value to insert (may be null)
     * @throws IndexOutOfBoundsException if index is outside the valid range [0, size]
     */
    public void add(int index, E value) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("Index out of bounds: " + index);
        }

        if (index == 0) {
            head = new Node<E>(value, head);
        } else {
            Node<E> prev = getNode(index - 1);
            prev.next = new Node<E>(value, prev.next);
        }

        size++;
    }

    /**
     * Adds an element to the end of the linked list.
     *
     * @param value the value to add (may be null)
     */
    public void add(E value) {
        add(size, value);
    }

    /**
     * Returns true if the linked list contains the given object.
     * Comparison is performed using equals(), except null is compared with ==.
     *
     * @param o the object to search for
     * @return true if the list contains the object; false otherwise
     */
    public boolean contains(Object o) {
        Node<E> curr = head;

        while (curr != null) {
            if (o == null) {
                if (curr.data == null) {
                    return true;
                }
            } else if (o.equals(curr.data)) {
                return true;
            }
            curr = curr.next;
        }

        return false;
    }

    /**
     * Returns the element stored at the given index.
     *
     * @param index the index to retrieve
     * @return the value at the specified index
     * @throws IndexOutOfBoundsException if index is outside the valid range [0, size - 1]
     */
    public E get(int index) {
        checkIndex(index);
        return getNode(index).data;
    }

    /**
     * Returns the index of the first occurrence of the specified object in the list,
     * or -1 if the object does not appear.
     *
     * @param o the object to search for
     * @return the index of the first matching occurrence, or -1 if not found
     */
    public int indexOf(Object o) {
        Node<E> curr = head;
        int i = 0;

        while (curr != null) {
            if (o == null) {
                if (curr.data == null) {
                    return i;
                }
            } else if (o.equals(curr.data)) {
                return i;
            }
            curr = curr.next;
            i++;
        }

        return -1;
    }

    /**
     * Removes and returns the element at the specified index.
     *
     * @param index the index of the element to remove
     * @return the removed element
     * @throws IndexOutOfBoundsException if index is outside the valid range [0, size - 1]
     */
    public E remove(int index) {
        checkIndex(index);

        E removed;

        if (index == 0) {
            removed = head.data;
            head = head.next;
        } else {
            Node<E> prev = getNode(index - 1);
            removed = prev.next.data;
            prev.next = prev.next.next;
        }

        size--;
        return removed;
    }

    /**
     * Removes the first occurrence of the specified object from the list.
     * Comparison uses equals(), except null is compared with ==.
     *
     * @param o the object to remove
     * @return true if an element was removed; false otherwise
     */
    public boolean remove(Object o) {
        if (head == null) {
            return false;
        }

        if (o == null && head.data == null
                || o != null && o.equals(head.data)) {
            head = head.next;
            size--;
            return true;
        }

        Node<E> curr = head;

        while (curr.next != null) {
            if (o == null && curr.next.data == null
                    || o != null && o.equals(curr.next.data)) {
                curr.next = curr.next.next;
                size--;
                return true;
            }
            curr = curr.next;
        }

        return false;
    }

    /**
     * Replaces the element at the given index with the specified value.
     *
     * @param index the index to update
     * @param value the new value to store
     * @return the previous value stored at that index
     * @throws IndexOutOfBoundsException if index is outside the valid range [0, size - 1]
     */
    public E set(int index, E value) {
        checkIndex(index);

        Node<E> node = getNode(index);
        E oldValue = node.data;
        node.data = value;
        return oldValue;
    }

    /**
     * Returns a string representation of this linked list.
     * Elements are shown within square brackets and separated by commas.
     *
     * @return the string representation of the list
     */
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");

        Node<E> curr = head;

        while (curr != null) {
            sb.append(String.valueOf(curr.data));
            if (curr.next != null) {
                sb.append(", ");
            }
            curr = curr.next;
        }

        sb.append("]");
        return sb.toString();
    }

    /**
     * Compares this list to another object for equality. The comparison checks type,
     * size, and then performs a node-by-node equality check (null-safe).
     *
     * @param o the object to compare
     * @return true if o is a LinkedList with the same elements in the same order
     */
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof LinkedList)) {
            return false;
        }

        LinkedList<?> other = (LinkedList<?>) o;
        if (this.size != other.size) {
            return false;
        }

        Node<E> currThis = this.head;
        LinkedList<?>.Node<?> currOther = other.head;

        while (currThis != null && currOther != null) {
            Object a = currThis.data;
            Object b = currOther.data;
            if (a == null) {
                if (b != null) {
                    return false;
                }
            } else {
                if (!a.equals(b)) {
                    return false;
                }
            }
            currThis = currThis.next;
            currOther = currOther.next;
        }

        return currThis == null && currOther == null;
    }

    /**
     * Throws an IndexOutOfBoundsException if the index is invalid.
     *
     * @param index the index to validate
     * @throws IndexOutOfBoundsException if index is not in [0, size - 1]
     */
    private void checkIndex(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds: " + index);
        }
    }

    /**
     * Returns the node at the specified index. Assumes the index is valid.
     *
     * @param index the index of the node to retrieve
     * @return the node at the given index
     */
    private Node<E> getNode(int index) {
        Node<E> curr = head;
        for (int i = 0; i < index; i++) {
            curr = curr.next;
        }
        return curr;
    }
}
