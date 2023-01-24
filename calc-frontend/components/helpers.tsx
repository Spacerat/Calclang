export function sliding<T>(arr: T[], n: number): [T, T][] {
  const result: [T, T][] = [];
  for (let i = 0; i < arr.length - n + 1; i++) {
    // @ts-expect-error
    result.push(arr.slice(i, i + n));
  }
  return result;
}
export function zip2<T, U>(arr1: T[], arr2: U[]): [T, U][] {
  return arr1.map((x, i) => [x, arr2[i]]);
}
export function mid(x: number, y: number) {
  return (x + y) / 2;
}
