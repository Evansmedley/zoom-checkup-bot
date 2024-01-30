import Button from "@mui/joy/Button";
import { FormControl } from "@mui/material";
import InputLabel from "@mui/material/InputLabel";
import OutlinedInput from "@mui/material/OutlinedInput";
import axios from "axios";
import { useState } from "react";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault(); // avoid page refresh

    axios
      .post("http://localhost:8080/api/auth/authenticate", {
        cpsoNumber: username,
        password: password,
      })
      .then((response) => {
        console.log(response);
        alert("submitted");
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div>
      <div className="main-rec">
        <div id="title">Doctor Sign In Portal</div>
        <div id="form">
          <FormControl fullWidth>
            <InputLabel htmlFor="username">Username/CPSO ID</InputLabel>
            <OutlinedInput
              id="username"
              label="Username/CPSO ID"
              defaultValue={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </FormControl>

          <FormControl fullWidth>
            <InputLabel htmlFor="password">Password</InputLabel>
            <OutlinedInput
              id="password"
              label="Password"
              defaultValue={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </FormControl>

          <Button
            size="md"
            color="primary"
            className="submit-login"
            onClick={handleSubmit}
          >
            Submit
          </Button>
        </div>
      </div>

      <div className="small-ellipse"></div>

      <div className="small-rec"></div>
    </div>
  );
};

export default Login;
