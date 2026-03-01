import React, { useEffect, useState, useCallback } from "react";
import axios from "axios";

export default function ContratoUser() {
    const [contratos, setContratos] = useState([]);
    const [vMin, setVMin] = useState('');
    const [vMax, setVMax] = useState('');
    const token = localStorage.getItem('token');

    const listar = useCallback(async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/contratos/', {
                params: { valor_min: vMin, valor_max: vMax },
                headers: { Authorization: `Bearer ${token}` }
            });
            setContratos(response.data);
        } catch (error) { console.error(error); }
    }, [vMin, vMax, token]);

    useEffect(() => { listar(); }, [listar]);

    return (
        <div style={{ padding: '20px' }}>
            <h2>Lista de Contratos</h2>
            <div style={{ marginBottom: '20px', display: 'flex', gap: '10px' }}>
                <input type="number" placeholder="Valor Mínimo" onChange={(e) => setVMin(e.target.value)} />
                <input type="number" placeholder="Valor Máximo" onChange={(e) => setVMax(e.target.value)} />
                <button onClick={listar}>🔍 Filtrar Valor</button>
            </div>
            <table border="1" width="100%" cellPadding="8">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Início</th>
                        <th>Fim</th>
                        <th>Valor Mensal</th>
                    </tr>
                </thead>
                <tbody>
                    {contratos.map(c => (
                        <tr key={c.id}>
                            <td>{c.id}</td>
                            <td>{c.data_inicio}</td>
                            <td>{c.data_fim}</td>
                            <td>R$ {c.valor}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}