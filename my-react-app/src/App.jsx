import React from "react";
import "./App.css";
import Camera from "./Camera";
import Text from "./Text";

function App() {
  return (
    <div className="app">
      <div className="split-screen">
        <Camera />
        <Text />
      </div>
    </div>
  );
}

export default App;
