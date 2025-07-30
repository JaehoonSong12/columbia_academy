package gui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class CardLayoutExample {
    public static void createAndShowGUI() {
        JFrame frame = new JFrame("CardLayout Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // CardLayout container
        JPanel cardPanel = new JPanel(new CardLayout());

        // First card
        JPanel card1 = new JPanel();
        card1.setBackground(Color.CYAN);
        card1.add(new JLabel("This is Card 1"));

        // Second card
        JPanel card2 = new JPanel();
        card2.setBackground(Color.ORANGE);
        card2.add(new JLabel("This is Card 2"));

        // Add cards to the container
        cardPanel.add(card1, "Card1");
        cardPanel.add(card2, "Card2");

        // Navigation buttons
        JButton nextButton = new JButton("Next");
        JButton prevButton = new JButton("Previous");

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(prevButton);
        buttonPanel.add(nextButton);

        // Action listeners to navigate cards
        CardLayout cl = (CardLayout) cardPanel.getLayout();
        nextButton.addActionListener(e -> cl.next(cardPanel));
        prevButton.addActionListener(e -> cl.previous(cardPanel));

        frame.setLayout(new BorderLayout());
        frame.add(cardPanel, BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);

        frame.setVisible(true);
    }
}
