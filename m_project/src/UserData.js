// import React, { useState } from "react";
// import {
//     BarChart,
//     Bar,
//     LineChart,
//     Line,
//     XAxis,
//     YAxis,
//     Tooltip,
//     Legend,
//     ResponsiveContainer,
// } from "recharts";
// import "./Dashboard.css";
// import { FaBars } from "react-icons/fa";

// const UserDetectionDashboard = () => {
//     const [isSidebarOpen, setSidebarOpen] = useState(false);

//     // Example static user data
//     const userData = [
//         { user_id: 1, username: "mahendra.kumar", first_name: "Mahendra", last_name: "Kumar", phone_number: "+91-847-1358", bio: "Admin", status: "Active", is_bot: false, language: "en", message_text: "Transfer, Plug, How much?" },
//         { user_id: 2, username: "abhijit.patil", first_name: "Abhijit", last_name: "Patil", phone_number: "+91-372-9453", bio: "User", status: "Inactive", is_bot: false, language: "en", message_text: "AUDIO_2024_01_12.wav" },
//         { user_id: 3, username: "lily.singh", first_name: "Lily", last_name: "Singh", phone_number: "+91-643-8473", bio: "Moderator", status: "Active", is_bot: false, language: "en", message_text: "MDMA, Scoops, Deal, Want to sell?" },
//     ];

//     const barData = [
//         { day: "Monday", suspicious: 30 },
//         { day: "Tuesday", suspicious: 45 },
//         { day: "Wednesday", suspicious: 25 },
//         { day: "Thursday", suspicious: 50 },
//         { day: "Friday", suspicious: 35 },
//     ];

//     const lineData = [
//         { month: "January", detections: 15 },
//         { month: "February", detections: 25 },
//         { month: "March", detections: 35 },
//         { month: "April", detections: 45 },
//         { month: "May", detections: 30 },
//         { month: "June", detections: 20 },
//         { month: "July", detections: 10 },
//     ];

//     return (
//         <div className="dashboard-container">
//             {/* Sidebar */}
//             <div className={`sidebar ${isSidebarOpen ? "open" : ""}`}>
//                 <button className="close-btn" onClick={() => setSidebarOpen(false)}>×</button>
//                 <ul>
//                     <li>Home</li>
//                     <li>File Manager</li>
//                     <li>About</li>
//                 </ul>
//             </div>

//             {/* Top Bar */}
//             <div className="top-bar">
//                 <FaBars className="menu-icon" onClick={() => setSidebarOpen(true)} />
//                 <h1 className="dashboard-title">User Detection Dashboard</h1>
//             </div>

//             {/* Main Content */}
//             <div className="dashboard">
//                 <button className="retrieve-chat-button" onClick={() => alert("Chat retrieved!")}>Retrieve Chat</button>
                
//                 {/* User Table */}
//                 <table className="user-table">
//                     <thead>
//                         <tr>
//                             <th>User ID</th>
//                             <th>Username</th>
//                             <th>First Name</th>
//                             <th>Last Name</th>
//                             <th>Phone Number</th>
//                             <th>Bio</th>
//                             <th>Status</th>
//                             <th>Is Bot</th>
//                             <th>Language</th>
//                             <th>Message Text</th>
//                         </tr>
//                     </thead>
//                     <tbody>
//                         {userData.map((user, index) => (
//                             <tr key={index}>
//                                 <td>{user.user_id}</td>
//                                 <td>{user.username}</td>
//                                 <td>{user.first_name}</td>
//                                 <td>{user.last_name}</td>
//                                 <td>{user.phone_number}</td>
//                                 <td>{user.bio}</td>
//                                 <td>{user.status}</td>
//                                 <td>{user.is_bot ? "Yes" : "No"}</td>
//                                 <td>{user.language}</td>
//                                 <td>{user.message_text}</td>
//                             </tr>
//                         ))}
//                     </tbody>
//                 </table>

//                 {/* Graphs Section */}
//                 <div className="graphs-section-horizontal">
//                     <div className="graph-container">
//                         <h3>Suspicious Activity by Day</h3>
//                         <ResponsiveContainer width="50%" height={200}>
//                             <BarChart data={barData}>
//                                 <XAxis dataKey="day" />
//                                 <YAxis />
//                                 <Tooltip />
//                                 <Legend />
//                                 <Bar dataKey="suspicious" fill="#FF0000" />
//                             </BarChart>
//                         </ResponsiveContainer>
//                     </div>

//                     <div className="graph-container">
//                         <h3>Monthly Suspicious Detection</h3>
//                         <ResponsiveContainer width="50%" height={200}>
//                             <LineChart data={lineData}>
//                                 <XAxis dataKey="month" />
//                                 <YAxis />
//                                 <Tooltip />
//                                 <Legend />
//                                 <Line type="monotone" dataKey="detections" stroke="#0000FF" />
//                             </LineChart>
//                         </ResponsiveContainer>
//                     </div>
//                 </div>
//             </div>
//         </div>
//     );
// };

// export default UserDetectionDashboard;
