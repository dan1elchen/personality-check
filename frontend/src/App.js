import "./App.css";
import ReactDOM from "react-dom";
import Home from "./components/Home";
import Load from "./components/Load";
import Result from "./components/Result";
import Navbar from "./Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/load" element={<Load />} />
        <Route path="/result" element={<Result />} />
      </Routes>
    </Router>
  );
}

export default App;
