async function getResult(code: string) {
  const params = new URLSearchParams({ code });
  const url = "https://walrus-app-wpbvo.ondigitalocean.app/compute/?" + params;

  const response = await fetch(url, { cache: "no-store" });

  const json = await response.json();
  console.log(JSON.stringify(json));
  return json;
}

export default async function Results({ code }: { code: string | undefined }) {
  const result = code ? await getResult(code) : {};

  await new Promise((resolve) => setTimeout(resolve, 5000));
  return <pre>{JSON.stringify(result, null, 2)}</pre>;
}
