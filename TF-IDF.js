var TfIdf = require('node-tfidf');
var tfidf = new TfIdf();
const fs = require('fs');
const { stringify } = require('querystring');
const { count } = require('console');

var corpus = [];
// var cnt = 0;
// while(cnt < 1944)
fs.readFile('./keyword.txt', (err, data)=>{
    if(err) throw err;
    corpus.join();
});

tfidf.addFileSync((corpus).toString());
 
tfidf.tfidfs('player', function(i, measure) {
    console.log('document #' + i + ' is ' + measure);
});
