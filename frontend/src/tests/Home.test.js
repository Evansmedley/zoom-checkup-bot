import React from "react";
import ReactDOM from "react-dom";
import Home from "../pages/Home.jsx";

describe("Test home page", () => {
  it("Renders without crashing", () => {
    const div = document.createElement("div");
    ReactDOM.render(<Home />, div);
  });
});
