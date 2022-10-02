import "../css/Home.css";
import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div class="Home">
      <div class="header">
        <h1>Personality Check!</h1>
        <img src={require("../assets/reddit.png")} width="120px" height="120px" alt="Cannot Display"/>
        <br></br>
      </div>
      <div class="form">
        <form>
          <label>
            Paste a link to a reddit post to get an in-depth sentiment analysis:
            <br></br>
            <input class="text-input" type="text" caption="caption" />
          </label>
        </form>
      </div>
      <div class="options">
        <Link to="/result">
          <button onClick={() => {}}>Submit</button>
        </Link>
      </div>
    </div>
  );
}

export default Home;
