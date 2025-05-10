// import React, { useState } from "react";
// import "./styles/AllChatsHistory.css";

// const AllChatsHistory = () => {
//   const [searchQuery, setSearchQuery] = useState("");
//   const [selectedChat, setSelectedChat] = useState(null);

//   // Example chat data
//   const chats = [
//     {
//       user_id: 1,
//       username: "mahendra.kumar",
//       phone_number: "+91-847-1358",
//       messages: [
//         { sender: "Me", text: "Hello!" },
//         { sender: "Mahendra", text: "Hi, how are you?" },
//       ],
//     },
//     {
//       user_id: 2,
//       username: "abhijit.patil",
//       phone_number: "+91-372-9453",
//       messages: [
//         { sender: "Me", text: "Did you receive my email?" },
//         { sender: "Abhijit", text: "Yes, I got it!" },
//       ],
//     },
//   ];

//   const filteredChats = chats.filter(
//     (chat) =>
//       chat.username.includes(searchQuery) ||
//       chat.phone_number.includes(searchQuery)
//   );

//   return (
//     <div className="chat-history-container">
//       <div className="chat-sidebar">
//         <input
//           type="text"
//           placeholder="Search by username or phone"
//           value={searchQuery}
//           onChange={(e) => setSearchQuery(e.target.value)}
//           className="search-bar"
//         />
//         <ul className="chat-list">
//           {filteredChats.map((chat) => (
//             <li
//               key={chat.user_id}
//               className={selectedChat === chat ? "active-chat" : ""}
//               onClick={() => setSelectedChat(chat)}
//             >
//               <span className="chat-username">{chat.username}</span>
//               <span className="chat-preview">
//                 {chat.messages[chat.messages.length - 1].text}
//               </span>
//             </li>
//           ))}
//         </ul>
//       </div>
//       <div className="chat-view">
//         {selectedChat ? (
//           <>
//             <div className="chat-header">
//               <h3>{selectedChat.username}</h3>
//               <button className="export-btn">Export Chat</button>
//             </div>
//             <div className="chat-messages">
//               {selectedChat.messages.map((msg, index) => (
//                 <p key={index} className={msg.sender === "Me" ? "sent" : "received"}>
//                   <strong>{msg.sender}:</strong> {msg.text}
//                 </p>
//               ))}
//             </div>
//           </>
//         ) : (
//           <p className="select-chat-msg">Select a chat to view messages</p>
//         )}
//       </div>
//     </div>
//   );
// };

// export default AllChatsHistory;


import React, { useState } from "react";
import { FiSearch } from "react-icons/fi";
import { FaDownload } from "react-icons/fa";
import "./styles/AllChatsHistory.css";


const chatData = [
  {
    userId: "1234",
    username: "@john_doe",
    firstName: "John",
    lastName: "Doe",
    phone: "+91-123456",
    messages: [
      { text: "Hey, how are you?", time: "10:00 AM", sender: "user" },
      { text: "I am fine, thanks!", time: "10:05 AM", sender: "me" },
    ],
  },
  {
    userId: "5678",
    username: "@alice_123",
    firstName: "Alice",
    lastName: "Smith",
    phone: "+44-987654",
    messages: [
      { text: "Selling crypto fast", time: "11:00 AM", sender: "user" },
      { text: "Not interested", time: "11:02 AM", sender: "me" },
    ],
  },
];

const AllChatsHistory = () => {
  const [searchTerm, setSearchTerm] = useState("");
  const [selectedChat, setSelectedChat] = useState(null);

  const filteredChats = chatData.filter((chat) =>
    chat.username.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="chat-history-container">
      {/* Sidebar */}
      <div className="chat-list-panel">
        <div className="search-bar">
          <FiSearch />
          <input
            type="text"
            placeholder="Search by Username, User ID, Phone..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        {filteredChats.map((chat) => (
          <div
            key={chat.userId}
            className={`chat-item ${selectedChat === chat ? "active" : ""}`}
            onClick={() => setSelectedChat(chat)}
          >
            <div className="chat-info">
              <strong>{chat.firstName} {chat.lastName}</strong>
              <p>{chat.messages[0].text}</p>
            </div>
          </div>
        ))}
      </div>

      {/* Chat View */}
      <div className="chat-view-panel">
        {selectedChat ? (
          <>
            <div className="chat-header">
              <h3>{selectedChat.firstName} {selectedChat.lastName}</h3>
              <button className="export-btn">
                <FaDownload /> Export Chat
              </button>
            </div>
            <div className="chat-messages">
              {selectedChat.messages.map((msg, index) => (
                <div key={index} className={`message ${msg.sender}`}> 
                  <span>{msg.text}</span>
                  <small>{msg.time}</small>
                </div>
              ))}
            </div>
          </>
        ) : (
          <p className="no-chat-selected">Select a chat to view messages</p>
        )}
      </div>
    </div>
  );
};

export default AllChatsHistory;

