package guireference;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

public class MainView extends JFrame {
    private JLabel label;
    private JButton button;

    public MainView() {
        super("Simple guireference App");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 200);
        setLayout(new BorderLayout());

        label = new JLabel("", JLabel.CENTER);
        add(label, BorderLayout.CENTER);

        button = new JButton("Click Me");
        JPanel buttonPanel = new JPanel();
        buttonPanel.add(button);
        add(buttonPanel, BorderLayout.SOUTH);

        setLocationRelativeTo(null);
    }

    public void setLabelText(String text) {
        label.setText(text);
    }

    public void addButtonListener(ActionListener listener) {
        button.addActionListener(listener);
    }
} 