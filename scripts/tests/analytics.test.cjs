const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const source = fs.readFileSync(path.join(__dirname, "../../assets/analytics.js"), "utf8");
const key = "midu.analytics.excluded";
const token = "0".repeat(32);

function visit({ search = "", hostname = "www.midu.com.au", storage = new Map(), brokenStorage = false, siteToken = token } = {}) {
  const scripts = [];
  const notices = [];
  const localStorage = {
    setItem: (key, value) => storage.set(key, value),
    removeItem: (key) => storage.delete(key),
    getItem: (key) => {
      if (brokenStorage) throw new Error("Storage unavailable");
      return storage.get(key) ?? null;
    },
  };
  if (brokenStorage) {
    localStorage.setItem = localStorage.removeItem = localStorage.getItem;
  }
  const document = {
    currentScript: { dataset: { analyticsToken: siteToken } },
    createElement: (tag) => ({
      tag, children: [], attributes: {},
      appendChild(child) { this.children.push(child); },
      setAttribute(name, value) { this.attributes[name] = value; },
    }),
    head: { appendChild: (script) => scripts.push(script) },
    body: { prepend: (notice) => notices.push(notice) },
  };
  vm.runInNewContext(source, { document, window: { location: { search, hostname }, localStorage }, URLSearchParams });
  return { scripts, notices, storage };
}

test("a normal public visit loads exactly the official module beacon", () => {
  const { scripts, notices } = visit();
  assert.equal(scripts.length, 1);
  assert.equal(scripts[0].src, "https://static.cloudflareinsights.com/beacon.min.js");
  assert.equal(scripts[0].type, "module");
  assert.deepEqual(JSON.parse(scripts[0].attributes["data-cf-beacon"]), { token });
  assert.equal(notices.length, 0);
});

test("opting out suppresses this visit and later visits", () => {
  const first = visit({ search: "?analytics=off" });
  assert.equal(first.scripts.length, 0);
  assert.equal(first.storage.get(key), "true");
  assert.equal(first.notices[0].attributes.role, "status");
  assert.match(first.notices[0].children[0].textContent, /excluded/);
  assert.equal(visit({ storage: first.storage }).scripts.length, 0);
});

test("opting back in affects only future visits", () => {
  const storage = new Map([[key, "true"]]);
  assert.equal(visit({ search: "?analytics=on", storage }).scripts.length, 0);
  assert.equal(storage.has(key), false);
  assert.equal(visit({ storage }).scripts.length, 1);
});

test("unavailable browser storage never sends a beacon", () => {
  for (const search of ["", "?analytics=off", "?analytics=on"]) {
    assert.equal(visit({ search, brokenStorage: true }).scripts.length, 0);
  }
});

test("previews, local development, blog and learning do not report", () => {
  for (const hostname of ["localhost", "127.0.0.1", "songgithub.github.io", "blog.midu.com.au", "learn.midu.com.au"]) {
    assert.equal(visit({ hostname }).scripts.length, 0);
  }
});

test("an invalid or absent public collection token does not report", () => {
  for (const siteToken of [undefined, "", "not-a-token"]) {
    // undefined uses the helper default, so explicitly remove the dataset value.
    assert.equal(visit({ siteToken: siteToken ?? null }).scripts.length, 0);
  }
});

test("unrelated query parameters cannot clear a saved exclusion", () => {
  const storage = new Map([[key, "true"]]);
  assert.equal(visit({ search: "?analytics=anything&utm_source=test", storage }).scripts.length, 0);
  assert.equal(storage.get(key), "true");
});
