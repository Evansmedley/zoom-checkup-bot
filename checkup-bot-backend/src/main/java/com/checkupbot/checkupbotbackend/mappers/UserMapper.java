package com.checkupbot.checkupbotbackend.mappers;

import com.checkupbot.checkupbotbackend.dtos.UserDto;
import com.checkupbot.checkupbotbackend.entities.Doctor;
import org.mapstruct.Mapper;
import org.mapstruct.Mapping;

@Mapper(componentModel = "spring")
public interface UserMapper {
    UserDto toUserDto(Doctor doctor);
}
