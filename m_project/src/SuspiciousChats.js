// import React, { useState, useEffect } from "react";
// import axios from "axios";
// import ChatHistoryModal from "./Components/ChatHistoryModal";
// import "./styles/SuspiciousChats.css";

// const SuspiciousChats = () => {
//     const [chats, setChats] = useState([]);
//     const [modalOpen, setModalOpen] = useState(false);
//     const [chatHistory, setChatHistory] = useState(null);

//     useEffect(() => {
//         const fetchChats = async () => {
//             try {
//                 const response = await axios.get("http://localhost:5000/api/suspicious-chats");
//                 setChats(response.data.reverse());
//             } catch (error) {
//                 console.error("Error fetching data:", error);
//             }
//         };

//         const interval = setInterval(fetchChats, 3000); // refresh every 3s
//         return () => clearInterval(interval);
//     }, []);

//     const openChatHistory = (history) => {
//         setChatHistory(history);
//         setModalOpen(true);
//     };

//     const blockUser = (userId) => {
//         alert(`User ${userId} has been blocked.`);
//     };

//     return (
//         <div className="suspicious-chats">
//             <h1>📡 Live Telegram Messages</h1>
//             <input type="text" placeholder="🔍 Search users..." className="search-bar" />

//             <table>
//                 <thead>
//                     <tr>
//                         <th>Type</th>
//                         <th>User ID</th>
//                         <th>Username</th>
//                         <th>First Name</th>
//                         <th>Last Name</th>
//                         <th>Phone</th>
//                         <th>Bio</th>
//                         <th>Status</th>
//                         <th>Is Bot</th>
//                         <th>Language</th>
//                         <th>Message</th>
//                         <th>Chat History</th>
//                         <th>Action</th>
//                     </tr>
//                 </thead>
//                 <tbody>
//                     {chats.map((chat) => (
//                         <tr key={chat.userId} className={chat.messageType === "Suspicious" ? "danger" : "normal"}>
//                             <td>{chat.messageType}</td>
//                             <td>{chat.userId}</td>
//                             <td>{chat.username}</td>
//                             <td>{chat.firstName}</td>
//                             <td>{chat.lastName}</td>
//                             <td>{chat.phone}</td>
//                             <td>{chat.bio}</td>
//                             <td>{chat.status}</td>
//                             <td>{chat.isBot}</td>
//                             <td>{chat.language}</td>
//                             <td>{chat.message}</td>
//                             <td>
//                                 <button className="view-btn" onClick={() => openChatHistory(chat.chatHistory)}>🔗 View</button>
//                             </td>
//                             <td>
//                                 <button className="block-btn" onClick={() => blockUser(chat.userId)}>🚫 Block</button>
//                             </td>
//                         </tr>
//                     ))}
//                 </tbody>
//             </table>

//             {modalOpen && <ChatHistoryModal chatHistory={chatHistory} closeModal={() => setModalOpen(false)} />}
//         </div>
//     );
// };

// export default SuspiciousChats;



import React, { useState, useEffect } from "react";
import axios from "axios";
import ChatHistoryModal from "./Components/ChatHistoryModal";
import "./styles/SuspiciousChats.css";

const SuspiciousChats = () => {
    const [chats, setChats] = useState([]);
    const [modalOpen, setModalOpen] = useState(false);
    const [chatHistory, setChatHistory] = useState([]);
    const [selectedUser, setSelectedUser] = useState(null);
    const [searchTerm, setSearchTerm] = useState("");

    useEffect(() => {
        const fetchChats = async () => {
            try {
                const response = await axios.get("http://localhost:5001/api/suspicious-chats");
                console.log("Fetched data:", response.data);
                setChats(response.data.reverse());
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        const interval = setInterval(fetchChats, 3000);
        return () => clearInterval(interval);
    }, []);

    const openChatHistory = (userId) => {
        const userMessages = chats.filter(chat => chat.userId === userId);
        setChatHistory(userMessages);
        setSelectedUser(userId);
        setModalOpen(true);
    };

    const blockUser = (userId) => {
        alert(`User ${userId} has been blocked.`);
    };

    const handleSearch = (e) => {
        setSearchTerm(e.target.value.toLowerCase());
    };

    const filteredChats = chats.filter(chat =>
        chat.username?.toLowerCase().includes(searchTerm) ||
        chat.firstName?.toLowerCase().includes(searchTerm) ||
        chat.lastName?.toLowerCase().includes(searchTerm) ||
        chat.userId?.toString().includes(searchTerm)
    );

    return (
        <div className="suspicious-chats">
            <h1>📡 Live Telegram Messages</h1>
            <input
                type="text"
                placeholder="🔍 Search users..."
                className="search-bar"
                value={searchTerm}
                onChange={handleSearch}
            />

            <table>
                <thead>
                    <tr>
                        <th>Type</th>
                        <th>User ID</th>
                        <th>Username</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Phone</th>
                        <th>Bio</th>
                        <th>Status</th>
                        <th>Is Bot</th>
                        <th>Language</th>
                        <th>Message</th>
                        <th>Chat History</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredChats.map((chat, index) => {
                        const isImage = chat.message.startsWith("[Image]");
                        const filename = isImage ? chat.message.replace("[Image] ", "").trim() : "";
                        const imageUrl = `http://localhost:5001/telegram_chat_exports/media/${filename}`;

                        return (
                            <tr key={index} className={chat.messageType === "Suspicious" ? "danger" : "normal"}>
                                <td>{chat.messageType}</td>
                                <td>{chat.userId}</td>
                                <td>{chat.username}</td>
                                <td>{chat.firstName}</td>
                                <td>{chat.lastName}</td>
                                <td>{chat.phone}</td>
                                <td>{chat.bio}</td>
                                <td>{chat.status}</td>
                                <td>{chat.isBot}</td>
                                <td>{chat.language}</td>
                                <td>
                                    {isImage ? (
                                        <img
                                            src={imageUrl}
                                            alt="Suspicious content"
                                            style={{ width: "100px", borderRadius: "4px" }}
                                        />
                                    ) : (
                                        chat.message
                                    )}
                                </td>
                                <td>
                                    <button className="view-btn" onClick={() => openChatHistory(chat.userId)}>
                                        🔗 View
                                    </button>
                                </td>
                                <td>
                                    <button className="block-btn" onClick={() => blockUser(chat.userId)}>
                                        🚫 Block
                                    </button>
                                </td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>

            {modalOpen && (
                <ChatHistoryModal
                    chatHistory={chatHistory}
                    userId={selectedUser}
                    closeModal={() => setModalOpen(false)}
                />
            )}
        </div>
    );
};

export default SuspiciousChats;
