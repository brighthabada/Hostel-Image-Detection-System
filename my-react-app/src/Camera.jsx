// my-react-app/src/Camera.jsx
import React, { useRef, useEffect } from "react";
import "./Camera.css"; // Import the CSS file

function Camera() {
  const videoRef = useRef(null);

  useEffect(() => {
    const getUserMedia = async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: true,
        });
        if (videoRef.current) {
          videoRef.current.srcObject = stream;
        }
      } catch (err) {
        console.error("Error accessing camera: ", err);
      }
    };

    getUserMedia();
  }, []);

  return (
    <div className="camera">
      <video ref={videoRef} autoPlay className="video" />
    </div>
  );
}

export default Camera;
