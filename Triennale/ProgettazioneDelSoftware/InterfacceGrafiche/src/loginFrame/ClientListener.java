package loginFrame;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JOptionPane;
import javax.swing.JTextField;

public class ClientListener implements ActionListener{
	
	private LoginFrame frame;
	private JTextField ipAddress;
	private JTextField ipPort;
	private JTextField matricola;
	
	public static final String START="Start";
	public static final String STOP="Stop";
	public static final String CONNECT="Connect";
	public static final String DISCONNECT="Disconnect";
	
	private boolean connected = false;
	private boolean transmitting = false;
	
	public ClientListener (LoginFrame frame, JTextField address, JTextField port, JTextField matricola) {
		this.frame = frame;
		this.ipAddress = address;
		this.ipPort = port;
		this.matricola = matricola;
	}
	
	
	@Override
	public void actionPerformed(ActionEvent e) {
		String cmd = e.getActionCommand();
		if (cmd.equals(CONNECT)) {
			System.out.println("connect "+this.ipAddress.getText()+":"+this.ipPort.getText());
			connected = true;
			frame.setButtons(connected, transmitting);
			JOptionPane.showMessageDialog(null, "Connessione Stabilita", "Connected", 1);
		}
		else if(cmd.equals(START)) {
			System.out.println("start");
			transmitting = true;
			frame.setButtons(connected, transmitting);
		}
		else if(cmd.equals(STOP)) {
			System.out.println("stop");
			transmitting = false;
			frame.setButtons(connected, transmitting);
		}
		else if(cmd.equals(DISCONNECT)) {
			System.out.println("disconnected");
			connected = false;
			frame.setButtons(connected, transmitting);
		}

		
	}
	

}
