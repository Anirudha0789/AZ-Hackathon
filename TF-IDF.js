var TfIdf = require('node-tfidf');
var tfidf = new TfIdf();
const fs = require('fs');

tfidf.addFileSync('data_files/one.txt');
tfidf.addFileSync('data_files/two.txt');
 
console.log("UIT =====================");
tfidf.tfidfs('UIT', function(i, measure) {
    console.log('document #' + i + ' is ' + measure);
});
 
console.log("ĐHQG-HCM =====================");
tfidf.tfidfs('ĐHQG-HCM', function(i, measure) {
    console.log('document #' + i + ' is ' + measure);
});