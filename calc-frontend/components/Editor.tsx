"use client";

import { Analysis } from "@/api/getResult";
import { useCallback, useEffect, useState, useMemo } from "react";
import { getResult } from "../api/getResult";
import { AnalysisDisplay } from "./AnalysisDisplay";

import styles from "./Editor.module.css";
import buttonStyles from "./Button.module.css";

import { useSearchParams } from "next/navigation";
import { useShortcutText } from "./useShortcutText";

const placeholder = `Write your model here`;

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
    const windowSearchParams = new URLSearchParams(window.location.search);
    if (code) {
      windowSearchParams.set("code", code);
      window.history.replaceState({}, "", "?" + windowSearchParams.toString());
      setResult(await getResult(code));
    } else {
      windowSearchParams.delete("code");
      window.history.replaceState({}, "", "?" + windowSearchParams.toString());
      setResult(null);
    }
    return false;
  }, [code]);

  const downloadLink = stringDownloadLink(code, result?.name ?? "out");

  const command = useShortcutText("Enter");

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
          <h2>Calculations</h2>
          <button
            className={`${buttonStyles.button} ${buttonStyles.runButton}`}
            type="submit"
          >
            Run {command}
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
            if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
              e.preventDefault();
              onSubmit();
            }
          }}
          value={code}
        />
      </form>
      <section className={styles.section}>
        <div>{result && <AnalysisDisplay analysis={result} />}</div>
        {/* <div>{!result && <Examples />}</div> */}
      </section>
    </main>
  );
}
