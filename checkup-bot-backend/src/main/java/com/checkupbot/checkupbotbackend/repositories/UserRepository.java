package com.checkupbot.checkupbotbackend.repositories;

import com.checkupbot.checkupbotbackend.entities.Doctor;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.Optional;

public interface UserRepository extends MongoRepository<Doctor, Long> {
    Optional<Doctor> findDoctorByCpsoId(String cpsoId);
}
