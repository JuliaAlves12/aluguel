import React, { useEffect, useState, useCallback } from "react";
import axios from "axios";

export default function PagamentoUser() {
    const [pagamentos, setPagamentos] = useState([]);
    const [statusPg, setStatusPg] = useState('');
    const [dataPg, setDataPg] = useState('');
    const token = localStorage.getItem('token');

    const listar = useCallback(async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/pagamentos/', {
                params: { status: statusPg, data_pagamento: dataPg },
                headers: { Authorization: `Bearer ${token}` }
            });
            setPagamentos(response.data);
        } catch (error) { console.error(error); }
    }, [statusPg, dataPg, token]);

    useEffect(() => { listar(); }, [listar]);

    return (
        <div style={{ padding: '20px' }}>
            <h2>Lista de Pagamentos</h2>
            <div style={{ marginBottom: '20px', display: 'flex', gap: '10px' }}>
                <select onChange={(e) => setStatusPg(e.target.value)}>
                    <option value="">STATUS (TODOS)</option>
                    <option value="true">PAGO</option>
                    <option value="false">PENDENTE</option>
                </select>
                <input type="date" onChange={(e) => setDataPg(e.target.value)} />
                <button onClick={listar}>🔍</button>
            </div>
            <table border="1" width="100%" cellPadding="8">
                <thead>
                    <tr>
                        <th>Data</th>
                        <th>Valor</th>
                        <th>Status</th>
                        <th>Contrato ID</th>
                    </tr>
                </thead>
                <tbody>
                    {pagamentos.map(p => (
                        <tr key={p.id}>
                            <td>{p.data_pagamento}</td>
                            <td>R$ {p.valor}</td>
                            <td>{p.status ? "✅ Pago" : "❌ Pendente"}</td>
                            <td>{p.contrato_id}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}