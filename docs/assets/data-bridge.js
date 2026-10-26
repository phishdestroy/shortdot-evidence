/* Fetch the existing upstream feeds; keep the packaged snapshot as a fallback. */
(function () {
  'use strict';
  var nativeFetch = window.fetch.bind(window);
  var source = (window.PD_SOURCE_CONFIG && window.PD_SOURCE_CONFIG.raw_docs_base) || 'https://raw.githubusercontent.com/phishdestroy/shortdot-evidence/main/docs/';
  var requests = new Map();
  var states = {};
  var versions = {};
  var feeds = ['chart-data.json', 'feed-ioc.json', 'data.json'];
  function notify(name, data, mode) {
    var state = {name:name, mode:mode, updated:data.last_updated || data.generated_at || data.generated || data.updated || '', checkedAt:new Date().toISOString()};
    states[name] = state;
    window.pdFeedStates = states;
    window.dispatchEvent(new CustomEvent('pd:source', {detail:state}));
  }
  async function load(name) {
    var response, data, mode = 'source';
    try {
      var controller = new AbortController();
      var timer = setTimeout(function(){controller.abort();},15000);
      try { response = await nativeFetch(source + name, {cache:'no-cache', signal:controller.signal}); }
      finally { clearTimeout(timer); }
      if (!response.ok) throw new Error('Source HTTP ' + response.status);
      data = await response.json();
      if (name === 'chart-data.json' && (!Array.isArray(data.days) || !data.last_updated)) throw new Error('Invalid analytics schema');
      if (name === 'data.json' && (!data.stats || !Array.isArray(data.domains))) throw new Error('Invalid evidence schema');
      if (name === 'feed-ioc.json' && !Array.isArray(data.domains)) throw new Error('Invalid IOC schema');
    } catch (error) {
      mode = 'snapshot';
      response = await nativeFetch(new URL(name, document.baseURI).href, {cache:'no-cache'});
      if (!response.ok) throw new Error('Both source and saved snapshot are unavailable');
      data = await response.json();
    }
    var body = JSON.stringify(data);
    versions[name] = body;
    notify(name,data,mode);
    return body;
  }
  window.fetch = function(input, init) {
    var url = typeof input === 'string' ? input : input instanceof URL ? input.href : input.url;
    var parsed = new URL(url, document.baseURI);
    var name = parsed.pathname.split('/').pop();
    if (parsed.origin === location.origin && feeds.includes(name)) {
      if (!requests.has(name)) requests.set(name,load(name).catch(function(error){requests.delete(name);throw error;}));
      return requests.get(name).then(function(body){return new Response(body,{status:200,headers:{'Content-Type':'application/json'}});});
    }
    return nativeFetch(input,init);
  };
  window.pdCheckForUpdates = async function() {
    if (document.hidden) return;
    if (!states['chart-data.json']) {
      // Retry initialization after an offline page load.
      try { await window.fetch('chart-data.json'); } catch (error) {}
      return;
    }
    try {
      var controller = new AbortController();
      var timer = setTimeout(function(){controller.abort();},12000);
      var response;
      try { response = await nativeFetch(source+'chart-data.json',{cache:'no-cache',signal:controller.signal}); }
      finally {clearTimeout(timer);}
      if (!response.ok) return;
      var data = await response.json();
      // Compare the same feed, including changes within a single UTC day.
      if (Array.isArray(data.days) && data.last_updated && JSON.stringify(data) !== versions['chart-data.json']) {
        var banner = document.getElementById('pd-update-banner');
        if (banner) banner.hidden = false;
      }
    } catch (error) { /* The current, labeled snapshot remains usable offline. */ }
  };

  // Main pages only request data.json; establish the small analytics baseline too.
  window.fetch('chart-data.json').catch(function(){});
  setInterval(window.pdCheckForUpdates,300000);
})();
