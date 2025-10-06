import Header from './components/Header.jsx'
import CategoryList from './components/CategoryList.jsx'
import './App.css'

function App() {

  return (
    <>
      <Header />

      <main className='app-content'>
        <p>Conteudo principal aqui</p>
        <p>Lista de categorias e formulario vira aqui</p>

        <CategoryList />  
        
      </main>
    </>
    
  )
}

// TO-DO: Integração com a API Backend

export default App
