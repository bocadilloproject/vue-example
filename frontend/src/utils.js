export const postJSON = (url, payload = {}) =>
  fetch(url, {
    body: JSON.stringify(payload),
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json"
    },
    method: "POST"
  });
