import React, { useEffect, useState } from "react";
import './CategoryList.css'

function CategoryList() {
    const [categorias, setCategorias] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:5000/api/categorias';

        console.log("Buscando dados da API...");

        fetch(apiUrl).then(response => response.json()).then(data => {
            console.log('Dados recebidos: ', data);
            setCategorias(data);
            setIsLoading(false);
        })
        .catch(error => {
            console.error("Houve um erro ao buscar as categorias: ", error);
            setIsLoading(false);
        })
    }, []);

    if (isLoading){
        return <p>Carregando categorias...</p>;
    }

    return (
        <div className="category-list-container">
            <h2>Lista de Categorias</h2>
            <ul>
                {categorias.map(categoria => (
                    <li key = {categoria.id}>
                        {categoria.nome}
                    </li>
                ))}
            </ul>
        </div>
    );

    // return (
        
    // )
}

export default CategoryList;