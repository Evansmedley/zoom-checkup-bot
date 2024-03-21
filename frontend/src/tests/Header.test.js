import React from "react";
import ReactDOM from "react-dom";
import Header from "../components/Header";
import { shallow, configure } from "enzyme";
import Adapter from "enzyme-adapter-react-16";

configure({ adapter: new Adapter() });

describe("Test header", () => {
  it("Renders without crashing", () => {
    const div = document.createElement("div");
    ReactDOM.render(<Header />, div);
  });

  //   it("renders a MaterialUI Login Button", () => {
  //     const app = { setState: jest.fn() };
  //     const wrapper = shallow(<Header />);
  //     wrapper.find("login-button").at(0).simulate("click");
  //     expect(wrapper.length).to
  //     expect(app.setState).toHaveProperty("callCount", 1);
  //   });
});
