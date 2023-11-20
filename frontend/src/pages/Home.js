import '../assets/Home.css';
import armPic from '../assets/images/arm.png'


const Home = () => {

    return(
        <div className="bg-image">

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

            <img src={armPic} className="App-logo" alt="arm" />
            
        </div>
    )
};

export default Home;