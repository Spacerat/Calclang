import { detect } from "detect-browser";

export function commandForOS(command: string) {
  const os = detect()?.os;

  if (os === "Mac OS") {
    return `( ⌘${command} )`;
  } else if (os?.includes("Windows") || os?.includes("Linux")) {
    return `( Ctrl+${command} )`;
  }
  return null;
}
