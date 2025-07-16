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
 * Main.java
 * 
 * this is the entry point of the application.
 */








/**
 * A simple Swing GUI application with a button and label.
 */
public class Main {
    public static void main(String[] args) {
        // Schedule GUI creation on the Event Dispatch Thread
        SwingUtilities.invokeLater(Main::createAndShowGUI);
    }


    /**
     * Create and display the GUI.
     */
    private static void createAndShowGUI() {
        // Main frame (Window Screen)
        // JFrame frame = new JFrame("Simple GUI App");
        JFrame view = new MenuView();
        new MenuController((MenuView) view);
    }
}