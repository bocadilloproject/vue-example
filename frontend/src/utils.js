const ROOT_URL = process.env.VUE_APP_BACKEND_ROOT_URL;

export const makeFullUrl = path => `${ROOT_URL}${path}`;

export const postJSON = (path, payload = {}) =>
  fetch(makeFullUrl(path), {
    body: JSON.stringify(payload),
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json"
    },
    method: "POST"
  }).then(res => res.json());
