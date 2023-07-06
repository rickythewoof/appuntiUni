package loginFrame;
import java.awt.*;
import java.awt.event.ActionListener;

import javax.swing.*;

public class LoginFrame extends JFrame{
	private JTextField matricolaField = new JTextField(20);
	private JTextField ipAddressField = new JTextField(20);
	private JTextField ipPortField = new JTextField(20);
	
	private JLabel ipAddressLabel = new JLabel("Indirizzo IP");
	private JLabel ipPortLabel = new JLabel("Porta");
	private JLabel matricolaLabel = new JLabel("Matricola");
	
	private JButton connectBtn = new JButton("Connect");
	private JButton disconnectBtn = new JButton("Disconnect");
	private JButton startBtn = new JButton("Start");
	private JButton stopBtn = new JButton("Stop");
	
	private JPanel southPanel = new JPanel();
	private JPanel centerPanel = new JPanel();
	private JPanel centerPanel1 = new JPanel();
	private JPanel centerPanel2 = new JPanel();
	private JPanel centerPanel3 = new JPanel();

	
	public LoginFrame() {
		super("connection box");
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		centerPanel1.add(matricolaLabel);
		centerPanel1.add(matricolaField);
		centerPanel2.add(ipAddressLabel);
		centerPanel2.add(ipAddressField);
		centerPanel3.add(ipPortLabel);
		centerPanel3.add(ipPortField);
		
		//Layout
		centerPanel.setLayout(new GridLayout(2,2));
		centerPanel.add(centerPanel1);	
		centerPanel.add(centerPanel2);
		centerPanel.add(centerPanel3);
		
		southPanel.add(connectBtn);
		southPanel.add(disconnectBtn);
		southPanel.add(startBtn);
		southPanel.add(stopBtn);
		
		
		//Layout
		this.getContentPane().add(centerPanel, BorderLayout.CENTER);
		this.getContentPane().add(southPanel, BorderLayout.SOUTH);
		
		
		//Visibility & first appearance
		this.pack();
		this.setLocation(500, 300);
		this.setVisible(true);
		setButtons(false, false);
		
		//listener
		ActionListener listener = new ClientListener(this,ipAddressField,ipPortField,matricolaField);
		connectBtn.setActionCommand(ClientListener.CONNECT);
		connectBtn.addActionListener(listener);
		disconnectBtn.setActionCommand(ClientListener.DISCONNECT);
		disconnectBtn.addActionListener(listener);
		startBtn.setActionCommand(ClientListener.START);
		startBtn.addActionListener(listener);
		stopBtn.setActionCommand(ClientListener.STOP);
		stopBtn.addActionListener(listener);

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
