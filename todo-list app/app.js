const bodyParser = require('body-parser');
const express = require('express');
const app = express();
const port = 3000;
const todoController = require('./controllers/todoController');

app.use(bodyParser.urlencoded({ extended: false }));

// setup template engine
app.set('view engine', 'ejs');

// static files
app.use(express.static('./public'));

// fire controller
todoController(app);

// listen to port
app.listen(port , ()=>{
    console.log(`You are listening to port ${port}`);
});