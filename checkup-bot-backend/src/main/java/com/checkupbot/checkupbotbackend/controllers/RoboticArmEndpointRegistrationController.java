package com.checkupbot.checkupbotbackend.controllers;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import com.checkupbot.checkupbotbackend.repositories.RoboticArmEndpointRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/endpoint")
public class RoboticArmEndpointRegistrationController {

    @Autowired
    private RoboticArmEndpointRepository roboticArmEndpointRepository;

    private static final Logger logger = LoggerFactory.getLogger(RoboticArmEndpointRegistrationController.class);


    @GetMapping(value = "")
    public List<RoboticArmEndpoint> getEndpoints() {
        logger.debug("Received request: GET ENDPOINTS");
        return roboticArmEndpointRepository.findAll();
    }

    @GetMapping(value = "/{uuid}")
    public Optional<RoboticArmEndpoint> getEndpoint(@PathVariable("uuid") String uuid) {
        logger.debug("Received request: GET ENDPOINT '" + uuid +"'");
        return roboticArmEndpointRepository.findById(uuid);
    }

    @PostMapping(value = "/register")
    public RoboticArmEndpoint registerRoboticArmEndpoint(@RequestBody RoboticArmEndpoint newEndpoint) {
        logger.info("Received Request: REGISTER ROBOTIC ARM ENDPOINT");
        logger.info(newEndpoint.toString());

        for (RoboticArmEndpoint existingEndpoint : roboticArmEndpointRepository.findAll()) {
            if (existingEndpoint.getUri().equals(newEndpoint.getUri())) {
                return existingEndpoint;
            }
        }

        roboticArmEndpointRepository.save(newEndpoint);

        return newEndpoint;
    }

    @DeleteMapping(value = "/{uuid}")
    public RoboticArmEndpoint deleteRoboticArmEndpoint(@PathVariable("uuid") String uuid) {
        logger.debug("Received request: DELETE ROBOTIC ARM ENDPOINT");
        Optional<RoboticArmEndpoint> roboticArmEndpoint = roboticArmEndpointRepository.findById(uuid);
        roboticArmEndpointRepository.deleteById(uuid);
        return roboticArmEndpoint.orElse(null);
    }
}
