// import * as React from 'react'
// import { request, setAuthHeader } from '../axios_helper';

// export default class Login extends React.Component {

//     constructor(props) {
//         super(props);
//         this.state = {
//             cpsoNumber: "",
//             password: "",
//         };
//     }

//     onChangeHandler = (event) => {
//         let name = event.target.name;
//         let value = event.target.value;
//         this.setState({[name]: value});
//     }

//     onSubmitLogin = (e, cpsoNumber, password) => {
//         e.preventDefault();
//         request(
//             "POST",
//             "/api/auth/authenticate",
//             {
//                 cpsoNumber: cpsoNumber,
//                 password: password
//             }).then(
//             (response) => {
//                 setAuthHeader(response.data.token);
//             }).catch(
//             (error) => {
//                 setAuthHeader(null);
//             }
//         );
//     }

//     render() {
//         return(
//             <div>
//                 <div className="main-rec">
//                     {/* <img src={mainRectange} alt="main-rectangle" /> */}

//                     <div id="sign-in">

//                         <div id="title">
//                             Doctor Sign In Portal
//                         </div>
//                         <form onSubmit={this.onSubmitLogin}>
//                             <label>
//                                 Username/CPSO ID:
//                                 <input type="text" name="cpsoNumber" onChange={this.onChangeHandler}/>
//                             </label>
//                             <label>
//                                 Password:
//                                 <input type="text" name="password" onChange={this.onChangeHandler}/>
//                             </label>
//                             <input type="submit" value="Submit"/>
//                         </form>

//                     </div>
//                 </div>

//                 <div className="small-ellipse">
//                 </div>

//                 <div className="small-rec">
//                 </div>

//                 {/* <img src={smallEllipse} className="small-ellipse" alt="small-ellipse" /> */}
//                 {/* <img src={smallRectange} className="small-rec" alt="small-rectangle" /> */}
//             </div>
//         )
//     }
// };

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
