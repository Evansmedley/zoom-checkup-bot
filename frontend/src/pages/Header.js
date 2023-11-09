import { Outlet, Link, BrowserRouter } from "react-router-dom";
import { Routes, Route } from "react-router-dom";
import { Router } from "react-router-dom";

import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import MenuIcon from "@mui/icons-material/Menu";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Tooltip from "@mui/material/Tooltip";
import MenuItem from "@mui/material/MenuItem";
import AdbIcon from "@mui/icons-material/Adb";
import { MenuList } from "@mui/material";

import Home from "./Home";
import Contact from "./Contact";
import Login from "./Login";

// const pages = ['Home', 'Contact', 'Log In'];
const settings = ["Profile", "Account", "Dashboard", "Logout"];

function Header() {
  const [anchorElNav, setAnchorElNav] = React.useState(null);
  const [anchorElUser, setAnchorElUser] = React.useState(null);

  const handleOpenNavMenu = (event) => {
    setAnchorElNav(event.currentTarget);
  };
  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseNavMenu = () => {
    setAnchorElNav(null);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  return (
    <BrowserRouter>
      <AppBar position="static" className="header-style">
        <Container maxWidth="xl">
          <Toolbar disableGutters>
            <Box sx={{ flexGrow: 1, display: { xs: "flex", md: "none" } }}>
              <IconButton
                size="large"
                aria-label="account of current user"
                aria-controls="menu-appbar"
                aria-haspopup="true"
                onClick={handleOpenNavMenu}
                color="black"
              >
                <MenuIcon />
              </IconButton>
              <Menu
                id="menu-appbar"
                anchorEl={anchorElNav}
                anchorOrigin={{
                  vertical: "bottom",
                  horizontal: "left",
                }}
                keepMounted
                transformOrigin={{
                  vertical: "top",
                  horizontal: "left",
                }}
                open={Boolean(anchorElNav)}
                onClose={handleCloseNavMenu}
                sx={{
                  display: { xs: "block", md: "none" },
                }}
              >
                <MenuList>
                  <Link
                    to="/"
                    style={{ textDecoration: "none", display: "block" }}
                  >
                    <MenuItem>Home</MenuItem>
                  </Link>
                  <Link
                    to="/contact"
                    style={{ textDecoration: "none", display: "block" }}
                  >
                    <MenuItem>Contact</MenuItem>
                  </Link>
                  <Link
                    to="/login"
                    style={{ textDecoration: "none", display: "block" }}
                  >
                    <MenuItem>Log In</MenuItem>
                  </Link>
                </MenuList>

                {/* {pages.map((page) => (
                <MenuItem key={page} onClick={handleCloseNavMenu}>
                  <Typography textAlign="center">{page}</Typography>
                </MenuItem>
              ))} */}
              </Menu>
            </Box>

            <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
              <Link to="/" style={{ textDecoration: "none", display: "block" }}>
                <MenuItem>Home</MenuItem>
              </Link>
              <Link
                to="/contact"
                style={{ textDecoration: "none", display: "block" }}
              >
                <MenuItem>Contact</MenuItem>
              </Link>
              <Link
                to="/login"
                style={{ textDecoration: "none", display: "block" }}
              >
                <MenuItem>Log In</MenuItem>
              </Link>

              {/* {pages.map((page) => (
              <Button
                key={page}
                onClick={handleCloseNavMenu}
                sx={{ my: 2, color: 'black', display: 'block' }}
              >
                {page}
              </Button>
            ))} */}
            </Box>

            <Box sx={{ flexGrow: 0 }}>
              <Tooltip title="Open settings">
                <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                  <Avatar alt="Remy Sharp" src="/static/images/avatar/2.jpg" />
                </IconButton>
              </Tooltip>
              <Menu
                sx={{ mt: "45px" }}
                id="menu-appbar"
                anchorEl={anchorElUser}
                anchorOrigin={{
                  vertical: "top",
                  horizontal: "right",
                }}
                keepMounted
                transformOrigin={{
                  vertical: "top",
                  horizontal: "right",
                }}
                open={Boolean(anchorElUser)}
                onClose={handleCloseUserMenu}
              >
                {settings.map((setting) => (
                  <MenuItem key={setting} onClick={handleCloseUserMenu}>
                    <Typography textAlign="center">{setting}</Typography>
                  </MenuItem>
                ))}
              </Menu>
            </Box>
          </Toolbar>
        </Container>
      </AppBar>

      <Routes>
        <Route path="/" element={<Home />}>
          <Route path="login" element={<Login />} />
          <Route path="contact" element={<Contact />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );

  // return (
  //   <BrowserRouter>
  //     <Routes>
  //       <Route path="/" element={<Home />}>
  //         <Route path="login" element={<Login />} />
  //         <Route path="contact" element={<Contact />} />
  //       </Route>
  //   </Routes>

  //     <nav>
  //       <ul>
  //           <Link to="/">Home</Link>
  //           <Link to="/login">Login</Link>
  //           <Link to="/contact">Contact</Link>
  //       </ul>
  //     </nav>

  //     <Outlet />
  //   </BrowserRouter>
  // )
}

export default Header;
