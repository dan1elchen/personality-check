import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div>
      <h1>Personality Check!</h1>
      <form>
        <label>
          Please type in your instagram caption:
          <input type="text" caption="caption" />
        </label>
      </form>
      <Link to="/result">
        <button>Submit</button>
      </Link>
    </div>
  );
}

export default Home;
