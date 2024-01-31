import Button from "@mui/joy/Button";
import { FormControl } from "@mui/material";
import InputLabel from "@mui/material/InputLabel";
import OutlinedInput from "@mui/material/OutlinedInput";
import { request, setAuthHeader } from "../axios_helper";
import { useState } from "react";
import Collapse from "@mui/material/Collapse";
import IconButton from "@mui/material/IconButton";
import InputAdornment from "@mui/material/InputAdornment";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import Alert from "@mui/material/Alert";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Header from "../components/Header";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);

  const handleClickShowPassword = () => setShowPassword((show) => !show);

  const [incorrectPassword, setIncorrectPassword] = useState(false);
  const navigate = useNavigate();

  const handleKeyPressEnter = (event) => {
    if (event.key === "Enter") {
      handleSubmit(event);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault(); // avoid page refresh
    request("POST", "/api/auth/authenticate", {
      cpsoNumber: username,
      password: password,
    })
      .then((response) => {
        setAuthHeader(response.data.jwt);
        setIncorrectPassword(false);
        navigate("/control");
      })
      .catch((error) => {
        setAuthHeader(null);
        setIncorrectPassword(true);
      });
  };

  useEffect(() => {
    const timeId = setTimeout(() => {
      // After 3 seconds set the show value to false
      setIncorrectPassword(false);
    }, 3000);

    return () => {
      clearTimeout(timeId);
    };
  }, [incorrectPassword]);

  return (
    <div>
      <Header login={false} />
      <div className="main-rec">
        <Collapse in={incorrectPassword} id="alert">
          <Alert variant="filled" severity="error">
            Incorrect username or password.
          </Alert>
        </Collapse>

        <div id="title">Doctor Sign In Portal</div>
        <div id="form">
          <FormControl fullWidth required>
            <InputLabel htmlFor="username">Username/CPSO ID</InputLabel>
            <OutlinedInput
              id="username"
              label="Username/CPSO ID"
              defaultValue={username}
              onChange={(e) => setUsername(e.target.value)}
              onKeyDown={handleKeyPressEnter}
            />
          </FormControl>

          <FormControl fullWidth required variant="outlined">
            <InputLabel htmlFor="password">Password</InputLabel>
            <OutlinedInput
              id="password"
              type={showPassword ? "text" : "password"}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleClickShowPassword}
                    edge="end"
                  >
                    {showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
              label="Password"
              onChange={(e) => setPassword(e.target.value)}
              onKeyDown={handleKeyPressEnter}
            />
          </FormControl>

          <FormControl>
            <Button
              size="md"
              color="primary"
              className="submit-login"
              onClick={handleSubmit}
              onKeyDown={handleKeyPressEnter}
            >
              Submit
            </Button>
          </FormControl>
        </div>
      </div>

      <div className="small-ellipse"></div>

      <div className="small-rec"></div>
    </div>
  );
};

export default Login;
