import { io } from 'socket.io-client';

export const stocksSocket = io('http://localhost:3000/stocks');
export const controllerSocket = io('http://localhost:3000/controller');