import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Sidebar from "./Sidebar";
import Dashboard from "./Dashboard";
import SuspiciousChats from "./SuspiciousChats";
import AllChatsHistory from './AllChatsHistory'; // Future Page
import "./App.css";

function App() {
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);

    const toggleSidebar = () => {
        setIsSidebarOpen(!isSidebarOpen);
    };

    return (
        <Router>
            <div className="App">
                <Sidebar isOpen={isSidebarOpen} toggleSidebar={toggleSidebar} />
                
                {/* Overlay when sidebar is open */}
                {isSidebarOpen && <div className="overlay" onClick={toggleSidebar}></div>}

                <div className="main-content">
                    <Routes>
                        <Route path="/" element={<Dashboard />} />
                        <Route path="/suspicious-chats" element={<SuspiciousChats />} />
                        <Route path="/history" element={<AllChatsHistory />} />
                    </Routes>
                </div>
            </div>
        </Router>
    );
}

export default App;
