fetch('data.json')
    .then(response => response.json())
    .then(data => {
        document.getElementById('title').textContent = data.title;
        document.getElementById('date').textContent = data.date;
        document.getElementById('image').src = data.image_url;
        document.getElementById('article').innerHTML = data.article;
    });