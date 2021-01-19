package Java;

import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class QI_TEST {
	
	  
	public static void main(String[] args) {
		 JFrame fenetre = new JFrame();
		   fenetre.setTitle("QI-TEST");
		   fenetre.setSize(500,650);
		   fenetre.setLocationRelativeTo(null);
		   fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		   fenetre.setVisible(true);
		   fenetre.setLayout(new BorderLayout());
		   JPanel panel = new JPanel();
		   JPanel panel1= new JPanel();
		   panel1.setBackground(Color.ORANGE);
		   JPanel panel2 = new JPanel();
		   panel2.setBackground(Color.RED);
		   CardLayout card = new CardLayout();
		   fenetre.setContentPane(panel);
		// TODO Auto-generated method stub
		 JLabel label = new JLabel("");
		   Font police = new Font("Tahoma",Font.BOLD,16);
		   label.setFont(police);
		   label.setHorizontalAlignment(JLabel.CENTER);
		   panel.add(label, BorderLayout.NORTH);
		   JOptionPane option1 = new JOptionPane(),option2= new JOptionPane(),option3= new JOptionPane();
   String nom =option1.showInputDialog(null,"veillez écrire votre ID","création de compte",JOptionPane.QUESTION_MESSAGE );
   String[] sexe = {"Homme","femme","Nom déterminer"};
   option2.showOptionDialog(null,"Veiller préciser votre sexe","Création de compte",JOptionPane.YES_NO_CANCEL_OPTION,JOptionPane.QUESTION_MESSAGE,null,sexe,sexe[2]);
   option3.showMessageDialog(null, "Bienvenue " +nom+ " ici nous allons tester votre cerveau pour savoir si vous êtes ou non intelligent","Bienvenue",JOptionPane.INFORMATION_MESSAGE);
	label.setText("Veillez faire un choix :");
	JButton bouton1 = new JButton("TEST RAPIDE");
	JButton bouton2 = new JButton("TEST LONG");
	label.setPreferredSize(new Dimension(500,350));
	fenetre.add(bouton1, BorderLayout.SOUTH);
	fenetre.add(bouton2,BorderLayout.SOUTH);
	bouton1.setPreferredSize(new Dimension(300,75));
	bouton2.setPreferredSize(new Dimension(300,75));
	panel.setLayout(card);
	panel1.add(bouton1);
	panel2.add(bouton2);
	panel.add(panel1,"1");
	panel.add(panel2,"2");
	card.show(panel2, "1");
	bouton1.addActionListener( new ActionListener(){
		public void  actionPerformed(ActionEvent arg0) {
			card.show(panel,"2");
		}
	});
	bouton2.addActionListener( new ActionListener(){
		public void  actionPerformed(ActionEvent arg0) {
			card.show(panel,"1");
		}
	});
    	}

}
