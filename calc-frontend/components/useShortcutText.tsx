import { detect } from "detect-browser";
import { useCallback, useEffect, useState, useMemo } from "react";

export function shortcutText(command: string) {
  const os = detect()?.os;

  if (os === "Mac OS") {
    return `( ⌘${command} )`;
  } else if (os?.includes("Windows") || os?.includes("Linux")) {
    return `( Ctrl+${command} )`;
  }
  return null;
}

export function useShortcutText(command: string) {
  // TODO: this super janky workaround is necessary because
  // I don't know how to get the browser to detect the OS
  // on the server side.
  const [text, setText] = useState<string | null>(`( ⌘${command} )`);
  useEffect(() => setText(shortcutText(command)), [command]);
  return text;
}
