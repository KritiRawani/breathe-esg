import { useEffect, useState } from "react";

import API from "../services/api";

import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import StatCard from "../components/StatCard";
import UploadPage from "./UploadPage";

import EmissionTable from "../components/EmissionTable";

const Dashboard = () => {

  const [summary, setSummary] = useState({});

  const fetchDashboard = async () => {

    try {

      const response = await API.get(
        "/dashboard/summary/"
      );

      setSummary(response.data);

    } catch (error) {

      console.error(error);
    }
  };

  useEffect(() => {
    fetchDashboard();
  }, []);

  return (

    <div>

      <Navbar />

      <div className="flex">

        <Sidebar />

        <div className="flex-1 p-6 bg-gray-100 min-h-screen">

          <h1 className="text-3xl font-bold mb-6">
            ESG Dashboard
          </h1>

          <div className="grid grid-cols-3 gap-6">

            <StatCard
              title="Total Records"
              value={summary.total_records}
            />

            <StatCard
              title="Approved Records"
              value={summary.approved_records}
            />

            <StatCard
              title="Rejected Records"
              value={summary.rejected_records}
            />

            <StatCard
              title="Flagged Records"
              value={summary.flagged_records}
            />

            <StatCard
              title="Pending Records"
              value={summary.pending_records}
            />

            <StatCard
              title="Total Emissions"
              value={summary.total_emissions_kg_co2e}
            />

          </div>

          {/* Upload Section */}
          <div className="mt-10">
            <UploadPage />
          </div>

          {/* Emission Table */}
          <div className="mt-10">
            <EmissionTable />
          </div>

        </div>

      </div>

    </div>
  );
};

export default Dashboard;