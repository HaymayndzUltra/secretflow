import { describe, expect, it } from 'vitest';
import { useOverlayStore } from '../src/renderer/hooks/useOverlayStore';

describe('overlay store', () => {
  it('cycles suggestions', () => {
    const store = useOverlayStore.getState();
    store.setSuggestions([
      { id: '1', text: 'a', confidence: 0.8, evidence: [] },
      { id: '2', text: 'b', confidence: 0.7, evidence: [] }
    ]);
    store.cycleSuggestion();
    expect(useOverlayStore.getState().activeIndex).toBe(1);
  });
});
