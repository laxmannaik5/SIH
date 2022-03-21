const express = require('express');
const {spawn} = require('child_process');


const app = express();

app.get('/', function(req, res){
  res.send('Hello World!')
});

app.get("/python", function(req, res){

  // var data;
  const python = spawn('python', ['script.py']);
  python.stdout.on('data', function (data) {
  data = data.toString();
  // res.render("python", {data: data});
  console.log(data);
 });


});




app.listen('8080', function(){
  console.log('Server started on port 8080');
});
