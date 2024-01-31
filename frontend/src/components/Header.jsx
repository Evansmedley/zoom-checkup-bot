const Header = ({ login }) => {
  return (
    <div className="App-group left">
      <div>
        <a className="App-link" href="/">
          Home
        </a>
        <a className="App-link" href="/contact">
          Contact
        </a>
        {login && (
          <a className="App-link" href="/control">
            Control
          </a>
        )}
      </div>
      {!login && (
        <a className="App-link right" href="/login">
          Log In
        </a>
      )}
    </div>
  );
};

export default Header;
