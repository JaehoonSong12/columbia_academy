package gui;

import javax.swing.JFrame;      // (1) Window Screen
import javax.swing.JPanel;      // (2) Scene Layout
import java.awt.BorderLayout;       // styling of layouts!
import java.awt.GridLayout;
import java.awt.FlowLayout;
import javax.swing.JButton;     // (3) UI component - control
import javax.swing.JLabel;      // (3) UI component - visual

import javax.swing.JTextArea;

public class InfoView extends JPanel implements Displayable {
    public static String getUrl() {
        String path = "/" + new Object() {}.getClass().getEnclosingClass().getName().replace('.', '/') + ".class";
        System.out.println("URL (registered statically): " + path);
        return path;
    }

    @Override
    public String getTitle() { return "Weather Forecast Information page"; }
    @Override
    public int getWidth() { return 780; }
    @Override
    public int getHeight() { return 620; }

    private JLabel lblTemp;
    public JLabel getLblTemp() { return this.lblTemp; };
    
    private JTextArea txaAskTemp;
    public JTextArea getTxaAskTemp() { return this.txaAskTemp; };

    private JButton btnSubmit;
    public JButton getBtnSubmit() { return this.btnSubmit; };

    private JButton btnBack;
    public JButton getBtnBack() { return this.btnBack; };

    public InfoView() {
        // super(TITLE);

        
        lblTemp = new JLabel("Temperature: ", JLabel.CENTER);
        txaAskTemp = new JTextArea(10, 30);  // 10 rows, 30 columns
        btnSubmit = new JButton("Submit");
        btnBack = new JButton("Back");

        this.setLayout(new FlowLayout());
        this.add(lblTemp);
        this.add(txaAskTemp);
        this.add(btnSubmit);
        this.add(btnBack);

        
    }
}

// import javax.swing.*;

// public class TextAreaInputExample {
//     public static void main(String[] args) {
//         // Create a JTextArea
//         JTextArea textArea = new JTextArea(10, 30);  // 10 rows, 30 columns
//         JScrollPane scrollPane = new JScrollPane(textArea); // Optional, adds scrollbars

//         // Show input dialog with JTextArea inside a scroll pane
//         int result = JOptionPane.showConfirmDialog(null, scrollPane, 
//                 "Enter your text below", JOptionPane.OK_CANCEL_OPTION);

//         // Get the input after user presses OK
//         if (result == JOptionPane.OK_OPTION) {
//             String userInput = textArea.getText();
//             System.out.println("User entered:\n" + userInput);
//         } else {
//             System.out.println("User canceled input.");
//         }
//     }
// }


// btn - JButton
// chk - JCheckBox
// clr - JColorChooser
// cmb - JComboBox
// ico - JDesktopIcon
// edt - JEditorPane
// fch - JFileChooser
// ifr - JInternalFrame
// lbl - JLabel
// lyp - JLayeredPane
// lst - JList
// mnu - JMenuBar
// mni - JMenuItem
// opt - JOptionPane
// pnl - JPanel
// pmn - JPopupMenu
// prg - JProgressBar
// rad - JRadioButton
// rot - JRootPane
// scb - JScollBar
// scr - JScrollPane
// spr - JSeparator
// sld - JSlider
// spn - JSpinner
// spl - JSplitPane
// tab - JTabbedPaneJTable
// tbl - JTable
// tbh - JTableHeader
// txa - JTextArea
// txt - JText