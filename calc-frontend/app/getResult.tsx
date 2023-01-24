export async function getResult(code: string): Promise<unknown> {
  const params = new URLSearchParams({ code });
  const url = "https://walrus-app-wpbvo.ondigitalocean.app/compute?" + params;

  const response = await fetch(url, { cache: "no-store" });

  return await response.json();
}
