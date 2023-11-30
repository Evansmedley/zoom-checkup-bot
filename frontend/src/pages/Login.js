import '../assets/Login.css';
import mainRectange from '../assets/images/login-rectangle-main.png'
import smallRectange from '../assets/images/login-rectangle-small.png'
import smallEllipse from '../assets/images/login-ellipse-small.png'

const Login = () => {

    return(
        <div>
            <div className="App-group">
                <a className="App-link" href="/">
                    Home
                    </a>
                    <a className="App-link" href="/contact">
                    Contact
                    </a>
                    <a className="App-link" href="/login">
                    Log In
                    </a>
            </div>


            <div className="shapes">
                <img src={smallEllipse} className="small-ellipse" alt="small-ellipse" />
                <img src={smallRectange} className="small-rec" alt="small-rectangle" />
                <img src={mainRectange} className="main-rec" alt="main-rectangle" />


            </div>
        </div>


    )
};

export default Login;