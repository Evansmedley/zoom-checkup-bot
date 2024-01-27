package com.checkupbot.checkupbotbackend;

import com.checkupbot.checkupbotbackend.documents.RoboticArmEndpoint;
import com.checkupbot.checkupbotbackend.repositories.RoboticArmEndpointRepository;
import jakarta.annotation.PostConstruct;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class RoboticArmEndpointRegistrationControllerTest {

    @Value(value = "${local.server.port}")
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;

    @MockBean
    private static RoboticArmEndpointRepository mockRoboticArmEndpointRepository;

    private List<RoboticArmEndpoint> roboticArmEndpoints;

    @PostConstruct
    private void setup() {

        this.roboticArmEndpoints = List.of(
                new RoboticArmEndpoint("TestEndpoint1", "127.0.0.1", 8080),
                new RoboticArmEndpoint("TestEndpoint2", "127.0.0.2", 8080),
                new RoboticArmEndpoint("TestEndpoint3", "127.0.0.3", 8080)
        );

        when(mockRoboticArmEndpointRepository.findAll()).thenReturn(roboticArmEndpoints);
        for (RoboticArmEndpoint roboticArmEndpoint : roboticArmEndpoints) {
            when(mockRoboticArmEndpointRepository.findById(roboticArmEndpoint.getUuid())).thenReturn(Optional.ofNullable(roboticArmEndpoint));
            when(mockRoboticArmEndpointRepository.save(roboticArmEndpoint)).thenReturn(roboticArmEndpoint);
        }
    }

    @Test
    public void testGetEndpoints() {

        // GIVEN
        String resourceUrl = "http://localhost:" + port + "/endpoint";

        // WHEN
        ResponseEntity<ArrayList<RoboticArmEndpoint>> response = restTemplate.exchange(resourceUrl, HttpMethod.GET,
                null, new ParameterizedTypeReference<>() {});

        // THEN
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals(MediaType.APPLICATION_JSON, response.getHeaders().getContentType());
        assertEquals(roboticArmEndpoints, response.getBody());
    }

    @ParameterizedTest
    @ValueSource(ints = {0, 1, 2})
    public void testGetEndpoint(int roboticArmEndpointIndex) {

        // GIVEN
        RoboticArmEndpoint roboticArmEndpoint = roboticArmEndpoints.get(roboticArmEndpointIndex);
        String resourceUrl = "http://localhost:" + port + "/endpoint/" + roboticArmEndpoints.get(roboticArmEndpointIndex).getUuid();

        // WHEN
        ResponseEntity<RoboticArmEndpoint> response = restTemplate.getForEntity(resourceUrl, RoboticArmEndpoint.class);

        // THEN
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals(MediaType.APPLICATION_JSON, response.getHeaders().getContentType());
        assertEquals(roboticArmEndpoint, response.getBody());
    }

    @Test
    public void registerEndpoint() {

        // GIVEN
        HttpEntity<RoboticArmEndpoint> request = new HttpEntity<>(roboticArmEndpoints.get(0));
        String resourceUrl = "http://localhost:" + port + "/endpoint/register";

        // WHEN
        ResponseEntity<RoboticArmEndpoint> response = restTemplate.postForEntity(resourceUrl, request, RoboticArmEndpoint.class);

        // THEN
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals(MediaType.APPLICATION_JSON, response.getHeaders().getContentType());
        assertEquals(roboticArmEndpoints.get(0), response.getBody());
    }

    @Test
    public void deleteEndpoint() {

        // GIVEN
        String resourceUrl = "http://localhost:" + port + "/endpoint/" + roboticArmEndpoints.get(0).getUuid() + "/delete";

        // WHEN
        ResponseEntity<RoboticArmEndpoint> response = restTemplate.exchange(resourceUrl, HttpMethod.DELETE, null, RoboticArmEndpoint.class);

        // THEN
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertEquals(MediaType.APPLICATION_JSON, response.getHeaders().getContentType());
        assertEquals(roboticArmEndpoints.get(0), response.getBody());
    }

    @Test
    public void addExistingEndpoint() {
        // TODO
    }
}
