import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetch('/articles/')
      .then(response => response.json())
      .then(data => setArticles(data));
  }, []);

  const generateArticle = () => {
    fetch('/articles/', { method: 'POST' })
      .then(response => response.json())
      .then(newArticle => setArticles([newArticle, ...articles]));
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Trends</h1>
        <button onClick={generateArticle}>Generate New Article</button>
      </header>
      <main>
        {articles.map(article => (
          <div key={article.id} className="article">
            <h2>{article.title}</h2>
            <p className="date">{article.date}</p>
            <img src={article.image_url} alt={article.title} />
            <p>{article.article}</p>
          </div>
        ))}
      </main>
    </div>
  );
}

export default App;