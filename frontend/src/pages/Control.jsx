import Slider from "@mui/material/Slider";
import * as React from "react";
import Button from "@mui/joy/Button";
import ToggleButtonGroup from "@mui/joy/ToggleButtonGroup";
import { ListItemText, TextField } from "@mui/material";
import Input from "@mui/material/Input";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import Chip from "@mui/material/Chip";

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

  const [robotEndpoint, setRobotEndpoint] = React.useState("");

  const handleChange = (event) => {
    setRobotEndpoint(event.target.value);
  };

  const allRobotEndpoints = ["endpoint1", "endpoint2", "endpoint3"];

  return (
    <div className="main">
      <div className="column">
        <p>*Add livestream here*</p>
        <p>Current arm: {arm}</p>
        <p>Current state: {slider}</p>

        <FormControl sx={{ m: 1, minWidth: 120 }}>
          <InputLabel id="demo-simple-select-helper-label" color="success">
            Endpoint
          </InputLabel>
          <Select
            className="endpoint-option"
            value={robotEndpoint}
            label="Endpoint"
            onChange={handleChange}
            color="success"
          >
            {allRobotEndpoints.map((robotEndpointOption) => (
              <MenuItem
                className="endpoint-option"
                key="robotEndpoint"
                value={robotEndpointOption}
              >
                <Chip label="Active" color="success" size="small" />
                <ListItemText primary={robotEndpointOption} />
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </div>

      <div className="column right">
        <TextField
          id="notes"
          label="Notes"
          multiline
          rows={12}
          fullWidth
          download="final_notes"
          variant="outlined"
          color="success"
        />
        <div className="save">
          <Input
            required
            id="filename"
            className="filename"
            placeholder="Name"
            color="success"
          />

          <Button
            className="saveBtn"
            onClick={download}
            variant="soft"
            size="md"
            color="success"
          >
            Download
          </Button>
        </div>

        <div className="arm-controls">
          <ToggleButtonGroup
            className="buttonGroup"
            value={arm}
            onChange={handleChangeArm}
            size="md"
            spacing={1}
          >
            <Button value="one">1</Button>
            <Button value="two">2</Button>
            <Button value="three">3</Button>
            <Button value="four">4</Button>
            <Button value="five">5</Button>
            <Button value="six">6</Button>
          </ToggleButtonGroup>

          <Slider
            aria-label="Default"
            valueLabelDisplay="auto"
            value={slider}
            onChange={handleChangeSlider}
            marks={marks}
            color="success"
          />
        </div>
      </div>
    </div>
  );
};

export default Control;
