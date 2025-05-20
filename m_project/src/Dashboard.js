import React, { useEffect, useState } from "react";
import StatsCard from "./Components/StatsCard";
import KeywordsChart from "./Components/KeywordsChart";
import axios from "axios";
import "./styles/Dashboard.css";

const Dashboard = () => {
    const [stats, setStats] = useState([
        { title: "Total Users Monitored", value: 0, icon: "👥", color: "#4CAF50" },
        { title: "Total Messages Scanned", value: 0, icon: "💬", color: "#2196F3" },
        { title: "Suspicious Messages", value: 0, icon: "🚨", color: "#FF5722" },
        { title: "Suspicious Users", value: 0, icon: "⚠️", color: "#FFC107" },
    ]);

    useEffect(() => {
        const fetchStats = async () => {
            try {
                const response = await axios.get("http://localhost:5001/api/chat-stats");
                const data = response.data;

                setStats([
                    { title: "Normal messages", value: data.normal_messages, icon: "👥", color: "#4CAF50" },
                    { title: "Total Messages Scanned", value: data.total_messages, icon: "💬", color: "#2196F3" },
                    { title: "Suspicious Messages", value: data.suspicious_messages, icon: "🚨", color: "#FF5722" },
                    { title: "Suspicious Users", value: data.suspicious_users, icon: "⚠️", color: "#FFC107" },
                ]);
                console.log("Fetched Stats:", data);

            } catch (error) {
                console.error("Error fetching dashboard stats:", error);
            }
        };

        fetchStats();
    }, []);

    return (
        <div className="dashboard-container">
            <div className="dashboard-header">
                <h1 className="dashboard-title">📊 Chat Monitoring Overview</h1>
                <button className="login-button">Login</button>
            </div>

            <div className="stats-grid">
                {stats.map((stat, index) => (
                    <StatsCard
                        key={index}
                        title={stat.title}
                        value={stat.value}
                        icon={stat.icon}
                        color={stat.color}
                    />
                ))}
            </div>

            <div className="chart-container">
                <h2>🔍 Top Keywords Detected</h2>
                <KeywordsChart />
            </div>
        </div>
    );
};

export default Dashboard;
