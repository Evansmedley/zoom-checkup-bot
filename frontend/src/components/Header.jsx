const Header = ({ login }) => {
  return (
    <div className="App-group">
      <a className="App-link" href="/">
        Home
      </a>
      <a className="App-link" href="/contact">
        Contact
      </a>
      {!login && (
        <a className="App-link" href="/login">
          Log In
        </a>
      )}
      {login && (
        <a className="App-link" href="/control">
          Control
        </a>
      )}
    </div>
  );
};

export default Header;
