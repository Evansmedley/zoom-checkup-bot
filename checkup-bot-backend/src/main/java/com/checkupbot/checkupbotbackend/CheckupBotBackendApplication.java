package com.checkupbot.checkupbotbackend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.data.mongodb.repository.config.EnableMongoRepositories;

@SpringBootApplication
@EnableMongoRepositories
public class CheckupBotBackendApplication {

	public static void main(String[] args) {
		SpringApplication.run(CheckupBotBackendApplication.class, args);
	}

}
