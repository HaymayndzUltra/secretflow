export interface OverlayAPI {
  onAccept: (handler: () => void) => void;
  onCycle: (handler: () => void) => void;
  onDismiss: (handler: () => void) => void;
}

declare global {
  interface Window {
    overlayAPI?: OverlayAPI;
  }
}
