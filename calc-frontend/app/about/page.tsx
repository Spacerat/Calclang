import styles from "@/app/layout.module.css";

import Link from "next/link";

export default async function Home() {
  return (
    <div className={styles.pageContainer}>
      <h2>About</h2>
      <p>Calculatish is a calculator for estimation and modeling.</p>
      <p>
        In addition to specifying single numbers, you can provide{" "}
        <em>ranges</em> by writing values like <code>10 to 20</code>.
      </p>
      <p>Try it for:</p>
      <ul>
        <li>Estimating project timelines and costs</li>
        <li>Predicting best and worst case financial scenarios</li>
        <li>Break down math problems into small pieces</li>
      </ul>
      <h2>Feedback</h2>
      <p>
        This is a very early, <strong>work in progress</strong> project, so
        I&apos;m eager for feedback!
      </p>
      <ul>
        <li>Did this project help you?</li>
        <li>Would you like to be kept up to date?</li>
        <li>Got any features like to see?</li>
        <li>Encountered any issues?</li>
      </ul>
      <p>
        Let me know <a href="https://forms.gle/CYrN2mXN93FJX2SY9">here</a>!
      </p>
    </div>
  );
}
