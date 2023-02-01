// TODO: can we get rid of 'window.location'?

import styles from "./AnalysisDisplay.module.css";

const examples = [
  `10 days + 3 weeks`,
  `cleaning project cost = 500 to $600 / 2 to 3 days`,
  `most often 90 = 10 .. 90 .. 100`,
  `
project time = (frontend + backend) / engineers
frontend = 2 to 3 weeks
backend = 3 to 4 weeks
engineers = 2 to 3
  `,
  `
expenses per month = food per day * 30 + rent + utilities

food per day = 20 .. 30 .. $50
rent = $1500
utilities = $300 to $400

expenses per month < 3000  
`,
];

function exampleHref(link: string) {
  const windowSearchParams = new URLSearchParams();
  windowSearchParams.set("code", link);
  return `?${windowSearchParams.toString()}`;
}

export function Examples() {
  return (
    <div className={styles.analysis}>
      <h2>Examples</h2>
      <div className={styles.analyses}>
        {examples.map((example) => (
          <div className={`${styles.full} ${styles.example}`} key={example}>
            <div>
              {example
                .trim()
                .split("\n")
                .map((x, i) => (
                  <p key={i}>{x}&nbsp;</p>
                ))}
            </div>
            <a href={exampleHref(example)}>Try it</a>
          </div>
        ))}
      </div>
    </div>
  );
}
