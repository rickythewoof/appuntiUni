package frame;
import java.awt.*;

import javax.swing.*;

public class MyFrame extends JFrame{
	private JTextField matricolaField = new JTextField(20);
	private JTextField ipAddressField = new JTextField(20);
	private JTextField ipPortField = new JTextField(20);
	
	private JLabel ipAddressLabel = new JLabel("Indirizzo IP");
	private JLabel ipPortLabel = new JLabel("Porta");
	private JLabel matricolaLabel = new JLabel("Matricola");
	
	private JButton connectBtn = new JButton("Conetti");
	private JButton disconnectBtn = new JButton("Disconnetti");
	private JButton startBtn = new JButton("Avvia");
	private JButton stopBtn = new JButton("Termina");
	
	private JPanel southPanel = new JPanel();
	private JPanel centerPanel = new JPanel();
	private JPanel centerPanel1 = new JPanel();
	private JPanel centerPanel2 = new JPanel();
	private JPanel centerPanel3 = new JPanel();
	
	public MyFrame() {
		super("Connection box");
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		centerPanel1.add(matricolaLabel);
		centerPanel1.add(matricolaField);
		centerPanel2.add(ipAddressLabel);
		centerPanel2.add(ipAddressField);
		centerPanel3.add(ipPortLabel);
		centerPanel3.add(ipPortField);
		
		centerPanel.setLayout(new GridLayout(2,2));
		centerPanel.add(centerPanel1);	
		centerPanel.add(centerPanel2);
		centerPanel.add(centerPanel3);
		
		southPanel.add(connectBtn);
		southPanel.add(disconnectBtn);
		southPanel.add(stopBtn);
		southPanel.add(startBtn);
		
		this.getContentPane().add(centerPanel, BorderLayout.CENTER);
		this.getContentPane().add(southPanel, BorderLayout.SOUTH);
		
		this.setSize(500,200);
		this.setVisible(true);
		setButtons(false, false);

	}
	
	public void setButtons(boolean connected, boolean transmitting) {
		if(connected) {
			connectBtn.setEnabled(false);
			disconnectBtn.setEnabled(true);
			if (transmitting) {
				disconnectBtn.setEnabled(false);
				startBtn.setEnabled(false);
				stopBtn.setEnabled(true);
			}
			else {
				disconnectBtn.setEnabled(true);
				startBtn.setEnabled(true);
				stopBtn.setEnabled(false);
			}
		}
		else {
			connectBtn.setEnabled(true);
			disconnectBtn.setEnabled(false);
			startBtn.setEnabled(false);
			stopBtn.setEnabled(false);
		}
		
	}
	
	
}
