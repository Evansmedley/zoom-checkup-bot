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
import { useState, useEffect } from "react";
import { getAuthToken } from "../axios_helper";
import Header from "../components/Header";

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

  const [arm, setArm] = useState("1");
  const [leftLabel, setLeftLabel] = useState("Left");
  const [rightLabel, setRightLabel] = useState("Right");
  const [slider, setSlider] = useState(30);

  const [allRobotEndpoints, setAllRobotEndpoints] = useState([]);
  const [selectRobotEndpointObject, setSelectRobotEndpointObject] =
    useState("");
  const [streamURL, setStreamURL] = useState("");

  const marks = [
    {
      value: 0,
      label: leftLabel,
    },
    {
      value: 180,
      label: rightLabel,
    },
  ];

  useEffect(() => {
    if (selectRobotEndpointObject.uuid !== undefined) {
      handleChangeArm(null, "1");
    }
  }, [selectRobotEndpointObject]);

  useEffect(() => {
    console.log("triggered");
    getEndpoints();
  }, []);

  const getEndpoints = () => {
    fetch("/endpoint", {
      headers: { Authorization: `Bearer ${getAuthToken()}` },
    })
      .then((response) => response.json())
      .then((data) => setAllRobotEndpoints(data));
  };

  const handleLabel = (newArm) => {
    if (newArm === "1") {
      setLeftLabel("Left");
      setRightLabel("Right");
    } else if (newArm === "5") {
      setLeftLabel("Counter");
      setRightLabel("Clockwise");
    } else if (newArm === "6") {
      setLeftLabel("Close");
      setRightLabel("Open");
    } else if (newArm === "2" || newArm === "3" || newArm === "4") {
      setLeftLabel("Down");
      setRightLabel("Up");
    }
  };

  const handleChangeArm = (event, newArm) => {
    if (newArm != null) {
      fetch(`/changeArm/${selectRobotEndpointObject.uuid}`, {
        method: "POST",
        body: JSON.stringify({
          arm: parseInt(newArm),
        }),
        headers: {
          "Content-Type": "application/json",
        },
      }).catch((err) => {
        console.error(err);
      });
      setArm(newArm);
      handleLabel(newArm);
    }
  };

  const handleChangeSlider = (event, newValue) => {
    fetch(`/changeSlider/${selectRobotEndpointObject.uuid}`, {
      method: "POST",
      body: JSON.stringify({
        move: parseInt(newValue),
      }),
      headers: {
        "Content-Type": "application/json",
      },
    }).catch((err) => {
      console.error(err);
    });
    setSlider(newValue);
  };

  const handleRobotEndpoint = (event) => {
    setSelectRobotEndpointObject(event.target.value);
    setStreamURL("http://" + event.target.value.ip + ":5000/stream.mjpg");
  };

  const getStatusColour = (status) => {
    if (status) {
      return "success";
    } else {
      return "error";
    }
  };

  const getStatusLabel = (status) => {
    if (status) {
      return "Active";
    } else {
      return "Inactive";
    }
  };

  return (
    <div>
      <Header login={true} />
      <div className="main">
        <div className="column">
          <span>Current arm: {arm}</span>
          <span>Current state: {slider}</span>
          {streamURL && (
            <img
              id="camera-stream"
              src={streamURL}
              // width="640"
              // height="480"
              alt="Select the Robot in the Endpoint drop-down menu"
            />
          )}
          <FormControl size="small" className="drop-down">
            <InputLabel id="demo-simple-select-helper-label" color="primary">
              Endpoint
            </InputLabel>
            <Select
              className="endpoint-option"
              value={selectRobotEndpointObject.name}
              label="Endpoint"
              onChange={handleRobotEndpoint}
              onOpen={getEndpoints}
              color="primary"
            >
              {allRobotEndpoints.map((robotEndpointOption) => (
                <MenuItem
                  className="endpoint-option"
                  key={robotEndpointOption.uuid}
                  value={robotEndpointOption}
                >
                  <Chip
                    small="small"
                    label={getStatusLabel(robotEndpointOption.active)}
                    color={getStatusColour(robotEndpointOption.active)}
                    size="small"
                  />
                  <ListItemText primary={robotEndpointOption.name} />
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
            min={0}
            max={180}
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
              <Button value="1">1</Button>
              <Button value="2">2</Button>
              <Button value="3">3</Button>
              <Button value="4">4</Button>
              <Button value="5">5</Button>
              <Button value="6">6</Button>
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
    </div>
  );
};

export default Control;
