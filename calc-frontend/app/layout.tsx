import "./globals.css";

import Link from "next/link";

import styles from "./layout.module.css";

import { Inter } from "@next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      {/*
        <head /> will contain the components returned by the nearest parent
        head.tsx. Find out more at https://beta.nextjs.org/docs/api-reference/file-conventions/head
      */}
      <head />

      <body>
        <div className={`${styles.container} ${inter.className}`}>
          <header className={styles.header}>
            <Link href="/">
              <h2>Calculatish</h2>
            </Link>
            <div>
              <Link href="/examples">Examples</Link>
            </div>
            <div>
              <Link href="/about">About</Link>
            </div>
          </header>
          <div className={styles.page}>{children}</div>
        </div>
      </body>
    </html>
  );
}
