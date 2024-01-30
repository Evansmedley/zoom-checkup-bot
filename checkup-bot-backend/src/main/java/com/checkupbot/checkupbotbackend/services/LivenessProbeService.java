package com.checkupbot.checkupbotbackend.services;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import com.checkupbot.checkupbotbackend.repositories.RoboticArmEndpointRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;
import org.springframework.web.client.ResourceAccessException;
import org.springframework.web.client.RestTemplate;

import java.text.SimpleDateFormat;
import java.time.Duration;
import java.util.Objects;

@Service
public class LivenessProbeService {

    private static final Logger logger = LoggerFactory.getLogger(LivenessProbeService.class);

    @Autowired
    private RoboticArmEndpointRepository roboticArmEndpointRepository;

    private final RestTemplate restTemplate;


    public LivenessProbeService() {
        RestTemplateBuilder restTemplateBuilder = new RestTemplateBuilder();
        this.restTemplate = restTemplateBuilder
                .setConnectTimeout(Duration.ofSeconds(5))
                .setReadTimeout(Duration.ofSeconds(5))
                .build();
    }

    @Scheduled(fixedRate = 15000)
    public void sendLivenessProbeToAllEndpoints() {
        logger.debug("Sending liveness probes to endpoints");

        // Iterate through all endpoints
        for (RoboticArmEndpoint roboticArmEndpoint : roboticArmEndpointRepository.findAll()) {

            // Attempt to send a liveness probe to each
            try {
                ResponseEntity<RoboticArmEndpoint> response = restTemplate.postForEntity(roboticArmEndpoint.getUri() + "/liveness", roboticArmEndpoint, RoboticArmEndpoint.class);

                RoboticArmEndpoint responseBody = response.getBody();

                if (response.getStatusCode() == HttpStatus.OK && Objects.equals(Objects.requireNonNull(responseBody).getUuid(), roboticArmEndpoint.getUuid())) {
                    // All conditions satisfied, endpoint is active!
                    logger.debug("Probe of endpoint '" + roboticArmEndpoint.getUuid() + "' successful");
                    successfulLivenessProbe(roboticArmEndpoint);
                } else {

                    // If response status code is not OK or the uuid received is not the expected uuid, set endpoint to inactive
                    failedLivenessProbe(roboticArmEndpoint);
                }

            } catch (ResourceAccessException e) {
                // If connection cannot be established during liveness probe, set endpoint as inactive
                logger.debug(e.toString());
                failedLivenessProbe(roboticArmEndpoint);
            }
        }
    }

    public void successfulLivenessProbe(RoboticArmEndpoint roboticArmEndpoint) {
        // If already active do nothing, if inactive mark as active (toggle)
        if (!roboticArmEndpoint.isActive()) {
            logger.info("Endpoint '" + roboticArmEndpoint.getUuid() + "' set to active.");
            roboticArmEndpoint.setActive(true);
            roboticArmEndpointRepository.save(roboticArmEndpoint);
        }
    }

    public void failedLivenessProbe(RoboticArmEndpoint roboticArmEndpoint) {
        // If already inactive do nothing, if active, mark as inactive (toggle)
        if (roboticArmEndpoint.isActive()) {
            logger.info("Endpoint '" + roboticArmEndpoint.getUuid() + "' set to inactive.");
            roboticArmEndpoint.setActive(false);
            roboticArmEndpointRepository.save(roboticArmEndpoint);
        }
    }
}
