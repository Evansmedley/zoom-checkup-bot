package com.checkupbot.checkupbotbackend.services;

import com.checkupbot.checkupbotbackend.documents.Doctor;
import com.checkupbot.checkupbotbackend.repositories.DoctorRepository;
import com.checkupbot.checkupbotbackend.requests.AuthenticationRequest;
import com.checkupbot.checkupbotbackend.responses.AuthenticationResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthenticationService {

    private final DoctorRepository doctorRepository;

    private final JwtService jwtService;

    private final AuthenticationManager authenticationManager;

    public AuthenticationResponse authenticate(AuthenticationRequest authenticationRequest) {
        authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(authenticationRequest.getCpsoNumber(), authenticationRequest.getPassword()));

        var doctor = doctorRepository.findByCpsoNumber(authenticationRequest.getCpsoNumber()).orElseThrow();

        var jwtToken = jwtService.generateToken(doctor);

        return AuthenticationResponse.builder().jwt(jwtToken).build();
    }
}
