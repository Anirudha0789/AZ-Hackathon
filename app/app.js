const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.set('view engine', 'ejs');
app.use('/static', express.static('static'));
app.use(bodyParser.urlencoded({ extended: false }));

// app.get('/', (req, res)=>{
//     res.send('This is Hompage');
// });

app.get('/', (req, res)=>{
    // res.sendFile(__dirname + '/index.html');
    res.render('index');
});

app.get('/contact', (req, res)=>{
    // res.sendFile(__dirname + '/contact.html');
    res.render('contact', {queryString:req.query});
});

app.post('/contact', (req, res)=>{
    console.log(req.body);
    // res.render('contact', {queryString:req.query});
    res.render('contact-success', {data : req.body});
});

app.get('/profile/:name', (req, res)=>{
    // res.send("You requested to see the profile the id of " + req.params.name);
    var data = {age: 21, job: 'none', hobbies: ['sdfsd', 'fvfdvcv']};
    res.render('profile', {person: req.params.name, data: data});
});

app.listen(3000);