var app = require('express')();
var express = require('express')
var server = require('http').Server(app);
var io = require('socket.io')(server);
var bodyParser = require('body-parser');
server.listen(9090);

app.all('*', function(req, res, next) {
  res.header("Access-Control-Allow-Origin", req.headers.origin);
  res.header("Access-Control-Allow-Headers", "X-Requested-With");
  res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
  res.header("Access-Control-Allow-Credentials", true);
  res.header("X-Powered-By",' 3.2.1');
  next();
});


app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));


app.get('/', function (req, res) {
  res.sendfile(__dirname + '/index.html');
});

app.get('/test', function(req, res) {
  let data = req.query.data;

   io.emit('news', {data_arr});
   res.send('ok');
})

app.post('/getData', function(req, res, next) {
  let data = req.body;
  console.log(data);
  let data_arr = [];
  let data_name = [];
  for(val in data) {
    data_name.push(val);
    data_arr.push(parseFloat(data[val]) * 10);
  }
  io.emit('news', {data_arr, data_name});
  res.json({
    info: 'ok',
    code: 200,
    data: data_arr,
    data_name
  });
});

io.on('connection', function (socket) {
  // socket.emit('news', { hello: 'world' });
  socket.on('my other event', function (data) {
    console.log(data);
  });
});