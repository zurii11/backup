'use strict';

const {app, BrowserWindow} = require('electron')
const path = require('path')

require('electron-reload')(__dirname, {
    electron: path.join(__dirname, 'node_modules', '.bin', 'electron')
})

function createWindow() {
    let win = new BrowserWindow({
        width: 700,
        height: 700,
        webPreferences: {
            nodeIntegration: true
        }
    })

    win.loadFile('/home/zura/Dev/electron/phaserGame/index.html')

    win.webContents.openDevTools()
}

app.whenReady().then(createWindow)