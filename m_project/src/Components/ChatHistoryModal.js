// import React from "react";
// import "../styles/ChatHistoryModal.css";

// const ChatHistoryModal = ({ chatHistory, closeModal }) => {
//     return (
//         <div className="modal-overlay">
//             <div className="modal-content">
//                 <h2>💬 Chat History</h2>
//                 <ul>
//                     {chatHistory.map((msg, index) => (
//                         <li key={index}>{msg}</li>
//                     ))}
//                 </ul>
//                 <button className="close-modal" onClick={closeModal}>❌ Close</button>
//             </div>
//         </div>
//     );
// };

// export default ChatHistoryModal;


import React from "react";
import "../styles/ChatHistoryModal.css";

const ChatHistoryModal = ({ chatHistory, userId, closeModal }) => {
    return (
        <div className="modal-overlay">
            <div className="modal-content">
                <h2>📜 Chat History for User ID: {userId}</h2>
                <button className="close-btn" onClick={closeModal}>❌ Close</button>
                <div className="chat-history-list">
                    {chatHistory.map((chat, index) => (
                        <div key={index} className={`chat-bubble ${chat.messageType === "Suspicious" ? "danger" : "normal"}`}>
                            <strong>{chat.firstName}:</strong> {chat.message}
                            <span className="label">{chat.messageType}</span>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
};

export default ChatHistoryModal;
