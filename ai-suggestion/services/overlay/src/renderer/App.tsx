import React, { useEffect } from 'react';
import { io } from 'socket.io-client';
import { useOverlayStore } from './hooks/useOverlayStore';
import { SuggestionList } from './components/SuggestionList';

const orchestratorUrl = import.meta.env.VITE_ORCHESTRATOR_URL ?? 'http://localhost:7003';

const socket = io(`${orchestratorUrl}/overlay`, { path: '/socket.io' });

const App: React.FC = () => {
  const { suggestions, acceptCurrent, cycleSuggestion, dismissSuggestions, setSuggestions } = useOverlayStore();

  useEffect(() => {
    socket.on('suggestion', payload => {
      setSuggestions(payload.suggestions);
    });
    return () => {
      socket.off('suggestion');
    };
  }, [setSuggestions]);

  useEffect(() => {
    if (window.overlayAPI) {
      window.overlayAPI.onAccept(acceptCurrent);
      window.overlayAPI.onCycle(cycleSuggestion);
      window.overlayAPI.onDismiss(dismissSuggestions);
    }
  }, [acceptCurrent, cycleSuggestion, dismissSuggestions]);

  return (
    <div
      style={{
        padding: '12px',
        background: 'rgba(15, 23, 42, 0.8)',
        color: 'white',
        fontFamily: 'Inter, sans-serif',
        borderRadius: '16px'
      }}
    >
      <h2 style={{ marginTop: 0 }}>Live Suggestions</h2>
      <SuggestionList suggestions={suggestions} />
    </div>
  );
};

export default App;
