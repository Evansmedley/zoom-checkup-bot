import Button from "@mui/joy/Button";
import { FormControl } from "@mui/material";
import TextField from "@mui/material/TextField";
import InputLabel from "@mui/material/InputLabel";
import Input from "@mui/material/Input";
import OutlinedInput from "@mui/material/OutlinedInput";

const Login = () => {
  return (
    <div>
      <div className="main-rec">
        <div id="title">Doctor Sign In Portal</div>

        <div id="form">
          <FormControl fullWidth>
            <InputLabel htmlFor="username">Username/CPSO ID</InputLabel>
            <OutlinedInput id="username" label="Username/CPSO ID" />
          </FormControl>

          <FormControl fullWidth>
            <InputLabel htmlFor="password">Password</InputLabel>
            <OutlinedInput id="password" label="Password" />
          </FormControl>

          <Button size="md" color="primary" className="submit-login">
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
