import { describe, expect, it } from 'vitest';
import { ASRPipeline } from '../src/pipelines/asrPipeline';

describe('ASRPipeline', () => {
  it('emits partials and finals', async () => {
    const pipeline = new ASRPipeline('test');
    let partials = 0;
    let finals = 0;
    pipeline.on('partial', () => {
      partials += 1;
    });
    pipeline.on('final', () => {
      finals += 1;
    });

    for (let i = 0; i < 6; i += 1) {
      pipeline.acceptFrame({ pcm16: new Int16Array([0, 1]), timestamp: Date.now() });
    }

    pipeline.close();
    expect(partials).toBeGreaterThan(0);
    expect(finals).toBeGreaterThan(0);
  });
});
