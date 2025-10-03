import { randomUUID } from 'crypto';
import { EventEmitter } from 'events';
import { logger } from '../utils/logger';
import { redactPII } from '../utils/pii';

export interface AudioFrame {
  pcm16: Int16Array;
  timestamp: number;
}

export interface TranscriptSegment {
  id: string;
  text: string;
  start: number;
  end: number;
  speaker: string;
  confidence: number;
  isFinal: boolean;
}

export interface ASRPipelineEvents {
  partial: (segment: TranscriptSegment) => void;
  final: (segment: TranscriptSegment) => void;
  diarization: (speakerMap: Record<string, string>) => void;
  error: (err: Error) => void;
}

const SPEAKERS = ['speaker_a', 'speaker_b'];

export class ASRPipeline extends EventEmitter {
  private buffer: AudioFrame[] = [];
  private readonly vadThreshold: number;
  private readonly fallbackMode: boolean;
  private ttlTimer: NodeJS.Timeout;

  constructor(private readonly sessionId: string) {
    super();
    this.vadThreshold = Number(process.env.VAD_THRESHOLD ?? 0.6);
    this.fallbackMode = process.env.FWHISPER_PATH ? false : true;

    this.ttlTimer = setTimeout(() => {
      logger.info({ sessionId: this.sessionId }, 'Session TTL expired, flushing buffer');
      this.close();
    }, 30_000);

    setImmediate(() => {
      this.emit('diarization', {
        speaker_a: 'Primary Caller',
        speaker_b: 'Secondary Participant'
      });
    });
  }

  acceptFrame(frame: AudioFrame): void {
    clearTimeout(this.ttlTimer);
    this.ttlTimer = setTimeout(() => {
      logger.info({ sessionId: this.sessionId }, 'Session TTL expired after activity, flushing');
      this.close();
    }, 30_000);
    this.buffer.push(frame);
    if (this.buffer.length < 5) {
      return;
    }

    const segment = this.generateStubTranscript();
    this.emit('partial', segment);

    if (segment.isFinal) {
      this.buffer = [];
      this.emit('final', segment);
    }
  }

  close(): void {
    clearTimeout(this.ttlTimer);
    if (this.buffer.length > 0) {
      const segment = this.generateStubTranscript();
      segment.isFinal = true;
      this.emit('final', segment);
      this.buffer = [];
    }
  }

  private generateStubTranscript(): TranscriptSegment {
    const chunkText = `placeholder summary ${Math.floor(Math.random() * 1000)}`;
    const redacted = redactPII(chunkText);
    const segment: TranscriptSegment = {
      id: randomUUID(),
      text: redacted,
      start: Date.now() - 1000,
      end: Date.now(),
      speaker: SPEAKERS[Math.floor(Math.random() * SPEAKERS.length)],
      confidence: this.fallbackMode ? 0.7 : 0.92,
      isFinal: Math.random() > 0.5
    };
    logger.debug({ sessionId: this.sessionId, text: segment.text }, 'ASR stub transcript');
    return segment;
  }
}

export type ASRPipelineEventMap = {
  [K in keyof ASRPipelineEvents]: Parameters<ASRPipelineEvents[K]>;
};
