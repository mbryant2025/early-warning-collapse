// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAw3Q4yx8pN98zY9T_Ce8Rb0tex96uB6CI",
  authDomain: "early-warning-collapse.firebaseapp.com",
  databaseURL: "https://early-warning-collapse-default-rtdb.firebaseio.com",
  projectId: "early-warning-collapse",
  storageBucket: "early-warning-collapse.appspot.com",
  messagingSenderId: "766245415822",
  appId: "1:766245415822:web:7ae5aa8f1dfd9782cc92df",
  measurementId: "G-HZDW0704TX",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

export const db = getDatabase(app);