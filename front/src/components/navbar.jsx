import { Link } from 'react-router-dom';

export default function Navbar() {
  const estiloNav = {
    display: 'flex',
    gap: '15px',
    padding: '15px',
    backgroundColor: '#333',
    marginBottom: '20px',
    justifyContent: 'center'
  };

  const estiloLink = {
    color: 'white',
    textDecoration: 'none',
    fontWeight: 'bold'
  };

  return (
    <nav style={estiloNav}>
      <Link style={estiloLink} to="/homeuser">Usuários</Link>
      <Link style={estiloLink} to="/imoveluser">Imóveis</Link>
      <Link style={estiloLink} to="/contratouser">Contratos</Link>
      <Link style={estiloLink} to="/pagamentouser">Pagamentos</Link>
      <Link style={{...estiloLink, color: '#ff6b6b'}} to="/login">Sair</Link>
    </nav>
  );
}