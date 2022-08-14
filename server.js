const io = require('socket.io').listen(6079); // import socket.io module and listen on port 6079

io.on('connection', (socket) => {
    console.info('connection established');

    socket.on('msg', (msg) => {
        console.log(msg);
        // do something with the message
    });

    socket.on('disconnect', function() {
      console.log('client disconnected');
   });
});
