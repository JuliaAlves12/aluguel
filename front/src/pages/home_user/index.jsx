import React, { useEffect, useState } from "react"
import axios from "axios"
 
export default function HomeUser() {
    const [user, setUser] = useState([]) // Lista de usuários
    const [usuarioFilter, setUsuarioFilter] = useState('') // Texto da busca
    const token = localStorage.getItem('token')
 
    const listar = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/usuarios', {
                headers: { Authorization: `Bearer ${token}` }
            })
            setUser(response.data)
        } catch (error) {
            console.log(error)
        }
    }
 
    useEffect(() => { listar() }, [])
 
    // Filtra usuários pelo nome
    const usuariosFiltrados = user.filter(u =>
        u.nome.toLowerCase().includes(usuarioFilter.toLowerCase())
    )
 
    return (
        <div>
            <h2>Lista de Usuários</h2>
            <div>
            <input
                type="text"
                placeholder="Buscar usuário..."
                onKeyDown={(e) => {
                if (e.key === "Enter") {
                    e.preventDefault()
                    setUsuarioFilter(e.target.value) // aplica o filtro ao apertar Enter
                }
                }}
            />
            </div>
 
            <table border="1" cellPadding="6" style={{ width: "100%" }}>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Nome</th>
                        <th>Email</th>
                        <th>Telefone</th>
                        <th>Tipo</th>
                    </tr>
                </thead>
                <tbody>
                    {usuariosFiltrados.map((u) => (
                        <tr key={u.id}>
                            <td>{u.id}</td>
                            <td>{u.nome}</td>
                            <td>{u.email}</td>
                            <td>{u.telefone}</td>
                            <td>{u.tipo}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    )
}