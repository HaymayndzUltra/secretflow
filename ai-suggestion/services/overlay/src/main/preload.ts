import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('overlayAPI', {
  onAccept: (handler: () => void) => ipcRenderer.on('overlay:accept', handler),
  onCycle: (handler: () => void) => ipcRenderer.on('overlay:cycle', handler),
  onDismiss: (handler: () => void) => ipcRenderer.on('overlay:dismiss', handler)
});
