import logo from './logo.svg';
import './App.css';
import ReactDOM from "react-dom";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import Home from './components/Home';

function App() {
  return (
    <div className="App">
      <Home></Home>
    </div>
  );
}

export default App;
