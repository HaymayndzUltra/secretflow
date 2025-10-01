import { io, Socket } from 'socket.io-client';
import EventEmitter from 'eventemitter3';

export interface AsrEvents {
  partial: { text: string; speaker: string; confidence: number; id: string };
  final: { text: string; speaker: string; confidence: number; id: string };
}

export class AsrSession extends EventEmitter<AsrEvents> {
  private socket: Socket;

  constructor(sessionId: string) {
    super();
    this.socket = io(`${process.env.ASR_URL ?? 'http://localhost:7001'}/ingress`, {
      path: '/webrtc',
      query: { sessionId }
    });

    this.socket.on('partial', payload => this.emit('partial', payload));
    this.socket.on('final', payload => this.emit('final', payload));
  }

  close(): void {
    this.socket.close();
  }
}
