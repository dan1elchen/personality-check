import "../css/Result.css";
import { React, useEffect, useState } from "react";
import Navbar from "./Navbar";
import axios from "axios";

function Result() {
  const [anaysis, setAnalysis] = useState("");
  const submitHandler = (e) => {
    e.preventDefault();
    axios({
      method: "GET",
    });
  };
  return (
    <div class="Result">
      <Navbar />
      <div class="output-header">
        {/* <img src="default.jpg"></img> */}
        <p class="username">Daniel Chen</p>
      </div>
      <div class="description info">
        <p>Description</p>
      </div>
      <div class="emojis">
        {/* <img
          src={require("../assets/positive.jpeg")}
          width="100px"
          height="100px"
        /> */}
      </div>
      <div class="info">
        <div class="text-info">0% Positive</div>
        <div class="text-info"> 72% Neutral </div>
        <div class="text-info">28% Negative</div>
      </div>
    </div>
  );
}

export default Result;
