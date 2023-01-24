import Editor from "./editor";
import { getResult } from "./getResult";

type HomeProps = {
  searchParams?: { code?: string };
};

export default async function Home({ searchParams }: HomeProps) {
  const code = searchParams?.code || "";
  const result = code ? await getResult(code) : null;

  return <Editor initialCode={code} initialResult={result} />;
}
