import Slider from "@mui/material/Slider";
import * as React from "react";
import ToggleButton from "@mui/material/ToggleButton";
import ToggleButtonGroup from "@mui/material/ToggleButtonGroup";
import { useState } from "react";

const Control = () => {
  const download = () => {
    const noteContent = document.getElementById("notes").value;
    const filename = document.getElementById("filename").value || "final_notes";
    const blob = new Blob([noteContent], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = `${filename}.txt`;
    link.click();
  };

  const [arm, setArm] = useState("one");
  const [leftLabel, setLeftLabel] = useState("Left");
  const [rightLabel, setRightLabel] = useState("Right");

  const marks = [
    {
      value: 0,
      label: leftLabel,
    },
    {
      value: 100,
      label: rightLabel,
    },
  ];

  const handleLabel = (newArm) => {
    if (newArm === "one") {
      setLeftLabel("Left");
      setRightLabel("Right");
    } else if (newArm === "five") {
      setLeftLabel("Counter");
      setRightLabel("Clockwise");
    } else if (newArm === "six") {
      setLeftLabel("Close");
      setRightLabel("Open");
    } else if (newArm === "two" || newArm === "three" || newArm === "four") {
      setLeftLabel("Down");
      setRightLabel("Up");
    }
  };

  const handleChangeArm = (event, newArm) => {
    if (newArm !== null) {
      let data = {arm: newArm}
      fetch("/changeArm", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
          "Content-Type": "application/json",
        },
      }).catch((err) => {
        console.error(err);
      });
      setArm(newArm);
      console.log("setting arm: " + newArm);
      handleLabel(newArm);
    }
  };

  const [slider, setSlider] = useState(30);

  const handleChangeSlider = (event, newValue) => {
    fetch("/changeSlider", {
      method: "POST",
      body: JSON.stringify({
        move: newValue,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }).catch((err) => {
      console.error(err);
    });
    setSlider(newValue);
  };

  return (
    <div className="main-control">
      <div className="column left">
        <p>*Add livestream here*</p>

        <p>Current arm: {arm}</p>
        <p>Current state: {slider}</p>
      </div>

      <div className="column">
        <div className="notes">
          Notes <br />
          <textarea
            id="notes"
            rows="15"
            cols="70"
            placeholder="Write notes here..."
            download="final_notes"
          ></textarea>
          <br />
          <br />
          <button className="saveBtn" onClick={download}>
            {" "}
            Download
          </button>
          <input
            id="filename"
            className="filename"
            placeholder="Specify a filename…"
          />
        </div>
        <div>
          <ToggleButtonGroup
            color="primary"
            value={arm}
            exclusive
            onChange={handleChangeArm}
            aria-label="Platform"
          >
            <ToggleButton value="one">1</ToggleButton>,
            <ToggleButton value="two">2</ToggleButton>,
            <ToggleButton value="three">3</ToggleButton>,
            <ToggleButton value="four">4</ToggleButton>,
            <ToggleButton value="five">5</ToggleButton>,
            <ToggleButton value="six">6</ToggleButton>
          </ToggleButtonGroup>

          <div>
            <Slider
              aria-label="Default"
              valueLabelDisplay="auto"
              value={slider}
              onChange={handleChangeSlider}
              marks={marks}
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Control;
