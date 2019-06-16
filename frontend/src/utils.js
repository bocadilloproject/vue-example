const ROOT_URL = process.env.VUE_APP_BACKEND_ROOT_URL;

const withApiBase = path => `${ROOT_URL}${path}`;
export const withBase = path => `${window.location.origin}${path}`;

export const http = {
  async get(path) {
    const res = await fetch(withApiBase(path));
    return res.json();
  },
  async post(path, payload = {}) {
    const res = await fetch(withApiBase(path), {
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
      },
      method: "POST"
    });
    return res.json();
  }
};
