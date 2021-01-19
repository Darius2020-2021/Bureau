package Java;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.EventObject;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;
import javax.swing.JFormattedTextField;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;
import javax.swing.text.MaskFormatter;


public class entrain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
  JFrame fenetre = new JFrame();
  fenetre.setSize(700,700);
  fenetre.setLocationRelativeTo(null);
  fenetre.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  fenetre.setVisible(true);
  JPanel panel = new JPanel();
  panel.setBackground(Color.ORANGE);
  fenetre.setContentPane(panel);
  JLabel label = new JLabel("Salut Tout le monde");
  Font police = new Font("Tahoma",Font.BOLD,16);
  label.setFont(police);
  label.setHorizontalAlignment(JLabel.CENTER);
  panel.add(label, BorderLayout.NORTH);
 JOptionPane option = new JOptionPane();
 ImageIcon img = new ImageIcon("unnamed.jpg");
 option.showMessageDialog(null,"Felicitation","informaton",JOptionPane.INFORMATION_MESSAGE,img);
 JOptionPane option1 = new JOptionPane();
	JOptionPane option2 = new JOptionPane();
	String nom = option1.showInputDialog(null,"Veillez écrire votre nom","identité",JOptionPane.QUESTION_MESSAGE);
	option2.showMessageDialog(null,"salut " +nom,"information",JOptionPane.INFORMATION_MESSAGE);
	String[] sexe = {"Homme","Femme","Aucun"};
	JOptionPane option3 =new JOptionPane(),option4 = new JOptionPane();
	int rang = option3.showOptionDialog(null,"quel est votre sexe ?","le genre",JOptionPane.YES_NO_CANCEL_OPTION,JOptionPane.QUESTION_MESSAGE,null,sexe,sexe[2]);
	option4.showMessageDialog(null, "vous êtes donc " +sexe[rang],"genre",JOptionPane.INFORMATION_MESSAGE);
	}
	}
