import { Button } from "@mui/material";
import { grey } from "@mui/material/colors";

const Header = ({ login }) => {
  const headerColor = grey["A200"];
  console.log(headerColor);
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

        {/* <Button href="#text-buttons" color={headerColor}>
          Link
        </Button> */}
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
