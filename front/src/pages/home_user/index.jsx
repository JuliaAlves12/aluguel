import React, { useEffect, useState, useCallback } from "react"
import axios from "axios"

export default function HomeUser() {
    const [user, setUser] = useState([]) 
    const [searchNome, setSearchNome] = useState('') // Para o input de nome
    const [tipo, setTipo] = useState('')           // Para o Select (TIPO)
    const token = localStorage.getItem('token')

    // Função para buscar dados da API com filtros
    // Usamos useCallback para poder chamar dentro do useEffect sem loops
    const listar = useCallback(async () => {
        try {
            // Monta a URL com os filtros que você definiu no Django (filters.py)
            // nome e tipo são os nomes dos campos no seu UsuarioFilter
            const response = await axios.get('http://localhost:8000/api/usuarios/', {
                params: {
                    nome: searchNome,
                    tipo: tipo
                },
                headers: { Authorization: `Bearer ${token}` }
            })
            setUser(response.data)
        } catch (error) {
            console.error("Erro ao buscar usuários:", error)
        }
    }, [searchNome, tipo, token])

    // Dispara a busca sempre que o tipo mudar ou ao carregar a página
    useEffect(() => { 
        listar() 
    }, [listar])

    return (
        <div style={{ padding: '20px' }}>
            <h2>Lista de Usuários</h2>
            
            <div style={{ marginBottom: '20px', display: 'flex', gap: '10px', justifyContent: 'center' }}>
                {/* SELECT para o TIPO (Conforme seu desenho) */}
                <select 
                    value={tipo} 
                    onChange={(e) => setTipo(e.target.value)}
                    style={{ padding: '8px', borderRadius: '5px' }}
                >
                    <option value="">TODOS</option>
                    <option value="LOCADOR">LOCADOR</option>
                    <option value="LOCATARIO">LOCATÁRIO</option>
                </select>

                {/* INPUT para busca por NOME */}
                <input
                    type="text"
                    placeholder="Buscar por nome..."
                    style={{ padding: '8px', width: '250px', borderRadius: '5px' }}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            setSearchNome(e.target.value)
                        }
                    }}
                />
                
                {/* Botão de Lupa (opcional, já que o Enter funciona) */}
                <button onClick={() => listar()}>🔍</button>
            </div>

            <table border="1" cellPadding="6" style={{ width: "100%", backgroundColor: '#fff', color: '#333' }}>
                <thead>
                    <tr style={{ backgroundColor: '#eee' }}>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {user.length > 0 ? (
                        user.map((u) => (
                            <tr key={u.id}>
                                <td>{u.id}</td>
                                <td>{u.nome}</td>
                                <td>{u.email}</td>
                                <td>{u.telefone}</td>
                                <td>{u.tipo}</td>
                            </tr>
                        ))
                    ) : (
                        <tr><td colSpan="5">Nenhum usuário encontrado.</td></tr>
                    )}
                </tbody>
            </table>
        </div>
    )
}