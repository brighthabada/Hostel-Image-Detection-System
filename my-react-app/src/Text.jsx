import React from "react";
import "./Text.css";
import hostelImage from "./assets/HIRRS_Form-1024.png";

function Text() {
  return (
    <div className="text">
      <h1>Welcome to Bani Hostel</h1>
      <p className="powered-by">powered by HIRRS</p>
      <p className="instructions">
        Look into the camera if you are a{" "}
        <span className="highlight">RETURNING VISITOR</span>. Scan the QR code
        if you are a <span className="highlight">NEW</span>.
      </p>
      <img src={hostelImage} alt="Bani Hostel" className="hostel-image" />
    </div>
  );
}

export default Text;
