import '../assets/Login.css';
import mainRectange from '../assets/images/login-rectangle-main.png'
import smallRectange from '../assets/images/login-rectangle-small.png'
import smallEllipse from '../assets/images/login-ellipse-small.png'
import Header from './Header';


const Login = () => {

    return(
        <div>
            <Header />
            <div className="main-rec">
                <form>
                    <label>
                        Name:
                        <input type="text" name="name" />
                    </label>
                    <input type="submit" value="Submit" />
                </form>
                <img src={mainRectange} className="center-rec" alt="main-rectangle" />

            </div>

            <img src={smallEllipse} className="small-ellipse" alt="small-ellipse" />
            <img src={smallRectange} className="small-rec" alt="small-rectangle" />
        </div>


    )
};

export default Login;