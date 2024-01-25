package com.checkupbot.checkupbotbackend.services;

import com.checkupbot.checkupbotbackend.dtos.CredentialsDto;
import com.checkupbot.checkupbotbackend.dtos.UserDto;
import com.checkupbot.checkupbotbackend.entities.Doctor;
import com.checkupbot.checkupbotbackend.execptions.LoginException;
import com.checkupbot.checkupbotbackend.mappers.UserMapper;
import com.checkupbot.checkupbotbackend.repositories.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.nio.CharBuffer;

@RequiredArgsConstructor
@Service
public class UserService {

    private final UserRepository userRepository;

    private final PasswordEncoder passwordEncoder;

    private final UserMapper userMapper;

    public UserDto login(CredentialsDto credentialsDto) {
        Doctor user = userRepository.findDoctorByCpsoId(credentialsDto.getLogin())
                .orElseThrow(() -> new LoginException("Unknown user", HttpStatus.NOT_FOUND));

        if (passwordEncoder.matches(CharBuffer.wrap(credentialsDto.getPassword()), user.getPassword())) {
            return userMapper.toUserDto(user);
        }
        throw new LoginException("Invalid password", HttpStatus.BAD_REQUEST);
    }

    public UserDto findByLogin(String login) {
        Doctor user = userRepository.findDoctorByCpsoId(login)
                .orElseThrow(() -> new LoginException("Unknown user", HttpStatus.NOT_FOUND));
        return userMapper.toUserDto(user);
    }
}
