const http = require('http');
const server = http.createServer(function(res){
  res.write('Hello Node')
  res.end()  
});

const { Server } = require("socket.io");
const io = new Server(server);
const PORT = process.env.PORT||3000;

io.on('connection', (socket) => {
  console.log('Client connected.');

  socket.on('msg', (msg) => {
    console.log(msg);
        // do something with the message
  });

  socket.on('disconnect', function() {
    console.log('Client disconnected.');
  });  
});

server.listen(PORT, () => console.log('Server runnning on port' ,  PORT));
