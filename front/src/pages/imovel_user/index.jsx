import React, { useEffect, useState, useCallback } from "react";
import axios from "axios";

export default function ImovelUser() {
    const [imoveis, setImoveis] = useState([]);
    const [statusFiltro, setStatusFiltro] = useState('');
    const [tipoBusca, setTipoBusca] = useState('');
    const token = localStorage.getItem('token');

    const listar = useCallback(async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/imoveis/', {
                params: { status: statusFiltro, tipo: tipoBusca },
                headers: { Authorization: `Bearer ${token}` }
            });
            setImoveis(response.data);
        } catch (error) {
            console.error("Erro ao buscar imóveis", error);
        }
    }, [statusFiltro, tipoBusca, token]);

    useEffect(() => { listar(); }, [listar]);

    return (
        <div style={{ padding: '20px' }}>
            <h2>Lista de Imóveis</h2>
            <div style={{ marginBottom: '20px', display: 'flex', gap: '10px' }}>
                <select value={statusFiltro} onChange={(e) => setStatusFiltro(e.target.value)}>
                    <option value="">STATUS (TODOS)</option>
                    <option value="DISPONIVEL">DISPONÍVEL</option>
                    <option value="ALUGADO">ALUGADO</option>
                </select>
                <input 
                    placeholder="Tipo (Ex: Casa, Apto)" 
                    onChange={(e) => setTipoBusca(e.target.value)}
                />
                <button onClick={listar}>🔍</button>
            </div>
            <table border="1" width="100%" cellPadding="8">
                <thead>
                    <tr>
                        <th>Título</th>
                        <th>Tipo</th>
                        <th>Valor Aluguel</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {imoveis.map(i => (
                        <tr key={i.id}>
                            <td>{i.titulo}</td>
                            <td>{i.tipo}</td>
                            <td>R$ {i.valor_aluguel}</td>
                            <td>{i.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}