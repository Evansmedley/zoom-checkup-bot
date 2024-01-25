package com.checkupbot.checkupbotbackend.repositories;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface RoboticArmEndpointRepository extends MongoRepository<RoboticArmEndpoint, String> {
}
