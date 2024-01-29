package com.checkupbot.checkupbotbackend.services;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import com.checkupbot.checkupbotbackend.repositories.RoboticArmEndpointRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.text.SimpleDateFormat;
import java.util.Objects;

@Service
public class LivenessProbeService {

    private static final Logger logger = LoggerFactory.getLogger(LivenessProbeService.class);

    private static final SimpleDateFormat dateFormat = new SimpleDateFormat("HH:mm:ss");

    @Autowired
    private RoboticArmEndpointRepository roboticArmEndpointRepository;

    @Scheduled(fixedRate = 10000)
    public void sendLivenessProbeToAllEndpoints() {
        logger.debug("Sending liveness probes to endpoints");
        RestTemplate restTemplate = new RestTemplate();
        for (RoboticArmEndpoint roboticArmEndpoint : roboticArmEndpointRepository.findAll()) {
            ResponseEntity<String> result = restTemplate.getForEntity(roboticArmEndpoint.getUri(), String.class);
            if (result.getStatusCode() == HttpStatus.OK && Objects.equals(result.getBody(), roboticArmEndpoint.getUuid())) {
                if (!roboticArmEndpoint.isActive()) {
                    logger.info("Endpoint '" + roboticArmEndpoint.getUuid() + "' set to active.");
                    roboticArmEndpoint.setActive(true);
                    roboticArmEndpointRepository.save(roboticArmEndpoint);
                }
            } else {
                if (roboticArmEndpoint.isActive()) {
                    logger.info("Endpoint '" + roboticArmEndpoint.getUuid() + "' set to inactive.");
                    roboticArmEndpoint.setActive(false);
                    roboticArmEndpointRepository.save(roboticArmEndpoint);
                }
            }
        }
    }
}
