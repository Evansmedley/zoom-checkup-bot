import '../assets/Home.css';
import armPic from '../assets/images/arm.png'


const Home = () => {

    return(
        <div className="bg-sphere">

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

            <div className="page-content">
                <div className="text">
                    <div id="mainText">
                        Your Remote Doctor is here to assist
                    </div>


                    <div id="subText">
                        Get your hands-on doctors appointment from the convenience of your home.
                    </div>
                </div>


                <img src={armPic} className="robot-pic" alt="arm" />
            
            </div>
        </div>
    )
};

export default Home;