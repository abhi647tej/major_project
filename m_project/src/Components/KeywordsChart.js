import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

const keywordData = [
    { keyword: "MDMA", count: 25 },
    { keyword: "Fraud", count: 18 },
    { keyword: "Cocaine", count: 22 },
    { keyword: "Scam", count: 12 },
    { keyword: "Bitcoin", count: 30 },
];

const KeywordsChart = () => {
    return (
        <ResponsiveContainer width="100%" height={250}>
            <BarChart data={keywordData}>
                <XAxis dataKey="keyword" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count" fill="#FF0000" />
            </BarChart>
        </ResponsiveContainer>
    );
};

export default KeywordsChart;
