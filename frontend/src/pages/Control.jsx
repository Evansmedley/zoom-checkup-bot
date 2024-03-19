import Slider from "@mui/material/Slider";
import * as React from "react";
import Button from "@mui/joy/Button";
import ToggleButtonGroup from "@mui/joy/ToggleButtonGroup";
import { Icon, ListItemText, TextField } from "@mui/material";
import Input from "@mui/material/Input";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";
import Chip from "@mui/material/Chip";
import { useState, useEffect } from "react";
import { getAuthToken } from "../axios_helper";
import Header from "../components/Header";
import debounce from "lodash/debounce";
import { useRef } from "react";
import NoPhotographyIcon from "@mui/icons-material/NoPhotography";

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
  const [rangeMax, setRangeMax] = useState(180);
  const [slider, setSlider] = useState(30);

  const [allRobotEndpoints, setAllRobotEndpoints] = useState([]);
  const [selectRobotEndpointObject, setSelectRobotEndpointObject] =
    useState("");
  const [streamURL, setStreamURL] = useState("");
  const [armEndpoint, setArmEndpoint] = useState("");

  const marks = [
    {
      value: 0,
      label: leftLabel,
    },
    {
      value: rangeMax,
      label: rightLabel,
    },
  ];

  useEffect(() => {
    getEndpoints();
    if (selectRobotEndpointObject.uuid !== undefined) {
      handleChangeArm(null, "1");
    }
  }, []);

  const debounceSlider = useRef(
    debounce((newValue) => {
      console.log("Changed value:", newValue);

      fetch(`${armEndpoint}/changeSlider/${selectRobotEndpointObject.uuid}`, {
        method: "POST",
        body: JSON.stringify({
          move: parseInt(newValue),
        }),
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${getAuthToken()}`,
        },
      }).catch((err) => {
        console.error(err);
      });
    }, 100)
  );

  const debounceArm = useRef(
    debounce((newValue) => {
      console.log("Changed arm:", newValue);

      fetch(`${armEndpoint}/changeArm/${selectRobotEndpointObject.uuid}`, {
        method: "POST",
        body: JSON.stringify({
          arm: parseInt(newValue),
        }),
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${getAuthToken()}`,
        },
      }).catch((err) => {
        console.error(err);
      });
    }, 100)
  );

  const getEndpoints = () => {
    fetch("http://localhost:8080/endpoint", {
      headers: { Authorization: `Bearer ${getAuthToken()}` },
    })
      .then((response) => response.json())
      .then((data) => setAllRobotEndpoints(data));
  };

  const handleLabel = (newArm) => {
    switch (newArm) {
      case "1":
        setLeftLabel("Left");
        setRightLabel("Right");
        setRangeMax(180);
        break;
      case "2":
        setLeftLabel("Down");
        setRightLabel("Up");
        setRangeMax(180);
        break;
      case "3":
        setLeftLabel("Down");
        setRightLabel("Up");
        setRangeMax(180);
        break;
      case "4":
        setLeftLabel("Down");
        setRightLabel("Up");
        setRangeMax(180);
        break;
      case "5":
        setLeftLabel("Counter-Clockwise");
        setRightLabel("Clockwise");
        setRangeMax(270);
        break;
      case "6":
        setLeftLabel("Close");
        setRightLabel("Open");
        setRangeMax(180);
        break;
      default:
        break;
    }
  };

  const handleChangeArm = (event, newValue) => {
    if (newValue != null) {
      setArm(newValue);
      handleLabel(newValue);
      debounceArm.current?.(newValue);
    }
  };

  const handleChangeSlider = (event, newValue) => {
    setSlider(newValue);
    debounceSlider.current?.(newValue);
  };

  const handleRobotEndpoint = (event) => {
    setSelectRobotEndpointObject(event.target.value);
    setStreamURL("http://" + event.target.value.ip + ":5000/stream.mjpg");
    setArmEndpoint(
      "http://" + event.target.value.ip + ":" + event.target.value.port
    );
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
          {!streamURL && (
            <div className="no-stream-view">
              <NoPhotographyIcon></NoPhotographyIcon>
              <p>Please choose an endpoint</p>
            </div>
          )}

          {streamURL && (
            <img id="camera-stream" src={streamURL} alt="Stream error" />
          )}
          <div className="controls">
            <ToggleButtonGroup
              className="arm-buttons"
              value={arm}
              onChange={handleChangeArm}
              size="md"
              spacing={1}
              defaultValue="1"
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
              valueLabelDisplay="on"
              value={slider}
              onChange={handleChangeSlider}
              marks={marks}
              color="success"
              defaultValue={0}
              max={rangeMax}
              min={0}
            />
          </div>
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
      </div>
    </div>
  );
};

export default Control;
