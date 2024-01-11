import '../assets/Header.css';


const Header = () => {

    return(

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
        <a className="App-link" href="/control">
            Control
        </a>
        </div>
    )
};

export default Header;