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

  const UP = "UP";
  const RIGHT = "RIGHT";
  const DOWN = "DOWN";
  const LEFT = "LEFT";

  const [selectedArrow, setSelectedArrow] = useState("No State");

  const buttonClick = (selectedDiv) => {
    setSelectedArrow(selectedDiv);
  };

  document.addEventListener("keydown", (event) => {
    if (event.isComposing || event.key === "a" || event.key === "A") {
      setSelectedArrow(LEFT);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.isComposing || event.key == "d" || event.key === "D") {
      setSelectedArrow(RIGHT);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.isComposing || event.key === "w" || event.key === "W") {
      setSelectedArrow(UP);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.isComposing || event.key === "s" || event.key === "S") {
      setSelectedArrow(DOWN);
    }
  });

  return (
    <div className="main-control">
      <div className="column left">
        <p>*Add livestream here*</p>

        <p>Current state: {selectedArrow}</p>

        <div className="xy arrow">
          {/* first row */}

          <div className="spacer"></div>
          <img
            className={`arrow up ${
              selectedArrow === UP ? " selected" : undefined
            }`}
            src={"/assets/images/arrow.png"}
            alt="up-arrow"
            onClick={() => buttonClick(UP)}
          />
          <div className="spacer"></div>

          {/* second row */}

          <img
            className={`arrow left ${
              selectedArrow === LEFT ? " selected" : undefined
            }`}
            src={"/assets/images/arrow.png"}
            alt="left-arrow"
            onClick={() => buttonClick(LEFT)}
          />

          <div className="spacer"></div>

          <img
            className={`arrow right ${
              selectedArrow === RIGHT ? " selected" : undefined
            }`}
            src={"/assets/images/arrow.png"}
            alt="right-arrow"
            onClick={() => buttonClick(RIGHT)}
          />

          {/* third row */}

          <div className="spacer"></div>
          <img
            className={`arrow down ${
              selectedArrow === DOWN ? " selected" : undefined
            }`}
            src={"/assets/images/arrow.png"}
            alt="down-arrow"
            onClick={() => buttonClick(DOWN)}
          />
          <div className="spacer"></div>
        </div>
      </div>
      <div className="column">
        Notes <br />
        <textarea
          id="notes"
          className="notes"
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
    </div>
  );
};

export default Control;
