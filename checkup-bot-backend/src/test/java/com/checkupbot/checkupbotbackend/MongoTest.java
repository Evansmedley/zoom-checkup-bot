package com.checkupbot.checkupbotbackend;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import com.checkupbot.checkupbotbackend.repositories.RoboticArmEndpointRepository;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.data.mongo.AutoConfigureDataMongo;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
@AutoConfigureDataMongo
public class MongoTest {

    @Autowired
    private RoboticArmEndpointRepository roboticArmEndpointRepository;

    @Test
    public void testAddAndRemoveObjectFromMongo() {

        // Create robotic arm endpoint instance
        RoboticArmEndpoint expected = new RoboticArmEndpoint("TEST", " 127.0.0.32", 8080);

        // Add instance to repository
        roboticArmEndpointRepository.save(expected);

        // Get instance from repository by id and confirm it is the same
        Optional<RoboticArmEndpoint> actual = roboticArmEndpointRepository.findById(expected.getUuid());
        assertTrue(actual.isPresent());
        assertEquals(expected, actual.get());

        // Remove instance from repository by id
        roboticArmEndpointRepository.deleteById(expected.getUuid());

        // Attempt to get again to confirm deletion
        assertTrue(roboticArmEndpointRepository.findById(expected.getUuid()).isEmpty());
    }
}
