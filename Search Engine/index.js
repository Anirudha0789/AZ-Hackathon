const express = require('express');
const ejs = require('ejs');
const port = 3000;
const app = express();

app.set('view engine', 'ejs');

app.get('/', (req, res, next)=>{
    res.render('index');
});

app.get('/search', (req, res)=>{
    const query = req.query;
    const question = query.question;

    // Tf-idf

    const arr = [
        {
        title: 'asdassd',
        url: 'google.com',
        statement: "sum of the two element"
    },
        {
        title: 'asdassd',
        url: 'google.com',
        statement: "sum of the two element"
    },
        {
        title: 'asdassd',
        url: 'google.com',
        statement: "sum of the two element"
    },
        {
        title: 'asdassd',
        url: 'google.com',
        statement: "sum of the two element"
    },
        {
        title: 'asdassd',
        url: 'google.com',
        statement: "sum of the two element"
    }
    ];
    
    res.json(arr);
});

app.listen(port, ()=>{
    console.log(`Listening on ${port}`);
});