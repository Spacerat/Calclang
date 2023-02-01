// TODO: can we get rid of 'window.location'?
import Link from "next/link";

import styles from "./AnalysisDisplay.module.css";

function exampleHref(link: string) {
  const windowSearchParams = new URLSearchParams();
  windowSearchParams.set("code", link);
  return `/?${windowSearchParams.toString()}`;
}

function Example({ example }: { example: string }) {
  const trimmed = example
    .trim()
    .split("\n")
    .map((x) => x.trim());

  return (
    <div className={`${styles.full} ${styles.example}`}>
      <div>
        {trimmed.map((x, i) => (
          <div key={i}>{x}&nbsp;</div>
        ))}
      </div>
      <Link href={exampleHref(trimmed.join("\n"))}>Try it</Link>
    </div>
  );
}

export function Examples() {
  return (
    <div className={styles.analysis}>
      <h2>Examples</h2>
      <div className={styles.analyses}>
        Do time math easily (seconds, minutes, days and weeks)
        <Example example="10 days + 3 weeks" />
        Break down calculations into simple steps
        <Example
          example={`
          monthly rent = $3000
          yearly rent = monthly rent * 12
        `}
        />
        Visualize a range of possible project times
        <Example
          example={`
        project time = (frontend + backend) / engineers
        frontend = 2 to 3 weeks
        backend = 3 to 4 weeks
        engineers = 2 to 3
        `}
        />
        Estimate a probability that monthly expenses will be less than $3000
        <Example
          example={`
        expenses per month = food per day * 30 + rent + utilities

        food per day = 20 .. 30 .. $50
        rent = $1500
        utilities = $300 to $400
        
        expenses per month < 3000  
        `}
        />
        {/* <Example example="cleaning project cost = 500 to $600 / 2 to 3 days" /> */}
      </div>
    </div>
  );
}
