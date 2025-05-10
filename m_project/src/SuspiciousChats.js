import React, { useState } from "react";
import ChatHistoryModal from "./Components/ChatHistoryModal";
import "./styles/SuspiciousChats.css";

const SuspiciousChats = () => {
    const [chatHistory, setChatHistory] = useState(null);
    const [modalOpen, setModalOpen] = useState(false);

    // Sample Suspicious Users Data
    const suspiciousChats = [
        {
            userId: "1234",
            username: "@john_doe",
            firstName: "John",
            lastName: "Doe",
            phone: "+91-123456",
            bio: "User",
            status: "Active",
            isBot: "No",
            language: "en",
            message: "Want to buy MDMA?",
            chatHistory: ["Hey, do you have MDMA?", "I can sell some.", "How much do you want?"]
        },
        {
            userId: "5678",
            username: "@alice_123",
            firstName: "Alice",
            lastName: "Smith",
            phone: "+44-987654",
            bio: "Moderator",
            status: "Active",
            isBot: "No",
            language: "en",
            message: "Selling crypto fast",
            chatHistory: ["I have some Bitcoin available.", "Fast transactions.", "DM me if interested."]
        }
    ];

    // Open chat history modal
    const openChatHistory = (history) => {
        setChatHistory(history);
        setModalOpen(true);
    };

    // Block user (simulate action)
    const blockUser = (userId) => {
        alert(`User ${userId} has been blocked.`);
    };

    return (
        <div className="suspicious-chats">
            <h1>🚨 Suspicious Chats</h1>
            <input type="text" placeholder="🔍 Search users..." className="search-bar" />

            <table>
                <thead>
                    <tr>
                        <th>User ID</th>
                        <th>Username</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                        <th>Phone</th>
                        <th>Bio</th>
                        <th>Status</th>
                        <th>Is Bot</th>
                        <th>Language</th>
                        <th>Message Text</th>
                        <th>Chat History</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {suspiciousChats.map((chat) => (
                        <tr key={chat.userId}>
                            <td>{chat.userId}</td>
                            <td>{chat.username}</td>
                            <td>{chat.firstName}</td>
                            <td>{chat.lastName}</td>
                            <td>{chat.phone}</td>
                            <td>{chat.bio}</td>
                            <td>{chat.status}</td>
                            <td>{chat.isBot}</td>
                            <td>{chat.language}</td>
                            <td>{chat.message}</td>
                            <td>
                                <button className="view-btn" onClick={() => openChatHistory(chat.chatHistory)}>🔗 View</button>
                            </td>
                            <td>
                                <button className="block-btn" onClick={() => blockUser(chat.userId)}>🚫 Block</button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {modalOpen && <ChatHistoryModal chatHistory={chatHistory} closeModal={() => setModalOpen(false)} />}
        </div>
    );
};

export default SuspiciousChats;
