import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer
} from "recharts";


const EmissionChart = ({ records }) => {

  const chartData = records.map((record) => ({
    category: record.category,
    emissions: record.emission_kg_co2e
  }));


  return (

    <div className="bg-white p-6 rounded-xl shadow-lg mt-8">

      <h2 className="text-2xl font-bold mb-6">
        Emissions Overview
      </h2>

      <ResponsiveContainer width="100%" height={300}>

        <BarChart data={chartData}>

          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="category" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="emissions" />

        </BarChart>

      </ResponsiveContainer>

    </div>
  );
};

export default EmissionChart;