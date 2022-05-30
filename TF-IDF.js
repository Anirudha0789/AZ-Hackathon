const fs = require("fs-extra");
const w2v = require("word2vec");

function clearText(text) {
    return text
      .toLowerCase()
      .replace(/[^A-Za-zА-Яа-яЁёЇїІіҐґЄє0-9\-]|\s]/g, " ")
      .replace(/\s{2,}/g, " ");
}

async function clear(filePath) {
    const contentRaw = await fs.readFile(filePath);
    const content = clearText(contentRaw.toString());
    return fs.writeFile(`cleared_${filePath}`, content);
}

w2v.word2vec(corpusFilePath, "vectors.txt", { size: 300 }, () => {
    console.log("DONE");
});

w2v.loadModel("vectors.txt", (error, model) => {
    console.log("SIZE: ", model.size);
    console.log("WORDS: ", model.words);
    console.log(model.mostSimilar(word, 20));
});

w2v.loadModel("vectors.txt", (error, model) => {
    console.log(model.analogy(word, pair, number_neighbors));
  });