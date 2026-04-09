import { HashRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import SmartISM from "./pages/SmartISM";
import SmartISMInput from "./pages/SmartISMInput";
import SmartISMResult from "./pages/SmartISMResult";
import Bharat from "./pages/Bharat";
import PSI from "./pages/PSI";
import ISMSequence from "./pages/ISMSequence";
function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/smart-ism" element={<SmartISM />} />
        <Route path="/smart-ism/input" element={<SmartISMInput />} />
        <Route path="/smart-ism/result" element={<SmartISMResult />} />
        <Route path="/bharat" element={<Bharat />} />
        <Route path="/psi" element={<PSI />} />
        <Route path="/ism-seq" element={<ISMSequence />} />
      </Routes>
    </Router>
  );
}

export default App;
