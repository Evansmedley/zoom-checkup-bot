package com.checkupbot.checkupbotbackend.services;

import com.checkupbot.checkupbotbackend.repositories.DoctorRepository;
import com.checkupbot.checkupbotbackend.requests.AuthenticationRequest;
import com.checkupbot.checkupbotbackend.responses.AuthenticationResponse;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.stereotype.Service;

@Service
public class AuthenticationService {

    private final DoctorRepository doctorRepository;

    private final JwtService jwtService;

    private final AuthenticationManager authenticationManager;

    public AuthenticationService(DoctorRepository doctorRepository, JwtService jwtService, AuthenticationManager authenticationManager) {
        this.doctorRepository = doctorRepository;
        this.jwtService = jwtService;
        this.authenticationManager = authenticationManager;
    }

    public AuthenticationResponse authenticate(AuthenticationRequest authenticationRequest) {
        authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(authenticationRequest.getCpsoNumber(), authenticationRequest.getPassword()));

        var doctor = doctorRepository.findByCpsoNumber(authenticationRequest.getCpsoNumber()).orElseThrow();

        var jwtToken = jwtService.generateToken(doctor);

        return AuthenticationResponse.builder().jwt(jwtToken).build();
    }
}
