import React, { useEffect, useState } from "react";
import { db } from "./utils/firebase";
import { ref, onValue } from "firebase/database";
import "./App.css";

function App() {
  const [flexState, setFlexState] = useState(0);

  useEffect(() => {
    const flexStateRef = ref(db, "ESP1/FlexSensor");
    onValue(flexStateRef, (snapshot) => {
      console.log(snapshot);
      const newState = snapshot.val();
      setFlexState(newState);
    });
  }, []);

  return (
    <div>
      <h1>Sensor Reading Test</h1>
      <h4>Sensor Data is collected by the ESP32 and stored in a Firebase Realtime Database. This app is set up to detect changes in the database and update the value accordingly.</h4>
      <p>Flex Sensor Reading: {flexState}</p>
    </div>
  );
}

export default App;
