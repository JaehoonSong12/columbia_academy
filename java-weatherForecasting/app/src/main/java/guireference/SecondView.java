/**
 * SecondView is the View in the MVC pattern for the second screen.
 * <p>
 * It displays a label and a button for navigation.
 */
package guireference;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

public class SecondView extends JPanel {
    private final JLabel label = new JLabel("Second Panel", JLabel.CENTER);
    private final JButton button = new JButton("Back to Main Panel");

    /**
     * Constructs the SecondView UI.
     */
    public SecondView() {
        setLayout(new BorderLayout());
        add(label, BorderLayout.CENTER);
        add(button, BorderLayout.SOUTH);
    }

    /**
     * Adds an ActionListener to the button.
     * @param l the ActionListener
     */
    public void addButtonListener(ActionListener l) { button.addActionListener(l); }
} 