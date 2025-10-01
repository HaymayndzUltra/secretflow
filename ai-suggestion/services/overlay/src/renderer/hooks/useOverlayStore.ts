import { create } from 'zustand';

export interface Suggestion {
  id: string;
  text: string;
  confidence: number;
  evidence: string[];
}

interface OverlayState {
  suggestions: Suggestion[];
  activeIndex: number;
  setSuggestions: (suggestions: Suggestion[]) => void;
  acceptCurrent: () => void;
  cycleSuggestion: () => void;
  dismissSuggestions: () => void;
}

export const useOverlayStore = create<OverlayState>(set => ({
  suggestions: [],
  activeIndex: 0,
  setSuggestions: suggestions => set({ suggestions, activeIndex: 0 }),
  acceptCurrent: () => {
    set(state => {
      const current = state.suggestions[state.activeIndex];
      if (current) {
        console.log('Accepted suggestion', current);
      }
      return state;
    });
  },
  cycleSuggestion: () => {
    set(state => ({
      ...state,
      activeIndex: state.suggestions.length ? (state.activeIndex + 1) % state.suggestions.length : 0
    }));
  },
  dismissSuggestions: () => set({ suggestions: [], activeIndex: 0 })
}));
