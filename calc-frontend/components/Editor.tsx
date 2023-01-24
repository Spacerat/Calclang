"use client";

import { Analysis } from "@/api/getResult";
import { useCallback, useEffect, useState } from "react";
import { getResult } from "../api/getResult";
import { AnalysisDisplay } from "./AnalysisDisplay";

import styles from "./Editor.module.css";
import buttonStyles from "./Button.module.css";

import { useSearchParams } from "next/navigation";

const placeholder = `spendable = income - cost

income = $2000 to $2300

cost = rent + utilities + food

rent = $700
utilities = $300 to $400
food = ($100 to $150) * 4

spendable > 600`;

function stringDownloadLink(text: string, filename: string) {
  const blob = new Blob([text], { type: "text/plain" });
  return URL.createObjectURL(blob);
}

type EditorProps = {
  initialResult: Analysis | null;
  initialCode: string;
};

export default function Editor({ initialResult, initialCode }: EditorProps) {
  const [code, setCode] = useState(initialCode);
  const [result, setResult] = useState<Analysis | null>(initialResult);

  // This seems to be necessary to get the initial code to load
  // in production. I'm not sure why.
  const searchParams = useSearchParams();
  useEffect(() => {
    (async () => {
      const paramsCode = searchParams.get("code");
      if (paramsCode && !initialCode) {
        const result = await getResult(paramsCode);
        setCode(paramsCode);
        setResult(result);
      }
    })();
  }, [initialCode, searchParams]);

  const onSubmit = useCallback(async () => {
    if (code) {
      const windowSearchParams = new URLSearchParams(window.location.search);
      windowSearchParams.set("code", code);
      window.history.replaceState({}, "", "?" + windowSearchParams.toString());
      setResult(await getResult(code));
    }
    return false;
  }, [code]);

  const downloadLink = stringDownloadLink(code, result?.name ?? "out");

  useEffect(() => {
    console.log({ initialResult, initialCode });
  }, [initialCode, initialResult]);

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
          <button
            className={`${buttonStyles.button} ${buttonStyles.runButton}`}
            type="submit"
          >
            Run
          </button>

          <a href={downloadLink} download>
            <button
              className={`${buttonStyles.button} ${buttonStyles.basicButton}`}
              type="button"
            >
              Download
            </button>
          </a>
        </div>
        <textarea
          placeholder={placeholder}
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
        <div>{result && <AnalysisDisplay analysis={result} />}</div>
      </section>
    </main>
  );
}
