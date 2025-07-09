package gui;

/// JDK already has the following as library (JRE)
import javax.swing.JFrame;      // (1) Window Screen
import javax.swing.JPanel;      // (2) Scene Layout
import java.awt.BorderLayout;       // styling of layouts!
import javax.swing.JButton;     // (3) UI component - control
import javax.swing.JLabel;      // (3) UI component - visual

/**
 * Logic (Coding Part) of the app, not visual compoenents on your Monitor
 */
import javax.swing.SwingUtilities;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


/**
 * A simple Swing GUI application with a button and label.
 */
public class Main {
    /**
     * Create and display the GUI.
     */
    private static void createAndShowGUI() {
        // Main frame (Window Screen)
        JFrame frame = new JFrame("Simple GUI App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 200);
        frame.setLayout(new BorderLayout());

        // Label
        JLabel label = new JLabel("Click the button below!", JLabel.CENTER);
        frame.add(label, BorderLayout.CENTER);

        // Button
        JButton button = new JButton("Click Me");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                label.setText("Hello, Swing world!");
            }
        });


        JPanel buttonPanel = new JPanel();
        buttonPanel.add(button);

        frame.add(buttonPanel, BorderLayout.SOUTH);

        // Show
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
    }

    public static void main(String[] args) {
        // Schedule GUI creation on the Event Dispatch Thread
        SwingUtilities.invokeLater(Main::createAndShowGUI);
    }
}