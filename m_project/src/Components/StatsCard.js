import React from "react";
import "./StatsCard.css";

const StatsCard = ({ title, value, icon, color }) => {
    return (
        <div className="stats-card" style={{ borderLeft: `5px solid ${color}` }}>
            <div className="stats-icon">{icon}</div>
            <div className="stats-info">
                <h3>{title}</h3>
                <p>{value}</p>
            </div>
        </div>
    );
};

export default StatsCard;
