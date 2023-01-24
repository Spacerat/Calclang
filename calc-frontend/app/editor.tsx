"use client";

import { useCallback, useState } from "react";
import { getResult } from "./getResult";

import styles from "./page.module.css";

type EditorProps = {
  initialResult: unknown;
  initialCode: string;
};

export default function Editor({ initialResult, initialCode }: EditorProps) {
  const [code, setCode] = useState(initialCode);
  const [result, setResult] = useState<unknown>(initialResult);

  const onSubmit = useCallback(async () => {
    if (code) {
      const windowSearchParams = new URLSearchParams(window.location.search);
      windowSearchParams.set("code", code);
      window.history.replaceState({}, "", "?" + windowSearchParams.toString());
      setResult(await getResult(code));
    }
    return false;
  }, [code]);

  return (
    <main className={styles.main}>
      <form
        className={styles.section}
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit();
        }}
      >
        <div className={styles.sectionHead}>
          <h2>Sheet</h2>
          <button type="submit">Run</button>
        </div>
        <textarea
          name="code"
          onChange={(e) => setCode(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && e.metaKey) {
              e.preventDefault();
              onSubmit();
            }
          }}
          value={code}
        />
      </form>
      <section className={styles.section}>
        <div className={styles.sectionHead}>
          <h2>Results</h2>
        </div>
        <pre>{JSON.stringify(result, null, 2)}</pre>
      </section>
    </main>
  );
}
