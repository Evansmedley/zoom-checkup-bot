package com.checkupbot.checkupbotbackend;

import com.checkupbot.checkupbotbackend.config.UserAuthenticationProvider;
import com.checkupbot.checkupbotbackend.dtos.CredentialsDto;
import com.checkupbot.checkupbotbackend.dtos.UserDto;
import com.checkupbot.checkupbotbackend.services.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RequiredArgsConstructor
@RestController
public class AuthenticationController {

    private final UserService userService;
    private final UserAuthenticationProvider userAuthenticationProvider;

    @PostMapping("/login")
    public ResponseEntity<UserDto> login(@RequestBody @Validated CredentialsDto credentialsDto) {
        UserDto userDto = userService.login(credentialsDto);
        userDto.setToken(userAuthenticationProvider.createToken(userDto.getCpsoId()));
        return ResponseEntity.ok(userDto);
    }
}
