package Java;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Moyenne_Calculater {
	public static void main (String[] args) {
		JFrame fenetre = new JFrame();
		fenetre.setSize(370,800);
		fenetre.setLocationRelativeTo(null);
		fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		JPanel panel =new JPanel();
		fenetre.setContentPane(panel);
		fenetre.setLayout( new GridLayout(4,4));
		JTextField bord = new JTextField();
		bord.setPreferredSize(new Dimension(370,100));
		bord.setBackground(Color.BLACK);
		JButton un = new JButton("1"), deux = new JButton("2"), trois = new JButton("3"), quatre = new JButton("4"),cinq = new JButton("5");
		JButton six = new JButton("6"), sept = new JButton("7"), huit = new JButton("8"), neuf = new JButton("9"),zero = new JButton("0");
		panel.add(bord, BorderLayout.NORTH);
		panel.add(un, BorderLayout.SOUTH);
		panel.add(deux, BorderLayout.SOUTH);
		panel.add(trois, BorderLayout.SOUTH);
		panel.add(quatre, BorderLayout.SOUTH);
		panel.add(cinq, BorderLayout.SOUTH);
	    panel.add(six, BorderLayout.SOUTH);	
	    panel.add(sept,BorderLayout.SOUTH);	
	    panel.add(huit, BorderLayout.SOUTH);	
	    panel.add(neuf, BorderLayout.SOUTH);	
	    panel.add(zero, BorderLayout.SOUTH);	
	    un.setPreferredSize(new Dimension(50,50));
	    
		fenetre.setVisible(true);

	}

}
