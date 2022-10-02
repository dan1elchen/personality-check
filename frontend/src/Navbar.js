import "./css/Navbar.css";
import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <ul className="Navbar">
      <li>
        <Link to="/">Home</Link>
      </li>
      <li>
        <Link to="/result">Result</Link>
      </li>
    </ul>
  );
};
export default Navbar;
