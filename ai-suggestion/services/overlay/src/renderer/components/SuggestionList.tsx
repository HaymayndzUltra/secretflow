import React from 'react';
import { useOverlayStore } from '../hooks/useOverlayStore';

interface Props {
  suggestions: ReturnType<typeof useOverlayStore.getState>['suggestions'];
}

export const SuggestionList: React.FC<Props> = ({ suggestions }) => {
  const activeIndex = useOverlayStore(state => state.activeIndex);

  if (!suggestions.length) {
    return <p style={{ opacity: 0.6 }}>Waiting for grounded suggestions…</p>;
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
      {suggestions.map((suggestion, index) => (
        <div
          key={suggestion.id}
          style={{
            padding: '12px',
            borderRadius: '12px',
            background: index === activeIndex ? 'rgba(59,130,246,0.25)' : 'rgba(15,23,42,0.65)',
            border: index === activeIndex ? '1px solid rgba(59,130,246,0.65)' : '1px solid transparent'
          }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '4px' }}>
            <span style={{ fontWeight: 600 }}>Suggestion #{index + 1}</span>
            <span>
              {Math.round(suggestion.confidence * 100)}%
              {suggestion.confidence < 0.6 && (
                <span
                  style={{
                    marginLeft: '6px',
                    padding: '2px 6px',
                    borderRadius: '6px',
                    background: 'rgba(248,113,113,0.4)',
                    color: '#fecaca',
                    fontSize: '11px'
                  }}
                >
                  verify
                </span>
              )}
            </span>
          </div>
          <p style={{ margin: 0 }}>{suggestion.text}</p>
          <div style={{ marginTop: '6px', fontSize: '12px', opacity: 0.7 }}>
            {suggestion.evidence.map(id => (
              <span key={id} style={{ marginRight: '8px' }}>
                #{id}
              </span>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
};
