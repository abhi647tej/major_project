import React from "react";
import StatsCard from "./Components/StatsCard";
import KeywordsChart from "./Components/KeywordsChart";
import "./styles/Dashboard.css";

const Dashboard = () => {
    // Dummy data for statistics
    const stats = [
        { title: "Total Users Monitored", value: 120, icon: "👥", color: "#4CAF50" },
        { title: "Total Messages Scanned", value: 5200, icon: "💬", color: "#2196F3" },
        { title: "Suspicious Messages", value: 98, icon: "🚨", color: "#FF5722" },
        { title: "Suspicious Users", value: 14, icon: "⚠️", color: "#FFC107" },
    ];

    return (
        <div className="dashboard-container">
            <h1 className="dashboard-title">📊 Chat Monitoring Overview</h1>

            {/* Stats Cards */}
            <div className="stats-grid">
                {stats.map((stat, index) => (
                    <StatsCard key={index} title={stat.title} value={stat.value} icon={stat.icon} color={stat.color} />
                ))}
            </div>

            {/* Top Keywords Chart */}
            <div className="chart-container">
                <h2>🔍 Top Keywords Detected</h2>
                <KeywordsChart />
            </div>
        </div>
    );
};

export default Dashboard;
