import './assets/App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import ReactDOM from "react-dom/client" 

import Home from './pages/Home';
import Login from './pages/Login';
import Contact from './pages/Contact';
import Layout from './pages/Layout';


export default function App() {
  return (

    <BrowserRouter>
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Home />} />
        <Route path="contact" element={<Contact />} />
        <Route path="login" element={<Login />} />
      </Route>
    </Routes>
  </BrowserRouter>
    
  );
}

// const root = ReactDOM.createRoot(document.getElementById('root'));
// root.render(<App />);


