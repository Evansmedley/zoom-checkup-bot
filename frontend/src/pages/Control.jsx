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
import debounce from "lodash/debounce";
import { useRef } from "react";
import NoPhotographyIcon from "@mui/icons-material/NoPhotography";
import { useMemo } from "react";

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


  useEffect(() => {
    console.log("rerender: ", armEndpoint);
  }, [armEndpoint]);

  // ----------------SLIDER DEBOUNCE-------------------

  const sendSliderMessage = () => {
    console.log(
      "new slider fetch: ",
      `${armEndpoint}/changeSlider`
    );
    console.log("slider value: ", slider);
    
    let startTime = performance.now();
    fetch(`${armEndpoint}/changeSlider`, {
      method: "POST",
      body: JSON.stringify({
        move: parseInt(slider),
      }),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAuthToken()}`,
      },
    }).catch((err) => {
      console.error(err);
    })
    setEndpointLatency(`${performance.now() - startTime} ms`);
  };

  const sliderRef = useRef(sendSliderMessage);

  useEffect(() => {
    sliderRef.current = sendSliderMessage;
  }, [armEndpoint, slider]);

  const useSliderDebounce = () => {
    const debouncedCallback = useMemo(() => {
      const func = () => {
        sliderRef.current?.();
      };
      return debounce(func, 50);
    }, []);

    return debouncedCallback;
  };

  const newSliderDebounce = useSliderDebounce(sendSliderMessage);

  // ----------------ARM DEBOUNCE-------------------

  const sendArmMessage = () => {
    console.log("new arm endpoint new: ", arm);
    console.log(
      "new fetch: ",
      `${armEndpoint}/changeArm`
    );

    let startTime = performance.now();
    fetch(`${armEndpoint}/changeArm`, {
      method: "POST",
      body: JSON.stringify({
        arm: parseInt(arm),
      }),
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${getAuthToken()}`,
      },
    }).catch((err) => {
      console.error(err);
    })
    .then((response) => response.json())
    .then((data) => setSlider(data.currentAngle));
    setEndpointLatency(`${performance.now() - startTime} ms`)
  };
  const armRef = useRef(sendArmMessage);

  useEffect(() => {
    armRef.current = sendArmMessage;
  }, [armEndpoint, arm]);

  const useArmDebounce = () => {
    const debouncedCallback = useMemo(() => {
      const func = () => {
        armRef.current?.();
      };
      return debounce(func, 50);
    }, []);

    return debouncedCallback;
  };

  const newArmDebounce = useArmDebounce(sendArmMessage);

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
      console.log("in pre: ", armEndpoint);
      setArm(newValue);
      handleLabel(newValue);
      newArmDebounce();
      // debounceArm.current?.(newValue, armEndpoint);
    }
  };

  const handleChangeSlider = (event, newValue) => {
    setSlider(newValue);
    newSliderDebounce();
    // debounceSlider.current?.(newValue);
  };

  const handleRobotEndpoint = (event) => {
    setSelectRobotEndpointObject(event.target.value);
    console.log(event.target.value)
    setEndpointLatencyDisabled(false)
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

  const [endpointLatency, setEndpointLatency] = useState("-");
  const [endpointLatencyDisabled, setEndpointLatencyDisabled] = useState(true);

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
            <TextField
              disabled={endpointLatencyDisabled}
              size="small"
              id="endpoint-latency"
              label="Endpoint Latency"
              defaultValue="-"
              value={endpointLatency}
              variant="outlined"
              color="success"
              InputProps={{readOnly: true}}
              style={{ width: '50%', margin: 'auto'}}
            />
        </div>
      </div>
    </div>
  );
};

export default Control;
