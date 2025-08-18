package gui;

/// JDK already has the following as library (JRE)
import javax.swing.JFrame;      // (1) Window Screen
import javax.swing.JPanel;      // (2) Scene Layout
import java.awt.BorderLayout;       // styling of layouts!
import java.awt.GridLayout;
import javax.swing.JButton;     // (3) UI component - control
import javax.swing.JLabel;      // (3) UI component - visual

public class MenuView extends JPanel implements Displayable {
    public static String getUrl() {
        String path = "/" + new Object() {}.getClass().getEnclosingClass().getName().replace('.', '/') + ".class";
        System.out.println("URL (registered statically): " + path);
        return path;
    }

    // Contant in Java, static == "since the program starts" && final == "permanent for the program lifetime"
    @Override
    public String getTitle() { return "Weather Forecast"; }
    @Override
    public int getWidth() { return 600; }
    @Override
    public int getHeight() { return 480; }





    private JButton btnStart;
    public JButton getBtnStart() { return this.btnStart; } // accessor / getter

    private JButton btnExit;
    private JLabel lblMessage;
    public JLabel getLblMessage() { return this.lblMessage; } // accessor / getter

    public MenuView() {
        // super(TITLE); // (1) Window Title on the top bar


        // Button (-> in the Panel -> *in the Frame)
        btnStart = new JButton("Start Forecasting");
        btnExit = new JButton("Exit");
        // Labels (-> in the Panel -> *in the Frame)
        lblMessage = new JLabel("Click the button below!", JLabel.CENTER);
        this.setLayout(new BorderLayout()); // Preferred for FlowLayout, BorderLayout, GridLayout
        this.add(btnStart, BorderLayout.NORTH);
        this.add(lblMessage, BorderLayout.CENTER);
        this.add(btnExit, BorderLayout.SOUTH);





        // pnlMain.setLayout(new GridLayout(3, 2, 10, 10)); // Preferred for FlowLayout, BorderLayout, GridLayout
        // // 3 rows, 2 columns, 10px hgap/vgap
        // /*
        //     GridLayout: 3 rows, 2 columns
        //     0,0 | 0,1
        //     1,0 | 1,1
        //     2,0 | 2,1
        // */
        // pnlMain.add(new JButton("One"));
        // pnlMain.add(new JButton("Two"));
        // pnlMain.add(new JButton("Three"));
        // pnlMain.add(new JButton("Four"));
        // pnlMain.add(new JButton("Five"));
        // pnlMain.add(new JButton("Six"));

        



        
        /**
         * super: refer to parent class (Jframe class)
         * this: refer to itself, child class (MenuView class)
         */
    }
}


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