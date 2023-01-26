import {
  Analysis,
  DistributionOutput,
  InequalityProbabilityOutput,
  MeasureOutput,
  PercentilesOutput,
  ValueInequalityOutput,
  ValueOutput,
} from "@/client";

import styles from "./AnalysisDisplay.module.css";
import { Histogram } from "./Histogram";

function fmtUnit(unit: string) {
  return unit.replaceAll("**", "^").replaceAll("*", "·");
}

function Value({ value, unit }: { value: number; unit: string }) {
  if (unit === "USD") {
    return (
      <>
        {value.toLocaleString("en-US", { style: "currency", currency: "USD" })}
      </>
    );
  }
  if (unit === "dimensionless") {
    return <>{value.toFixed(2)}</>;
  }
  return (
    <>
      {value.toFixed(2)} <em>{fmtUnit(unit)}</em>
    </>
  );
}

function Name({ name, unit }: { name: string; unit: string }) {
  if (unit === "USD") {
    return <>${name}</>;
  }
  if (unit === "dimensionless") {
    return <>{name.toString()}</>;
  }
  return (
    <>
      {name} <em>{fmtUnit(unit)}</em>
    </>
  );
}

function NameAndValue({
  name,
  unit,
  value,
}: {
  name?: string;
  unit: string;
  value: number;
}) {
  const valNode = <Value value={value} unit={unit} />;
  if (!name) {
    return valNode;
  }
  return (
    <>
      <strong>{name}</strong> ({valNode})
    </>
  );
}

function fmtProbability(probability: number) {
  return `${(probability * 100).toFixed(2)}%`;
}

function capFirst(str: string) {
  return str[0].toUpperCase() + str.slice(1);
}

export function AnalysisDisplay({ analysis }: { analysis: Analysis }) {
  const outputs = analysis.outputs.map((output) => {
    if (output.typename == ValueOutput.typename.VALUE) {
      return (
        <div key={`${analysis.name}-${output.name}`} className={styles.small}>
          <strong>{output.name}</strong> = <Value {...output} />
        </div>
      );
    }

    if (output.typename == MeasureOutput.typename.MEASURE) {
      const measureName =
        output.kind == "mean" ? "Average (mean)" : capFirst(output.kind);

      return (
        <div key={`${analysis.name}-${output.kind}`} className={styles.small}>
          <strong>{measureName}</strong>: <Value {...output} />
        </div>
      );
    }

    if (output.typename == DistributionOutput.typename.DISTRIBUTION) {
      return (
        <div
          key={`${analysis.name}-${output.distribution.name}`}
          className={styles.full}
        >
          <Histogram distribution={output} />
        </div>
      );
    }

    if (
      output.typename ==
      InequalityProbabilityOutput.typename.INEQUALITY_PROBABILITY
    ) {
      return (
        <div
          key={`${analysis.name}-${output.distribution.name}-dist-inequality`}
          className={styles.full}
        >
          <strong>
            Probability of <Name {...output.distribution} /> {output.op}{" "}
            {output.threshold.name != null ? (
              <Name name={output.threshold.name} unit={output.threshold.unit} />
            ) : (
              <Value {...output.threshold} />
            )}
          </strong>
          : {fmtProbability(output.probability)}
        </div>
      );
    }

    if (output.typename == ValueInequalityOutput.typename.INEQUALITY) {
      return (
        <div key={`${analysis.name}-inequality`} className={styles.full}>
          <strong>
            <NameAndValue {...output.lhs} /> {output.op}{" "}
            <NameAndValue {...output.rhs} />
          </strong>
          : {output.result ? "true" : "false"}
        </div>
      );
    }

    if (output.typename == PercentilesOutput.typename.PERCENTILES) {
      return (
        <div key={`${analysis.name}-inequality`} className={styles.full}>
          <table>
            <thead>
              <tr>
                <th>This percent of the time</th>
                {output.percentiles.map((p) => (
                  <th key={p.percentile}>{p.percentile}%</th>
                ))}
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>The result is below...</td>
                {output.percentiles.map((p) => (
                  <td key={p.percentile}>
                    <Value value={p.value} unit={output.unit} />
                  </td>
                ))}
              </tr>
            </tbody>
          </table>
        </div>
      );
    }

    return (
      <div key={output.typename}>
        <pre>{JSON.stringify(output, null, 2)}</pre>
      </div>
    );
  });
  return (
    <div className={styles.analysis}>
      <h2>Analysis: {analysis.name}</h2>
      <div className={styles.analyses}>{outputs}</div>
    </div>
  );
}
