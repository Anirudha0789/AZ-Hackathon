const bodyParser = require('body-parser');
const mongoose = require('mongoose'); 

// connnect to the database
mongoose.connect('mongodb+srv://tangent_veil:Jyoshita1014@todo.4sk4r.mongodb.net/?retryWrites=true&w=majority');

// create a schema - this is like a blueprint
var todoSchema = new mongoose.Schema({
    item: String
});

var Todo = mongoose.model('Todo', todoSchema);
// var itemOne = Todo({item: 'Buy flowers'}).save((err)=>{
//     if(err) throw err;
//     console.log("Item Saved");
// });

// var data = [{item: 'get milk'}, {item: 'walk dog'}, {item: 'kick some coding ass'}];

var urlencodedParser = bodyParser.urlencoded({ extended: false });

module.exports = (app)=>{
    app.get('/todo', (req, res)=>{
        // get data from mongodb and pass to view
        Todo.find({}, (err, data)=>{
            if(err) throw err;
            res.render('todo', {todos: data});
        });
    });

    app.post('/todo', urlencodedParser, (req, res)=>{
        // get data from the view and add to the mongodb
        var newTodo = Todo(req.body).save((err, data)=>{
            if(err) throw err;
            res.json(data);
        });
        // data.push(req.body);
    });

    app.delete('/todo/:item', (req, res)=>{
        // detele the requested item from mongodb
        Todo.findByIdAndDelete(req.params.item, (err, data)=>{
            if(err) throw err;
            res.json(data);
        });

        // deleting from local array
        // data = data.filter((todo)=>{
        //     return todo.item.replace(/ /g, '-') !== req.params.item;
        // });
        // res.json(data);
    });
};