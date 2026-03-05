
/*

     javac MainGUI.java
     jar cfe MainGUI.jar MainGUI MainGUI*.class
     java -jar MainGUI.jar
     rm -rf *.class *.jar

 */


import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/**
 * MainGUI - Temperature Converter using MVC Pattern.
 * * Model: Handles the mathematical calculations.
 * View: Handles the UI layout and display.
 * Controller: Listens to the View and updates the Model/View accordingly.
 */
public class MainGUI {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            TemperatureModel model = new TemperatureModel();
            TemperatureView view = new TemperatureView();
            new TemperatureController(model, view);
            
            view.setVisible(true);
        });
    }

    // --- MODEL ---
    /**
     * The Model represents the data and the "business logic".
     * It doesn't know anything about the GUI.
     */
    static class TemperatureModel {
        public double convertFtoC(double f) {
            return (f - 32) * 5 / 9;
        }

        public double convertCtoF(double c) {
            return (c * 9 / 5) + 32;
        }
    }

    // --- VIEW ---
    /**
     * The View represents the visual interface.
     * It only focuses on how things look and provides access to its components.
     */
    static class TemperatureView extends JFrame {
        private JTextField fieldF = new JTextField(10);
        private JTextField fieldC = new JTextField(10);
        private JButton btnConvertFtoC = new JButton("Convert F to C");
        private JButton btnConvertCtoF = new JButton("Convert C to F");
        private JLabel statusLabel = new JLabel("Enter a value...");

        public TemperatureView() {
            this.setTitle("MVC Temp Converter");
            this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            this.setSize(450, 200);
            this.setLayout(new GridLayout(4, 2, 10, 10));

            this.add(new JLabel("Fahrenheit:"));
            this.add(fieldF);
            this.add(new JLabel("Celsius:"));
            this.add(fieldC);
            this.add(btnConvertFtoC);
            this.add(btnConvertCtoF);
            this.add(new JLabel("Status:"));
            this.add(statusLabel);
            
            this.setLocationRelativeTo(null);
        }

        // Methods to get/set data without exposing the raw components too much
        public String getFText() { return fieldF.getText(); }
        public String getCText() { return fieldC.getText(); }
        public void setFText(String text) { fieldF.setText(text); }
        public void setCText(String text) { fieldC.setText(text); }
        public void setStatus(String text) { statusLabel.setText(text); }

        // Methods to attach listeners from the Controller
        public void addFtoCListener(ActionListener listener) {
            btnConvertFtoC.addActionListener(listener);
        }

        public void addCtoFListener(ActionListener listener) {
            btnConvertCtoF.addActionListener(listener);
        }
    }

    // --- CONTROLLER ---
    /**
     * The Controller acts as the bridge.
     * It takes user input from the View, processes it via the Model, 
     * and updates the View with the results.
     */
    static class TemperatureController {
        private TemperatureModel model;
        private TemperatureView view;

        public TemperatureController(TemperatureModel model, TemperatureView view) {
            this.model = model;
            this.view = view;

            // Define what happens when buttons are clicked
            this.view.addFtoCListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    try {
                        double f = Double.parseDouble(view.getFText());
                        double c = model.convertFtoC(f);
                        view.setCText(String.format("%.2f", c));
                        view.setStatus("Fahrenheit converted to Celsius.");
                    } catch (NumberFormatException ex) {
                        view.setStatus("Error: Invalid Fahrenheit input.");
                    }
                }
            });

            this.view.addCtoFListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    try {
                        double c = Double.parseDouble(view.getCText());
                        double f = model.convertCtoF(c);
                        view.setFText(String.format("%.2f", f));
                        view.setStatus("Celsius converted to Fahrenheit.");
                    } catch (NumberFormatException ex) {
                        view.setStatus("Error: Invalid Celsius input.");
                    }
                }
            });
        }
    }
}