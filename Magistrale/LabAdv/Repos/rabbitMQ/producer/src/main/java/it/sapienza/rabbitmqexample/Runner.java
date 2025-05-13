package it.sapienza.rabbitmqexample;

import java.util.concurrent.TimeUnit;

import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class Runner implements CommandLineRunner {

	private final RabbitTemplate rabbitTemplate;
	
	public Runner(RabbitTemplate rabbitTemplate) {
		this.rabbitTemplate = rabbitTemplate;
	}

	@Override
	public void run(String... args) throws Exception {
		System.out.println("Sending messages..");
		int i = 0;
		while (true)
		{
			String message = "Hello from RabbitMQ: I am message " + String.valueOf(i);
			rabbitTemplate.convertAndSend(MessagingRabbitmqApplication.topicExchangeName, "mecellone.done", message);
			System.out.println("... sent message " + i);
			i = i+1;
			Thread.sleep(5000);
		}	
	}

}
