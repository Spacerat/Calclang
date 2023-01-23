import { Suspense } from "react";

import styles from "./page.module.css";
import Results from "./Results";

export default async function Home({
  searchParams,
}: {
  searchParams: { code?: string };
}) {
  const code = searchParams.code;

  return (
    <main className={styles.main}>
      <form className={styles.section} method="get">
        <div className={styles.sectionHead}>
          <button type="submit">Run</button>
        </div>
        <textarea name="code">{code}</textarea>
      </form>
      <section className={styles.section}>
        <Suspense fallback={"Loading"}>
          {/* @ts-expect-error Server Component */}
          <Results code={code} />
        </Suspense>
      </section>
    </main>
  );
}
