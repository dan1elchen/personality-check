import "../css/Result.css";
import React from "react";
import Navbar from "./Navbar";

function Result() {
  return (
    <div class="Result">
      <Navbar />
      <div class="Profile">
        {/* <img src="default.jpg"></img> */}
        <p class="username">Daniel Chen</p>
      </div>
      <div class="output">
        <p>ISTJ</p>
        <p>96% MATCH</p>
        <p>Description</p>
      </div>
    </div>
  );
}

export default Result;
