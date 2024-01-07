import '../assets/Header.css';
import { Routes, Route } from "react-router-dom";
import Home from './Home';
import Login from './Login';
import Contact from './Contact';
import Layout from './Layout';


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
        </div>
        
        // <Routes>
        // <Route path="/" element={<Layout />}>
        //     <Route index element={<Home />} />
        //     <Route path="contact" element={<Contact />} />
        //     <Route path="login" element={<Login />} />
        // </Route>
        // </Routes>
    )
};

export default Header;