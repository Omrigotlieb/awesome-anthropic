/* Service Worker — Awesome Anthropic
   Caches core assets for offline use.
   Cache-first for static assets, network-first for markdown docs.
*/
const CACHE_VERSION = 'aa-v1';
const STATIC_CACHE = CACHE_VERSION + '-static';
const DOCS_CACHE   = CACHE_VERSION + '-docs';

const STATIC_ASSETS = [
  '/awesome-anthropic/',
  '/awesome-anthropic/index.html',
  'https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=Inter:wght@400;500;600;700&display=swap',
  'https://cdn.jsdelivr.net/npm/docsify@4/lib/docsify.min.js',
  'https://cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css',
  'https://cdn.jsdelivr.net/npm/docsify@4/lib/plugins/search.min.js',
];

const DOCS_ASSETS = [
  '/awesome-anthropic/_sidebar.md',
  '/awesome-anthropic/README.md',
  '/awesome-anthropic/docs/NEWS.md',
  '/awesome-anthropic/docs/CHANGELOG.md',
  '/awesome-anthropic/docs/BENCHMARKS.md',
  '/awesome-anthropic/docs/CLAUDE_CODE.md',
  '/awesome-anthropic/docs/INTERVIEW.md',
  '/awesome-anthropic/docs/PROMPTS.md',
  '/awesome-anthropic/docs/TOOLS.md',
];

// Install: cache static assets
self.addEventListener('install', function(e) {
  self.skipWaiting();
  e.waitUntil(
    caches.open(STATIC_CACHE).then(function(cache) {
      return cache.addAll(STATIC_ASSETS).catch(function(err) {
        console.warn('[SW] Static prefetch failed (non-fatal):', err);
      });
    })
  );
});

// Activate: clean up old caches
self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(keys) {
      return Promise.all(
        keys.filter(function(k) { return k.startsWith('aa-') && k !== STATIC_CACHE && k !== DOCS_CACHE; })
            .map(function(k) { return caches.delete(k); })
      );
    }).then(function() { return self.clients.claim(); })
  );
});

// Fetch: strategy depends on resource type
self.addEventListener('fetch', function(e) {
  var url = e.request.url;

  // Skip non-GET and non-http(s) requests
  if (e.request.method !== 'GET' || !url.startsWith('http')) return;

  // Skip HN Firebase and other external APIs — always network
  if (url.includes('firebaseio.com') || url.includes('reddit.com/r/') || url.includes('nitter')) return;

  // Docs (markdown) — network first, fallback to cache
  var isDoc = DOCS_ASSETS.some(function(d) { return url.endsWith(d) || url.includes(d.split('/').pop()); });
  if (isDoc) {
    e.respondWith(
      fetch(e.request).then(function(res) {
        if (res.ok) {
          var clone = res.clone();
          caches.open(DOCS_CACHE).then(function(c) { c.put(e.request, clone); });
        }
        return res;
      }).catch(function() {
        return caches.match(e.request);
      })
    );
    return;
  }

  // Static assets — cache first
  e.respondWith(
    caches.match(e.request).then(function(cached) {
      if (cached) return cached;
      return fetch(e.request).then(function(res) {
        if (res.ok && (url.includes('jsdelivr') || url.includes('fonts.g'))) {
          var clone = res.clone();
          caches.open(STATIC_CACHE).then(function(c) { c.put(e.request, clone); });
        }
        return res;
      });
    })
  );
});
