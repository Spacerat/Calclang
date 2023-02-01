import { Examples } from "@/components/Examples";

import styles from "@/app/layout.module.css";

export default async function Home() {
  return (
    <div className={styles.pageContainer}>
      <Examples />
    </div>
  );
}
