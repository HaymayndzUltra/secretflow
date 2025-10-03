import { app, BrowserWindow, globalShortcut } from 'electron';
import path from 'path';

function createWindow(): void {
  const window = new BrowserWindow({
    width: 420,
    height: 640,
    alwaysOnTop: true,
    frame: false,
    transparent: true,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  });

  if (process.env.VITE_DEV_SERVER_URL) {
    window.loadURL(process.env.VITE_DEV_SERVER_URL);
  } else {
    window.loadFile(path.join(__dirname, '../renderer/index.html'));
  }
}

app.whenReady().then(() => {
  createWindow();
  globalShortcut.register('CommandOrControl+Enter', () => {
    BrowserWindow.getAllWindows().forEach(win => win.webContents.send('overlay:accept'));
  });
  globalShortcut.register('CommandOrControl+Tab', () => {
    BrowserWindow.getAllWindows().forEach(win => win.webContents.send('overlay:cycle'));
  });
  globalShortcut.register('Escape', () => {
    BrowserWindow.getAllWindows().forEach(win => win.webContents.send('overlay:dismiss'));
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
