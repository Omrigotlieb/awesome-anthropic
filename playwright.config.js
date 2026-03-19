// @ts-check
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 30_000,
  use: {
    baseURL: process.env.BASE_URL || 'http://127.0.0.1:42173',
    trace: 'on-first-retry',
  },
  webServer: {
    command: 'python3 -m http.server 42173 --bind 127.0.0.1',
    url: 'http://127.0.0.1:42173',
    reuseExistingServer: true,
    cwd: '.',
    timeout: 30_000,
  },
});
