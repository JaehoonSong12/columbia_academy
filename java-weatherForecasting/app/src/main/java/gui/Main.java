package gui;

/// JDK already has the following as library (JRE)
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingUtilities;
import java.awt.BorderLayout;
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
        // Main frame
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