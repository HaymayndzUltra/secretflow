import { describe, expect, it } from 'vitest';
import { buildPrompt, detectIntent } from '../src/utils/promptRouter';

describe('prompt router', () => {
  it('detects requirements intent', () => {
    expect(detectIntent('We need requirements list')).toBe('requirements');
  });

  it('builds prompt with evidence', () => {
    const prompt = buildPrompt(
      'generic',
      [
        {
          id: 'doc-1',
          text: 'Example evidence snippet',
          source: 'doc',
          span: [0, 10],
          rerankScore: 1
        }
      ],
      'hello world'
    );
    expect(prompt).toContain('doc-1');
  });
});
