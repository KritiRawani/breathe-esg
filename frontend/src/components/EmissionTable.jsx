import { useEffect, useState } from "react";

import API from "../services/api";


const EmissionTable = () => {

    const [records, setRecords] = useState([]);
    const [search, setSearch] = useState("");


    const fetchRecords = async () => {

        try {

            const response = await API.get(
                "/emissions/records/"
            );

            setRecords(response.data);

        } catch (error) {

            console.error(error);
        }
    };


    const approveRecord = async (id) => {

        try {

            await API.post(
                `/reviews/approve/${id}/`,
                {
                    reviewed_by: "kriti"
                }
            );

            fetchRecords();

        } catch (error) {

            console.error(error);
        }
    };


    const rejectRecord = async (id) => {

        try {

            await API.post(
                `/reviews/reject/${id}/`,
                {
                    reviewed_by: "kriti"
                }
            );

            fetchRecords();

        } catch (error) {

            console.error(error);
        }
    };


    useEffect(() => {
        fetchRecords();
    }, []);


    return (

        <div className="bg-white p-6 rounded-xl shadow-lg mt-8">

            <h2 className="text-2xl font-bold mb-4">
                Emission Records
            </h2>

            <input
                type="text"
                placeholder="Search category..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="border p-2 mb-4 rounded-lg w-full"
            />

            <table className="w-full border">

                <thead className="bg-gray-200">

                    <tr>

                        <th className="p-3 border">Category</th>

                        <th className="p-3 border">Scope</th>

                        <th className="p-3 border">Emission</th>

                        <th className="p-3 border">Status</th>

                        <th className="p-3 border">Suspicious</th>

                        <th className="p-3 border">Actions</th>

                    </tr>

                </thead>

                <tbody>

                    {records
                        .filter((record) =>
                            record.category
                                .toLowerCase()
                                .includes(search.toLowerCase())
                        )
                        .map((record) => (

                            <tr
                                key={record.id}
                                className={
                                    record.is_suspicious
                                        ? "bg-red-100"
                                        : ""
                                }
                            >

                                <td className="p-3 border">
                                    {record.category}
                                </td>

                                <td className="p-3 border">
                                    {record.scope}
                                </td>

                                <td className="p-3 border">
                                    {record.emission_kg_co2e}
                                </td>

                                <td className="p-3 border">

                                    <span
                                        className={
                                            record.status === "APPROVED"
                                                ? "bg-green-200 px-3 py-1 rounded-full"
                                                : record.status === "REJECTED"
                                                    ? "bg-red-200 px-3 py-1 rounded-full"
                                                    : "bg-yellow-200 px-3 py-1 rounded-full"
                                        }
                                    >
                                        {record.status}
                                    </span>

                                </td>

                                <td className="p-3 border">

                                    {record.is_suspicious ? (

                                        <span className="bg-red-500 text-white px-2 py-1 rounded-full text-xs">
                                            Suspicious
                                        </span>

                                    ) : (

                                        <span className="bg-green-500 text-white px-2 py-1 rounded-full text-xs">
                                            Normal
                                        </span>

                                    )}

                                </td>

                                <td className="p-3 border space-x-2">

                                    <button
                                        onClick={() =>
                                            approveRecord(record.id)
                                        }
                                        className="bg-green-600 text-white px-3 py-1 rounded"
                                    >
                                        Approve
                                    </button>

                                    <button
                                        onClick={() =>
                                            rejectRecord(record.id)
                                        }
                                        className="bg-red-600 text-white px-3 py-1 rounded"
                                    >
                                        Reject
                                    </button>

                                    <button
                                        className="bg-black text-white px-3 py-1 rounded"
                                    >
                                        Lock
                                    </button>

                                </td>

                            </tr>

                        ))}

                </tbody>

            </table>

        </div>
    );
};

export default EmissionTable;