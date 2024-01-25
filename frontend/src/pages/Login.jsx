
const Login = () => {

    return(
        <div>
            <div className="main-rec">
            {/* <img src={mainRectange} alt="main-rectangle" /> */}

                <div id="sign-in">
                
                    <div id="title">
                        Doctor Sign In Portal
                    </div>
                    <form>
                        <label>
                            Username/CPSO ID:
                            <input type="text" name="username" />
                        </label>
                        <label>
                            Password:
                            <input type="text" name="password" />
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
};

export default Login;