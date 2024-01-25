import * as React from 'react'
import { request, setAuthHeader } from '../axios_helper';

export default class Login extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            cpsoId: "",
            password: "",
        };
    }

    onChangeHandler = (event) => {
        let name = event.target.name;
        let value = event.target.value;
        this.setState({[name]: value});
    }

    onSubmitLogin = (e, cpsoId, password) => {
        e.preventDefault();
        request(
            "POST",
            "/login",
            {
                cpsoId: cpsoId,
                password: password
            }).then(
            (response) => {
                setAuthHeader(response.data.token);
            }).catch(
            (error) => {
                setAuthHeader(null);
            }
        );
    }

    render() {
        return(
            <div>
                <div className="main-rec">
                {/* <img src={mainRectange} alt="main-rectangle" /> */}

                    <div id="sign-in">
                    
                        <div id="title">
                            Doctor Sign In Portal
                        </div>
                        <form onSubmit={this.onSubmitLogin}>
                            <label>
                                Username/CPSO ID:
                                <input type="text" name="cpsoId" onChange={this.onChangeHandler}/>
                            </label>
                            <label>
                                Password:
                                <input type="text" name="password" onChange={this.onChangeHandler}/>
                            </label>
                            <input type="submit" value="Submit"/>
                        </form>

                    </div>
                </div>

                <div className="small-ellipse">
                </div>

                <div className="small-rec">
                </div>

                {/* <img src={smallEllipse} className="small-ellipse" alt="small-ellipse" /> */}
                {/* <img src={smallRectange} className="small-rec" alt="small-rectangle" /> */}
            </div>
        )
    }
};