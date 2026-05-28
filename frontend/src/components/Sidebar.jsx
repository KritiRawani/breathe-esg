const Sidebar = () => {
  return (
    <div className="bg-gray-900 text-white w-64 min-h-screen p-5">

      <h2 className="text-xl font-bold mb-6">
        ESG Menu
      </h2>

      <ul className="space-y-4">

        <li>Dashboard</li>

        <li>Uploads</li>

        <li>Emission Records</li>

        <li>Audit Logs</li>

      </ul>

    </div>
  );
};

export default Sidebar;