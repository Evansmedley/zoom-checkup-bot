import { Button } from "@mui/material";
import { grey } from "@mui/material/colors";
import { createTheme, ThemeProvider } from "@mui/material/styles";

const Header = ({ login }) => {
  const headerColor = grey["A200"];
  const { palette } = createTheme();

  const theme = createTheme({
    palette: {
      headerColor: palette.augmentColor({
        color: {
          main: grey["900"],
        },
      }),
    },
  });

  return (
    <ThemeProvider theme={theme}>
      <div className="App-group left">
        <div>
          <Button
            className="App-link"
            href="/"
            color="headerColor"
            size="large"
          >
            Home
          </Button>
          <Button
            className="App-link"
            href="/contact"
            color="headerColor"
            size="large"
          >
            Contact
          </Button>
          {login && (
            <Button
              className="App-link"
              href="/control"
              color="headerColor"
              size="large"
              id="login-button"
            >
              Control
            </Button>
          )}
        </div>
        <div className="right">
          {!login && (
            <Button href="/login" color="headerColor" size="large">
              Log In
            </Button>
          )}
        </div>
      </div>
    </ThemeProvider>
  );
};

export default Header;
