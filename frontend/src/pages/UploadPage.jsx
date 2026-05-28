import { useState } from "react";

import API from "../services/api";


const UploadPage = ({ fetchDashboard }) => {

  const [file, setFile] = useState(null);

  const [message, setMessage] = useState("");


  const handleUpload = async () => {

    if (!file) {
      alert("Please select file");
      return;
    }

    const formData = new FormData();

    formData.append("file", file);

    formData.append("uploaded_by", "Kriti");

    try {

      const response = await API.post(
        "/upload/sap/",
        formData
      );

      setMessage(response.data.message);

      alert("Upload successful");

      fetchDashboard();

      window.location.reload();

    } catch (error) {

      console.error(error);

      alert("Upload failed");
    }
  };


  return (

    <div className="bg-white p-6 rounded-xl shadow-lg">

      <h2 className="text-2xl font-bold mb-4">
        Upload SAP CSV
      </h2>

      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />

      <button
        onClick={handleUpload}
        className="bg-black text-white px-6 py-2 rounded-lg"
      >
        Upload
      </button>

      <p className="mt-4 text-green-600">
        {message}
      </p>

    </div>
  );
};

export default UploadPage;