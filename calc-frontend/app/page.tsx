"use client";

import { Suspense, useState } from "react";

import styles from "./page.module.css";
import Results from "./Results";

async function getResult(code: string): Promise<unknown> {
  const params = new URLSearchParams({ code });
  const url = "https://walrus-app-wpbvo.ondigitalocean.app/compute?" + params;

  const response = await fetch(url, { cache: "no-store" });

  const json = await response.json();
  return json;
}

export default function Home({
  searchParams,
}: {
  searchParams?: { code?: string };
}) {
  const [code, setCode] = useState(searchParams?.code ?? "");
  const [result, setResult] = useState<unknown>(null);

  return (
    <main className={styles.main}>
      <form
        className={styles.section}
        onSubmit={async (e) => {
          e.preventDefault();
          if (code) {
            setResult(await getResult(code));
          }
          return false;
        }}
      >
        <div className={styles.sectionHead}>
          <button type="submit">Run</button>
        </div>
        <textarea
          name="code"
          onChange={(e) => setCode(e.target.value)}
          value={code}
        />
      </form>
      <section className={styles.section}>
        <pre>{JSON.stringify(result, null, 2)}</pre>
      </section>
    </main>
  );
}
