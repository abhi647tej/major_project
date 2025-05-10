import React, { useState } from "react";
import {
    FaBars, FaHome, FaExclamationTriangle, FaHistory,
    FaUsers, FaCog, FaSignOutAlt
} from "react-icons/fa";
import { Link } from "react-router-dom";
import "./Sidebar.css";

const Sidebar = () => {
    const [isOpen, setIsOpen] = useState(false);

    const toggleSidebar = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className="sidebar-container">
            {/* Hamburger Menu */}
            <div className="hamburger" onClick={toggleSidebar}>
                <FaBars />
            </div>

            {/* Sidebar Menu */}
            <nav className={`sidebar ${isOpen ? "open" : ""}`}>
                {/* <ul>
                    <li><FaHome /><span>Dashboard</span></li>
                    <li><FaExclamationTriangle /><span>Suspicious Chats</span></li>
                    <li><FaHistory /><span>All Chats History</span></li>
                    <li><FaUsers /><span>User Management</span></li>
                    <li><FaCog /><span>Settings</span></li>
                    <li><FaSignOutAlt /><span>Logout</span></li>
                </ul> */}
            <ul>
                <li><FaHome /><Link to="/" onClick={toggleSidebar}>Dashboard</Link></li>
                <li><FaExclamationTriangle /><Link to="/suspicious-chats" onClick={toggleSidebar}>Suspicious Chats</Link></li>
                <li><FaHistory /><Link to="/history" onClick={toggleSidebar}>All Chats History</Link></li>
                <li><FaUsers /><Link to="/users" onClick={toggleSidebar}>User Management</Link></li>
                <li><FaCog /><Link to="/settings" onClick={toggleSidebar}>Settings</Link></li>
                <li><FaSignOutAlt /><Link to="/logout" onClick={toggleSidebar}>Logout</Link></li>
            </ul>
            </nav>
        </div>
    );
};

export default Sidebar;


// import React from "react";
// import { Link } from "react-router-dom";
// import "./Sidebar.css";

// const Sidebar = ({ isOpen, toggleSidebar }) => {
//     return (
//         <div className={`sidebar ${isOpen ? "open" : ""}`}>
//             <button className="close-btn" onClick={toggleSidebar}>✖</button>
//             <h2>📊 Menu</h2>
//             <ul>
//                 <li><Link to="/" onClick={toggleSidebar}>🏠 Dashboard</Link></li>
//                 <li><Link to="/suspicious-chats" onClick={toggleSidebar}>🚨 Suspicious Chats</Link></li>
//                 <li><Link to="/history" onClick={toggleSidebar}>📜 All Chats History</Link></li>
//                 <li><Link to="/users" onClick={toggleSidebar}>👤 User Management</Link></li>
//                 <li><Link to="/settings" onClick={toggleSidebar}>⚙️ Settings</Link></li>
//                 <li><Link to="/logout" onClick={toggleSidebar}>🚪 Logout</Link></li>
//             </ul>
//         </div>
//     );
// };

// export default Sidebar;
