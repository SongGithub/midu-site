(() => {
  const loader = document.currentScript;
  const preference = new URLSearchParams(window.location.search).get("analytics");
  const storageKey = "midu.analytics.excluded";

  function showStatus(message) {
    const notice = document.createElement("aside");
    notice.className = "analytics-notice";
    notice.setAttribute("role", "status");
    const content = document.createElement("div");
    content.className = "shell";
    content.textContent = message;
    notice.appendChild(content);
    document.body.prepend(notice);
  }

  let excluded;
  try {
    if (preference === "off") window.localStorage.setItem(storageKey, "true");
    if (preference === "on") window.localStorage.removeItem(storageKey);
    excluded = window.localStorage.getItem(storageKey) === "true";
  } catch {
    // Without storage we cannot honour a saved exclusion, so do not report.
    if (preference === "off" || preference === "on") {
      showStatus("Visitor measurement is off for this visit. Browser storage is unavailable, so this choice cannot be saved.");
    }
    return;
  }

  if (excluded) {
    showStatus("This browser is excluded from visit counts.");
    return;
  }
  if (preference === "on") {
    showStatus("This browser will be included in visit counts from your next visit.");
    return;
  }
  if (window.location.hostname !== "www.midu.com.au") return;

  const token = loader?.dataset.analyticsToken;
  if (!/^[a-f0-9]{32}$/.test(token || "")) return;
  // Cloudflare's manual snippet, loaded only after the local exclusion check.
  // https://developers.cloudflare.com/web-analytics/get-started/
  const beacon = document.createElement("script");
  beacon.type = "module";
  beacon.src = "https://static.cloudflareinsights.com/beacon.min.js";
  beacon.setAttribute("data-cf-beacon", JSON.stringify({ token }));
  document.head.appendChild(beacon);
})();
