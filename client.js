const {io } = require("socket.io-client")
const socket = io("http://localhost:3000");

console.log(socket.id); // undefined

socket.on("connect", () => {
  console.log(socket.id); // "G5p5..."
});