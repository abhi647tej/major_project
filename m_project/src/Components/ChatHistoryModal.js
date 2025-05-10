import React from "react";
import "../styles/ChatHistoryModal.css";

const ChatHistoryModal = ({ chatHistory, closeModal }) => {
    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <h2>💬 Chat History</h2>
                <ul>
                    {chatHistory.map((msg, index) => (
                        <li key={index}>{msg}</li>
                    ))}
                </ul>
                <button className="close-modal" onClick={closeModal}>❌ Close</button>
            </div>
        </div>
    );
};

export default ChatHistoryModal;
